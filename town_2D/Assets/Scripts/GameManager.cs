using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.Diagnostics;
using System.IO;
using System.Text;

public class GameManager : MonoBehaviour
{
    // Start is called before the first frame update
    //pythonがある場所
    private string pyExePath = @"/Users/murase/anaconda3/bin/python";

    //実行したいスクリプトがある場所
    private string pyCodePath = @"/Users/murase/Unity/town_2D/Assets/GPTstart.py";
    //セリフ
    private string words;
    void Start()
    {
        //外部プロセスの設定
        ProcessStartInfo processStartInfo = new ProcessStartInfo() {
            FileName = pyExePath, //実行するファイル(python)
            UseShellExecute = false,//シェルを使うかどうか
            CreateNoWindow = true, //ウィンドウを開くかどうか
            RedirectStandardOutput = true, //テキスト出力をStandardOutputストリームに書き込むかどうか
            Arguments = pyCodePath 
        };
        
        //外部プロセスの開始
        Process process = Process.Start(processStartInfo);
        using (StreamReader streamReader = new StreamReader(process.StandardOutput.BaseStream, Encoding.UTF8))//標準出力からテキストを取得してUnityに渡す
        {
            words = streamReader.ReadLine();
            UnityEngine.Debug.Log(words);
        }
        //外部プロセスの終了
        process.WaitForExit();
        process.Close();

    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
