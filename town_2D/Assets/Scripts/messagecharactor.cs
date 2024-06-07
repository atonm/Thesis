
using UnityEngine;
using UnityEngine.UI;
using System.Diagnostics;
using System.IO;
using System.Text;
public class messagecharactor : MonoBehaviour
{
    public GameObject dialogue;
    public Text Text;

   [SerializeField] 
   string words = "";
   [SerializeField] 
   int npc = 1;//NPC番号

    //pythonがある場所
    private string pyExePath = @"/Users/murase/anaconda3/bin/python";

    //実行したいスクリプトがある場所
    private string pyCodePath = @"/Users/murase/Unity/town_2D/Assets/lines.py";

    private void Start () {

    }    
    private void OnCollisionEnter2D(Collision2D other)
     {
        if (other.gameObject.CompareTag("Player"))
        {
        //外部プロセスの設定
        ProcessStartInfo processStartInfo = new ProcessStartInfo() {
            FileName = pyExePath, //実行するファイル(python)
            UseShellExecute = false,//シェルを使うかどうか
            CreateNoWindow = false, //ウィンドウを開くかどうか
            RedirectStandardOutput = true, //テキスト出力をStandardOutputストリームに書き込むかどうか
            Arguments = pyCodePath + " " + npc, //実行するスクリプト 引数(複数可)
        };
        //外部プロセスの開始
        Process process = Process.Start(processStartInfo);
        using (StreamReader streamReader = new StreamReader(process.StandardOutput.BaseStream, Encoding.UTF8))//Pythonで生成したセリフを取得
        {
           /* while (!streamReader.EndOfStream)
        {
            string line = streamReader.ReadLine();
            
            words+=line;
        }*/
            words = streamReader.ReadLine();
            UnityEngine.Debug.Log(words);
        }
        Text.text = words;
        dialogue.SetActive (true);//テキスト表示
        
        //外部プロセスの終了
        process.WaitForExit();
        process.Close();
            
        }
    }

    private void OnCollisionExit2D(Collision2D other)//プレイヤーがNPCから離れたらテキストボックスを非表示に
     {
        if (other.gameObject.CompareTag("Player"))
        {
   dialogue.SetActive (false);
   words="";
        }
    }
}