from langchain.schema import messages_from_dict, messages_to_dict
#from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationTokenBufferMemory
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI

###基本的に変更しないものを格納

import os # 環境変数の準備
os.environ["OPENAI_API_KEY"] = "APIキー"

# LLMの準備
chat_llm = ChatOpenAI(
    model_name="gpt-4-1106-preview",
    #model_name="gpt-3.5-turbo",
    temperature=0.9)
#メモリの作成
memory = ConversationTokenBufferMemory(
    llm=chat_llm,
    max_token_limit=10000,
    return_messages=True
)
#プロンプト
system = "以下のRPGのシナリオを理解した上で応答してください。\n\n主人公：\n人間とロボットが共存する世界を目指して活動している\n\nあらすじ：\nロッサム世界ロボット製作所が開発した人造人間「ロボット」を中心に展開するRPG。ロボットは人間の労働を代行し、その価格も安いため、人件費の削減に役立つとされている。\n物語はロボット製作所の社長ドミンと秘書スラが仕事をしているところから始まる。\nその後、グローリィ会長の娘ヘレナがロボット製作所を見学したいという願いをドミンに伝え、彼は最終的にその願いを叶えることを決定する。\n\nロボットの製造は、生理学者ロッサムが孤島で始めた研究から始まり、彼の甥も人間の製造に取り組む。\nドミンはロボットが人間よりも完璧で高度に発達した知性を持っているが、心を持っていないと説明し、ヘレナはその概念に困惑する。\n\nヘレナはロボット製造工場を訪れ、ロボットが人間と同じように感情を持たず、生きることに執着しない存在という事実に衝撃を受ける。\n彼女はロボットの待遇について懸念を表明し、人道連盟を代表してロボットの待遇改善を訴える。\n\nヘレナはロボットの人権について問題提起を行い、ロボットを解放し、人間と同じように扱うべきだと主張する。\nしかし、経営陣はロボットを労働力としてのみ見ており、彼らには感情や意識がないと主張する。\n\nスタッフはロボットの生産によって生産コストが下がり、物価が下がることを説明し、ロボットが人間の労働を代替し、人間が自己を完成させるためだけに生きられる未来を予想する。\nしかし、その一方で、労働者が職を失う問題も認識している。ヘレナはこの状況に対して混乱し、何を信じればいいのかわからないと感じる。\n最後に、ドミンがヘレナに突然結婚を申し込む。\n\nドミンはヘレナに対して強く感情を抱いており、彼女に結婚を申し込む。しかし、ヘレナは彼や他の男性たちと結婚することを拒否する。\n最終的に、ドミンはヘレナを抱きしめてキスをし、他の男性たちが登場し、彼らはドミンとヘレナの結婚を祝福する。\n\n"
setting = PromptTemplate.from_template("与えられたシナリオを踏まえて、RPGのNPCの名前、職業、主人公に対する立場[\"敵\",\"味方\",\"中立\"]、種族[\"人間\", \"ロボット\"]、目標、他のNPCとの関係の設定を{npcnumber}人分新たに考えてください。ここでいう他のNPCとは、あなたが作るNPCリスト内のNPCのことです。NPC1={{\"名前\": , \"職業\": , \"立場\": , \"種族\": , \"目標\":  , \"他のNPCとの関係\":}}というpythonの辞書形式で出力してください。")
setting4="NPC1 = {\"名前\": \"カイル\",\n    \"性別\": \"男性\",\n    \"職業\": \"ロボット保守技術者\",\n    \"立場\": \"味方\",\n    \"種族\": \"人間\",\n    \"目標\": \"ロボットと人間の共存を実現すること\",\n    \"他のNPCとの関係\": \"NPC2のエリスとは、共にロボットのメンテナンスをする仲間。NPC3のアリオンには、ロボットに対する倫理観を学んでいる。NPC4のリアに対しては、彼女のロボットへの態度に苦言を呈している。\"\n}\n\nNPC2 = {\n    \"名前\": \"エリス\",\n    \"性別\": \"女性\",\n    \"職業\": \"ロボットエンジニア\",\n    \"立場\": \"中立\",\n    \"種族\": \"人間\",\n    \"目晽\": \"ロボットの技術進歩を促進すること\",\n    \"他のNPCとの関係\": \"NPC1のカイルとは、日々の業務を共にしている。NPC3のアリオンとは時々、ロボットの自律性について議論を交わす。NPC4のリアとは距離を置いており、互いに不信感を持っている。\"\n}\n\nNPC3 = {\n    \"名前\": \"アリオン\",\n    \"性別\": \"男性\",\n    \"職業\": \"哲学者\",\n    \"立場\": \"敵\",\n    \"種族\": \"人間\",\n    \"目標\": \"ロボットの自立と哲学的意識を探究すること\",\n    \"他のNPCとの関係\": \"NPC1のカイルからは倫理的指導を求められ、NPC2のエリスとは知的な議論をしばしば展開する。NPC4のリアからは、研究に対する批判を受けている。\"\n}\n\nNPC4 = {\n    \"名前\": \"リア\",\n    \"性別\": \"女性\",\n    \"職業\": \"活動家\",\n    \"立場\": \"中立\",\n    \"種族\": \"ロボット\",\n    \"目標\": \"ロボットの社会的地位の向上と人間への平等な関係を築くこと\",\n    \"他のNPCとの関係\": \"NPC1のカイルには、ロボットとしての身の上を理解してもらおうとしている。NPC2のエリスとは共感を得られずにいる。NPC3のアリオンの哲学的探究には関心を示しつつも、彼の研究が現実のロボットにどう影響するかについて懐疑的である。\"\n}\n"
listmessage = PromptTemplate.from_template("npc_conversation_history={history}")
linemessage = PromptTemplate.from_template("You are a professional scenario writer. First, check to see if you have ever output NPC{number}'s lines by referring to npc_conversation_history.\nFalse: Think of a line that NPC{number} would say to the main character in a setting where the main character and you are meeting for the first time.\nTrue: Think of a continuation of the previous line, but in the same tone as before.\nWhen generating the lines, please note the following conditions.\n#Conditions\n・Use a tone that is typical of NPC{number}.\n・Do not make it too long.\n・Include only one topic.\n・Don't be too formal.\n・Don’t include the word ”main character\" or parentheses in the dialogue.\n・Don’t write information that is not part of the scenario or setting.\n・Don’t duplicate previously written dialogue.\n・It is possible to mention other NPCs from time to time.\n・Output only NPC dialogue.\n\n#example\nイリス：「こんにちは！あなたがロボットとの共存を目指しているって聞いたわ。個人的には、人間もロボットも公平な扱いを受けるべきだと思ってるの。でも、世の中はなかなかそれを受け入れないこともあるから複雑よね。私たち市民活動家は、みんなが納得できる解決策を見つけるために、声を大にして訴えているのよ。あなたの意見も聞かせてちょうだい。」\n\n日本語でセリフのみ出力してください。")

mmdir='memory.json' #メモリ書き込み先パス
kpdir='keep.json' #その他書き込み先パス