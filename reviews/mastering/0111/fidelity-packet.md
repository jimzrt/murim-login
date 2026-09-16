# Fidelity Gate — Chapter 111

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
  1|＃111화
  2|
  3|
  4|
  5|두두두두!
  6|
  7|네 마리 준마가 관도를 내달린다. 휴식이 부족했던 탓에 지칠 대로 지친 말들이 숨을 헐떡거렸지만 고삐를 늦출 수 없었다.
  8|
  9|
 10|
 11|제한 시간 : 16:25:32
 12|
 13|
 14|
 15|31, 30. 시간은 계속해서 줄어들고 있다.
 16|
 17|벌써 세 시진, 자그마치 여섯 시간이 흘렀다. 오는 길에 작은 마을에 들러 갈아탈 말을 구하려 했지만 작고 느려 터진 짐말밖에 없었다.
 18|
 19|‘휴식을 취하긴 해야 하는데.’
 20|
 21|외통수다.
 22|
 23|충분히 강행군을 이어 가고 있지만 제한 시간이 아슬아슬하고, 지금처럼 달리면 말이 버티지 못할 거다.
 24|
 25|‘어쩔 수 없나.’
 26|
 27|월화와 진무경에게 잠시라도 쉬어 가자고 말하려던 찰나였다.
 28|
 29|“어?”
 30|
 31|“진 공자! 앞에!”
 32|
 33|굳이 월화의 외침이 아니더라도 나는 이미 놈들을 보고 있었다. 수십 장 앞, 관도를 막아선 시커먼 사내들.
 34|
 35|하나같이 너저분한 옷차림에 허리춤에는 곡도 한 자루가 삐죽 튀어나와 있다. 이제 두말하면 입 아프다.
 36|
 37|‘적풍단.’
 38|
 39|양민으로 보이는 이들을 빙 둘러싸고 으름장을 놓던 놈들이 말발굽 소리에 고개를 홱 돌렸다.
 40|
 41|멀찍이 선두에서 앞서 달리던 나를 발견한 마적들이 누런 이를 드러내며 웃는다.
 42|
 43|“어이구, 벌써 다음 손님 오셨네. 정지!”
 44|
 45|“어, 그래.”
 46|
 47|멈추라는데 멈춰야지, 별수 있나.
 48|
 49|퍼버벅!
 50|
 51|“커허어억!”
 52|
 53|“끄악!”
 54|
 55|내가 타고 있는 준마는 앞을 가로막고 있던 두어 놈을 짓밟고 나서야 멈췄다. 마적들은 물론이고 붙잡혀 있던 행인들까지 눈을 동그랗게 뜨고 날 쳐다본다.
 56|
 57|“너, 너 이 새끼!”
 58|
 59|안장에서 훌쩍 뛰어내리며 물었다.
 60|
 61|“혹시 몰라서 물어본다. 적풍단, 맞지?”
 62|
 63|“웬 놈이냐!”
 64|
 65|“반응 보니까 맞나 보네. 시간 없으니까 빨리 끝내자.”
 66|
 67|망설임 없이 가장 가까이 있는 놈의 다리를 걷어찼다.
 68|
 69|콰직, 섬뜩한 소리와 함께 정강이뼈가 부러진 놈이 주저앉는다.
 70|
 71|창졸간에 벌어진 일. 순간 얼이 빠져 있던 놈들이 재빨리 곡도와 창을 들이댔다.
 72|
 73|“죽여!”
 74|
 75|“남자는 항상 후방을 주의해라.”
 76|
 77|“뭐?”
 78|
 79|“뒤에 조심하라고.”
 80|
 81|열 쌍의 눈이 내 말이 끝나자마자 등 뒤를 돌아보던 그때.
 82|
 83|콰드드득! 뻐억!
 84|
 85|전속력으로 달려온 세 마리의 준마가 놈들을 쓸어 버렸다.
 86|
 87|
 88|
 89|* * *
 90|
 91|
 92|
 93|전투는 시작되기도 전에 끝났다. 말에 치여 볼링 핀처럼 나가떨어진 놈들은 산송장처럼 누워 있었고 나머지 놈들도 손쉽게 제압당했다.
 94|
 95|“사, 살려만 주십시오.”
 96|
 97|“안 죽인다. 몇 군데는 손봐 줘야겠지만.”
 98|
 99|“히익!”
100|
101|진무경이 살아남은 산적들의 팔다리를 똑똑 분지르는 사이 혁무진은 길옆에 매여 있던 말들을 끌고 왔다.
102|
103|“여기 팔팔한 놈들로 갈아타면 될 것 같은데요? 열 마리는 되니까 아예 싹 가져가서 지칠 때마다 교체하고.”
104|
105|나도 같은 생각이다. 지난번 놈들과는 달리 이번에 만난 마적들은 각자 말을 소지하고 있어서 다행이었다.
106|
107|‘그나저나…….’
108|
109|이놈의 적풍단 놈들은 도대체 몇 명이나 있는 거야?
110|
111|사당에서 얻은 정보에 의하면 백 명이 넘는 잔당들이 산서 북부 곳곳으로 흩어졌다고 했다.
112|
113|더러는 산자락으로, 더러는 궁벽한 마을 혹은 번화한 곳에서 숨어 있다가 명령에 따라 집결지로 모인다는 것이다.
114|
115|‘이놈들, 패잔병이 아니야.’
116|
117|놈들은 작전을 수행 중인 복병이다. 적풍단주는 고원에서 병력을 충원하여 남하(南下)하는 한편 남겨 둔 수하들을 북상(北上)시키고 있다.
118|
119|월화가 적풍단주를 무서운 인물이라고 평한 이유를 충분히 짐작하고도 남는다.
120|
121|‘전황이 불리하게 흘러가니 신속하게 물러나는 판단력, 그 와중에도 다음 계획을 준비하는 치밀함, 그리고 계획을 실행시키는 추진력.’
122|
123|거기에 더해 그는 일신에 지닌 무공도 고강하다고 들었다.
124|
125|이쯤 되면 단순한 마적 취급하기도 미안할 지경이다.
126|
127|‘이거 일이 상당히 지저분하게 됐는데.’
128|
129|왜 퀘스트 등급이 절정으로 바뀌었는지 알겠다. 점입가경으로 알고 보니까 뭐, 적풍단주가 절정 고수라든지 그런 건 아니겠지?
130|
131|혹시나 하는 마음에 월화에게 물었더니 대번에 고개를 끄덕인다.
132|
133|“네. 맞는데요?”
134|
135|“……아.”
136|
137|“이렇게 급속도로 두각을 드러낸 것에는 이유가 있기 마련이죠. 아직 널리 알려지지는 않았지만 본 문의 정보에 의하면 적풍단주는 절정 고수가 맞아요.”
138|
139|나는 어이가 없어져서 물었다.
140|
141|“아니, 절정 고수가 왜 마적질을 합니까?”
142|
143|“산적, 수적 중에서는 초절정 고수도 있는데 마적이라고 못 할 것 있나요.”
144|
145|“초절정 고수요? 산적, 수적이?”
146|
147|“나중에 녹림맹주나 장강수로맹주를 만나면 물어보세요. 그럴 일은 없겠지만.”
148|
149|“……제발 그랬으면 좋겠네요.”
150|
151|초절정 고수라니, 진심으로 만나는 일이 없었으면 좋겠다.
152|
153|고개를 절레절레 흔들고 새로 뺏은 말에 올라탔다. 적풍단의 마적들을 꽁꽁 묶어 양민들에게 넘긴 진무경과 혁무진이 그 뒤를 잇는다.
154|
155|
156|
157|제한 시간: 15:59:13
158|
159|
160|
161|이 순간에도 제한 시간은 흘러가는 중이다. 우리는 허리 숙여 감사를 표하는 양민들을 뒤로하고 말 옆구리를 걷어찼다.
162|
163|“이랴!”
164|
165|
166|
167|* * *
168|
169|
170|
171|항산검문 깊숙한 내원에는 극소수의 사람들만 드나들 수 있는 화원이 존재한다. 항산호 철무백은 외부인 중 유일하게 그 자격을 부여받은 사람이었다.
172|
173|“이곳에 온 것은 이번이 처음이구나.”
174|
175|“특별한 공간이었으니까요. 아버지는 고민이 있으실 때마다 화원을 찾으셨죠.”
176|
177|눈 덮인 화원을 사박사박 걷던 이소월이 서리 낀 꽃 한 송이를 발견하고 문득 걸음을 멈췄다.
178|
179|“어머니가 좋아하시던 꽃이에요.”
180|
181|“그랬느냐?”
182|
183|“네, 화원을 가꿀 때면 항상 저를 이곳으로 데려와서 꽃의 이름을 알려 주시곤 했죠.”
184|
185|잠시 곰곰이 생각에 잠겨 있던 이소월이 말을 이었다.
186|
187|“그런데 지금은 기억이 안 나네요.”
188|
189|“오래전 일이니 그럴 만하다. 괘념치 말거라.”
190|
191|“철 숙부.”
192|
193|“응?”
194|
195|“저, 꽃 싫어해요. 어머니가 좋아서 따라왔을 뿐이지, 사실 꽃에는 관심도 없었어요. 아버지께서 화원을 찾으시는 이유와 같은 거죠.”
196|
197|이소월은 눈 덮인 화원을 천천히 둘러보았다. 꽃은 시들었고 화원 중앙에 마련된 봉분(封墳)은 하나에서 넷으로 늘었다.
198|
199|가족들이 잠들어 있는 봉분을 말없이 바라보는 그녀의 눈빛이 깊게 가라앉았다.
200|
201|‘누구의 잘못일까?’
202|
203|어쩌면 무림인의 딸로 태어난 자신의 잘못일지도 모르겠다.
204|
205|그것이 십 년 전 어머니에 이어 아버지와 두 오라버니를 차례로 잃어야 했던 이유다.
206|
207|‘끝까지 말렸어야 했는데…….’
208|
209|문득 두 달 전의 기억이 떠올라 눈 앞을 가린다.
210|
211|그건 어느 야심한 밤, 단둘이 나눴던 부녀(父女) 간의 대화였다.
212|
213|
214|
215|‘널 태원진가의 셋째와 엮어야겠다.’
216|
217|‘셋째라면. 설마 그 망나니와 절 맺어 줄 생각이신가요?’
218|
219|‘아니다. 그러나 너로서는 견디기 힘든 추문(醜聞)이 될 것이다.’
220|
221|‘그렇군요.’
222|
223|‘그뿐이냐?’
224|
225|‘어쩌겠어요. 비정한 아비를 둔 제 잘못이죠.’
226|
227|‘알다가도 모를 아이구나. 정말 아무렇지 않은 게냐?’
228|
229|‘제가 싫다고 하면, 마음을 돌리실 건가요?’
230|
231|‘적어도 다른 방법을 찾아보겠지.’
232|
233|‘결국 태원진가와의 전쟁은 기정사실이군요.’
234|
235|‘산서괴협(山西怪俠)과 진천검이 없는 지금이 적기다. 두 번 다시 오지 않을 기회야.’
236|
237|‘가주와 이공자가 없어도 태원진가는 강해요. 부디 재고를.’
238|
239|‘불가(不可). 결정은 이미 내렸다.’
240|
241|‘그렇다면 반드시 승리하세요. 산서 땅에서 저에 관한 추문 따위는 입도 벙긋 못 할 정도로 강해지세요.’
242|
243|‘……네가 사내였다면 소문주로 삼았을 것이다.’
244|
245|‘여인으로 태어나서 다행이네요. 본문의 소문주 따위, 관심도 없으니.’
246|
247|
248|
249|우려는 얼마 지나지 않아 현실로 바뀌었다.
250|
251|보름이나 지났을까, 이소군이 싸늘한 시신으로 돌아왔다. 그리고 얼마 후에는 이천백이, 결국은 큰 오라버니인 이소광마저 잃고 말았다.
252|
253|‘이제는 나 혼자야.’
254|
255|그렇게 혈랑검 이천백의 마지막 남은 혈육은 새로운 문주가 되었다.
256|
257|말없이 봉분을 응시하는 이소월의 어깨를 따뜻한 손바닥이 조심스레 어루만졌다.
258|
259|“미안하구나. 내가 더 빨리 왔어야 했는데…….”
260|
261|“철 숙부, 그런 말씀 마세요. 숙부께서 와 주시지 않았다면 본 문은 지금까지 버티지도 못했을 테니까.”
262|
263|적풍단의 거친 공세에 항산검문은 속절없이 밀리는 중이었다. 뒤늦게 이천백의 변고를 접하고 달려온 항산호라는 절정 고수가 없었다면 적들이 물러나는 일도 없었을 것이다.
264|
265|“내 반드시 그놈의 사지를 찢어 죽일 것이다.”
266|
267|적풍단주를 떠올린 이소월은 고개를 저었다.
268|
269|절정 고수끼리의 생사결이라면 철무백이 한 수 앞선다.
270|
271|이미 앞서 한 번의 격돌이 있었고 풍양은 가벼운 내상과 함께 물러난 전적이 있다.
272|
273|‘하지만 두 번 다시 그런 기회는 오지 않아.’
274|
275|항산검문은 북쪽 고원의 마적들에 관해 늘 정보를 수집하고 촉각을 곤두세우고 있었다.
276|
277|고원에 존재하는 마적단은 수십 개지만 그중에서도 풍양이 이끄는 적풍단은 눈에 띌 정도로 무섭게 성장했다.
278|
279|고원의 우두머리 중에서도 특히 강하고 치밀한 자. 그가 바로 풍양이다.
280|
281|‘그런 자가 철 숙부와 생사결을 펼칠 리 없어. 섣불리 상대하려 했다가는 거꾸로 당하고 말 거야.’
282|
283|이소월은 철무백을 향해 고개를 돌렸다.
284|
285|“철 숙부. 풍양의 무공에 대해 다시 한번 말씀해 주실 수 있나요?”
286|
287|“절정 초입. 도법과 비도술이 경지에 오른 자였다. 다만.”
288|
289|철무백의 미간에 깊은 골이 파였다.
290|
291|“초식 하나하나가 음험하기 짝이 없더구나. 아마 사마외도(邪魔外道)의 무공을 익힌 듯싶었다.”
292|
293|“사마외도…….”
294|
295|정마대전 이후 중원에서 사마외도는 곧 죽음이라는 단어와 동일시되었다. 정파를 표방하는 사파는 있을지언정, 당당히 사파라고 외치는 이들은 없다.
296|
297|“아직까지는 짐작일 뿐이다. 다시 한번 붙어 보면 알게 되겠지.”
298|
299|“철 숙부를 믿어요. 그러나 적풍단주를 우습게 보진 마세요. 그에게는 목숨을 대신할 수하들이 얼마든지 있으니까.”
300|
301|위아래로 짓쳐 드는 적들을 합하면 삼백에 가까운 대병력.
302|
303|반면 항산검문은 각 지부에 나가 있는 무인들까지 모두 끌어모았음에도 그 절반에도 못 미친다.
304|
305|상황이 이렇다 보니 일반 무인들은 물론이고 새로 임명된 중진들의 사기도 저조했다.
306|
307|“소월아. 내 한마디 해도 되겠느냐?”
308|
309|죽은 벗과의 우정을 위해 자신의 목숨을 건 은인의 말이다. 이소월은 공손히 고개를 숙였다.
310|
311|“새겨듣겠습니다.”
312|
313|철무백이 무겁게 입을 뗐다.
314|
315|“떠나거라.”
316|
317|많은 의미가 담겨 있는 한마디.
318|
319|그러나 이소월의 대답에는 한 치의 망설임도 없었다.
320|
321|“죄송합니다.”
322|
323|“아직 늦지 않았다. 넌 살아남아야 한다.”
324|
325|“아직 끝나지 않았습니다. 살아남을 거고요.”
326|
327|“천백이 그 친구가 이런 걸 원한다고 생각했다면…….”
328|
329|“숙부님.”
330|
331|단호한 목소리에 철무백이 입을 다물었다. 이소월의 맑은 눈동자엔 굳은 결의가 어려 있었다.
332|
333|“제가 원한 겁니다. 항산검문의 문주로서.”
334|
335|“휴우…….”
336|
337|철무백은 대답 대신 한숨을 토해 냈다.
338|
339|“숙부께는 이미 많은 신세를 졌습니다. 이대로 떠나신다고 해도 원망하지 않을 거예요.”
340|
341|“굳이 내 대답을 들어야 직성이 풀리겠느냐?”
342|
343|이소월은 고개를 저었다. 어릴 적부터 그녀를 자식처럼 아껴 주었던 철무백이다. 오히려 아버지보다 더 아버지 같은 사람이기도 했다.
344|
345|“이 은혜는 결코 잊지 않겠습니다. 철 숙부는 저와 항산검문의 은인이십니다.”
346|
347|“어려서부터 봤지만…… 너는 참 영악한 아이다.”
348|
349|“어릴 때는 영악했고, 지금은 독한 년이죠.”
350|
351|싱긋 웃는 이소월을 보며 철무백은 연신 깊은 한숨만 내쉬었다.
352|
353|“승산은 있는 게냐?”
354|
355|“지금이라면 일 할.”
356|
357|“뭐라?”
358|
359|“하지만 지원군이 도착한다면 오 할. 그 이상이죠.”
360|
361|“지원군이라니, 혹시 태원진가에서?”
362|
363|“두 시진 전에 하오문 정양 지부에서 보낸 전서구가 도착했어요.”
364|
365|“얼마나 된다 하더냐? 백? 이백?”
366|
367|“넷이요. 그중 하나는 진천검 진무경이고, 다른 하나는…….”
368|
369|이소월이 실소를 흘렸다. 그와 얽힌 악연이 생각나서다.
370|
371|“산서잠룡 진태경.”
```

## Assembled English

```markdown
[P1]
# Chapter 111

[P2]
*Thudthudthudthud!*

[P3]
Four fine horses thundered down the main road. Exhausted from too little rest, they were already gasping for breath, but we couldn’t afford to ease the reins.

[P4]
> **System**
>
> **Time Limit:** 16:25:32

[P5]
31, 30. The time kept ticking down.

[P6]
Three *shichen*—a full six hours—had already passed. We had stopped at a small village along the way to look for fresh horses, but all they had were small, painfully slow packhorses.

[P7]
*We really do need to rest.*

[P8]
We were trapped between a rock and a hard place.

[P9]
We had been forcing our march as hard as we could, but the time limit was dangerously close. If we kept running like this, the horses wouldn’t hold out.

[P10]
*Do we have a choice?*

[P11]
I was just about to suggest to Wolhwa and Jin Mukyung that we rest, even if only briefly, when—

[P12]
“Hm?”

[P13]
“Young Master Jin! Ahead!”

[P14]
Even without Wolhwa’s shout, I had already seen them. Several dozen *jang* ahead, a group of dark figures blocked the main road.

[P15]
Every one of them wore filthy clothes, with a single curved saber sticking out from his belt. There was no need to say anything more.

[P16]
*The Red Wind Band.*

[P17]
The men had surrounded what appeared to be ordinary civilians and were threatening them. At the sound of hoofbeats, they whipped their heads around.

[P18]
The mounted bandits spotted me riding well out in front and grinned, baring their yellow teeth.

[P19]
“Well, look at that. Our next customer’s here already. Stop!”

[P20]
“Oh, sure.”

[P21]
They told me to stop, so I had to stop. What else could I do?

[P22]
*Thud! Thud!*

[P23]
“Gaaah!”

[P24]
“Argh!”

[P25]
My horse didn’t come to a halt until it had trampled the two or so men blocking the road. The mounted bandits—and even the travelers they had captured—stared at me wide-eyed.

[P26]
“You—you bastard!”

[P27]
I hopped down from the saddle and asked,

[P28]
“I’m asking just to make sure. You’re the Red Wind Band, right?”

[P29]
“Who the hell are you?”

[P30]
“Judging by your reaction, I guess I was right. I’m short on time, so let’s finish this quickly.”

[P31]
Without hesitation, I kicked the nearest man in the leg.

[P32]
*Crack.*

[P33]
With a chilling sound, his shinbone snapped, and he crumpled to the ground.

[P34]
It all happened in an instant. The others stood stunned for a moment, then hastily leveled their curved sabers and spears at me.

[P35]
“Kill him!”

[P36]
“A man should always watch his back.”

[P37]
“What?”

[P38]
“I said, watch behind you.”

[P39]
The instant I finished speaking, ten pairs of eyes turned to look behind them.

[P40]
*Craack! Thud!*

[P41]
Three fine horses charging at full speed swept the men away.

[P42]
* * *

[P43]
The battle was over before it had even begun. The men struck by the horses had been sent flying like bowling pins and lay sprawled out half-dead. The rest were easily subdued.

[P44]
“P-Please, just spare my life.”

[P45]
“I won’t kill you. But I’ll have to fix a few things first.”

[P46]
“Eek!”

[P47]
While Jin Mukyung methodically broke the limbs of the surviving bandits, Hyuk Mujin brought over the horses tied up beside the road.

[P48]
“It looks like we can switch to these healthy ones. There must be at least ten of them, so we might as well take them all and change horses whenever one gets tired.”

[P49]
I had been thinking the same thing. Unlike the last group we encountered, these mounted bandits each had their own horses. It was fortunate.

[P50]
*But still…*

[P51]
How many of these Red Wind Band bastards were there?

[P52]
According to the information we obtained at the shrine, more than a hundred remnants had scattered throughout northern Shanxi.

[P53]
Some were hiding in the foothills, while others were concealed in remote villages or crowded areas, gathering at a designated rendezvous point when ordered.

[P54]
*These men aren’t stragglers.*

[P55]
They were ambush forces carrying out an operation. The Red Wind Band Leader was replenishing his forces on the plateau and moving south, while sending the subordinates he had left behind north.

[P56]
I could easily understand why Wolhwa had described the Red Wind Band Leader as such a terrifying man.

[P57]
*The judgment to retreat swiftly when the tide turned against him. The meticulousness to prepare his next plan even while retreating. And the drive to put that plan into action.*

[P58]
On top of that, I had heard that his own martial arts were formidable.

[P59]
At this point, I almost felt bad for treating him as nothing more than a mounted bandit.

[P60]
*This has gotten seriously messy.*

[P61]
Now I understood why the Quest Grade had risen to Peak. Things kept getting worse the more I learned.

[P62]
Surely the Red Wind Band Leader wasn’t a Peak master too… right?

[P63]
I asked Wolhwa just in case, and she immediately nodded.

[P64]
“Yes. He is.”

[P65]
“…Ah.”

[P66]
“There has to be a reason someone rose to prominence so quickly. He isn’t widely known yet, but according to our sect’s intelligence, the Red Wind Band Leader is indeed a Peak master.”

[P67]
I was dumbfounded.

[P68]
“Why would a Peak master become a mounted bandit?”

[P69]
“There are even Supreme Peak masters among mountain bandits and water bandits. Why couldn’t a mounted bandit be one?”

[P70]
“Supreme Peak masters? Among mountain bandits and water bandits?”

[P71]
“If you ever meet the Green Forest Alliance Leader or the Alliance Leader of the Yangtze River Channel League, ask them yourself. Not that you ever will.”

[P72]
“…I sincerely hope that’s true.”

[P73]
A Supreme Peak master? I genuinely hoped I would never meet one.

[P74]
I shook my head repeatedly and mounted one of the newly taken horses. Jin Mukyung and Hyuk Mujin followed after tying up the Red Wind Band’s mounted bandits and handing them over to the commoners.

[P75]
> **System**
>
> **Time Limit:** 15:59:13

[P76]
The time limit continued to tick down even now. Leaving the commoners behind as they bowed deeply in thanks, we kicked the horses in the ribs.

[P77]
“Giddyap!”

[P78]
* * *

[P79]
Deep within the inner grounds of the Mount Heng Sword Sect stood a garden that only a very small number of people were allowed to enter. Cheol Mubaek, the Tiger of Mount Heng, was the only outsider granted that privilege.

[P80]
“This is my first time here.”

[P81]
“Because it was a special place. Whenever Father had something weighing on his mind, he would come to the garden.”

[P82]
Lee Seowol walked through the snow-covered garden, her footsteps crunching softly. Then she suddenly stopped when she spotted a frost-covered flower.

[P83]
“Mother loved this flower.”

[P84]
“Did she?”

[P85]
“Yes. Whenever she tended the garden, she would always bring me here and tell me the names of the flowers.”

[P86]
After thinking quietly for a moment, Lee Seowol continued.

[P87]
“But I can’t remember it now.”

[P88]
“It was a long time ago. Don’t trouble yourself over it.”

[P89]
“Uncle Cheol.”

[P90]
“Yes?”

[P91]
“I don’t like flowers. I only followed Mother because she liked them. In truth, I never cared about flowers. It’s the same reason Father used to come to the garden.”

[P92]
Lee Seowol slowly looked around the snow-covered garden. The flowers had withered, and the number of burial mounds in the center of the garden had grown from one to four.

[P93]
Her gaze sank as she silently stared at the mounds where her family slept.

[P94]
*Whose fault was it?*

[P95]
Perhaps it was her own fault for being born the daughter of a Murim martial artist.

[P96]
That was why she had lost her father and two older brothers one after another, after losing her mother ten years ago.

[P97]
*I should have kept trying to stop him until the very end…*

[P98]
A memory from two months ago suddenly resurfaced and blurred her vision.

[P99]
It had been a conversation between father and daughter, held late one night with no one else present.

[P100]
*“I’ll have to tie you to the third son of the Jin Family of Taiyuan.”*

[P101]
*“The third son? Surely you’re not thinking of marrying me to that good-for-nothing?”*

[P102]
*“No. But it will become an unbearable scandal for you.”*

[P103]
*“I see.”*

[P104]
*“Is that all you have to say?”*

[P105]
*“What can I do? It’s my fault for having a heartless father.”*

[P106]
*“You’re a child I can never understand. Are you really all right with this?”*

[P107]
*“If I say I don’t like it, will you change your mind?”*

[P108]
*“At the very least, I’ll look for another way.”*

[P109]
*“So the war with the Jin Family of Taiyuan is a foregone conclusion.”*

[P110]
*“Now that the Strange Hero of Shanxi and the Heaven Shaking Sword are absent, this is the perfect time. This opportunity will never come again.”*

[P111]
*“The Jin Family of Taiyuan is strong even without the Family Head and the Second Young Master. Please reconsider.”*

[P112]
*“No. My decision has already been made.”*

[P113]
*“Then make sure you win. Become strong enough that no one in Shanxi can even open their mouth about a scandal involving me.”*

[P114]
*“…If you had been a man, I would have made you the Young Sect Leader.”*

[P115]
*“I’m glad I was born a woman. I have no interest in being this sect’s Young Sect Leader.”*

[P116]
Her fears soon became reality.

[P117]
Had even a fortnight passed before Lee Seogeun returned as a cold corpse? Not long after, she lost Lee Cheonbaek. In the end, even her eldest brother, Lee Seogwang, was gone.

[P118]
*Now I’m alone.*

[P119]
And so, the Blood Wolf Sword Lee Cheonbaek’s last surviving blood relative became the new Sect Leader.

[P120]
As she silently gazed at the burial mounds, a warm palm gently caressed her shoulder.

[P121]
“I’m sorry. I should have come sooner…”

[P122]
“Uncle Cheol, please don’t say that. If you hadn’t come, our sect wouldn’t have been able to hold out this long.”

[P123]
Under the Red Wind Band’s fierce assault, the Mount Heng Sword Sect had been helplessly driven back. If not for the Peak master known as the Tiger of Mount Heng, who had rushed over after belatedly learning of Lee Cheonbaek’s calamity, the enemy would never have withdrawn.

[P124]
“I’ll tear that bastard limb from limb and kill him.”

[P125]
At the thought of the Red Wind Band Leader, Lee Seowol shook her head.

[P126]
In a life-and-death duel between Peak masters, Cheol Mubaek had the edge.

[P127]
They had already clashed once, and Pung Yang had retreated with a minor internal injury.

[P128]
*But an opportunity like that will never come again.*

[P129]
The Mount Heng Sword Sect had always gathered information on the mounted bandits of northern Gaoyuan and remained constantly on alert.

[P130]
There were dozens of mounted-bandit groups in Gaoyuan, but among them, the Red Wind Band led by Pung Yang had grown frighteningly fast.

[P131]
A man particularly strong and meticulous even among Gaoyuan’s chieftains.

[P132]
That man was Pung Yang.

[P133]
*There’s no way someone like that would engage Uncle Cheol in a life-and-death duel. If Uncle Cheol rashly tried to confront him, Pung Yang would turn the tables on him instead.*

[P134]
Lee Seowol turned toward Cheol Mubaek.

[P135]
“Uncle Cheol, could you tell me once more about Pung Yang’s martial arts?”

[P136]
“Early Peak. His saber arts and throwing-knife techniques had reached a high realm. However…”

[P137]
A deep furrow formed between Cheol Mubaek’s brows.

[P138]
“Every one of his forms was thoroughly insidious. I suspect he has learned demonic, heterodox martial arts.”

[P139]
“Demonic, heterodox arts…”

[P140]
Ever since the Great Faction War, practicing demonic, heterodox arts had become synonymous with death in the Central Plains. Unorthodox factions might present themselves as orthodox, but no one openly declared themselves unorthodox.

[P141]
“For now, it’s only a suspicion. We’ll know if we clash again.”

[P142]
“I trust you, Uncle Cheol. But don’t underestimate the Red Wind Band Leader. He has any number of subordinates he can sacrifice in his place.”

[P143]
With enemies bearing down from both directions, their combined force was close to three hundred strong.

[P144]
Meanwhile, even after gathering every martial artist stationed at its branches, the Mount Heng Sword Sect had less than half that number.

[P145]
Given the situation, morale was low among both the ordinary martial artists and the newly appointed senior members.

[P146]
“Seowol. May I say something?”

[P147]
These were the words of a benefactor who had risked his life out of loyalty to his dead friend. Lee Seowol bowed politely.

[P148]
“I’ll take your words to heart.”

[P149]
Cheol Mubaek spoke heavily.

[P150]
“Leave.”

[P151]
It was a single word laden with meaning.

[P152]
But there was not the slightest hesitation in Lee Seowol’s answer.

[P153]
“I’m sorry.”

[P154]
“It isn’t too late. You must survive.”

[P155]
“It isn’t over yet. And I will survive.”

[P156]
“If you thought Cheonbaek would have wanted this…”

[P157]
“Uncle.”

[P158]
At her resolute voice, Cheol Mubaek closed his mouth. Firm determination filled Lee Seowol’s clear eyes.

[P159]
“This is what I wanted. As the Sect Leader of the Mount Heng Sword Sect.”

[P160]
“Whew…”

[P161]
Cheol Mubaek let out a sigh instead of answering.

[P162]
“I’m already deeply indebted to you, Uncle. Even if you leave now, I won’t resent you.”

[P163]
“Do you really need to hear my answer before you’ll be satisfied?”

[P164]
Lee Seowol shook her head. Cheol Mubaek had cherished her like his own child since she was young. In some ways, he had been more of a father to her than her actual father.

[P165]
“I will never forget this debt. Uncle Cheol, you are the benefactor of both me and the Mount Heng Sword Sect.”

[P166]
“I’ve watched you since you were little, but… you really are a sly child.”

[P167]
“I was sly when I was young. Now I’m a ruthless bitch.”

[P168]
Watching Lee Seowol smile faintly, Cheol Mubaek could only continue to sigh deeply.

[P169]
“Do we have any chance of winning?”

[P170]
“If we fought now? Ten percent.”

[P171]
“What?”

[P172]
“But if reinforcements arrive, fifty percent. More than that.”

[P173]
“Reinforcements? From the Jin Family of Taiyuan?”

[P174]
“A messenger pigeon from the Lower District Sect’s Jeongyang Branch arrived two *shichen* ago.”

[P175]
“How many are coming? A hundred? Two hundred?”

[P176]
“Four. One of them is the Heaven Shaking Sword, Jin Mukyung, and another is…”

[P177]
Lee Seowol let out a wry laugh, reminded of her ill-fated connection with him.

[P178]
“The Sleeping Dragon of Shanxi, Jin Taekyung.”
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
# Chapter 111

[P2]
*Thudthudthudthud!*

[P3]
Four fine horses raced down the main road. Exhausted from their lack of rest, the horses were already gasping for breath, but there was no way we could loosen the reins.

[P4]
> **System**
>
> **Time Limit:** 16:25:32

[P5]
31, 30. The time kept ticking down.

[P6]
Three *sijin*—six hours—had already passed. We had tried to stop at a small village along the way and find fresh horses, but all they had were small, painfully slow packhorses.

[P7]
*We really do need to rest.*

[P8]
We were trapped between a rock and a hard place.

[P9]
We had been forcing our march as hard as we could, but the time limit was dangerously close. If we kept running like this, the horses wouldn’t hold out.

[P10]
*Can’t be helped.*

[P11]
I was just about to suggest to Wolhwa and Jin Mukyung that we rest, even if only briefly, when—

[P12]
“Hm?”

[P13]
“Young Master Jin! Ahead!”

[P14]
Even without Wolhwa’s shout, I had already seen them. Several dozen *jang* ahead, a group of dark figures blocked the main road.

[P15]
Every one of them wore filthy clothes, with a single curved saber sticking out from his belt. There was no need to say anything more.

[P16]
*The Red Wind Band.*

[P17]
The men had surrounded what appeared to be ordinary civilians and were threatening them. At the sound of hoofbeats, they whipped their heads around.

[P18]
The mounted bandits spotted me riding well out in front and grinned, baring their yellow teeth.

[P19]
“Well, look at that. Our next customers have already arrived. Stop!”

[P20]
“Oh, sure.”

[P21]
They told me to stop, so I had to stop. What else could I do?

[P22]
*Thud! Thud!*

[P23]
“Gaaah!”

[P24]
“Argh!”

[P25]
The fine horse I was riding didn’t come to a stop until it had trampled the two men blocking the road. The mounted bandits—and even the travelers they had been holding captive—stared at me with their eyes wide.

[P26]
“You—you bastard!”

[P27]
I hopped down from the saddle and asked,

[P28]
“I’m asking just to make sure. You’re the Red Wind Band, right?”

[P29]
“What the hell are you?”

[P30]
“Judging by your reaction, I guess I was right. I’m short on time, so let’s finish this quickly.”

[P31]
Without hesitation, I kicked the leg of the nearest man.

[P32]
*Crack.*

[P33]
With a chilling sound, his shinbone snapped, and he collapsed.

[P34]
It all happened in an instant. The men who had been momentarily stunned quickly thrust curved sabers and spears at me.

[P35]
“Kill him!”

[P36]
“A man should always watch his rear.”

[P37]
“What?”

[P38]
“Be careful behind you.”

[P39]
The instant I finished speaking, ten pairs of eyes turned to look behind them.

[P40]
*Craack! Thud!*

[P41]
Three fine horses charging at full speed swept the men away.

[P42]
* * *

[P43]
The battle was over before it had even begun. The men struck by the horses had been sent flying like bowling pins and lay sprawled out half-dead. The rest were easily subdued.

[P44]
“P-Please, just spare my life.”

[P45]
“I won’t kill you. But I’ll have to fix a few things first.”

[P46]
“Eek!”

[P47]
While Jin Mukyung methodically broke the limbs of the surviving bandits, Hyuk Mujin brought over the horses tied up beside the road.

[P48]
“It looks like we can switch to these healthy ones. There must be at least ten of them, so we could take them all and switch whenever they get tired.”

[P49]
I had been thinking the same thing. Unlike the last group we encountered, these mounted bandits each had their own horses. It was fortunate.

[P50]
*But still…*

[P51]
How many of these Red Wind Band bastards were there?

[P52]
According to the information we obtained at the shrine, more than a hundred remnants had scattered throughout northern Shanxi.

[P53]
Some were hiding in the foothills, while others were concealed in remote villages or crowded areas, gathering at a designated rendezvous point when ordered.

[P54]
*These men aren’t stragglers.*

[P55]
They were ambush forces carrying out an operation. The Red Wind Band Leader was replenishing his forces on the plateau and moving south, while sending the subordinates he had left behind north.

[P56]
I could easily understand why Wolhwa had described the Red Wind Band Leader as such a terrifying man.

[P57]
*The judgment to retreat swiftly when the battle turned against him. The meticulousness to prepare his next plan even in the middle of it all. And the drive to carry that plan out.*

[P58]
On top of that, I had heard that his own martial arts were formidable.

[P59]
At this point, I almost felt bad for treating him as nothing more than a mounted bandit.

[P60]
*This has gotten seriously messy.*

[P61]
Now I understood why the Quest Grade had risen to Peak. And when I thought about it, things seemed to be getting worse by the minute.

[P62]
It couldn’t be that the Red Wind Band Leader was a Peak master too, could it?

[P63]
I asked Wolhwa just in case.

[P64]
She immediately nodded.

[P65]
“Yes. He is.”

[P66]
“…Ah.”

[P67]
“There has to be a reason someone rose to prominence so quickly. He isn’t widely known yet, but according to our sect’s intelligence, the Red Wind Band Leader is indeed a Peak master.”

[P68]
I was dumbfounded.

[P69]
“Why would a Peak master become a mounted bandit?”

[P70]
“There are even Supreme Peak masters among mountain bandits and water bandits. Why couldn’t a mounted bandit be one?”

[P71]
“Supreme Peak masters? Among mountain bandits and water bandits?”

[P72]
“When you meet the Green Forest Alliance Leader or the Alliance Leader of the Yangtze River Channel League, ask them yourself. Not that you ever will.”

[P73]
“…I sincerely hope that’s true.”

[P74]
A Supreme Peak master? I genuinely hoped I would never meet one.

[P75]
I shook my head repeatedly and mounted one of the newly taken horses. Jin Mukyung and Hyuk Mujin followed after tying up the Red Wind Band’s mounted bandits and handing them over to the commoners.

[P76]
> **System**
>
> **Time Limit:** 15:59:13

[P77]
The time limit continued to tick down even now. Leaving the commoners behind as they bowed deeply in thanks, we kicked the horses in the ribs.

[P78]
“Giddyap!”

[P79]
* * *

[P80]
Deep within the inner grounds of the Mount Heng Sword Sect stood a garden that only a very small number of people were allowed to enter. Cheol Mubaek, the Tiger of Mount Heng, was the only outsider granted that privilege.

[P81]
“This is my first time here.”

[P82]
“Because it was a special place. Whenever Father had something weighing on his mind, he would come to the garden.”

[P83]
Lee Seowol walked through the snow-covered garden, her footsteps crunching softly. Then she suddenly stopped when she spotted a frost-covered flower.

[P84]
“This was one of Mother’s favorite flowers.”

[P85]
“Was it?”

[P86]
“Yes. Whenever she tended the garden, she would always bring me here and tell me the names of the flowers.”

[P87]
After thinking quietly for a moment, Lee Seowol continued.

[P88]
“But I can’t remember it now.”

[P89]
“It was a long time ago. Don’t trouble yourself over it.”

[P90]
“Uncle Cheol.”

[P91]
“Yes?”

[P92]
“I don’t like flowers. I only followed Mother because she liked them. In truth, I never cared about flowers. It’s the same reason Father used to come to the garden.”

[P93]
Lee Seowol slowly looked around the snow-covered garden. The flowers had withered, and the number of burial mounds in the center of the garden had grown from one to four.

[P94]
Her gaze sank as she silently stared at the mounds where her family slept.

[P95]
*Whose fault was it?*

[P96]
Perhaps it was her own fault for being born the daughter of a Murim martial artist.

[P97]
That was why she had lost her father and two older brothers one after another, after losing her mother ten years ago.

[P98]
*I should have kept trying to stop him until the very end…*

[P99]
A memory from two months ago suddenly resurfaced and blurred her vision.

[P100]
It had been a conversation between father and daughter, held late one night with no one else present.

[P101]
*“I’ll have to tie you to the third son of the Jin Family of Taiyuan.”*

[P102]
*“The third son? Surely you’re not thinking of marrying me to that good-for-nothing?”*

[P103]
*“No. But it will become an unbearable scandal for you.”*

[P104]
*“I see.”*

[P105]
*“Is that all you have to say?”*

[P106]
*“What can I do? It’s my fault for having a heartless father.”*

[P107]
*“You’re a child I can never understand. Are you really all right with this?”*

[P108]
*“If I say I don’t like it, will you change your mind?”*

[P109]
*“At the very least, I’ll look for another way.”*

[P110]
*“So the war with the Jin Family of Taiyuan is a foregone conclusion.”*

[P111]
*“Now that the Strange Hero of Shanxi and the Heaven Shaking Sword are absent, this is the perfect time. This opportunity will never come again.”*

[P112]
*“The Jin Family of Taiyuan is strong even without the Family Head and the Second Young Master. Please reconsider.”*

[P113]
*“No. My decision has already been made.”*

[P114]
*“Then make sure you win. Become strong enough that no one in Shanxi can even open their mouth about a scandal involving me.”*

[P115]
*“…If you had been a man, I would have made you the Young Sect Leader.”*

[P116]
*“I’m glad I was born a woman. I have no interest in being this sect’s Young Sect Leader.”*

[P117]
Her fears soon became reality.

[P118]
Had even a fortnight passed before Lee Seogeun returned as a cold corpse? Not long after, she lost Lee Cheonbaek, and in the end, even her eldest older brother, Lee Seogwang.

[P119]
*Now I’m alone.*

[P120]
And so, the Blood Wolf Sword Lee Cheonbaek’s last surviving blood relative became the new Sect Leader.

[P121]
A warm palm gently caressed Lee Seowol’s shoulder.

[P122]
“I’m sorry. I should have come sooner…”

[P123]
“Uncle Cheol, please don’t say that. If you hadn’t come, our sect wouldn’t have been able to hold out this long.”

[P124]
Under the Red Wind Band’s fierce assault, the Mount Heng Sword Sect had been helplessly driven back. If not for the Peak master known as the Tiger of Mount Heng, who had rushed over after belatedly learning of Lee Cheonbaek’s calamity, the enemy would never have withdrawn.

[P125]
“I’ll tear that bastard limb from limb and kill him.”

[P126]
At the thought of the Red Wind Band Leader, Lee Seowol shook her head.

[P127]
In a life-and-death duel between Peak masters, Cheol Mubaek had the edge.

[P128]
They had already clashed once, and Pung Yang had retreated with a minor internal injury.

[P129]
*But an opportunity like that will never come again.*

[P130]
The Mount Heng Sword Sect had always gathered information on the mounted bandits of the northern plateau and remained constantly on alert.

[P131]
There were dozens of mounted-bandit groups on the plateau, but among them, the Red Wind Band led by Pung Yang had grown frighteningly fast.

[P132]
A man particularly strong and meticulous even among the plateau’s chieftains.

[P133]
That man was Pung Yang.

[P134]
*There’s no way someone like that would engage Uncle Cheol in a life-and-death duel. If Uncle Cheol rashly tried to confront him, Pung Yang would turn the tables on him instead.*

[P135]
Lee Seowol turned toward Cheol Mubaek.

[P136]
“Uncle Cheol, could you tell me once more about Pung Yang’s martial arts?”

[P137]
“Early Peak. His saber arts and throwing-knife techniques had reached a high realm. However…”

[P138]
A deep furrow formed between Cheol Mubaek’s brows.

[P139]
“Every one of his forms was thoroughly insidious. I suspect he has learned demonic, heterodox martial arts.”

[P140]
“Demonic, heterodox arts…”

[P141]
After the Great Faction War, belonging to the evil and heretical paths was tantamount to death in the Central Plains. Unorthodox factions might present themselves as orthodox, but no one openly proclaimed themselves unorthodox.

[P142]
“For now, it’s only a suspicion. We’ll know if we clash again.”

[P143]
“I trust you, Uncle Cheol. But don’t underestimate the Red Wind Band Leader. He has any number of subordinates he can sacrifice in his place.”

[P144]
With enemies bearing down from both directions, their combined force was close to three hundred strong.

[P145]
Meanwhile, even after gathering every martial artist stationed at its branches, the Mount Heng Sword Sect had less than half that number.

[P146]
Given the situation, morale was low among both the ordinary martial artists and the newly appointed senior members.

[P147]
“Seowol. May I say something?”

[P148]
These were the words of a benefactor who had risked his life out of loyalty to his dead friend. Lee Seowol bowed politely.

[P149]
“I’ll take your words to heart.”

[P150]
Cheol Mubaek spoke heavily.

[P151]
“Leave.”

[P152]
It was a single word laden with meaning.

[P153]
But there was not the slightest hesitation in Lee Seowol’s answer.

[P154]
“I’m sorry.”

[P155]
“It isn’t too late. You must survive.”

[P156]
“It isn’t over yet. And I will survive.”

[P157]
“If you thought Cheonbaek would have wanted this…”

[P158]
“Uncle.”

[P159]
At her resolute voice, Cheol Mubaek closed his mouth. Firm determination filled Lee Seowol’s clear eyes.

[P160]
“This is what I wanted. As the Sect Leader of the Mount Heng Sword Sect.”

[P161]
“Whew…”

[P162]
Cheol Mubaek let out a sigh instead of answering.

[P163]
“I’m already deeply indebted to you, Uncle. Even if you leave now, I won’t resent you.”

[P164]
“Do you really need to hear my answer before you’ll be satisfied?”

[P165]
Lee Seowol shook her head. Cheol Mubaek had cherished her like his own child since she was young. In some ways, he had been more of a father to her than her actual father.

[P166]
“I will never forget this debt. Uncle Cheol, you are the benefactor of both me and the Mount Heng Sword Sect.”

[P167]
“I’ve watched you since you were little, but… you really are a sly child.”

[P168]
“I was sly when I was young. Now I’m a ruthless bitch.”

[P169]
Watching Lee Seowol smile faintly, Cheol Mubaek could only continue to sigh deeply.

[P170]
“Do we have any chance of winning?”

[P171]
“If we fought now? Ten percent.”

[P172]
“What?”

[P173]
“But if reinforcements arrive, fifty percent. More than that.”

[P174]
“Reinforcements? From the Jin Family of Taiyuan?”

[P175]
“A messenger pigeon sent by the Lower District Sect’s Jeongyang Branch arrived four hours ago.”

[P176]
“How many are there? One hundred? Two hundred?”

[P177]
“Four. One of them is the Heaven Shaking Sword, Jin Mukyung, and another is…”

[P178]
Lee Seowol let out a wry laugh, reminded of her ill-fated connection with him.

[P179]
“The Sleeping Dragon of Shanxi, Jin Taekyung.”
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 이소광    | **Lee Seogwang**   |
| 이소군    | **Lee Seogeun**    |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 일신     | **One God**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 초식     | **form**                                         | Numbered technique movement                           |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 은인     | **Benefactor**                               |
| 퀘스트              | **Quest**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 본문      | **our sect / this sect**                                        |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 정양 | **Jeongyang** | Shanxi location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 산서괴협 | **Strange Hero of Shanxi** | Epithet referenced for the absent martial artist. |
| 녹림맹주 | **Green Forest Alliance Leader** | Leader title for the Green Forest Alliance. |
| 장강수로맹주 | **Alliance Leader of the Yangtze River Channel League** | Leader title for the Yangtze River Channel League. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 111,
  "passed": true,
  "metrics": {
    "source_characters": 5818,
    "translation_characters": 13476,
    "length_ratio": 2.316,
    "source_paragraphs": 175,
    "translation_paragraphs": 178
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "일신",
        "preferred": "One God"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진태",
        "preferred": "Jintae"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "송이",
        "preferred": "Song-i"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "천백",
        "romanization": "cheonbaek"
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
