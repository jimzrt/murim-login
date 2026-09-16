# Fidelity Gate — Chapter 125

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
  1|＃125화
  2|
  3|
  4|
  5|“은공.”
  6|
  7|오늘의 이소월은 특히 아름다웠다. 눈처럼 새하얀 흰색 궁장에, 옥색 비녀로 틀어 올린 머리카락은 윤기가 흘렀다.
  8|
  9|연달아 고초를 겪은 탓인지 아직 초췌해 보이긴 했지만 워낙 눈부신 미모의 소유자라 그것마저도 매력적으로 보일 정도다.
 10|
 11|‘아니, 내가 지금 무슨 생각을 하는 거야.’
 12|
 13|미인? 매력적? 열일곱이면 한창 교복 입고 다닐 나이 아닌가. 현실에서는 혼사가 아니라 내신을 준비해야 할 시기다.
 14|
 15|하연이보다도 두 살이 어리니 나와는 열 살 차이. 이 정도면 조카뻘이나 다름없다.
 16|
 17|‘그런데 확실히 나이에 맞지 않게 성숙한…… 아니다. 정신 차리자.’
 18|
 19|이소월의 그윽한 시선을 피하면서 포권을 취했다.
 20|
 21|“안녕하십니까.”
 22|
 23|“문주를 뵙소.”
 24|
 25|이소월은 평범한 소녀가 아니라 엄연히 일문(一門)을 책임진 문주다. 나와 진무경의 정중한 인사에 그녀가 화답하려던 그때였다.
 26|
 27|“대항산검문의 문주님께서 친히 나와 주시다니. 소생 혁무진, 실로 감격했습니다!”
 28|
 29|그래, 네가 빠지면 섭섭하지.
 30|
 31|그녀에게 시선을 고정한 채 허리를 넙죽거리는 혁무진을 보니 한숨밖에 안 나온다.
 32|
 33|“죄송합니다. 원체 좀 모자란 놈이라.”
 34|
 35|“……조장.”
 36|
 37|“보셨죠? 저랑 아무 사이도 아닌데 친한 척하는 거. 그냥 무시하시면 편합니다.”
 38|
 39|이소월의 입가에 살짝 보조개가 패었다.
 40|
 41|“아니에요. 저분도 본문을 위해서 싸워 주신 은인이신걸요.”
 42|
 43|“괜찮아요. 저 녀석은 검 하나 까딱 안 했으니까 은인으로 안 치셔도 됩니다.”
 44|
 45|“……아, 네.”
 46|
 47|내 친절한 팩트 체크에 그녀의 웃음이 어색해진 그 순간이었다.
 48|
 49|“은인이지, 나한테는.”
 50|
 51|이소월의 등 뒤에서 들려온 걸걸한 목소리의 주인공은 반백의 장년인이었다. 덜컹거리는 목제 수레에 앉은 그가 눈인사를 건넨다.
 52|
 53|“일어나지 못하는 부분은 양해 바라네. 이거 참, 나이를 먹었더니 몸이 예전 같지 않아.”
 54|
 55|나이와 명성으로는 이 자리의 그 누구도 눈앞의 장년인을 따라갈 수 없다.
 56|
 57|항산호 철무백의 등장에 혁무진이 잽싸게 허리를 꺾었다.
 58|
 59|“철무백 대협을 뵙습…….”
 60|
 61|“내 얼굴 처음 보나? 거추장스러운 인사는 넣어 둬.”
 62|
 63|“그래도 위명이 자자하신 무림의 대선배님이신데…….”
 64|
 65|“선배는 무슨. 그렇게 일일이 따지면 무림 살기 피곤해.”
 66|
 67|“…….”
 68|
 69|영감쟁이 성격 쿨한 것 보소.
 70|
 71|뻔뻔하기로는 남부럽지 않은 혁무진이 조용히 찌그러지자 그다음은 진무경 차례였다.
 72|
 73|“오셨습니까.”
 74|
 75|별로 대단한 것도 없다. 짧은 한마디에 적당히 포권을 취했을 뿐이다. 그러나 진무경을 발견한 철무백의 얼굴에는 꽃이 활짝 폈다.
 76|
 77|“어이구, 우리 진천검 아니신가. 그래, 이제 가려고?”
 78|
 79|“그렇게 되었습니다.”
 80|
 81|“왜, 좀 더 있다 가지 않고서. 나중에 무공에 대해 심도 깊은 이야기도 나누고 말이야. 응?”
 82|
 83|“죄송합니다. 시간이 촉박한지라.”
 84|
 85|“저런, 어쩔 수 없지. 하면 나중에 이 노인네 한 번 보러 와 줄 텐가?”
 86|
 87|“강호의 대선배님께서 한 수 가르쳐 주신다니, 오히려 이 후배가 부탁드리고 싶은 일입니다.”
 88|
 89|“으허허! 후배라, 듣기 좋네그려.”
 90|
 91|이게 도대체 무슨 그림이지?
 92|
 93|기껏해야 사나흘 머물렀을 뿐인데 사이좋은 조손지간을 보는 것 같다.
 94|
 95|거기다가, 뭐? 방금은 선후배 따지면 세상 살기 피곤하다더니 말 바꾸는 것 봐라.
 96|
 97|나는 혁무진을 향해 눈짓했다.
 98|
 99|‘저 두 사람. 왜 저래?’
100|
101|‘몰라요, 은인이라고 할 때는 언제고. 사람을 이렇게까지 차별해도 되는 겁니까?’
102|
103|‘근데 솔직히 까 보면 넌 한 거 없잖아.’
104|
105|‘…….’
106|
107|열받은 얼굴로 입을 꾹 다무는 걸 보니 내 뜻이 충분히 전달된 모양이다.
108|
109|“그래, 다음에 꼭 보자고.”
110|
111|흐뭇한 할배 미소로 진무경을 바라본 철무백이 나를 향해 고개를 돌렸다.
112|
113|“자넨 할 말 없나?”
114|
115|순간 맹수의 눈빛이 느껴졌다고 하면 기분 탓인가?
116|
117|나는 앞서 목격한 두 가지 예시 중 좋은 쪽을 따라가기로 마음먹었다.
118|
119|“오셨습니까.”
120|
121|“그럼 왔지, 갔나?”
122|
123|“…….”
124|
125|이게 아닌데?
126|
127|하지만 힘들 때 웃는 것이 일류인 법. 당황하지 않고 웃음을 지어 보였다.
128|
129|“몸은 괜찮으시고요?”
130|
131|이번엔 철무백이 부목을 댄 사지를 흔들었다.
132|
133|“괜찮아 보이나?”
134|
135|“……아뇨.”
136|
137|“괜찮았으면 걸어왔지. 요즘 마적 놈들은 정년도 없이 부려 먹으니 나 같은 늙은이가 버틸 재간이 있어?”
138|
139|“…….”
140|
141|노인네가 기억력도 좋다. 처음 만났을 때 말실수했던 걸 아직도 마음에 담아 두고 있는 모양이다.
142|
143|상황을 알 리 없는 이소월은 당황한 얼굴로 빽 소리쳤다.
144|
145|“숙부!”
146|
147|“아이고, 늙은이 귀청 떨어지겠다.”
148|
149|투덜거리던 그가 돌연 정중하게 고개를 숙였다.
150|
151|“다들 고맙네.”
152|
153|마지못해서 하는 인사가 아니다. 항산호 철무백. 오랜 세월 동안 오직 자신만의 길을 걸었던 노고수가 진심을 다해 말하고 있었다.
154|
155|“얼마 남지 않은 늙은이의 명줄을 늘려 줘서가 아닐세. 소월이, 저 아이를 지켜 줘서 고맙네. 자네들 덕분에 항산검문이 살아남을 수 있었어.”
156|
157|그가 잔잔한 눈빛으로 나와 진무경, 혁무진을 차례대로 응시했다.
158|
159|“한 갑자를 넘게 살아오며 깨달은 사실이 있네. 은원(恩怨)은 무슨 수를 써서라도 갚아야 한다는 것. 내 이 자리에서 맹세하건대, 이번 일은 죽을 때까지 잊지 않겠네. 자네들이 원한다면 내 목숨을 잃는 한이 있더라도 말일세.”
160|
161|이소월이 곧장 철무백의 말을 이어받았다.
162|
163|“항산검문도 은인들을 기억하겠습니다. 또한 돌아가신 아버지께서 저지른 과오…… 이 자리를 빌려 사죄드립니다.”
164|
165|“사죄드립니다!”
166|
167|“부디 용서를!”
168|
169|쩌렁쩌렁한 외침은 항산검문 무인들의 입에서 터져 나왔다.
170|
171|하나같이 크고 작은 부상을 입은 그들이 아직 녹지 않은 눈밭에 무릎을 꿇은 채 우리의 대답을 기다리고 있었다.
172|
173|툭.
174|
175|- 네가 답해라.
176|
177|진무경의 전음에 나는 바짝 마른 입술을 핥았다.
178|
179|‘용서라.’
180|
181|전쟁에서는 승리했지만 상처는 남았다.
182|
183|명령에 따라 끊임없이 싸우고 죽어 간 무인, 심지어는 무공을 익히지 않은 여인과 아이들까지 희생됐다. 아들의 복수에 눈이 먼 이천백이 저지른 짓이었다.
184|
185|항산검문과의 전쟁이 남긴 상처는 깊었고, 아물기까지는 오랜 시간이 걸릴 것이다.
186|
187|‘그리고 흉터가 남겠지.’
188|
189|어떤 종류의 흉터는 영원히 지워지지 않는다.
190|
191|한순간에 집과 부모를 잃은 어린 남매가 그럴 것이고, 나 역시 그렇다. 고금제일인이라는 허무맹랑한 꿈을 꾼 녀석의 얼굴이 지금까지도 어른거리는 걸 보면 말이다.
192|
193|그러나 지금이 봉합되어 가는 과정이라는 사실 또한 부정할 수는 없다.
194|
195|‘그 상처를 준 사람들은 모두 죽었으니까.’
196|
197|각자의 복수를 꿈꿨던 대장로와 이천백은 이미 최후를 맞이했다.
198|
199|우리가 항산검문을 구하기 위해 며칠 밤낮을 달려왔던 이유도 그 때문이 아닐까?
200|
201|진심 어린 사과와 용서가 있다면…… 흉터가 남을지라도 상처는 아물 수 있다.
202|
203|바로 지금처럼.
204|
205|“사죄는 받지 않겠습니다.”
206|
207|고심 끝에 튀어나온 한마디다. 나는 다른 사람들의 반응을 기다리지 않고 말을 이었다.
208|
209|“제가 누군가에게 사죄받고, 용서할 만한 자격이 있는 사람은 못 되거든요.”
210|
211|이 자리의 누구도 그럴 만한 자격이 안 된다. 저들이 사죄해야 할 사람들은 태원진가에 있다.
212|
213|내 말을 알아들었는지 이소월과 철무백이 고개를 끄덕였다.
214|
215|“돌아오는 원단(元旦)에 뵐게요.”
216|
217|“태원이라. 삼십 년 만의 외유가 되겠군.”
218|
219|항산검문은 결코 환영받지 못하는 손님이다. 특히 형편없이 쪼그라든 현재로서는 온갖 수모와 굴욕을 당할 수도 있다.
220|
221|하지만 이 또한 저들이 모두 감내해야 할 문제. 내가 할 수 있는 일도, 끼어들 이유도 없다.
222|
223|- 잘했다.
224|
225|진무경의 짤막한 전음을 들으며 마지막 인사를 건넸다.
226|
227|“그럼 이만.”
228|
229|마차를 향해 돌아서려던 그 순간이었다.
230|
231|“은공.”
232|
233|“네?”
234|
235|“그거 아세요? 원단까지 보름도 남지 않았다는 거.”
236|
237|이소월의 시냇물 같은 목소리가 졸졸졸 이어졌다.
238|
239|“지난번에 듣지 못한 대답, 기대할게요.”
240|
241|당황해서 입만 벙긋거리는 나를 진무경이 잡아끌었다.
242|
243|등 뒤로 들려오는 철무백의 심기 불편한 듯한 기침 소리를 마지막으로, 마차가 힘차게 출발했다.
244|
245|
246|
247|* * *
248|
249|
250|
251|태원진가로 돌아가는 길은 빠르고 순탄했다. 마부의 숙련된 솜씨도 한몫했지만 조급한 마음이 사라지니 모든 게 그렇게 느껴졌다.
252|
253|“후우.”
254|
255|막 운기조식을 끝마친 진무경이 문득 중얼거렸다.
256|
257|“생각해 보니 절정 무공은 구경도 못 했군.”
258|
259|항산검문에 가면 절정 무공을 볼 수 있다는 진위경의 꾐에 빠져 동행하게 된 그다. 나는 점잖게 대꾸했다.
260|
261|“괜찮아. 풍양 덕분에 북망산 구경은 했잖아.”
262|
263|“그따위 말을 위로라고 하는 거냐?”
264|
265|“아니, 놀린 건데.”
266|
267|진무경의 손에서 뼈 어긋나는 소리가 들렸다.
268|
269|“많이 컸군.”
270|
271|“부상 다 회복하면 비무 한 판 하실?”
272|
273|“지금 당장이라도…… 끙.”
274|
275|자리를 박차고 일어나려던 진무경이 눈살을 찌푸렸다.
276|
277|아무리 회복이 빠르다 한들 이제 고작 나흘이다. 그가 입은 부상이 완쾌되기에는 턱도 없이 짧은 시간.
278|
279|자리에 무너지듯 주저앉은 녀석이 나를 노려보았다.
280|
281|“운 좋은 줄 알아라.”
282|
283|“운 좋은 건 모르겠고, 명줄 하나는 기똥차게 굵지.”
284|
285|매번 죽을 고비를 맞이하는데도 사는 걸 보면 날 때부터 명줄 하나는 튼튼한 모양이다. 아니면 천운(天運)을 타고났거나.
286|
287|“어쨌건 잘했다.”
288|
289|“응?”
290|
291|“이잉?”
292|
293|뜬금없는 칭찬 스티커에 나와 혁무진이 동시에 눈을 동그랗게 떴다. 정작 당사자는 뭐 잘못됐냐는 얼굴이다.
294|
295|“왜 그러지? 못 들을 말이라도 들은 표정들인데.”
296|
297|“귀신이 따로 없네.”
298|
299|“앗, 혹시 이미 풍양한테 죽고 원귀가 되어서 여기 계시는 거 아닐까요?”
300|
301|제법 그럴듯한 가설이었지만 진무경 앞에서는 자나 깨나 입조심해야 한다.
302|
303|나는 먼지 나게 두들겨 맞는 혁무진을 바라보며 품 안을 더듬었다.
304|
305|‘인벤토리 오픈. 소환.’
306|
307|다음 순간, 동그랗고 단단한 뭔가가 손끝에 닿았다.
308|
309|풍양이 남기고 간. 아니, 풍양에게서 빼앗은 유일한 물건이다.
310|
311|‘아이템 확인.’
312|
313|띠링.
314|
315|
316|
317|아이템창
318|
319|
320|
321|[잠력단]
322|
323|종류 : 영단
324|
325|등급 : ???
326|
327|제한 : [절정 무인] 이상
328|
329|설명 : [알 수 없는 누군가]가 제조한 단환. 약 한 시진 동안 복용자의 잠재된 힘을 대폭 끌어 올리는 대신, 그에 대한 대가가 뒤따른다. 최악의 경우가 아니고서는 복용하지 말 것.
330|
331|효과 : 전투 관련 능력치 +100
332|
333|[공력] +15년
334|
335|[호신강기] 사용 가능
336|
337|
338|
339|
340|
341|제한 시간이 짧은 걸 감안해도 무지막지한 효과. 풍양이 그렇게 자신만만하던 이유가 충분히 이해가 된다.
342|
343|후유증이 얼마나 심각한지는 모르겠지만 당장 목숨이 위태롭다면 두 개가 아니라 스무 개도 먹어야지, 뭘.
344|
345|하지만 정작 마음에 걸리는 부분은 따로 있었다.
346|
347|‘알 수 없는 누군가가 제조한 단환이라.’
348|
349|아이템 등급도 물음표에, 정확한 후유증은 나와 있지 않으며 심지어 제조자는 베일에 싸여 있다.
350|
351|도대체 어떤 놈이 이런 괴상한 물건을 만들어 냈을까?
352|
353|‘이거, 구린내가 진동을 하는데.’
354|
355|잠력단을 손안에서 굴리며 생각에 잠겨 있던 그때였다.
356|
357|저 멀리서 아련하게 들려오는 누군가의 외침.
358|
359|- 무경아아! 태경아아아!!
360|
361|열정적으로 혁무진의 이마를 후려치던 진무경이 멈칫했다.
362|
363|“환청인가?”
364|
365|응, 아냐.
```

## Assembled English

```markdown
[P1]
# Chapter 125

[P2]
“Benefactor.”

[P3]
Lee Seowol looked especially beautiful today. She wore a snow-white formal robe, and her hair gleamed where it had been swept up with a jade hairpin.

[P4]
She still looked haggard from everything she had been through, but she was so dazzlingly beautiful that even her exhaustion seemed charming.

[P5]
*No. What am I thinking?*

[P6]
Beautiful? Charming? At seventeen, she should still be wearing a school uniform and worrying about her grades, not marriage.

[P7]
She was two years younger than Hayeon, putting ten years between us. With an age gap like that, she might as well have been my niece.

[P8]
*Still, she certainly seems mature for her age… No. Get a grip.*

[P9]
Avoiding Lee Seowol’s deep gaze, I clasped my hands in a formal salute.

[P10]
“Greetings.”

[P11]
“I greet the Sect Leader.”

[P12]
Lee Seowol was no ordinary girl. She was the Sect Leader responsible for an entire sect. Just as she was about to return Jin Mukyung’s and my polite greetings—

[P13]
“Imagine the Sect Leader of the great Mount Heng Sword Sect coming out to greet us in person! I, Hyuk Mujin, am truly honored!”

[P14]
Of course. It wouldn’t be complete without you.

[P15]
Hyuk Mujin kept his eyes fixed on her as he bowed over and over. All I could do was sigh.

[P16]
“I apologize. He’s not all there.”

[P17]
“…Captain.”

[P18]
“You saw that, right? We’re not even close, but he’s pretending we are. You’ll be better off ignoring him.”

[P19]
A faint dimple appeared at the corner of Lee Seowol’s mouth.

[P20]
“Not at all. He’s also a Benefactor who fought for our sect.”

[P21]
“It’s fine. He didn’t lift a finger, so you don’t have to count him as a Benefactor.”

[P22]
“…Oh. I see.”

[P23]
Her smile had just turned awkward when a rough voice came from behind her.

[P24]
“He’s a Benefactor to me.”

[P25]
The speaker was a middle-aged man with half-gray hair. Seated in a rattling wooden cart, he greeted us with a nod.

[P26]
“Please excuse me for being unable to stand. Well, age has caught up with me. My body isn’t what it used to be.”

[P27]
No one here could match the man before us in either age or fame.

[P28]
At the appearance of Cheol Mubaek, the Tiger of Mount Heng, Hyuk Mujin quickly bent at the waist.

[P29]
“I greet Great Hero Cheol Mubaek—”

[P30]
“Is this your first time seeing my face? Spare me the tiresome formalities.”

[P31]
“But you’re a renowned great senior of the Murim…”

[P32]
“Senior, my foot. If you fuss over every little distinction like that, life in the Murim gets exhausting.”

[P33]
“…”

[P34]
Look at how laid-back this old man was.

[P35]
Even Hyuk Mujin, who was as shameless as they came, quietly shrank back. That left Jin Mukyung.

[P36]
“You’ve arrived.”

[P37]
Nothing special. He simply clasped his hands in a brief salute. Yet Cheol Mubaek’s face lit up the instant he saw him.

[P38]
“Well, if it isn’t our Heaven Shaking Sword. So, you’re leaving now?”

[P39]
“It seems so.”

[P40]
“Why not stay a little longer? We could have an in-depth discussion about martial arts later. Hmm?”

[P41]
“I’m sorry, but I’m pressed for time.”

[P42]
“Oh, what a shame. It can’t be helped, then. Will you come visit this old man sometime?”

[P43]
“If a great senior of the martial world is willing to teach me, then I should be the one asking for the opportunity.”

[P44]
“Ha-ha-ha! Senior, huh? I like the sound of that.”

[P45]
What exactly was I looking at?

[P46]
They had only spent three or four days together, but they looked like a close grandfather and grandson.

[P47]
And what was that? Hadn’t he just said fussing over seniority made life exhausting? Look at him changing his tune.

[P48]
I shot Hyuk Mujin a glance.

[P49]
*What’s with those two?*

[P50]
*No idea. He called me a Benefactor before, but is it really all right to treat people this differently?*

[P51]
*But if you’re being honest, you didn’t actually do anything.*

[P52]
*…*

[P53]
He clamped his mouth shut with an irritated expression. My meaning seemed to have gotten through.

[P54]
“All right. Make sure you come next time.”

[P55]
Cheol Mubaek gazed at Jin Mukyung with a pleased, grandfatherly smile before turning toward me.

[P56]
“What about you? Don’t you have anything to say?”

[P57]
Was it my imagination, or had I just felt a predator’s gaze?

[P58]
I decided to follow the better of the two examples I had just witnessed.

[P59]
“You’ve arrived.”

[P60]
“Of course I have. Did I go somewhere?”

[P61]
“…”

[P62]
That wasn’t it.

[P63]
But smiling in hard times was the mark of a First Rate man. I put on a smile without panicking.

[P64]
“Are you feeling all right?”

[P65]
This time, Cheol Mubaek shook his splinted limbs.

[P66]
“Do I look all right?”

[P67]
“…No.”

[P68]
“If I were all right, I would’ve walked here. These days, those mounted-bandit bastards work people without even a retirement age. How is an old man like me supposed to keep up?”

[P69]
“…”

[P70]
The old man had quite a memory. He still seemed to be holding on to what I had said by mistake when we first met.

[P71]
Lee Seowol, who knew nothing about the situation, shouted in embarrassment.

[P72]
“Uncle!”

[P73]
“Good grief, you’ll burst this old man’s eardrums.”

[P74]
After grumbling, he suddenly bowed his head politely.

[P75]
“Thank you, all of you.”

[P76]
He wasn’t thanking us out of obligation. Cheol Mubaek, the Tiger of Mount Heng—an old master who had walked his own path for many years—was speaking from the bottom of his heart.

[P77]
“Not because you prolonged what little remains of this old man’s life. Seowol—thank you for protecting that child. Thanks to all of you, the Mount Heng Sword Sect survived.”

[P78]
He gazed calmly at me, Jin Mukyung, and Hyuk Mujin in turn.

[P79]
“I’ve learned something after living for more than a jiazi.[^1] Gratitude and grudges must be repaid, no matter what it takes. I swear here and now that I will never forget what happened, not until the day I die. If you wish it, I’ll repay you even if it costs me my life.”

[P80]
Lee Seowol immediately continued where he left off.

[P81]
“The Mount Heng Sword Sect will also remember our Benefactors. And for the wrongs committed by my late father… I would like to offer our apology here and now.”

[P82]
“We apologize!”

[P83]
“Please forgive us!”

[P84]
The thunderous cries burst from the mouths of the Mount Heng martial artists.

[P85]
Every one of them bore injuries, both great and small. Kneeling in the snow that had yet to melt, they waited for our answer.

[P86]
A light tap.

[P87]
*You answer.*

[P88]
At Jin Mukyung’s Sound Transmission, I licked my parched lips.

[P89]
*Forgiveness.*

[P90]
We had won the war, but wounds remained.

[P91]
Martial artists had fought and died without end on the orders of their superiors. Even women and children who had never learned martial arts had been sacrificed. It was all the work of Lee Cheonbaek, blinded by his desire to avenge his son.

[P92]
The wounds left by the war with the Mount Heng Sword Sect ran deep. They would take a long time to heal.

[P93]
*And scars will remain.*

[P94]
Some scars could never be erased.

[P95]
The young siblings who had lost their home and parents in an instant would carry scars like that. So would I, judging by how the face of that man who had dreamed the absurd dream of becoming the greatest of all time still haunted me.

[P96]
But I couldn’t deny that the wounds were beginning to close.

[P97]
*Because everyone who caused them is dead.*

[P98]
The Head Elder and Lee Cheonbaek, each of whom had dreamed of revenge, had already met their ends.

[P99]
Wasn’t that why we had raced here day and night to save the Mount Heng Sword Sect?

[P100]
With a sincere apology and forgiveness… wounds could heal, even if the scars remained.

[P101]
Just as they were now.

[P102]
“I won’t accept your apology.”

[P103]
The words came out only after considerable thought. Without waiting for anyone else to react, I continued.

[P104]
“I’m not someone with the right to receive your apology or forgive you.”

[P105]
No one here had that right. The people they needed to apologize to were back at the Jin Family of Taiyuan.

[P106]
Lee Seowol and Cheol Mubaek seemed to understand. Both nodded.

[P107]
“I’ll see you on New Year’s Day.”

[P108]
“Taiyuan, is it? It will be my first journey away from home in thirty years.”

[P109]
The Mount Heng Sword Sect would hardly be a welcome guest. Especially now, diminished to such a pitiful state, they might have to endure all manner of humiliation and disgrace.

[P110]
But that was something they would have to bear themselves. There was nothing I could do, nor any reason for me to interfere.

[P111]
*Well done.*

[P112]
With Jin Mukyung’s brief Sound Transmission in my ear, I offered one last farewell.

[P113]
“Then we’ll be going.”

[P114]
I had just turned toward the carriage when Lee Seowol called out.

[P115]
“Benefactor.”

[P116]
“Yes?”

[P117]
“Did you know there are fewer than fifteen days left until New Year’s Day?”

[P118]
Her voice babbled on like a little stream.

[P119]
“I’m looking forward to hearing the answer I didn’t get last time.”

[P120]
I could only open and close my mouth in confusion as Jin Mukyung grabbed me and dragged me away.

[P121]
With Cheol Mubaek’s distinctly displeased cough sounding behind us, the carriage set off at full speed.

[P122]
* * *

[P123]
The journey back to the Jin Family of Taiyuan was quick and smooth. The coachman’s skill played a part, but with the impatience gone from my heart, everything seemed that way.

[P124]
“Phew.”

[P125]
Jin Mukyung had just finished circulating his qi when he suddenly muttered, “Now that I think about it, I didn’t even get to see a Peak martial art.”

[P126]
He had joined us after Jin Wikyung lured him in with the promise that he could see Peak martial arts at Mount Heng. I answered him calmly.

[P127]
“It’s fine. Thanks to Pung Yang, you got to see Mount Beimang.”

[P128]
“You call that consolation?”

[P129]
“No. I was making fun of you.”

[P130]
Bones cracked in Jin Mukyung’s hand.

[P131]
“You’ve grown a lot.”

[P132]
“Want to spar once your injuries are fully healed?”

[P133]
“I could do it right now… Urgh.”

[P134]
Jin Mukyung tried to spring to his feet, then immediately frowned.

[P135]
No matter how quickly he recovered, it had only been four days. That was nowhere near enough time for his injuries to heal completely.

[P136]
He collapsed back into his seat and glared at me.

[P137]
“Consider yourself lucky.”

[P138]
“I don’t know about lucky, but my lifeline sure is damn thick.”

[P139]
Considering how I kept surviving every brush with death, I must have been born with an unusually sturdy lifeline. Either that, or I had been blessed with heaven’s fortune.

[P140]
“Anyway, you did well.”

[P141]
“Huh?”

[P142]
“Eeeh?”

[P143]
Hyuk Mujin and I both widened our eyes at the unexpected praise sticker. Jin Mukyung looked at us as if he couldn’t understand what was wrong.

[P144]
“Why are you looking at me like that? You look as if you’ve heard something you weren’t supposed to.”

[P145]
“You’re practically a ghost.”

[P146]
“Wait, could Pung Yang have already killed you? Are you sitting here as a vengeful spirit?”

[P147]
It was a fairly plausible theory, but around Jin Mukyung, you had to watch your mouth at all times.

[P148]
As I watched Hyuk Mujin get beaten until dust flew, I felt around inside my robes.

[P149]
*Inventory open. Summon.*

[P150]
The next moment, my fingertips touched something round and hard.

[P151]
It was the only thing Pung Yang had left behind.

[P152]
No—the only thing I had taken from him.

[P153]
*Check Item.*

[P154]
*Ding.*

[P155]
> **System**
>
> **Item Window**
>
> **Temporary Strength Pill**
>
> **Type:** Elixir  
> **Grade:** ???  
> **Restriction:** Peak martial artist or higher  
> **Description:** A pill manufactured by an unknown person. It greatly raises the user’s latent power for about one shichen, but a price must be paid in return. Do not take it except in the worst-case scenario.  
> **Effect:** Combat-related stats +100  
>
> **Internal energy:** +15 years  
>
> **Body-Protecting Qi:** Available

[P156]
Even accounting for the short time limit, its effects were monstrous. I could understand why Pung Yang had been so confident.

[P157]
I had no idea how severe the aftereffects were, but if my life were in danger, I’d swallow twenty of them, not two. Obviously.

[P158]
But something else bothered me.

[P159]
*An elixir manufactured by an unknown person.*

[P160]
The Item’s Grade was marked with question marks, its exact aftereffects weren’t listed, and even its maker was shrouded in mystery.

[P161]
What kind of bastard had created something this bizarre?

[P162]
*This thing reeks of something shady.*

[P163]
I was rolling the Temporary Strength Pill around in my palm, lost in thought, when a distant cry drifted toward us.

[P164]
“Mukyuuung! Taekyuuung!”

[P165]
Jin Mukyung froze in the middle of enthusiastically hammering Hyuk Mujin’s forehead.

[P166]
“Was that a hallucination?”

[P167]
Yeah, no.

[P168]
[^1]: A jiazi is a traditional sixty-year cycle.
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
# Chapter 125

[P2]
“Benefactor.”

[P3]
Lee Seowol was especially beautiful today. She wore a snow-white formal robe, and her hair, twisted up with a jade hairpin, gleamed.

[P4]
She still looked haggard from everything she had been through, but her beauty was so dazzling that even her exhaustion seemed charming.

[P5]
*No. What am I thinking?*

[P6]
Beautiful? Charming? At seventeen, she was at the age when she should be wearing a school uniform and preparing for her grades, not marriage.

[P7]
She was two years younger than Hayeon, which put ten years between us. With an age gap like that, she might as well have been my niece.

[P8]
*Still, she certainly seems mature for her age… No. Get a grip.*

[P9]
Avoiding Lee Seowol’s deep gaze, I clasped my hands in a formal salute.

[P10]
“Greetings.”

[P11]
“I greet the Sect Leader.”

[P12]
Lee Seowol was no ordinary girl. She was the Sect Leader responsible for an entire sect. Just as she was about to return Jin Mukyung’s and my polite greetings—

[P13]
“Imagine the Sect Leader of the great Mount Heng Sword Sect coming out to greet us in person. I, Hyuk Mujin, am deeply honored!”

[P14]
Of course. It wouldn’t be complete without you.

[P15]
Hyuk Mujin kept his gaze fixed on her while repeatedly bowing at the waist. All I could do was sigh.

[P16]
“I apologize. He’s a little short in the head.”

[P17]
“...Captain.”

[P18]
“You saw that, right? He’s pretending to be close to you even though you two have nothing to do with each other. You’ll be better off ignoring him.”

[P19]
A faint dimple appeared beside Lee Seowol’s mouth.

[P20]
“Not at all. He’s also a Benefactor who fought for our sect.”

[P21]
“It’s fine. He didn’t lift a finger, so you don’t have to count him as a Benefactor.”

[P22]
“...Oh. I see.”

[P23]
Her smile had just turned awkward when a rough voice came from behind her.

[P24]
“He’s a Benefactor to me.”

[P25]
The speaker was a middle-aged man with half-gray hair. Sitting in a clattering wooden cart, he gave us a nod.

[P26]
“Please excuse me for being unable to stand. Well, growing old has made me less sturdy than I used to be.”

[P27]
No one here could match the middle-aged man before us in either age or fame.

[P28]
At the appearance of Cheol Mubaek, the Tiger of Mount Heng, Hyuk Mujin quickly bent at the waist.

[P29]
“I greet Great Hero Cheol Mubaek—”

[P30]
“Is this the first time you’ve seen my face? Skip the troublesome formalities.”

[P31]
“But you’re a great senior of the Murim, renowned throughout the martial world...”

[P32]
“Senior, my foot. If you worry about things like that one by one, life in the Murim gets tiring.”

[P33]
“...”

[P34]
The old man had quite the laid-back personality.

[P35]
Even Hyuk Mujin, who was shameless enough to rival anyone, quietly shrank back. That left Jin Mukyung.

[P36]
“You’ve arrived.”

[P37]
Nothing special. He simply clasped his hands in a brief salute. Yet Cheol Mubaek’s face lit up the instant he saw him.

[P38]
“Well, look at that. Isn’t this our Heaven Shaking Sword? So, you’re leaving now?”

[P39]
“It seems so.”

[P40]
“Why don’t you stay a little longer? We could have a serious discussion about martial arts later. Hmm?”

[P41]
“I’m sorry, but I’m pressed for time.”

[P42]
“Oh, what a shame. It can’t be helped, then. How about coming to see this old man sometime?”

[P43]
“If a great senior of the martial world is willing to teach me, then I’m the one who should be asking for such an opportunity.”

[P44]
“Ha-ha-ha! Senior, huh? That sounds nice.”

[P45]
What was I looking at?

[P46]
They had only spent three or four days together, but they looked like a close grandfather and grandson.

[P47]
And what about that? Hadn’t he just said that life became tiring if you worried about seniority and junior status? Look at him changing his tune.

[P48]
I shot Hyuk Mujin a glance.

[P49]
*What’s with those two?*

[P50]
*No idea. He called me a Benefactor before. Is it really okay to treat people this differently?*

[P51]
*But if you’re being honest, you didn’t actually do anything.*

[P52]
*...*

[P53]
He clamped his mouth shut with an irritated expression. My meaning seemed to have gotten through.

[P54]
“All right. Make sure you come next time.”

[P55]
Cheol Mubaek looked at Jin Mukyung with a satisfied grandfatherly smile before turning toward me.

[P56]
“What about you? Don’t you have anything to say?”

[P57]
For a moment, I could have sworn I felt the gaze of a predator.

[P58]
I decided to follow the better of the two examples I had just witnessed.

[P59]
“You’ve arrived.”

[P60]
“Of course I have. Did I go somewhere?”

[P61]
“...”

[P62]
That wasn’t it.

[P63]
But smiling in hard times was the mark of a First Rate man. I put on a smile without panicking.

[P64]
“Are you feeling all right?”

[P65]
This time, Cheol Mubaek shook his splinted limbs.

[P66]
“Do I look all right?”

[P67]
“...No.”

[P68]
“If I were all right, I would have walked here. These days, those mounted-bandit bastards work people without even a retirement age. What chance does an old man like me have?”

[P69]
“...”

[P70]
The old man had quite a memory. He still seemed to be holding on to the mistake I had made when we first met.

[P71]
Lee Seowol, who knew nothing about the situation, shouted in embarrassment.

[P72]
“Uncle!”

[P73]
“Good grief, my old ears are going to fall off.”

[P74]
After grumbling, he suddenly bowed his head politely.

[P75]
“Thank you, everyone.”

[P76]
This wasn’t a reluctant gesture. Cheol Mubaek, the Tiger of Mount Heng, was an old master who had walked his own path for many years. He was speaking from the bottom of his heart.

[P77]
“It’s not because you extended the life of an old man with little time left. Seowol—thank you for protecting that child. Thanks to all of you, the Mount Heng Sword Sect survived.”

[P78]
He gazed calmly at me, Jin Mukyung, and Hyuk Mujin in turn.

[P79]
“I’ve learned something after living for more than a jiazi.[^1] Gratitude and grudges must be repaid, no matter what it takes. I swear here and now that I will never forget what happened, not until the day I die. If you wish it, I’ll repay you even if it costs me my life.”

[P80]
Lee Seowol immediately took up his words.

[P81]
“The Mount Heng Sword Sect will remember our Benefactors. I would also like to apologize here for the wrongdoing committed by my late father...”

[P82]
“We apologize!”

[P83]
“Please forgive us!”

[P84]
The thunderous cries burst from the mouths of the Mount Heng martial artists.

[P85]
All of them bore injuries, both major and minor. Kneeling in the snow that had not yet melted, they waited for our answer.

[P86]
A tap.

[P87]
*You answer.*

[P88]
At Jin Mukyung’s Sound Transmission, I licked my dry lips.

[P89]
*Forgiveness.*

[P90]
We had won the war, but wounds remained.

[P91]
Martial artists had fought and died without end on the orders of their superiors. Even women and children who had never learned martial arts had been sacrificed. It was all the work of Lee Cheonbaek, who had been blinded by his desire to avenge his son.

[P92]
The wounds left by the war with the Mount Heng Sword Sect ran deep, and it would take a long time for them to heal.

[P93]
*And scars will remain.*

[P94]
Some scars could never be erased.

[P95]
The young siblings who had lost their home and parents in an instant would carry such scars. So would I. Even now, I could still see the face of the man who had dreamed of becoming the greatest under heaven.

[P96]
But I couldn’t deny that the wounds were beginning to close.

[P97]
*The people who caused them are all dead.*

[P98]
The Head Elder and Lee Cheonbaek, each of whom had dreamed of revenge, had already met their ends.

[P99]
Wasn’t that why we had raced here day and night to save the Mount Heng Sword Sect?

[P100]
With a sincere apology and forgiveness... wounds could heal, even if scars remained.

[P101]
Just as they were now.

[P102]
“I won’t accept your apology.”

[P103]
The words came out only after considerable thought. Without waiting for anyone else to react, I continued.

[P104]
“I’m not someone with the right to receive an apology from you or to forgive you.”

[P105]
No one here had that right. The people they needed to apologize to were in the Jin Family of Taiyuan.

[P106]
Apparently understanding what I meant, Lee Seowol and Cheol Mubaek both nodded.

[P107]
“I’ll see you on New Year’s Day.”

[P108]
“Taiyuan. It will be my first time venturing out in thirty years.”

[P109]
The Mount Heng Sword Sect was hardly a welcome guest. Especially in its current, pitifully diminished state, it might have to endure all kinds of humiliation and disgrace.

[P110]
But that was something they would have to bear themselves. There was nothing I could do, nor any reason for me to interfere.

[P111]
*Well done.*

[P112]
With Jin Mukyung’s brief Sound Transmission in my ear, I offered one last farewell.

[P113]
“Then, we’ll be going.”

[P114]
I had just turned toward the carriage when Lee Seowol called out.

[P115]
“Benefactor.”

[P116]
“Yes?”

[P117]
“Did you know that there are fewer than fifteen days left until New Year’s Day?”

[P118]
Her voice flowed like a little stream.

[P119]
“I’m looking forward to hearing the answer I didn’t get last time.”

[P120]
I could only open and close my mouth in confusion. Jin Mukyung grabbed me and pulled me away.

[P121]
The carriage set off at full speed, with the sound of Cheol Mubaek’s distinctly displeased cough following us from behind.

[P122]
* * *

[P123]
The journey back to the Jin Family of Taiyuan was quick and smooth. The coachman’s skill played a part, but with the impatience in my heart gone, everything seemed easier.

[P124]
“Phew.”

[P125]
Jin Mukyung had just finished circulating his qi when he suddenly muttered,

[P126]
“Now that I think about it, I didn’t even get to see a Peak martial art.”

[P127]
He had joined the journey after being lured by Jin Wikyung’s claim that he could see Peak martial arts if he went to Mount Heng. I answered him calmly.

[P128]
“It’s fine. Thanks to Pung Yang, you got to see Mount Beimang.”

[P129]
“You call that consolation?”

[P130]
“No. I was teasing you.”

[P131]
The sound of bones cracking came from Jin Mukyung’s hand.

[P132]
“You’ve grown a lot.”

[P133]
“Would you like to spar once your injuries have fully healed?”

[P134]
“I could do it right now... Urgh.”

[P135]
Jin Mukyung tried to spring to his feet, then immediately frowned.

[P136]
No matter how quickly he recovered, it had only been four days. That was nowhere near enough time for his injuries to heal completely.

[P137]
He collapsed back into his seat and glared at me.

[P138]
“You should consider yourself lucky.”

[P139]
“I don’t know about lucky, but my lifeline sure is damn tough.”

[P140]
The fact that I kept surviving despite facing the brink of death every time suggested that I had been born with an unusually sturdy lifeline. Either that, or I had been blessed with heaven’s fortune.

[P141]
“Anyway, you did well.”

[P142]
“Huh?”

[P143]
“Eeeh?”

[P144]
Hyuk Mujin and I both widened our eyes at the unexpected praise sticker. The person who had given it looked at us as if he couldn’t understand what was wrong.

[P145]
“Why are you looking at me like that? You look as if you’ve heard something you weren’t supposed to.”

[P146]
“You’re like a ghost.”

[P147]
“Wait, could it be that you already died to Pung Yang and became a vengeful spirit, and you’re here with us?”

[P148]
It was a fairly plausible theory, but around Jin Mukyung, you had to watch your mouth at all times.

[P149]
I felt around inside my clothes while watching Hyuk Mujin get beaten until dust flew.

[P150]
*Inventory open. Summon.*

[P151]
The next moment, my fingertips touched something round and hard.

[P152]
It was the only thing Pung Yang had left behind.

[P153]
Or rather, the only thing I had taken from Pung Yang.

[P154]
*Check item.*

[P155]
*Ding.*

[P156]
> **System**
>
> **Item Window**
>
> **Temporary Strength Pill**
>
> **Type:** Elixir  
> **Grade:** ???  
> **Restriction:** Peak martial artist or higher  
> **Description:** A pill manufactured by an unknown person. It greatly raises the user’s latent power for about one shichen, but a price must be paid in return. Do not take it except in the worst-case scenario.  
> **Effect:** Combat-related stats +100  
>
> **Internal energy:** +15 years  
>
> **Body-Protecting Qi:** Available

[P157]
Even with the short time limit, the effect was absurd. It was easy to understand why Pung Yang had been so confident.

[P158]
I had no idea how severe the aftereffects were, but if my life were in danger, I’d eat twenty of them, not two. Obviously.

[P159]
But the part that bothered me was something else.

[P160]
*An elixir manufactured by an unknown person.*

[P161]
The Item’s Grade was marked with question marks, its exact aftereffects were not listed, and even its maker was shrouded in mystery.

[P162]
What kind of bastard had created such a bizarre thing?

[P163]
*This thing reeks of something shady.*

[P164]
I was turning the Temporary Strength Pill over in my hand and lost in thought when a distant cry reached us.

[P165]
“Mukyuuung! Taekyuuung!”

[P166]
Jin Mukyung, who had been enthusiastically hammering Hyuk Mujin on the forehead, suddenly stopped.

[P167]
“Was that a hallucination?”

[P168]
Yeah, no.

[P169]
[^1]: A jiazi is a traditional sixty-year cycle.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 명성               | **Fame**                       |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 매력               | **Charm**                      |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 소생      | **I**; occasionally “this humble one” in highly formal dialogue |
| 본문      | **our sect / this sect**                                        |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 고금제일인 | **greatest of all time** | Superlative martial distinction used in Hong Jin's exaggerated praise. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 125,
  "passed": true,
  "metrics": {
    "source_characters": 5490,
    "translation_characters": 12094,
    "length_ratio": 2.203,
    "source_paragraphs": 176,
    "translation_paragraphs": 168
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "살기",
        "preferred": "killing intent"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "운기조식",
        "preferred": "circulate one's qi"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "마적",
        "preferred": "mounted bandits"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "소생",
        "preferred": "I; occasionally “this humble one” in highly formal dialogue"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "귀가",
        "preferred": "your family"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "대협",
        "preferred": "Great Hero or Sir depending tone"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "원단",
        "preferred": "New Year's Day"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "주신",
        "preferred": "God of Drinking"
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
