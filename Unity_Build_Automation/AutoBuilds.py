#first get latest from git
#next get create build

#if someone else needs
from os import getcwd
from discord import guild
from git import Repo, cmd
import configparser, subprocess, sys, os, discord
from datetime import datetime

#make sure machine is set up with github ssh
#add discord token to enviornement variables
itchUser = 'itch.io username goes here'
itchPageName = 'itch.io page name goes here'
projectPath = 'unity projectPath goes here'
editorPath = 'unity editor path goes here'
buildPath = 'location to store build'
buildChanel = 'channel id bot should talk to'

class GitRepoClass:
    def __init__(self, repoPath, buildPath):
        self.repoPath = repoPath
        self.buildPath = buildPath
        
    def PullLatestProject(self):
        g = cmd.Git(self.repoPath)
        msg = g.pull()
        print(msg)

        repo = Repo(self.repoPath)
        master = repo.head.reference
        commitID = master.commit.hexsha
        commitLastDate = datetime.fromtimestamp(master.commit.committed_date)
        commitLastDate = commitLastDate.strftime('%m/%d/%Y')
        commitMessage = master.commit.message

        commitDictionary = {'ID' : commitID, 'LastDate' : commitLastDate, 'Message' : commitMessage}
        return commitDictionary.copy()
    
    def PushNewBuild(self):
        repo = Repo(self.buildPath)
        repo.git.add(update=True)
        repo.index.commit('Adding New Build')
        origin = repo.remote(name='origin')

        origin.push()
        print('pushed new build to git')
        subprocess.run(f'butler push {self.buildPath} {itchUser}/{itchPageName}:windows-beta')
        print('pushed build to itch')

class BuildUnity:
    def __init__(self,projectPath, unityPath):
        subprocess.run(f'{unityPath} -quit -projectPath {projectPath} -bathcmode {os.getcwd()} -executeMethod UnityBuildPipe.BuildWindows')

# class CleanFolder:


#make a place for this in the config file
if __name__ == "__main__":
    e = GitRepoClass(projectPath, buildPath)
    dick = e.PullLatestProject()
    k = BuildUnity(projectPath, unityPath)
    e.PushNewBuild()

client = discord.Client()

@client.event
async def on_ready():
    channel = client.get_channel(buildChanel)
    #role = discord.utils.get(ctx.guild.roles, name="CrashTestDummies")
    for g in client.guilds:
        for r in g.roles:
            if 'CrashTestDummies' in r.name:
                role = r

    messToSend = role.mention + ' A new Build is live on itch and github! \n The latest commit information is: \n' + 'The Commit ID is: ' + str(dick['ID']) + '\n' + 'The Commit Date is: ' + dick['LastDate'] + '\n' + 'The Commit Message is: ' + dick['Message']
    await channel.send(messToSend)
    sys.exit()

client.run(os.getenv('DISCORD_TOKEN'))

