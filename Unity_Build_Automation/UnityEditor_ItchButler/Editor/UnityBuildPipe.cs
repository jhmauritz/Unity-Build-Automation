using System.Collections.Generic;
using UnityEditor;
using UnityEditor.Build.Reporting;
using UnityEngine;

public class UnityBuildPipe : MonoBehaviour
{

    [MenuItem("File/Build All")]
    static void BuildAll()
    {
        var scenes = EditorBuildSettings.scenes;
        BuildPipeline.BuildPlayer(scenes, "buildloc", BuildTarget.StandaloneWindows, BuildOptions.None);
        BuildPipeline.BuildPlayer(scenes, "buildloc", BuildTarget.StandaloneLinux64, BuildOptions.None);
        BuildPipeline.BuildPlayer(scenes, "buildloc", BuildTarget.StandaloneOSX, BuildOptions.None);
        BuildPipeline.BuildPlayer(scenes, "buildloc", BuildTarget.WebGL, BuildOptions.None);
    }

    [MenuItem("File/Build Windows")]
    static void BuildWindows()
    {
        BuildPipeline.BuildPlayer(EditorBuildSettings.scenes, "buildloc", BuildTarget.StandaloneWindows, BuildOptions.Development);
    }

    [MenuItem("File/Build Linux")]
    static void BuildLinux()
    {
        BuildPipeline.BuildPlayer(EditorBuildSettings.scenes, "buildloc", BuildTarget.StandaloneLinux64, BuildOptions.None);
    }

    [MenuItem("File/Build OS X")]
    static void BuildOSX()
    {
        BuildPipeline.BuildPlayer(EditorBuildSettings.scenes, "buildloc", BuildTarget.StandaloneOSX, BuildOptions.None);
    }

    [MenuItem("File/Build WebGL")]
    static void BuildWebGL()
    {
        BuildPipeline.BuildPlayer(EditorBuildSettings.scenes, "buildloc", BuildTarget.WebGL, BuildOptions.None);
    }

    static void PerformAssetBundleBuild()
    {
        BuildPipeline.BuildAssetBundles("../AssetBundles/", BuildAssetBundleOptions.ChunkBasedCompression, BuildTarget.StandaloneLinux64);
        BuildPipeline.BuildAssetBundles("../AssetBundles/", BuildAssetBundleOptions.ChunkBasedCompression, BuildTarget.StandaloneWindows);
        BuildPipeline.BuildAssetBundles("../AssetBundles/", BuildAssetBundleOptions.ChunkBasedCompression, BuildTarget.StandaloneOSX);
        BuildPipeline.BuildAssetBundles("../AssetBundles/", BuildAssetBundleOptions.ChunkBasedCompression, BuildTarget.WebGL);
    }
}
