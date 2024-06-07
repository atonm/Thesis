# coding: UTF-8
import sys #引数を得るために使用
import json
from langchain.schema import messages_from_dict, messages_to_dict
from langchain.chains import ConversationChain
from langchain.schema import SystemMessage
import GPTmodule as gptm


with open(gptm.mmdir, mode="rt", encoding="utf-8") as f:#メモリ読み込み
	memory = json.load(f)		# JSONのファイル内容をdictに変換する。
f.close()
with open(gptm.kpdir, mode="rt", encoding="utf-8") as f:#その他読み込み
	keep = json.load(f)		# JSONのファイル内容をdictに変換する。
f.close()

talkcount=int(keep["talkcount"])
history=keep["history"]
setting=keep["setting"]

#memory復元
gptm.memory.chat_memory.messages = messages_from_dict(memory)
#print(memory)
#会話の準備
conversation = ConversationChain(memory=gptm.memory, llm=gptm.chat_llm)

number=sys.argv[1]#セリフ生成したいNPCの番号
response=conversation.predict(input=gptm.linemessage.format(number=number))#セリフ生成、保存
talkcount+=1#会話回数更新
keep["talkcount"]=talkcount

#会話済みリスト更新
if history[number]==False:
  history[number]=True
  listmessage = "npc_conversation_history=" + str(history) + "\n変更しました。把握しておいてください。"
  gptm.memory.chat_memory.add_user_message(listmessage)
  keep["history"]=history
 
if talkcount%3==0:#n回に一回keepの内容を思い出してもらう。トークン上限対策
  gptm.memory.chat_memory.add_message(SystemMessage(content=gptm.system))#システム欄追加
  gptm.memory.chat_memory.add_user_message(setting)#辞書を履歴に追加
  gptm.memory.chat_memory.add_user_message(listmessage)#辞書を履歴に追加
  
print(response)#セリフ表示

#別ファイルのデータ上書き保存
new_memory = messages_to_dict(gptm.memory.chat_memory.messages) #memoryを辞書型に変えとかないとエラー
with open(gptm.kpdir, mode="wt", encoding="utf-8") as f:
	json.dump(keep, f, ensure_ascii=False, indent=2)
f.close()
with open(gptm.mmdir, mode="wt", encoding="utf-8") as f:
	json.dump(new_memory, f, ensure_ascii=False, indent=2)
f.close()