# coding: UTF-8
import json
from langchain.schema import messages_to_dict
from langchain.chains import ConversationChain
from langchain.schema import SystemMessage
import GPTmodule as gptm

talkcount=1#セリフ生成回数初期設定。０じゃないのはわざと
npcnumber=4 #生成するNPCの人数

#会話履歴辞書作成
npc_conversation_history={}
for i in range(npcnumber):
  npc_conversation_history[i+1]=False

#設定、会話履歴準備
gptm.memory.chat_memory.add_message(SystemMessage(content=gptm.system))#システム欄追加
conversation = ConversationChain(memory=gptm.memory, llm=gptm.chat_llm)#会話の準備
#npcsetting=conversation.predict(input=gptm.setting.format(npcnumber=npcnumber))#設定生成プロンプトを入力、生成、設定を保存
npcsetting=gptm.setting4
gptm.memory.chat_memory.add_user_message(npcsetting)
gptm.memory.chat_memory.add_user_message(gptm.listmessage.format(history=str(npc_conversation_history)))#辞書を履歴に追加
print(npcsetting)

#必要なデータだけ別ファイルに保存
keep={"talkcount":talkcount,"history":npc_conversation_history,"setting":npcsetting} #メモリ以外をまとめて辞書へ
memory = messages_to_dict(gptm.memory.chat_memory.messages) #memoryを辞書型に変えとかないとエラー
with open(gptm.mmdir, mode="wt", encoding="utf-8") as f: #memory書き込み
	json.dump(memory, f, ensure_ascii=False, indent=2)
f.close()

#メモリが圧迫された時に追い出されたら困るものはkeepにも避けておく
with open(gptm.kpdir, mode="wt", encoding="utf-8") as f: #keep書き込み
	json.dump(keep, f, ensure_ascii=False, indent=2)
f.close()
