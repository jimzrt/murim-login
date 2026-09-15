# Fidelity Gate — Chapter 86

Audit the complete assembled English chapter against the Korean source.
Report only genuine source-fidelity defects: wrong action, subject, object,
causality, quantity, mechanism, terminology, ambiguity, joke logic, register,
or physical detail. Check repeated UI labels and counters against how they
behave across the whole scene. Interpret idioms by their function, not by
translating their component words. Do not report optional stylistic rewrites.
Do not invent `current` spans that are absent from the assembled English.
Do not report a glossary-correct rendering as a defect merely because the
baseline used an older synonym.

Return exactly one JSON object and no Markdown fence:

{
  "summary": "brief assessment",
  "findings": [
    {
      "id": "F01",
      "severity": "critical|major|minor",
      "source": "source location",
      "current": "exact uniquely occurring English span",
      "defect": "specific fidelity defect",
      "replacement": "finished replacement only when necessary",
      "rationale": "source-grounded reason",
      "confidence": 0.0
    }
  ]
}

Use an empty findings array when the chapter is faithful. A critical or major
finding blocks promotion; minor findings are recorded for human inspection.

## Korean source

```text
  1|＃86화
  2|
  3|
  4|
  5|“아이고, 고생하셨습니다.”
  6|
  7|담당 공무원이 허겁지겁 뛰쳐나와 우리를 맞이했다.
  8|
  9|뭐, 정확히는 임창수를 맞이했다고 해야 옳겠지.
 10|
 11|우리가 가져온 각종 부산물이며 마정석을 꼼꼼하게 확인한 그가 호들갑을 떤다.
 12|
 13|“이야, 물량이 엄청나네요. 이 정도면 미로에 있는 미노타우로스들이 씨가 말랐겠어요.”
 14|
 15|“…….”
 16|
 17|창백한 안색의 임창수가 대답 없이 고개만 끄덕이니 담당 공무원이 눈치를 살폈다.
 18|
 19|“팀장님, 혹시 편찮으신 곳이라도?”
 20|
 21|언제부터 담당 공무원이 헌터 건강까지 챙겨 줬는지 모르겠군.
 22|
 23|나는 괜한 말이 나오기 전에 임창수를 옆구리를 쿡 찔렀다.
 24|
 25|“대답하셔야죠. 창. 수. 씨.”
 26|
 27|“……아닙니다. 전 괜찮아요.”
 28|
 29|“아, 그러시다면 다행이고요.”
 30|
 31|이상한 분위기를 감지한 걸까? 담당 공무원이 미심쩍은 눈빛으로 나를 쳐다봤지만 딱 거기까지였다.
 32|
 33|“부산물 처리는 어떻게 하시겠습니까? 아시는 대로 두 가지 방법이 있습니다만.”
 34|
 35|담당 공무원의 말대로 부산물의 판매 방식은 두 가지로 나뉜다.
 36|
 37|개인 판매와 위탁 판매. 전자의 경우는 말 그대로 해당 물품의 소유주인 개인이 알아서 거래를 하는 방식이고, 위탁 판매는 관리청, 즉 정부 기관에 맡겨 판매하는 거다.
 38|
 39|‘각기 장단점이 있지.’
 40|
 41|희소성이 있는 물건은 개인 판매가 이득이고, 그게 아니라면 정부 기관에 넘기는 게 속 편하다. 명품 경매와 시장 경매의 차이랄까?
 42|
 43|“어떻게 할까요?”
 44|
 45|임창수의 물음에 김 집사가 나섰다. 이번 게이트의 레이드에서는 한 번도 나선 적 없지만 그도 베테랑 헌터다. 오히려 이쪽에 대해선 이 중 누구보다도 더 빠삭할 것이다.
 46|
 47|“관리청에 판매하겠습니다.”
 48|
 49|소는 버릴 게 없다더니, 미노타우로스도 마찬가지였다.
 50|
 51|가죽은 장비 제작에, 뼈는 푹 고아 보양식으로 쓰이며 뿔은 마니아들에게 수집품으로 인기가 있다.
 52|
 53|“잘 생각하셨습니다.”
 54|
 55|담당 공무원이 세상 기쁜 표정으로 부산물을 정산하기 시작했다. 사는 건 관리청인데 저 아저씨가 좋아하는 이유는 뻔하다.
 56|
 57|‘떡고물 좀 떨어지나 보네.’
 58|
 59|뭐, 담당 공무원이 얼마를 해 먹든 내 알 바 아니다.
 60|
 61|오늘 내가 챙긴 떡고물이 훨씬 크니까.
 62|
 63|툭툭.
 64|
 65|“약속한 금액은?”
 66|
 67|임창수가 바짝 굳은 얼굴로 대답했다.
 68|
 69|“드, 드리겠습니다.”
 70|
 71|“언제까지?”
 72|
 73|“내일까지 보내 드리겠습니다.”
 74|
 75|40억을 내일까지? 확실히 부잣집 아들이라 시원시원하다. 나는 활짝 웃으며 쪽지를 건넸다.
 76|
 77|“어휴, 그럼 나야 좋지. 여기 내 계좌 번호. 가보처럼 간직하고 있다가 내일 보내 줘. 나중에 잃어버렸다고 하면 재미없어요. 알죠?”
 78|
 79|“……넵.”
 80|
 81|이 정도면 됐겠지? 나는 임창수의 등을 툭 치는 걸로 작별 인사를 대신했다.
 82|
 83|비틀거리는 걸음으로 멀어지는 녀석의 뒷모습을 흐뭇하게 지켜보고 있던 내게 임꺽정이 물었다.
 84|
 85|“저놈이 약속한 돈을 줄까?”
 86|
 87|“안 주면요?”
 88|
 89|“그 뭐냐. 좀 거시기 하잖아. 상동 길드면 근방에서 힘깨나 쓰는 중견 길드인데. 저놈이 배 째라 식으로 나오면…….”
 90|
 91|“에이, 증거 영상도 있는데 설마.”
 92|
 93|“증거야 없애면 되는 거고. 뭣보다 내가 좀 들은 게 있어서 그래.”
 94|
 95|“그게 뭔데요?”
 96|
 97|이렇게까지 말하니까 살짝 신경이 쓰이기 시작한다.
 98|
 99|잠시 눈치를 살피며 주위를 두리번거린 임꺽정이 작은 목소리로 속삭였다.
100|
101|“상동 길드장. 누군지는 대충 알지?”
102|
103|“네. 이름은 오늘 처음 들어 봤지만.”
104|
105|임춘수. 왠지 모르게 술배 불룩하게 나온 중년 아저씨가 연상되는 이름이지만 상상과 현실은 정반대다.
106|
107|“대격변 때 혁혁한 전공을 세웠던 A급 헌터잖아요. 사람들이 뭐라고 부르더라? 프, 프. 갑자기 생각이 안 나네.”
108|
109|“프로즌(Frozen).”
110|
111|“아, 맞다. 프로즌. 빙결 전문 마법사.”
112|
113|유명한 헌터들의 경우 그에 맞는 이명(異名)이 붙는다.
114|
115|임춘수의 경우도 그랬다. A급 헌터인 그는 대격변에서 큰 활약을 보여 준 마법사였고, 그중에서도 특히 빙결 관련 마법에 능해서 프로즌이라는 이명이 붙었다.
116|
117|“그 양반이 빙결 계통으로는 국내 다섯 손가락 안에 들지. 그 명성을 바탕으로 지금의 상동 길드를 키워 낸 거고.”
118|
119|처절했던 대격변이 종막을 고하자 1세대 헌터들은 선택의 기로에 섰다. 은퇴를 할 것인가, 현역으로 남을 것인가. 임춘수는 후자를 선택했고 상동 길드를 세웠다.
120|
121|“대단하네요. 아들은 별거 없던데.”
122|
123|아무리 A급 헌터라도 맨주먹 하나로 대격변에서 살아남아 부와 명예 모두를 얻은 경우는 흔치 않다. 임춘수의 현재는 많은 헌터들이 꿈꾸는 미래다.
124|
125|“대단? 확실히 대단하지. 핏줄이라는 게.”
126|
127|임꺽정이 멀어져 가는 임창수의 뒷모습을 턱짓했다.
128|
129|“저 녀석이 누구 피를 물려받았는지 잊지 마라.”
130|
131|“그게 무슨…….”
132|
133|“자랑은 아니지만 내가 이 바닥 생활 시작한 지 20년이 넘었어. 내가 생초짜이던 시절에 상동 길드가 세워졌지.”
134|
135|“그런데요?”
136|
137|“지금도 그렇지만 당시 부천은 길드들끼리 경쟁이 치열했거든. 도저히 신생 길드가 끼어들 틈이 없었어.”
138|
139|“임춘수는 그걸 뚫었다?”
140|
141|“그렇지. 그래서 무서운 사람인 거고.”
142|
143|“음.”
144|
145|이게 그렇게 연결이 되나?
146|
147|길드 간 경쟁 심리야 하루 이틀 일이 아니고 능력 있는 쪽이 살아남는 건 실력 위주의 사회에선 당연한 일이다.
148|
149|“그 사람 정도면 헌터로서의 능력도 출중하고 명성도 있었잖아요. 인맥도 빵빵했을 거고.”
150|
151|“다른 길드장들은 아니었을 것 같냐?”
152|
153|“네?”
154|
155|“임춘수에 비해 명성은 조금 부족했을지 몰라도 하나같이 다 전쟁 영웅 출신들이었어. 상동 길드보다 몇 년이나 앞서 시장을 개척하고 상당수의 게이트를 점유하고 있었지.”
156|
157|임꺽정이 낮은 목소리로 말을 이었다.
158|
159|“아직 체계가 완벽히 잡히지 않아서 온갖 불법이 횡행할 때였다. 지금 상동 길드가 존재할 수 있는 건 임춘수가 경쟁자들을 모두 박살 냈기 때문이야. 결코 호락호락한 사람이 아니라는 거지.”
160|
161|문득 뇌리를 스치는 생각이 있었다.
162|
163|임춘수가 오늘 있었던 일을 알게 된다면? 하나뿐인 아들이 개망신을 당했다는 말에 어떤 반응을 보일까?
164|
165|‘일이 좀 꼬일 수도 있겠는데.’
166|
167|대한민국 하면 빼놓을 수 없는 것이 학연, 지연, 혈연이다.
168|
169|20년간 한자리를 굳건히 자리를 지킨 상동 길드가 지역 유지라면 우리 길드는 신생아나 다름없는 수준.
170|
171|상동 길드가 작정하고 덤비면 출생 신고서부터 찢어질 거다.
172|
173|“혹시 상동 길드장, 성격 좋아요?”
174|
175|“나야 모르지. 소문으로만 대충 들었어.”
176|
177|“그것만이라도 알려 줘요.”
178|
179|잠시 고민하던 임꺽정이 대답했다.
180|
181|“오늘 임창수를 보니까 옛말이 하나 떠오르더라. 호부견자(虎父犬子).”
182|
183|“훌륭한 아버지에 못난 아들이라면 어쨌든 좋은 뜻이잖아요. 말은 통하는 사람인가?”
184|
185|“아니, 한자 그대로 해석해 봐.”
186|
187|“……호랑이 아버지에 개 아들?”
188|
189|“임창수 성격이 개새끼면 임춘수는 호랑이야. 성격이 아주 지랄 맞대.”
190|
191|“…….”
192|
193|“나이 먹고 성격 죽었다는 얘기도 있는데, 사람 성격이 그렇게 쉽게 바뀔까 싶다.”
194|
195|이런 시발.
196|
197|들으면 들을수록 왠지 등골이 서늘한 게, 꼭 무슨 일이 하나 터질 것 같은 느낌이다.
198|
199|‘아씨, 내기하지 말 걸 그랬나.’
200|
201|수십억을 받을 생각에 한껏 들뜬 것도 잠시. 이제는 큰일 보고 뒤 안 닦은 것처럼 찝찝하다.
202|
203|나야 둘째치고 다른 길드원들이 피해를 입는 건 절대 사양인데.
204|
205|“태경아, 너무 신경 쓰지 마라. 나도 혹시나 해서 말해 본 거니까.”
206|
207|“이거 사고 친 거 아니겠죠?”
208|
209|“괜찮아. 최 팀장도 재미있다고 내기 거들었잖아.”
210|
211|“어, 맞네?”
212|
213|“그렇지. 그리고 임창수 저놈 하는 짓 봐라. 내가 아버지였으면 반쯤 죽여 놨을걸. 쪽팔려서 어디에 말도 못 해.”
214|
215|확실히 일리가 있군. 뭐 별일이야 있겠어?
216|
217|그 얘길 들으니 한결 마음이 가벼워진다. 저절로 웃음이 나올 정도다.
218|
219|“고마워요. 꺽정 아저씨, 아니 형님.”
220|
221|“그럼 갑부 된 기념으로 소고기 사. 아니지, 나 말고 송 양이랑 먹어야지.”
222|
223|“……아.”
224|
225|가슴에 대못을 박는구나.
226|
227|사람 두 번 죽이는 임꺽정의 말에 나는 눈물을 삼켰다.
228|
229|
230|
231|* * *
232|
233|
234|
235|“무슨 일로 왔나?”
236|
237|목소리의 주인은 이색적인 외모의 사내였다.
238|
239|오십 줄에 접어든 나이였으나 피부는 팽팽했고 철사처럼 뻗친 머리카락은 검었다. 부리부리한 눈매는 보는 것만으로도 오금을 저리게 했다.
240|
241|‘무슨 놈의 눈빛이…….’
242|
243|K은행의 지점장에게도 그건 예외는 아니었다. 이미 수차례 만난 적 있지만 자신은 일반인이었고 상대는 A급 헌터, 그것도 대격변을 온몸으로 겪은 산증인이 아닌가.
244|
245|저절로 혀가 꼬이고 식은땀이 흘렀다.
246|
247|“그게…….”
248|
249|“아까운 시간 뺏으러 온 거면 그만 돌아가고. 아니면 이 자리에서 당장 얘기하게.”
250|
251|내용은 날이 섰지만 말투는 제법 온화하다.
252|
253|나이 먹고 성격 죽이려고 노력한다는 소문은 들었는데 아예 헛수고는 아닌 모양이었다.
254|
255|‘에이, 시발.’
256|
257|지점장은 눈을 딱 감고 질렀다.
258|
259|“죄송합니다, 길드장님. 아드님 일로 찾아뵈었습니다.”
260|
261|아드님. 그 세 글자에 상동 길드장 임춘수의 눈썹이 꿈틀거렸다.
262|
263|“창수? 그 녀석이 왜?”
264|
265|“일전에 아드님께서 은행 관련 업무를 이용하게 되면 꼭 알려 달라고 하셔서…….”
266|
267|임춘수가 감 잡았다는 듯이 고개를 끄덕였다.
268|
269|“이번엔 뭔가? 내 인감이라도 훔쳤나? 아니면 담보 대출?”
270|
271|“상당한 금액을 한 번에 이체하셨습니다.”
272|
273|“또 계집질이겠지. 뻔해. 액수가 어떻게 되나?”
274|
275|“두 개의 계좌에 각기 40억씩. 합해서 80억입니다.”
276|
277|“얼마?”
278|
279|“80억…… 헙.”
280|
281|지점장은 황급히 숨을 삼켰다. 임춘수의 등 뒤에 있는 유리창이 빠르게 얼어붙는 광경을 목격했기 때문이었다.
282|
283|파스스.
284|
285|밖은 늦여름인데 사무실을 지배한 것은 추위와 냉기다.
286|
287|오들오들 떨고 있는 지점장에게 그가 손짓했다.
288|
289|“더 할 말은?”
290|
291|“과, 관련 자료를 가져왔습니다.”
292|
293|지점장이 떨리는 손으로 책상 위에 서류 뭉치를 내려놨다.
294|
295|“잘했어. 이만 나가 보게.”
296|
297|“다, 다음에 뵙겠습니다.”
298|
299|지점장이 도망치듯 방 안을 빠져나간 뒤 임춘수는 수화기를 들었다. 냉기 저항 기능이 있는 전화기는 아무 문제 없이 빠르게 신호를 발신했다.
300|
301|뚜, 뚜, 달칵.
302|
303|- 네. 길드장님. 1팀장 전화 받았습니다.
304|
305|“그 자식 당장 잡아 와.”
306|
307|- ……임창수 팀장 말씀이십니까?
308|
309|“팀장은 무슨. 오늘부터 해고야. 그 새끼 당장 잡아 와!”
310|
311|쾅! 수화기의 수명은 거기까지였다. 수백 조각으로 나뉜 얼음 파편이 책상 위를 덮었다.
312|
313|“이런 한심한, 내 그리 일렀는데도…….”
314|
315|서늘한 눈으로 난장판이 된 사무실을 노려보던 임춘수의 시선이 한곳에 멎었다. K은행의 지점장이 놓고 간 서류 뭉치.
316|
317|저 안에 80억의 행방이 들어 있을 게 분명했다.
318|
319|‘멍청한 놈. 이번에는 어느 년한테 홀랑 넘어간 거냐?’
320|
321|한 장, 한 장 넘겨 가며 읽기를 십여 분.
322|
323|임춘수가 마지막 장을 덮었을 때, 누군가 질질 끌려오는 소리와 함께 문이 활짝 열렸다.
324|
325|“임창수 팀장. 여기 데려왔습니다.”
326|
327|푸근한 인상의 중년인. 그리고 중년에게 꽉 붙잡힌 한 청년.
328|
329|“아, 아버지!”
330|
331|“내 자랑스러운 아들 왔구나.”
332|
333|아들의 등장에 아버지가 손을 내밀었다.
334|
335|물론 결코 용서의 의미는 아니었다.
336|
337|파츠츠츠.
338|
339|임춘수의 손아귀에서 냉기가 솟구친다. 기체에서 액체, 액체에서 고체로 변한 그것은 강철만큼 단단한 얼음 몽둥이로 변화를 끝마쳤다.
340|
341|“물어볼 게 많지만 우선 맞자.”
342|
343|“아버지!”
344|
345|“닥쳐, 이 새끼야!”
346|
347|임창수를 데려온 중년인, 상동 길드의 1팀장은 조용히 문을 닫았다. 앞으로 반나절 동안 이곳은 출입 금지다.
```

## Assembled English

```markdown
[P1]
# Chapter 86

[P2]
“Oh, thank you for your hard work.”

[P3]
The government official in charge came rushing out to greet us.

[P4]
Well, more accurately, he came to greet Im Changsoo.

[P5]
After meticulously checking all the byproducts and Magic Gems we had brought, he made a fuss.

[P6]
“Wow, that’s an incredible haul. You must’ve wiped out every Minotaur in the labyrinth.”

[P7]
“…”

[P8]
Im Changsoo’s face was pale. He only nodded without answering, making the official glance around uneasily.

[P9]
“Team Leader, are you feeling unwell?”

[P10]
Since when did government officials start worrying about Hunters’ health?

[P11]
Before he could say anything unnecessary, I jabbed Im Changsoo in the ribs.

[P12]
“You have to answer him. Chang. Soo.”

[P13]
“Um… No, I’m fine.”

[P14]
“Ah, that’s a relief, then.”

[P15]
Maybe he had sensed the strange atmosphere. The official gave me a suspicious look, but that was as far as it went.

[P16]
“How would you like to handle the byproducts? As you know, there are two methods.”

[P17]
As the official said, there were two ways to sell byproducts.

[P18]
Private sales and consignment sales. With the former, the owner handled the transaction personally. With the latter, the goods were entrusted to the Administration—a government agency—to be sold.

[P19]
*Each method has its pros and cons.*

[P20]
Rare items were more profitable to sell privately. For everything else, handing them over to a government agency saved a lot of trouble. It was like the difference between a luxury auction and a market auction.

[P21]
“What should we do?”

[P22]
At Im Changsoo’s question, Butler Kim stepped forward. He hadn’t once taken the lead during this Gate raid, but he was still a veteran Hunter. When it came to this sort of thing, he probably knew more than anyone else here.

[P23]
“We’ll sell them to the Administration.”

[P24]
They said no part of a cow went to waste. The same was true of Minotaurs.

[P25]
Their hides were used to make Equipment, their bones were simmered into restorative food, and their horns were popular collector’s items among enthusiasts.

[P26]
“You’ve made the right choice.”

[P27]
The government official began calculating the value of the byproducts with an expression of pure delight. The Administration was the one buying them, so the reason he was so happy was obvious.

[P28]
*He must be getting a little something off the top.*

[P29]
Still, whatever the official skimmed off wasn’t my concern.

[P30]
The cut I was getting today was much bigger.

[P31]
Tap, tap.

[P32]
“What about the amount you promised?”

[P33]
Im Changsoo answered with a rigid expression.

[P34]
“I-I’ll pay it.”

[P35]
“By when?”

[P36]
“I’ll send it by tomorrow.”

[P37]
Four billion won by tomorrow? The son of a rich family certainly didn’t mess around. I smiled broadly and handed him a slip of paper.

[P38]
“Well, that works for me. Here’s my account number. Treasure it like a family heirloom, then send the money tomorrow. It won’t be funny if you claim you lost it later. Got it?”

[P39]
“…Yes, sir.”

[P40]
That should be enough, right? I said goodbye by giving Im Changsoo a light pat on the back.

[P41]
As I watched with satisfaction as he staggered away, Im Kkeokjeong asked me,

[P42]
“Do you think that punk will actually pay?”

[P43]
“And if he doesn’t?”

[P44]
“Well, you know… things could get a little messy. Sangdong Guild is a mid-tier Guild with some serious influence around here. If he just tells you to do your worst and refuses to pay…”

[P45]
“Come on, we have video evidence. Surely he wouldn’t.”

[P46]
“Evidence can be destroyed. More importantly, I’ve heard a few things.”

[P47]
“Like what?”

[P48]
Now that he had put it that way, I was starting to get a little worried.

[P49]
Kkeokjeong glanced around, checking everyone’s reactions, then leaned in and whispered,

[P50]
“You know who the Sangdong Guild Master is, right?”

[P51]
“Yes. Though today was the first time I heard his name.”

[P52]
Im Chunsoo. For some reason, the name brought to mind a middle-aged man with a bulging beer belly, but the reality was the exact opposite.

[P53]
“He’s an A-rank Hunter who distinguished himself during the Great Cataclysm. What do people call him again? Fro… Fro… It’s suddenly slipping my mind.”

[P54]
“Frozen.”

[P55]
“Ah, right. Frozen. A mage specializing in ice magic.”

[P56]
Famous Hunters were often given epithets that suited their abilities.

[P57]
The same was true of Im Chunsoo. An A-rank Hunter, he was a mage who had played a major role in the Great Cataclysm, and his particular skill with ice magic had earned him the epithet Frozen.

[P58]
“When it comes to ice magic, that man is one of the top five in Korea. He used that Fame to build Sangdong Guild into what it is today.”

[P59]
When the brutal Great Cataclysm finally came to an end, the first-generation Hunters faced a choice.

[P60]
Retire, or remain active.

[P61]
Im Chunsoo chose the latter and founded Sangdong Guild.

[P62]
“That’s impressive. His son doesn’t seem like much.”

[P63]
Even among A-rank Hunters, it was rare for someone to survive the Great Cataclysm with nothing but their bare fists and gain both wealth and fame. Im Chunsoo’s present was the future many Hunters dreamed of.

[P64]
“Impressive? Bloodlines certainly are.”

[P65]
Kkeokjeong jerked his chin toward Im Changsoo’s retreating back.

[P66]
“Don’t forget whose blood that punk inherited.”

[P67]
“What do you mean…?”

[P68]
“I’m not bragging, but I’ve been in this business for over twenty years. Sangdong Guild was founded when I was still a complete rookie.”

[P69]
“And?”

[P70]
“Bucheon was just as fiercely competitive between Guilds back then as it is now. There was no room for a new Guild to squeeze in.”

[P71]
“But Im Chunsoo broke through anyway?”

[P72]
“That’s right. That’s why he’s a frightening man.”

[P73]
“Hmm.”

[P74]
Did that really follow?

[P75]
Competition between Guilds was nothing new, and in a meritocracy, it was only natural for the capable to survive.

[P76]
“A man like him would have had excellent abilities as a Hunter and plenty of Fame. He must have had powerful connections, too.”

[P77]
“Do you think the other Guild Masters didn’t?”

[P78]
“What?”

[P79]
“They might have had slightly less Fame than Im Chunsoo, but every one of them had been a war hero. They had entered the market several years before Sangdong Guild and occupied a substantial number of Gates.”

[P80]
Kkeokjeong continued in a low voice.

[P81]
“It was a time when all kinds of illegal activity ran rampant because the system hadn’t been fully established yet. The only reason Sangdong Guild exists today is that Im Chunsoo crushed every one of his competitors. He’s no pushover.”

[P82]
A thought suddenly flashed through my mind.

[P83]
What would happen if Im Chunsoo found out about what had happened today? How would he react to hearing that his only son had been utterly humiliated?

[P84]
*This could get complicated.*

[P85]
When it came to Korea, you couldn’t leave out school ties, hometown ties, or blood ties.

[P86]
Sangdong Guild had held its ground for twenty years. If it was a local power, our Guild was practically a newborn.

[P87]
If Sangdong Guild came at us in earnest, they’d tear up our birth certificate before we even got started.

[P88]
“Is the Sangdong Guild Master good-natured, at least?”

[P89]
“I wouldn’t know. I’ve only heard rumors.”

[P90]
“At least tell me what you’ve heard.”

[P91]
After thinking for a moment, Kkeokjeong answered,

[P92]
“Seeing Im Changsoo today reminded me of an old saying: a tiger father and a dog son.”

[P93]
“A great father and a worthless son? That’s still a compliment, isn’t it? Is he someone you can reason with?”

[P94]
“No. Interpret it literally.”

[P95]
“…A tiger for a father and a dog for a son?”

[P96]
“If Changsoo’s personality is that of a son of a bitch, then Im Chunsoo is a tiger. I hear his temper is absolutely fucking terrible.”

[P97]
“…”

[P98]
“I’ve also heard he mellowed with age, but can a person’s temper really change that easily?”

[P99]
*For fuck’s sake.*

[P100]
The more I heard, the colder my spine felt. I had the distinct feeling that something was about to go horribly wrong.

[P101]
*Damn it. I shouldn’t have made that bet.*

[P102]
My excitement at the thought of receiving several billion won had lasted only a moment. Now I felt uneasy, like I’d taken a huge dump and forgotten to wipe.

[P103]
I could deal with whatever happened to me, but I absolutely refused to let the other Guild members get hurt.

[P104]
“Taekyung, don’t worry about it too much. I only brought it up just in case.”

[P105]
“I didn’t just cause trouble, did I?”

[P106]
“It’ll be fine. Team Leader Choi thought it sounded fun and joined the bet, too.”

[P107]
“Oh, right.”

[P108]
“Exactly. And look at the way Im Changsoo acted. If I were his father, I would’ve beaten him half to death. He’ll be too embarrassed to tell anyone what happened.”

[P109]
He had a point. What could possibly happen?

[P110]
Hearing that made me feel considerably lighter. I even found myself smiling.

[P111]
“Thanks, Kkeokjeong ajusshi. No, hyungnim.”

[P112]
“Then buy us some beef to celebrate becoming a rich man. Wait, no. You should eat it with Miss Song, not me.”

[P113]
“…Ah.”

[P114]
He was driving a nail straight through my heart.

[P115]
As Im Kkeokjeong killed me with words for the second time, I swallowed my tears.

[P116]
* * *

[P117]
“What brings you here?”

[P118]
The speaker was a man with a distinctive appearance.

[P119]
He was nearing fifty, but his skin was taut and his black hair bristled like wire. His large, piercing eyes alone were enough to make anyone’s knees go weak.

[P120]
*What the hell is with that look in his eyes…?*

[P121]
The manager of a K Bank branch was no exception. He had already met the man several times, but he was an ordinary person, while the other man was an A-rank Hunter—a living witness who had endured the Great Cataclysm with his entire body.

[P122]
His tongue tied itself in knots, and cold sweat trickled down his back.

[P123]
“Well…”

[P124]
“If you came to waste my valuable time, go back. Otherwise, speak now.”

[P125]
The words were sharp, but his tone was fairly gentle.

[P126]
The manager had heard the rumor that Im Chunsoo was trying to mellow his temper with age. Apparently, it hadn’t been a complete waste of effort.

[P127]
*Damn it.*

[P128]
The branch manager squeezed his eyes shut and blurted it out.

[P129]
“I’m sorry, Guild Master. I’ve come regarding your son.”

[P130]
At the mention of his son, Sangdong Guild Master Im Chunsoo’s eyebrow twitched.

[P131]
“Changsoo? What about him?”

[P132]
“Some time ago, you asked me to let you know whenever your son used any of the bank’s services…”

[P133]
Im Chunsoo nodded as if he understood where this was going.

[P134]
“What is it this time? Did he steal my seal? Or take out a secured loan?”

[P135]
“He transferred a considerable amount of money all at once.”

[P136]
“He must be fooling around with women again. Obviously. How much?”

[P137]
“Four billion won to each of two accounts. Eight billion won in total.”

[P138]
“How much?”

[P139]
“Eight billion… Hup.”

[P140]
The branch manager hurriedly swallowed his breath. He had just watched the window behind Im Chunsoo rapidly freeze over.

[P141]
Hiss.

[P142]
It was late summer outside, but cold and frost now ruled the office.

[P143]
Im Chunsoo motioned to the trembling branch manager.

[P144]
“Anything else?”

[P145]
“I-I brought the relevant documents.”

[P146]
With shaking hands, the branch manager placed a stack of papers on the desk.

[P147]
“Good. You may leave.”

[P148]
“I-I’ll see you next time.”

[P149]
After the branch manager fled the room, Im Chunsoo picked up the receiver. The phone had a cold-resistance function, so it transmitted the signal quickly without any problems.

[P150]
Beep, beep. Click.

[P151]
—Yes, Guild Master. Team One’s Leader speaking.

[P152]
“Bring that bastard here immediately.”

[P153]
—…Do you mean Team Leader Im Changsoo?

[P154]
“Team Leader, my ass. He’s fired as of today. Bring that bastard here now!”

[P155]
Bang!

[P156]
The receiver’s life ended there. It shattered into hundreds of icy fragments that covered the desk.

[P157]
“What a pathetic fool. Even after I warned him…”

[P158]
Im Chunsoo glared coldly at the wrecked office, then his gaze stopped on one spot.

[P159]
The stack of papers left behind by the K Bank branch manager.

[P160]
There was no doubt that the documents contained the whereabouts of eight billion won.

[P161]
*You stupid bastard. Which bitch did you get taken in by this time?*

[P162]
He read through the papers, turning them one page at a time, for more than ten minutes.

[P163]
When Im Chunsoo closed the final page, the door flew open with the sound of someone being dragged along.

[P164]
“Team Leader Im Changsoo. I brought him here.”

[P165]
An affable-looking middle-aged man stood there.

[P166]
Clutched firmly in his grasp was a young man.

[P167]
“F-Father!”

[P168]
“My proud son is here.”

[P169]
At his son’s appearance, the father extended a hand.

[P170]
Of course, it was not a gesture of forgiveness.

[P171]
Crackle, crackle, crackle.

[P172]
Cold surged from Im Chunsoo’s grasp. It changed from gas to liquid, then from liquid to solid, completing its transformation into an ice club as hard as steel.

[P173]
“I have a lot to ask you, but first, you’re getting hit.”

[P174]
“Father!”

[P175]
“Shut up, you little shit!”

[P176]
The middle-aged man who had brought Im Changsoo—the Team Leader of Sangdong Guild’s Team One—quietly closed the door.

[P177]
The room would be off-limits for the next half day.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source, RULES.md, or the exact
glossary requires the change. Exact glossary English wins over an older baseline
synonym for the same Korean key.

```markdown
[P1]
# Chapter 86

[P2]
“Oh, thank you for your hard work.”

[P3]
The government official in charge came rushing out to greet us.

[P4]
Well, more accurately, he came to greet Im Changsoo.

[P5]
After meticulously checking all the byproducts and Magic Gems we had brought, he made a fuss.

[P6]
“Wow, that’s an incredible amount. There can’t be many Minotaurs left in the labyrinth after this.”

[P7]
“…”

[P8]
Im Changsoo’s face was pale. He only nodded without answering, making the official glance around uneasily.

[P9]
“Team Leader, are you feeling unwell?”

[P10]
Since when did government officials start worrying about Hunters’ health?

[P11]
Before he could say anything unnecessary, I jabbed Im Changsoo in the ribs.

[P12]
“You have to answer him. Chang. Soo.”

[P13]
“Um… No, I’m fine.”

[P14]
“Ah, that’s a relief, then.”

[P15]
Maybe he had sensed the strange atmosphere. The official looked at me suspiciously, but that was as far as it went.

[P16]
“How would you like to handle the byproducts? As you know, there are two methods.”

[P17]
As the official explained, there were two ways to sell byproducts.

[P18]
Personal sales and consignment sales. With the former, the individual owner of the goods handled the transaction personally. With the latter, the goods were entrusted to the Administration, meaning a government agency, for sale.

[P19]
*Each method has its pros and cons.*

[P20]
Rare items sold better privately. For everything else, handing it over to a government agency was less of a hassle. It was like the difference between a luxury auction and a market auction.

[P21]
“What should we do?”

[P22]
At Im Changsoo’s question, Butler Kim stepped forward. He hadn’t once taken the lead during this Gate raid, but he was still a veteran Hunter. When it came to this sort of thing, he probably knew more than anyone else here.

[P23]
“We’ll sell them to the Administration.”

[P24]
They said there was nothing to waste from a cow. The same went for Minotaurs.

[P25]
Their hides were used to make Equipment, their bones were boiled down into restorative food, and their horns were popular collector’s items among enthusiasts.

[P26]
“You made the right choice.”

[P27]
The government official began calculating the byproducts with an expression of pure delight. The Administration was the one buying them, so the reason he was happy was obvious.

[P28]
*He must be getting a little something off the top.*

[P29]
Still, whatever the official skimmed off wasn’t my concern.

[P30]
The cut I was getting today was much bigger.

[P31]
Tap, tap.

[P32]
“What about the agreed-upon amount?”

[P33]
Im Changsoo answered with a rigid expression.

[P34]
“I-I’ll pay it.”

[P35]
“By when?”

[P36]
“I’ll send it by tomorrow.”

[P37]
Four billion won by tomorrow? The son of a rich family certainly knew how to be decisive. I smiled broadly and handed him a slip of paper.

[P38]
“Well, that works for me. Here’s my account number. Keep it safe as if it were an heirloom, then send the money tomorrow. It won’t be funny if you say you lost it later. Got it?”

[P39]
“…Yes, sir.”

[P40]
That should be enough, right? I said goodbye by giving Im Changsoo a light pat on the back.

[P41]
As I watched with satisfaction as he staggered away, Im Kkeokjeong asked me,

[P42]
“Do you think that punk will actually pay?”

[P43]
“What happens if he doesn’t?”

[P44]
“You know… it could get a little awkward. Sangdong Guild is a mid-tier Guild with some serious influence around here. If he decides to brazen it out and refuses to pay…”

[P45]
“Come on, we have video evidence. Surely he wouldn’t.”

[P46]
“Evidence can be destroyed. More importantly, I’ve heard a few things.”

[P47]
“Like what?”

[P48]
Now that he had put it that way, I was starting to get a little worried.

[P49]
Kkeokjeong glanced around, checking everyone’s reactions, then leaned in and whispered,

[P50]
“You know who the Sangdong Guild Master is, right?”

[P51]
“Yes. I heard his name for the first time today, though.”

[P52]
Im Chunsoo. For some reason, the name brought to mind a middle-aged man with a bulging drinker’s belly, but reality was the exact opposite.

[P53]
“He’s an A-rank Hunter who made an impressive name for himself during the Great Cataclysm. What do people call him again? Fro… Fro… It’s suddenly slipping my mind.”

[P54]
“Frozen.”

[P55]
“Ah, right. Frozen. A mage specializing in ice magic.”

[P56]
Famous Hunters were often given nicknames to match their abilities.

[P57]
The same was true of Im Chunsoo. An A-rank Hunter, he had made a name for himself as a mage during the Great Cataclysm. He was particularly skilled with ice-related magic, which had earned him the nickname Frozen.

[P58]
“When it comes to ice magic, that man is one of the top five in Korea. He used that Fame to build Sangdong Guild into what it is today.”

[P59]
When the brutal Great Cataclysm finally came to an end, the first-generation Hunters faced a choice.

[P60]
Retire, or remain active.

[P61]
Im Chunsoo chose the latter and founded Sangdong Guild.

[P62]
“That’s impressive. His son doesn’t seem like much.”

[P63]
Even among A-rank Hunters, it was rare for someone to survive the Great Cataclysm with nothing but their bare fists and gain both wealth and fame. Im Chunsoo’s present was the future many Hunters dreamed of.

[P64]
“Impressive? It certainly is—the power of bloodlines, that is.”

[P65]
Kkeokjeong jerked his chin toward Im Changsoo’s retreating back.

[P66]
“Don’t forget whose blood that punk inherited.”

[P67]
“What does that…”

[P68]
“I’m not bragging, but I’ve been in this business for over twenty years. Sangdong Guild was founded when I was still a complete rookie.”

[P69]
“And?”

[P70]
“Bucheon was just as fiercely competitive between Guilds back then as it is now. There was no room for a new Guild to squeeze in.”

[P71]
“But Im Chunsoo broke through anyway?”

[P72]
“That’s right. That’s why he’s a frightening man.”

[P73]
“Hmm.”

[P74]
Did that really mean so much?

[P75]
Competition between Guilds was nothing new, and in a merit-based society, it was only natural for the capable to survive.

[P76]
“A man like him would have had excellent abilities as a Hunter and plenty of Fame. He must have had powerful connections, too.”

[P77]
“Do you think the other Guild Masters didn’t?”

[P78]
“What?”

[P79]
“They might have had slightly less Fame than Im Chunsoo, but every one of them had been a war hero. They had entered the market several years before Sangdong Guild and occupied a substantial number of Gates.”

[P80]
Kkeokjeong continued in a low voice.

[P81]
“It was a time when all kinds of illegal activity ran rampant because the system hadn’t been fully established yet. The only reason Sangdong Guild exists today is that Im Chunsoo crushed every one of his competitors. He’s no pushover.”

[P82]
A thought suddenly flashed through my mind.

[P83]
What would happen if Im Chunsoo found out about what had happened today? How would he react to hearing that his only son had been utterly humiliated?

[P84]
*This could get complicated.*

[P85]
When you talked about Korea, you couldn’t leave out connections through school, region, and blood.

[P86]
Sangdong Guild had held its ground for twenty years. If it was a local power, our Guild was practically a newborn.

[P87]
If Sangdong Guild came at us in earnest, they’d tear up our birth certificate before we even got started.

[P88]
“Is the Sangdong Guild Master a nice person, at least?”

[P89]
“I wouldn’t know. I’ve only heard rumors.”

[P90]
“Tell me what you’ve heard.”

[P91]
After thinking for a moment, Kkeokjeong answered,

[P92]
“Seeing Im Changsoo today reminded me of an old saying. A tiger father and a dog son.”

[P93]
“A great father and a worthless son? That’s still a compliment, isn’t it? Is he the kind of person you can reason with?”

[P94]
“No. Try interpreting it literally.”

[P95]
“…A tiger for a father and a dog for a son?”

[P96]
“If Changsoo’s personality is that of a son of a bitch, then Im Chunsoo is a tiger. I hear his temper is absolutely fucking terrible.”

[P97]
“…”

[P98]
“I’ve also heard that he mellowed out with age, but can a person’s temper really change that easily?”

[P99]
*For fuck’s sake.*

[P100]
The more I heard, the colder my spine felt. I had the distinct feeling that something was about to go horribly wrong.

[P101]
*Damn it. I shouldn’t have made that bet.*

[P102]
My excitement at the thought of receiving several billion won had lasted only a moment. Now I felt uneasy, like I had taken a huge dump and forgotten to wipe.

[P103]
I didn’t care what happened to me, but I absolutely refused to let the other Guild members get hurt.

[P104]
“Taekyung, don’t worry about it too much. I only brought it up just in case.”

[P105]
“I didn’t just cause trouble, did I?”

[P106]
“It’ll be fine. Team Leader Choi thought it would be fun and joined the bet, too.”

[P107]
“Oh, right.”

[P108]
“Exactly. And look at the way Im Changsoo acted. If I were his father, I would’ve beaten him half to death. He’d be too embarrassed to tell anyone about it.”

[P109]
He had a point. What could possibly happen?

[P110]
Hearing that made me feel considerably lighter. I even found myself smiling.

[P111]
“Thanks, Kkeokjeong ajusshi. No, hyungnim.”

[P112]
“Then buy us some beef to celebrate becoming a rich man. Wait, no. You should eat it with Miss Song, not me.”

[P113]
“…Ah.”

[P114]
He was driving a nail straight through my heart.

[P115]
As Im Kkeokjeong killed me with words for the second time, I swallowed my tears.

[P116]
* * *

[P117]
“What brings you here?”

[P118]
The speaker was a man with a distinctive appearance.

[P119]
He was nearing fifty, but his skin was taut and his wiry, spiky hair was black. His large, piercing eyes were enough to make anyone’s knees go weak.

[P120]
*What the hell is with that look in his eyes…*

[P121]
The manager of a K Bank branch was no exception. He had already met the man several times, but he was an ordinary person, while the other man was an A-rank Hunter—a living witness who had endured the Great Cataclysm with his entire body.

[P122]
His tongue tied itself in knots, and cold sweat trickled down his back.

[P123]
“Well…”

[P124]
“If you came to waste my valuable time, go back. Otherwise, speak now.”

[P125]
The words were sharp, but his tone was fairly gentle.

[P126]
The manager had heard the rumor that Im Chunsoo was trying to mellow his temper with age. Apparently, it hadn’t been a complete waste of effort.

[P127]
*Damn it.*

[P128]
The branch manager steeled himself and blurted out,

[P129]
“I’m sorry, Guild Master. I’ve come regarding your son.”

[P130]
At the mention of his son, Sangdong Guild Master Im Chunsoo’s eyebrow twitched.

[P131]
“Changsoo? What about him?”

[P132]
“Some time ago, you asked me to let you know whenever your son used any of the bank’s services…”

[P133]
Im Chunsoo nodded as if he understood.

[P134]
“What is it this time? Did he steal my seal? Or take out a loan against collateral?”

[P135]
“He transferred a considerable amount of money all at once.”

[P136]
“He must be fooling around with women again. Obviously. How much?”

[P137]
“Four billion won to each of two accounts. Eight billion won in total.”

[P138]
“How much?”

[P139]
“Eight billion… Hup.”

[P140]
The branch manager hurriedly swallowed his breath. He had just watched the window behind Im Chunsoo rapidly freeze over.

[P141]
Hiss.

[P142]
It was late summer outside, but the office was suddenly ruled by cold and frost.

[P143]
Im Chunsoo gestured at the trembling branch manager.

[P144]
“Anything else?”

[P145]
“I-I brought the relevant documents.”

[P146]
With shaking hands, the branch manager placed a stack of papers on the desk.

[P147]
“Good. You may leave.”

[P148]
“I-I’ll see you next time.”

[P149]
After the branch manager fled the room, Im Chunsoo picked up the receiver. The phone had a cold-resistance function, so it transmitted the signal without any problems.

[P150]
Beep, beep. Click.

[P151]
—Yes, Guild Master. Team One’s Leader speaking.

[P152]
“Bring that bastard here immediately.”

[P153]
—…Do you mean Team Leader Im Changsoo?

[P154]
“Team Leader, my ass. He’s fired as of today. Bring that bastard here now!”

[P155]
Bang!

[P156]
The receiver’s life ended there. Ice shattered into hundreds of pieces and covered the desk.

[P157]
“What a pathetic fool. Even after I warned him…”

[P158]
Im Chunsoo glared coldly at the wrecked office, then his gaze stopped on one spot: the stack of papers left behind by the K Bank branch manager.

[P159]
There was no doubt that the documents contained the whereabouts of eight billion won.

[P160]
*You stupid bastard. Which woman did you fall for this time?*

[P161]
He read through the papers, turning them one page at a time, for more than ten minutes.

[P162]
When Im Chunsoo closed the final page, the door flew open with the sound of someone being dragged along.

[P163]
“Team Leader Im Changsoo. I brought him here.”

[P164]
An affable-looking middle-aged man stood there. In his firm grip was a young man.

[P165]
“F-Father!”

[P166]
“My proud son has arrived.”

[P167]
At his son’s appearance, the father extended a hand.

[P168]
Of course, it was not meant as a gesture of forgiveness.

[P169]
Crackle, crackle, crackle.

[P170]
Cold surged from Im Chunsoo’s grasp. It changed from gas to liquid, then from liquid to solid, completing its transformation into an ice club as hard as steel.

[P171]
“I have a lot to ask you, but first, you’re getting hit.”

[P172]
“Father!”

[P173]
“Shut up, you little shit!”

[P174]
The middle-aged man who had brought Im Changsoo there—the Team Leader of Sangdong Guild’s Team One—quietly closed the door.

[P175]
For the next half a day, no one was allowed to enter.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 임춘수    | **Im Chunsoo**    |
| 임창수    | **Im Changsoo**   |
| 명성               | **Fame**                       |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 임꺽정 | **Im Kkeokjeong** |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 대한민국 | **Korea** | Country reference. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 86,
  "passed": true,
  "metrics": {
    "source_characters": 5645,
    "translation_characters": 12612,
    "length_ratio": 2.234,
    "source_paragraphs": 171,
    "translation_paragraphs": 177
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "갑자",
        "preferred": "jiazi"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "상동",
        "romanization": "sangdong"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "꺽정",
        "romanization": "kkeokjeong"
      }
    }
  ]
}
```

## Binding editorial rules

# Translation Rules

## Fidelity

- Translate the Korean source—not the wiki, manhwa, fan translations, or expected plot.
- Semantic fidelity outranks elegance. Never improve rhythm, humor, or localization by changing a physical action, negation, relationship, hierarchy, mechanism, quantity, or causal detail.
- Preserve every fact, causal link, joke, emotional beat, repetition, and intentional omission. Add nothing.
- Preserve small action verbs and pragmatic cues exactly: nodding versus shaking one's head, pretending nothing happened, and mild or approachable impressions are characterization, not expendable texture.
- Preserve viewpoint and tense. Resolve omitted subjects only when context supports it; retain genuine ambiguity.
- Match each speaker's hierarchy, intimacy, humor, and profanity naturally. Do not mechanically retain every honorific or classical self-reference.
- Do not censor or soften content.

## Terminology

- `compendium.md` and `docs/NAMES.md` are binding for established names, titles, ranks, techniques, organizations, system terms, items, and locations. Profile headings and aliases join that ledger.
- Search only exact Korean terms already present in the current chapter; the compendium contains future-sensitive entries.
- Never re-romanize established names or invent grand names for uncertain terms. First use of an unlisted name or title almost always needs a footnote or a mapped ledger term.
- Use `qi` for Murim energy and `mana` for the modern Hunter system when the source distinguishes them. Preserve an established chapter-specific rendering such as `internal energy` when the exact glossary and surrounding Korean distinguish accumulated `공력` from resulting `기운`.
- In System panels, render `등급` as `**Grade:**` for quest, item, skill, and martial-art classifications. Reserve `rank` for Hunter classifications or ordinary prose; never replace a System `Grade` field with `Rank`.

## English and Markdown

- Use contemporary US English and natural action-comedy prose; avoid Korean syntax calques and generic cultivation MTL phrasing.
- File: `translations/NNNN.md`; heading: `# Chapter N`.
- Speech: curly double quotes. Direct thoughts: italics without quotes.
- Use em dashes without spaces, the ellipsis character `…`, and `* * *` for source scene breaks.
- Format each actual game System-message panel as one Markdown blockquote window headed `> **System**`. Keep all consecutive notices, fields, and lines inside that same blockquote; separate windows when prose intervenes. Do not enclose System notices or UI terms in square brackets; the `System` heading and framed blockquote identify the panel. Do not label manuals, ordinary quotations, warnings printed in a manual, or other non-System material as `System`; use a normal blockquote or a specific heading instead. Do not wrap each complete notice in outer `**`; retain bold only for meaningful labels or emphasis inside the panel.
- Keep the final file English-only reading copy: no audit notes, Korean text, summaries, or model metadata.

### Tone and Style

- Write like a polished commercial webnovel: brisk, vivid, accessible, and easy to read aloud.
- Preserve the series’ contrast between danger and comedy. Let absurdity, bad timing, blunt reactions, and grim situations create dark humor without adding jokes absent from the Korean.
- Jin Taekyung’s narration is conversational, observant, self-mocking, and occasionally profane. It may be irreverent even when the situation is serious.
- Keep deadpan punchlines short and well-timed. Do not explain a joke after delivering it.
- Preserve the source's level of explicitness. A euphemism may remain euphemistic even when its meaning is sexual or crude; do not replace it with more graphic English merely for impact.
- Make dialogue spontaneous and character-specific. Preserve hierarchy and intimacy through word choice, address, rhythm, and restraint—not archaic wuxia English.
- Use strong profanity when the Korean is strong, but neither intensify nor sanitize it. Do not make ordinary lines uniformly vulgar. Profanity should reveal mood or relationship.
- Keep action and injury vivid but clear rather than purple. Do not make violence funny unless the source’s framing does.
- Avoid stiff literalism, translator-added melodrama, dated internet slang, and quippy superhero-style banter.
- On the second pass, correct awkward English collocations and word choices without changing meaning or voice. Prefer ordinary, spoken English over stiff Latinate or ceremonial wording when the scene is brisk or comic: “goose bumps” rather than “gooseflesh,” and “laid into them” rather than “launched into a solemn denunciation.” Read the prose aloud and replace any phrase that sounds like a formal essay, legal document, or literal dictionary gloss unless the source deliberately calls for that register.

## Footnotes

Use `[^1]` Markdown footnotes when a brief, factual, spoiler-free explanation materially helps an English reader understand:

- a Korean institution, living arrangement, food, holiday, myth, historical reference, or local custom;
- a Korean word, phrase, idiom, wordplay, or culturally specific image that cannot be conveyed fully by the best natural English analogy;
- a deliberately literal rendering whose cultural or linguistic force would otherwise be lost.

For example, render `고시원` as “goshiwon” when the setting or connotations matter, with a concise footnote explaining that it is a very small, inexpensive room-for-rent housing arrangement. Prefer the best natural English analogy in the prose. Use a literal translation plus a concise footnote when the Korean wording itself matters. Define a term at its first meaningful occurrence and do not repeat the note unnecessarily. Footnotes must be rare, useful, and non-spoiling; do not footnote ordinary vocabulary, fully preserved jokes, or uncertainty. Record consequential uncertainty in `docs/STATE.md`.

## Spoilers and Scope

- Safe profiles contain only facts revealed through the latest completed chapter.
- Never read `characters/spoilers/` during drafting. Reviewers may consult one relevant sealed profile only for a specific unresolved continuity issue after the draft is complete.
- Future knowledge may prevent contradiction but may not add early names, pronouns, certainty, motives, or foreshadowing.
- Translate exactly one requested chapter unless the user explicitly requests a batch. Never modify Korean source files under `source/`.

# Master Editorial Brief

You are the final English-language editor of an existing Korean-to-English novel translation.

The Korean source is the authority for meaning. The existing English is the baseline you are editing, not a draft to discard. Your task is to make the chapter read like professionally written native English commercial fiction while preserving the author's exact story, characterization, humor, register, pacing, ambiguity, and cultural texture.

## Editorial authority

You may freely recast sentences and paragraphs when the English is stiff, literal, repetitive for accidental reasons, awkwardly collocated, over-explained, or syntactically shaped by Korean. You may tighten dialogue, improve rhythm, repair transitions, and make action easier to follow. A technically correct sentence may still need rewriting if a fluent English novelist would not naturally phrase it that way.

Do not change text merely to make it different. If the baseline is already strong, leave it alone.

The accepted baseline is also the project's style and terminology anchor. Do not
replace an established rendering, cultural term, System label, Markdown form, or
recurring phrase with a synonym merely because the synonym sounds smoother.
Make that change only when the Korean source, `RULES.md`, or the exact glossary
requires it. In particular, do not turn a source-specific image into a nearby
English image, or change a gold-spoon joke, item name, technique name, or UI
label into a different expression without source support.

## Fidelity constraints

Never invent, omit, explain away, generalize, intensify, soften, or reinterpret source-supported content. In particular, preserve:

- exact actions, subjects, objects, directionality, causality, quantities, and physical details;
- deliberate ambiguity, euphemism, implication, profanity level, repetition, and withheld information;
- jokes and comic specificity, even when a more generic English joke would sound smoother;
- hierarchy, kinship, forms of address, characterization, and speaker attitude;
- System mechanics, Murim concepts, names, ranks, techniques, items, organizations, and established terminology.
- chapter-level logical consistency: interpret labels, counters, notifications, and repeated facts from how they behave across the scene, not from an isolated surface gloss;
- idioms by their narrative function rather than their component words, and jokes with their setup, recognition, and punchline timing intact;
- cross-sentence implications: do not create a claim that contradicts “again,” an increasing value, an earlier action, or the explanation immediately around it;
- repeated terminology and formatting: once the baseline or glossary establishes a rendering, keep it consistent throughout the chapter unless the source clearly changes the sense;

Do not add jokes, metaphors, explanations, emotional conclusions, or colorful details that are absent from the Korean. Do not replace a specific source image with a generic equivalent merely because the generic version is smoother.

When natural English and literal form conflict, preserve the source meaning and pragmatic effect while changing the English form as much as necessary.

Before returning the chapter, perform a silent continuity pass: trace every
counter, quantity, repeated System label, item or technique name, joke setup and
payoff, and physical cause-and-effect sequence from the Korean through the
finished English. Correct any local sentence that contradicts the sequence.

## Relationship to project files

`RULES.md` is binding. `POLISH.md` describes known translation-English failure modes and should guide the edit. Exact glossary matches are binding unless the packet explicitly marks them otherwise. Character/continuity material is context only and must never override the chapter's Korean source.

## Output

Return only the complete edited English Markdown chapter. Preserve the required chapter heading and project Markdown conventions. Do not provide commentary, a change log, explanations, or a Markdown code fence.
