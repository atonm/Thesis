import GPTstart as gpt
#履歴リセット
messages=[]
for i in range(gpt.npcnumber):
  gpt.npc_conversation_history[i+1]=False