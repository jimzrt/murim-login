# Fidelity Gate — Chapter 110

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
  1|＃110화
  2|
  3|
  4|
  5|쾅!
  6|
  7|굉음과 함께 나타난 것은 장대한 체구의 중년인이었다.
  8|
  9|억세게 뻗친 눈썹 아래, 성난 맹수처럼 호목(虎目)을 부릅뜬 그가 좌중을 쓸어 본다.
 10|
 11|“방금 헛소리를 지껄인 자가 누구냐?”
 12|
 13|이 자리에 모인 이들은 모두 항산검문의 중진.
 14|
 15|전임자만큼은 아니어도 일류의 무공과 일정 이상의 경륜을 지닌 이들이다. 그러나 그들조차도 목을 움츠리고 시선을 피하기 바빴다.
 16|
 17|눈앞의 중년인은 그럴 자격이 충분히 있는 사람이니까.
 18|
 19|‘제길, 하필이면 항산호(恒山虎)한테…….’
 20|
 21|호사가들이 이르길, 항산에는 두 마리 맹수가 산다고 했다.
 22|
 23|혈랑검과 항산호. 절친한 벗이자 서로가 넘어야 할 벽.
 24|
 25|중년인, 철무백은 이미 수십 년 전부터 항산의 호랑이라 불리는 절정 고수였다.
 26|
 27|“어느 놈이냐 물었다!”
 28|
 29|그 포효 같은 외침에 항산검문의 중진들은 전신의 털이 쭈뼛 곤두섰다.
 30|
 31|철무백이 한번 꼭지가 돌면 친우였던 이천백조차 자리를 피한다고 했다. 하물며 무공과 연배에서 한참 뒤처지는 그들이니 두말할 것도 없다.
 32|
 33|“일치단결하여 저 말 도적놈들을 몰아내도 모자랄 판에, 감히 천백의 유지를 어기고 역심을 품어?”
 34|
 35|화염이 쏟아질 듯한 눈빛에 항산검문의 중진들은 불에 덴 것처럼 화들짝 놀랐다.
 36|
 37|“처, 철 대협. 오해십니다.”
 38|
 39|“저희가 어찌 감히 역심을 품겠습니까.”
 40|
 41|“그럼 내 나이가 늙어 귀가 어두워진 것이냐?”
 42|
 43|그 순간, 대전 안의 사람들은 갈증을 느꼈다. 단순한 착각이 아니라 철무백이 뿜어내는 가공할 만한 열양지기(熱陽地氣) 때문이었다.
 44|
 45|‘이런 미친.’
 46|
 47|‘도대체 뭘 얼마나 처먹었기에 이런 무지막지한 공력이…….’
 48|
 49|단순히 가까이 있는 것만으로도 숨이 막히고 땀이 줄줄 흐른다. 항산호. 약관 무렵부터 광활한 산맥의 어딘가에서 홀로 무공을 익혔다는 절정 고수의 진면목이 드러나는 순간이다.
 50|
 51|“훅, 후우욱.”
 52|
 53|“대협, 부디 고정하십, 후욱.”
 54|
 55|거친 숨을 몰아쉬는 항산검문의 중진들, 그리고 용서의 기미 없이 그들을 노려보는 절정 고수.
 56|
 57|대전 안의 공기가 용암처럼 들끓어 오르려던 그때였다.
 58|
 59|“철 숙부, 더워요.”
 60|
 61|시냇물처럼 청량한 목소리와 철무백의 소매를 잡아당기는 희고 가느다란 손가락. 그와 동시에 분노로 주름져 있던 철무백의 미간이 누군가 잡아당긴 것처럼 쫙 펴졌다.
 62|
 63|“마, 많이 더웠느냐?”
 64|
 65|“네, 숨도 못 쉬겠어요.”
 66|
 67|“이런, 내가 미처 네 생각을 못 했구나. 지금은 어떠하냐?”
 68|
 69|“한결 나아졌어요. 고마워요, 철 숙부.”
 70|
 71|“그런 말은 하지 말거라. 소월이 너를 지키는 게 내 할 일인 것을.”
 72|
 73|철무백의 강대한 열양지기가 사그라든다.
 74|
 75|그제야 곳곳에서 참았던 숨이 터져 나왔다. 땀으로 흠뻑 젖은 사람들은 정신을 차리고 난 뒤에 철무백이 혼자가 아님을 깨달았다.
 76|
 77|“아, 아가씨.”
 78|
 79|“아가씨를 뵙습니다.”
 80|
 81|황급히 자리에서 일어나 예의를 표하는 중진들의 모습에 눈썹을 치켜뜨는 철무백. 그러나 ‘아가씨’가 한발 빨랐다.
 82|
 83|“철검대주님, 수문각주님. 두 분께 마지막으로 말씀드릴게요.”
 84|
 85|철무백의 거구에 가려져 보이지 않던 그녀가 모습을 드러낸다. 마르고 늘씬한 체구. 푸른색 궁장 밑단이 바닥을 스칠 때마다 사각거렸다.
 86|
 87|“호칭을 바꾸세요. 아가씨가 아니라 문주님, 으로.”
 88|
 89|서리가 내려앉은 듯한 그녀의 눈빛을 마주한 사람들은 잠시 잊고 있던 사실 하나를 떠올렸다.
 90|
 91|‘아, 그랬지.’
 92|
 93|혈랑검 이천백.
 94|
 95|이소월은 그의 피를 가장 진하게 이어받은 자식이다.
 96|
 97|
 98|
 99|* * *
100|
101|
102|
103|나는 승마에 관해서는 문외한이다. 무림에 온 후에야 몇 번 타 본 정도지. 현대에서 승마는 부자들에게만 허락된 귀족 스포츠나 다름없어서 접해 볼 기회가 없었다.
104|
105|하지만 신체 능력이 워낙 좋은 데다가 잘 훈련된 말을 타고 있어서 그런지, 격렬한 질주 중에도 시스템창을 볼 만큼 여유가 있었다.
106|
107|‘퀘스트창 오픈.’
108|
109|띠링.
110|
111|
112|
113|퀘스트
114|
115|
116|
117|[어제의 적, 오늘의 동지]
118|
119|모든 진실이 밝혀진 지금, 항산검문은 적이 아니라 손을 잡아야 할 동지입니다. 곧 다가오는 원단에 그들을 태원진가로 초대하십시오.
120|
121|
122|
123|등급 : 절정
124|
125|제한 : 진태경
126|
127|임무 : 초대장 전달 (미완료)
128|
129|보상 : ???
130|
131|실패 : 없음
132|
133|
134|
135|
136|
137|퀘스트는 유동적이다. 상황에 따라서 돌발 퀘스트가 발생하기도 하고 지금처럼 퀘스트가 갱신되기도 한다.
138|
139|‘등급 상향 조정이라.’
140|
141|퀘스트 등급이 일류에서 절정으로 바뀌었다는 것은 항산검문으로 가는 길이 녹록지 않아졌다는 걸 의미했다.
142|
143|예를 들자면 적풍단이라든지. 혹은 적풍단이라든지. 아마 적풍단…… 됐다. 더 말해 봤자 마음만 아프다.
144|
145|‘이 동네는 하루하루가 살얼음판이 따로 없네.’
146|
147|간만에 쉬운 퀘스트 하나 받나 했더니 또 일이 터졌다.
148|
149|하지만 예전만큼 초조하지 않은 이유는, 진무경이라는 든든한 존재 덕분도 있지만 나 자신이 강해졌기 때문이다.
150|
151|‘상태창 오픈.’
152|
153|띠링.
154|
155|
156|
157|상태창
158|
159|
160|
161|[Lv.55 진태경]
162|
163|직업 : 일류 무인
164|
165|명성 : 1300 (+150)
166|
167|칭호 : 4개 (칭호 효과 적용 중)
168|
169|- 귀환자 (모든 능력치 +10)
170|
171|- 산서잠룡 (모든 능력치 +10, 명성 +100)
172|
173|- 명가의 자제 (모든 능력치 +5, 명성 +50)
174|
175|- 승부사 (일대일 전투 시 전투 관련 능력치 +10%)
176|
177|근력 : 196 (+25)체력 : 195 (+25)
178|
179|민첩 : 192 (+25)지력 : 35(+25)
180|
181|매력 : 35(+25)공력 : 15년
182|
183|맷집 : 155(+25)
184|
185|잔여 포인트 : 0
186|
187|
188|
189|
190|
191|‘크으, 주모.’
192|
193|혼자 잘 컸다, 잘 컸어.
194|
195|각각 200포인트에 육박하는 근력, 민첩, 체력은 보기만 해도 배가 부르고, 진무경에게 두들겨 맞으면서 생겨난 맷집도 잘 크고 있다.
196|
197|‘칭호 옵션 효과도 빵빵하고. 이 정도면 충분해.’
198|
199|지금까지는 살기 위해 스탯을 올렸다. 퀘스트 하나 진행할 때마다 온갖 위기가 삼각파도처럼 밀려오는데 매력과 지력에 포인트를 투자할 여력이 있었을 리가.
200|
201|‘지력 올려서 아이큐 180 되면 창을 과학적으로 찌르는 것도 아니고.’
202|
203|매력도 마찬가지다. 조필이나 대장로가 얼굴 좀 잘생겼다고 살려 줄 것 같진 않거든.
204|
205|물론 올려 둔다면 나중에 어떤 식으로든 도움이 되겠지만, 당장 목숨이 간당거리는 와중에 비전투 스탯에 투자할 용기가 없었다.
206|
207|‘이제 내 한목숨 지키는 건 어느 정도 가능하다.’
208|
209|이번 퀘스트만 끝나면 공력과 비전투 스탯에 신경을 써 볼 생각이다.
210|
211|안 그래도 조필을 쓰러트리고 얻은 [열화신단]을 포함한 아이템들이 인벤토리에 고이 잠자고 있다.
212|
213|‘물론 잘못 먹으면 골로 가겠지만.’
214|
215|그때 선두에서 달려가던 월화가 개울을 발견하고 멈춰 섰다.
216|
217|“잠시만 쉬어 갈게요. 말들이 너무 지쳐서.”
218|
219|시간이 얼마나 흘렀을까?
220|
221|사당에서부터 쉬지 않고 달리다 보니 동이 트고 해가 중천에 걸렸다. 중간에 근력과 체력이 올랐다는 시스템 메시지도 두 번이나 뜰 정도였으니 강행군은 강행군이었던 모양이다.
222|
223|“후. 엉덩이 아파 죽겠네요. 이럴 줄 알았으면 농부가 아니라 마부 아들로 태어났어야 했는데.”
224|
225|말이 휴식하는 틈을 타 혁무진이 털썩 주저앉았다. 일행 중 가장 레벨이 떨어지는 녀석이니만큼 체력 소모가 눈에 띄었다.
226|
227|“힘드냐?”
228|
229|혁무진이 소매로 이마의 땀을 훔치며 대답했다.
230|
231|“솔직히 힘들긴 한데…… 이상하게 지난번보다는 훨씬 낫네요.”
232|
233|“지난번이라니?”
234|
235|“벌써 잊으셨어요? 정찰 임무 때요.”
236|
237|“아, 기억난다.”
238|
239|백호당 소속으로 정찰 임무를 맡았다가 조필을 만나는 바람에 죽을 뻔했던 일. 그때도 분명 말을 끌고 가긴 했었지.
240|
241|‘나중에는 폭설이 내리는 바람에 말도 버리고 갔지만.’
242|
243|예전 일을 떠올리자 피식 웃음이 새어 나왔다.
244|
245|“왜 그러세요?”
246|
247|“네 생각 나서. 나한테 멋모르고 까불다가 엄청 맞았잖아.”
248|
249|“……꼭 그렇게 지난 얘기를 들춰내야 속이 후련하세요?”
250|
251|“물어본 건 너야, 인마.”
252|
253|“어쨌든, 그때보다는 훨씬 나아진 것 같다고요.”
254|
255|“그래?”
256|
257|“네. 정찰 임무 때보다 훨씬 많이 달렸는데 별로 지치지도 않고 그러네요. 말 타는 게 좀 익숙해져서 그런가?”
258|
259|“그런 걸지도…… 아, 잠깐만.”
260|
261|“예?”
262|
263|문득 짚이는 구석이 있어 기감을 끌어올렸다.
264|
265|띠링. 익숙한 시스템 알림과 함께 어리둥절해하는 혁무진의 얼굴 위로 레벨창이 떠오른다.
266|
267|
268|
269|[Lv.38 혁무진]
270|
271|
272|
273|“……엥?”
274|
275|벌어진 입에서 바람 빠지는 소리가 새어 나온다. 혁무진이 언제부터 레벨이 이렇게 높았지?
276|
277|‘엄밀히 말해서 엄청나게 높은 건 아니지만.’
278|
279|녀석과 처음 만났을 때 20레벨에 불과했던 걸 생각하면 장족의 발전이라는 말도 부족하다. 이 정도면 거의 새로 태어난 수준인데?
280|
281|‘그러고 보면 처음 만난 이후로 꾸준히 올랐던 것 같기도 하고.’
282|
283|기억을 더듬어 보니 처음보다 또렷하게 떠올릴 수 있었다.
284|
285|정찰조로 재회했을 때도 그랬고, 틈틈이 기감을 끌어올릴 때마다 옆에 있던 혁무진의 레벨은 1, 2씩 올라 있었다.
286|
287|그러던 게 어느새 38레벨. 무림에서의 시간으로만 치면 근 두 달 남짓한 시간 동안 두 배 가까이 성장을 이룬 거다.
288|
289|‘그럼 혹시?’
290|
291|설마 하는 마음에 혁무진을 뚫어져라 바라봤다.
292|
293|이 녀석도 나처럼 스탯 포인트를 받는다면? 그걸 내가 대신 분배해 줄 수도 있지 않을까?
294|
295|‘가능성이 있는 이야기지.’
296|
297|내가 비슷한 레벨의 헌터나 무인보다 훨씬 강한 걸로 봐서는 시스템 보정 효과가 있는 것 같긴 한데…….
298|
299|‘한 번 시도해 볼 만해.’
300|
301|“왜 그러세요? 제 얼굴에 뭐라도 묻었습니까?”
302|
303|“아니. 그냥 못생겨서.”
304|
305|“……아, 진짜.”
306|
307|꿍얼거리는 혁무진의 어깨를 잡고 마음으로 외쳤다.
308|
309|‘상태창 오픈!’
310|
311|바로 그 순간.
312|
313|“뭐 하세요? 어깨 아파요.”
314|
315|“어, 그래.”
316|
317|아무 일도 없네. 뭐 하나쯤 뜰 줄 알았는데.
318|
319|하긴 본캐도 만렙 찍으려면 아직 한참 남았는데 부캐가 웬 말이냐. 그래도 아쉽긴 하다.
320|
321|‘소리 내서 해 볼까?’
322|
323|분명히 이상한 놈 취급받겠지만 화장실 다녀와서 손 안 닦는 기분으로 가는 것보단 낫겠지.
324|
325|나는 슬그머니 혁무진의 등에 손을 살짝, 아주 살짝 가져다 대며 작게 중얼거렸다.
326|
327|“상태창 오픈.”
328|
329|“아, 진짜. 아까부터 진짜 왜 이러세요?”
330|
331|녀석의 말을 무시하고 자리에서 벌떡 일어났다.
332|
333|기다리던 알림 소리와 함께 시스템창이 떴기 때문이었다.
334|
335|“이야아, 떴다!”
336|
337|띠링.
338|
339|
340|
341|- 퀘스트 조건에 [제한 시간]이 추가되었습니다.
342|
343|- [22:00:00] 안에 항산검문에 도착하십시오. 늦는다면 돌이킬 수 없게 됩니다.
344|
345|
346|
347|“이야아…….”
348|
349|사그라지는 목소리. 흔들리는 눈동자.
350|
351|‘제한 시간이라니. 뭔 놈의 제한 시간.’
352|
353|나한테 왜 이러냐, 진짜.
354|
355|한숨을 푹 내쉬는 내게 눈을 동그랗게 뜬 월화가 물었다.
356|
357|“진 공자, 어디 아파요?”
358|
359|“아뇨. 그건 아니고요. 혹시 우리 언제쯤 도착하는지 알 수 있어요?”
360|
361|“음. 오늘 같은 속도라면 내일 저녁 전에?”
362|
363|“아.”
364|
365|지금 정오를 약간 넘긴 시간이니까 꼬박 하루는 넘게 달려야 한단 말이다.
366|
367|퀘스트창이 변경된 걸 보니 그 제한 시간 안에 적풍단 놈들이 항산검문을 친다는 얘기 같은데…… 이걸 어쩐다?
368|
369|“이제 슬슬 출발할까요?”
370|
371|“말들이 지쳤어요. 반 시진은 쉬어야 해요.”
372|
373|“말들아, 괜찮지? 방금 들으셨어요? 괜찮다고 대답한 거.”
374|
375|“…….”
376|
377|그래, 그런 눈으로 볼 줄 알았다.
```

## Assembled English

```markdown
[P1]
# Chapter 110

[P2]
*Boom!*

[P3]
The thunderous crash heralded the arrival of a powerfully built middle-aged man.

[P4]
Beneath his thick, bristling brows, he swept the hall with tiger eyes like an enraged beast.

[P5]
“Which one of you was spouting that nonsense just now?”

[P6]
Everyone gathered here was a senior figure of the Mount Heng Sword Sect.

[P7]
Even if they weren’t on their predecessor’s level, they possessed First Rate martial arts and considerable experience. Yet even they were busy shrinking back and avoiding his gaze.

[P8]
The middle-aged man before them had every right to make them do so.

[P9]
*Damn it. Of all people, it had to be the Tiger of Mount Heng…*

[P10]
The storytellers said that two beasts lived on Mount Heng.

[P11]
The Blood Wolf Sword and the Tiger of Mount Heng. The closest of friends, yet each a wall the other had to overcome.

[P12]
The middle-aged man, Cheol Mubaek, had been a Peak master known as the tiger of Mount Heng for decades.

[P13]
“I asked which one of you it was!”

[P14]
His roar made every hair on the senior figures’ bodies stand on end.

[P15]
They said that whenever Cheol Mubaek lost his temper, even his close friend Lee Cheonbaek would leave the area. These men lagged far behind him in both martial arts and age. What more needed to be said?

[P16]
“We should be united in driving out those mounted-bandit bastards, and even that would not be enough, yet you dare defy Cheonbaek’s dying wishes and harbor rebellious intentions?”

[P17]
Under his gaze, which seemed ready to pour out flames, the senior figures of the Mount Heng Sword Sect flinched as though they had been burned.

[P18]
“G-Great Hero Cheol, you misunderstand.”

[P19]
“How could we ever dare harbor rebellious intentions?”

[P20]
“Then have I grown so old that my ears no longer work?”

[P21]
At that moment, everyone inside the main hall felt thirsty. It wasn’t a simple illusion. It was caused by the terrifying Scorching Yang Qi radiating from Cheol Mubaek.

[P22]
*This is insane.*

[P23]
*What the hell did he eat to amass such monstrous internal energy…?*

[P24]
Just being near him made it hard to breathe, and sweat poured down their bodies. The Tiger of Mount Heng. This was the moment the true nature of the Peak master who had supposedly trained alone somewhere in the vast mountain range since around the age of twenty revealed itself.

[P25]
“Huff… Haaah…”

[P26]
“Great Hero, please calm yourself… Hah.”

[P27]
The senior figures of the Mount Heng Sword Sect panted harshly, while the Peak master glared at them without the slightest sign of forgiveness.

[P28]
Just as the air in the hall threatened to boil like lava—

[P29]
“Uncle Cheol, it’s hot.”

[P30]
A voice as clear and refreshing as a stream, and slender white fingers tugging at Cheol Mubaek’s sleeve. At the same time, the angry furrows in his brow smoothed out as though someone had pulled them flat.

[P31]
“W-Was it very hot?”

[P32]
“Yes. I can’t even breathe.”

[P33]
“Oh dear. I didn’t think of you. How is it now?”

[P34]
“Much better. Thank you, Uncle Cheol.”

[P35]
“Don’t say such things. Protecting you, Seowol, is my duty.”

[P36]
Cheol Mubaek’s mighty Scorching Yang Qi subsided.

[P37]
Only then did held breaths burst out across the hall. Once the people soaked in sweat came to their senses, they realized that Cheol Mubaek was not alone.

[P38]
“Y-Young Lady.”

[P39]
“We greet the Young Lady.”

[P40]
Cheol Mubaek raised his brows at the senior figures hurriedly standing to show their respect. But the “Young Lady” was faster.

[P41]
“I’ll tell you both one last time, Iron Sword Squad Leader, Master of the Gatekeeper Pavilion.”

[P42]
The woman who had been hidden behind Cheol Mubaek’s massive frame stepped into view. She was slim and graceful, and the hem of her blue gown rustled whenever it brushed the floor.

[P43]
“Change how you address me. Not Young Lady—Sect Leader.”

[P44]
Those who met her frost-covered gaze remembered one fact they had momentarily forgotten.

[P45]
*Ah. That’s right.*

[P46]
The Blood Wolf Sword, Lee Cheonbaek.

[P47]
Lee Seowol was the child in whom his blood ran strongest.

[P48]
* * *

[P49]
I knew nothing about horseback riding. After coming to Murim, I had ridden only a few times. In the modern world, horseback riding was practically an aristocratic sport reserved for the rich, so I’d never had the chance to try it.

[P50]
But perhaps because my physical abilities were so good and I was riding a well-trained horse, I had enough leisure to look at the System Window even during a furious gallop.

[P51]
*Open Quest Window.*

[P52]
*Ding.*

[P53]
> **System**
>
> **Quest**
>
> **Yesterday’s Enemy, Today’s Ally**
>
> Now that all the truth has been revealed, the Mount Heng Sword Sect is not an enemy but an ally you must join hands with. Invite them to the Jin Family of Taiyuan during the upcoming New Year’s Day.
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Deliver the invitation (Incomplete)
>
> **Reward:** ???
>
> **Failure:** None

[P54]
Quests were fluid. Depending on the circumstances, sudden Quests could appear or existing Quests could be updated, as this one had been.

[P55]
*The Grade was raised.*

[P56]
The Quest Grade changing from First Rate to Peak meant that the road to the Mount Heng Sword Sect had become anything but easy.

[P57]
For example, the Red Wind Band. Or the Red Wind Band. Probably the Red Wind Band…

[P58]
Never mind. Thinking about it any more would only hurt.

[P59]
*Every day in this place is like walking on thin ice.*

[P60]
I thought I’d finally received an easy Quest for once, only for trouble to erupt again.

[P61]
The reason I wasn’t as anxious as before was partly because of the reliable presence of Jin Mukyung, but also because I myself had grown stronger.

[P62]
*Open Status Window.*

[P63]
*Ding.*

[P64]
> **System**
>
> **Status Window**
>
> **Level:** 55 — Jin Taekyung
>
> **Class:** First Rate Martial Artist
>
> **Fame:** 1,300 (+150)
>
> **Titles:** 4 (Title effects active)
>
> — Returnee (All stats +10)
>
> — Sleeping Dragon of Shanxi (All stats +10, Fame +100)
>
> — Scion of a Prestigious Family (All stats +5, Fame +50)
>
> — Gambler (Combat-related stats +10% in one-on-one combat)
>
> **Strength:** 196 (+25)  
> **Stamina:** 195 (+25)
>
> **Agility:** 192 (+25)  
> **Intelligence:** 35 (+25)
>
> **Charm:** 35 (+25)  
> **Internal Energy:** 15 years
>
> **Toughness:** 155 (+25)
>
> **Remaining Points:** 0

[P65]
*Ahh, barkeep.*

[P66]
*Look how well I’ve grown. All by myself.*

[P67]
Strength, Agility, and Stamina were each nearing 200. Just looking at them made me feel full, and my Toughness, born from getting beaten by Jin Mukyung, was growing nicely too.

[P68]
*The Title bonuses are hefty, too. This should be enough.*

[P69]
Until now, I had raised my stats just to survive. Every time I advanced a Quest, one crisis after another came crashing down like three waves at once. There was no way I could afford to invest points in Charm or Intelligence.

[P70]
*Even if I raised my Intelligence enough to reach an IQ of 180, it’s not like I’d start thrusting a spear scientifically.*

[P71]
The same went for Charm. Jopil and the Head Elder weren’t going to spare me just because I was handsome.

[P72]
Of course, raising them would help me in some way eventually. But with my life hanging by a thread, I hadn’t had the courage to invest in noncombat stats.

[P73]
*I can protect this one life of mine to some extent now.*

[P74]
Once this Quest was over, I planned to devote some attention to my internal energy and noncombat stats.

[P75]
As it was, the items I had obtained after defeating Jopil—including the Blazing Flame Divine Pill—were sitting untouched in my Inventory.

[P76]
*Of course, taking it wrong could send me straight to the grave.*

[P77]
Just then, Wolhwa, who had been riding at the front, spotted a stream and pulled to a stop.

[P78]
“We’ll rest for a little while. The horses are too exhausted.”

[P79]
How much time had passed?

[P80]
We had ridden without stopping since leaving the shrine. Dawn had broken, and now the sun hung high overhead. System messages announcing increases to my Strength and Stamina had even appeared twice, so this really had been a forced march.

[P81]
“Whew. My ass is killing me. If I’d known this would happen, I should’ve been born the son of a coachman instead of a farmer.”

[P82]
While the horses rested, Hyuk Mujin dropped heavily to the ground. Since he was the lowest-level member of the group, his exhaustion was obvious.

[P83]
“Having a hard time?”

[P84]
Hyuk Mujin wiped the sweat from his forehead with his sleeve before answering.

[P85]
“Honestly, yes… But strangely enough, it’s much better than last time.”

[P86]
“Last time?”

[P87]
“You’ve already forgotten? During the scouting mission.”

[P88]
“Ah, I remember.”

[P89]
I had nearly died after running into Jopil during a scouting mission for White Tiger Hall. We had taken horses with us then too.

[P90]
*Though we ended up abandoning them when the heavy snow came.*

[P91]
The memory drew a quiet laugh from me.

[P92]
“What’s wrong?”

[P93]
“I was thinking about you. You mouthed off to me without knowing any better and got the crap beaten out of you.”

[P94]
“……Do you really have to dredge up the past to feel better?”

[P95]
“You’re the one who asked, punk.”

[P96]
“Anyway, I’m saying it seems much better than back then.”

[P97]
“Really?”

[P98]
“Yes. We’ve ridden much farther than we did during the scouting mission, but I’m not even that tired. Maybe I’m getting used to riding?”

[P99]
“Maybe… Ah, wait.”

[P100]
“Hm?”

[P101]
Something suddenly occurred to me, so I heightened my Qi Sense.

[P102]
*Ding.*

[P103]
With the familiar System notification, a Level Window appeared over Hyuk Mujin’s bewildered face.

[P104]
> **System**
>
> **Level:** 38 — Hyuk Mujin

[P105]
“……Huh?”

[P106]
A breathy sound escaped my open mouth. When had Hyuk Mujin’s Level gotten this high?

[P107]
*Strictly speaking, it wasn’t all that high.*

[P108]
But considering that he had been only Level 20 when we first met, calling it astonishing progress wasn’t enough. At this point, it was practically like he had been reborn.

[P109]
*Come to think of it, his Level has been rising steadily ever since we met.*

[P110]
As I searched my memory, the details came back more clearly.

[P111]
It had been the same when we reunited as a scouting unit. Whenever I heightened my Qi Sense from time to time, Hyuk Mujin’s Level had risen by one or two.

[P112]
Now he was Level 38. In terms of time spent in Murim, he had nearly doubled his Level in just over two months.

[P113]
*Then maybe…?*

[P114]
With a doubtful heart, I stared intently at Hyuk Mujin.

[P115]
What if he received stat points like I did? Could I distribute them for him?

[P116]
*It’s possible.*

[P117]
Judging by how much stronger I was than a Hunter or martial artist of a similar Level, there seemed to be some kind of System enhancement effect…

[P118]
*It’s worth trying once.*

[P119]
“Why are you staring at me like that? Is there something on my face?”

[P120]
“No. You’re just ugly.”

[P121]
“……Seriously.”

[P122]
I grabbed Hyuk Mujin by the shoulder and shouted inwardly.

[P123]
*Open Status Window!*

[P124]
At that very moment—

[P125]
“What are you doing? My shoulder hurts.”

[P126]
“Oh. Okay.”

[P127]
Nothing happened. I thought at least something would appear.

[P128]
Then again, my main character was still far from reaching the Level cap. Why would my alt character get anything? Still, it was disappointing.

[P129]
*Should I try saying it out loud?*

[P130]
They would definitely treat me like some kind of weirdo, but it was better than moving on with the feeling of not washing my hands after using the bathroom.

[P131]
I stealthily placed my hand against Hyuk Mujin’s back—lightly, very lightly—and muttered under my breath.

[P132]
“Open Status Window.”

[P133]
“Seriously, what has gotten into you today?”

[P134]
I ignored him and shot to my feet.

[P135]
The notification I had been waiting for chimed, and a System Window appeared.

[P136]
“Yes! There it is!”

[P137]
*Ding.*

[P138]
> **System**
>
> The Quest condition **Time Limit** has been added.
>
> Arrive at the Mount Heng Sword Sect within **22:00:00**. If you are late, there will be no turning back.

[P139]
“Yes…”

[P140]
My voice died away. My eyes trembled.

[P141]
*A time limit? What the hell kind of time limit is this?*

[P142]
*Why are you doing this to me? Seriously.*

[P143]
As I let out a deep sigh, Wolhwa’s eyes widened and she asked,

[P144]
“Young Master Jin, are you hurt?”

[P145]
“No, it’s not that. Do you know around when we’ll arrive?”

[P146]
“Hmm. At today’s pace, before tomorrow evening?”

[P147]
“Ah.”

[P148]
It was a little past noon now. That meant we still had more than a full day’s ride ahead of us.

[P149]
Judging by the Quest Window’s change, it seemed the Red Wind Band bastards would attack the Mount Heng Sword Sect within that time limit…

[P150]
What was I supposed to do?

[P151]
“Shall we get going soon?”

[P152]
“The horses are tired. They need to rest for half a shichen.”

[P153]
“Horses, you’re fine, aren’t you? You heard that, right? They said they’re fine.”

[P154]
“……”

[P155]
Yeah. I knew you’d look at me like that.
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
# Chapter 110

[P2]
*Bang!*

[P3]
The person who appeared with the thunderous explosion was a middle-aged man of imposing stature.

[P4]
Beneath his thick, sharply angled brows, he glared around the room with tiger eyes like an enraged beast.

[P5]
“Who was the one spouting that nonsense just now?”

[P6]
Everyone gathered here was a senior figure of the Mount Heng Sword Sect.

[P7]
Even if they weren’t on their predecessor’s level, they possessed First Rate martial arts and more than enough experience. Yet even they were busy shrinking their necks and avoiding his gaze.

[P8]
The middle-aged man before them had every right to make them do so.

[P9]
*Damn it. Of all people, it had to be the Tiger of Mount Heng…*

[P10]
The storytellers said that two beasts lived on Mount Heng.

[P11]
The Blood Wolf Sword and the Tiger of Mount Heng. They were close friends, but each was also the wall the other had to overcome.

[P12]
The middle-aged man, Cheol Mubaek, had been a Peak master known as the tiger of Mount Heng for decades.

[P13]
“I asked which one of you it was!”

[P14]
At that roar, the senior figures of the Mount Heng Sword Sect felt every hair on their bodies stand on end.

[P15]
They said that whenever Cheol Mubaek lost his temper, even his friend Lee Cheonbaek would leave the area. These men were far inferior to him in both martial arts and age, so there was no need to say more.

[P16]
“We should be united in driving out those mounted bandit bastards, and yet you dare defy Cheonbaek’s final wishes and harbor rebellious intentions?”

[P17]
Under his gaze, which seemed ready to pour out flames, the senior figures of the Mount Heng Sword Sect flinched as though they had been burned.

[P18]
“G-Great Hero Cheol. You misunderstand.”

[P19]
“How could we ever dare harbor rebellious intentions?”

[P20]
“Then have I grown old enough for my ears to fail me?”

[P21]
At that moment, everyone inside the main hall felt thirsty. It wasn’t a simple illusion. It was caused by the terrifying Scorching Yang Qi radiating from Cheol Mubaek.

[P22]
*What the hell?*

[P23]
*What on earth has he been eating to build up such ridiculous internal energy…?*

[P24]
Just being near him made it hard to breathe, and sweat poured down their bodies. The Tiger of Mount Heng. This was the moment the true nature of the Peak master who had supposedly trained alone somewhere in the vast mountain range since around the age of twenty revealed itself.

[P25]
“Haah… Hoo…”

[P26]
“Great Hero, please calm down… Hah.”

[P27]
The senior figures of the Mount Heng Sword Sect panted harshly, while the Peak master glared at them without the slightest sign of forgiveness.

[P28]
The air inside the main hall was about to boil like lava when—

[P29]
“Uncle Cheol, it’s hot.”

[P30]
A clear voice like a flowing stream, and slender white fingers tugging at Cheol Mubaek’s sleeve. At the same time, the wrinkles furrowed across his brow in anger smoothed out as though someone had pulled them flat.

[P31]
“W-Was it very hot?”

[P32]
“Yes. I can barely breathe.”

[P33]
“Goodness, I didn’t think of you. How are you now?”

[P34]
“Much better. Thank you, Uncle Cheol.”

[P35]
“Don’t say such things. Protecting you, Seowol, is my duty.”

[P36]
Cheol Mubaek’s powerful Scorching Yang Qi subsided.

[P37]
Only then did the people throughout the hall finally release the breaths they had been holding. Once they came to their senses, their clothes drenched in sweat, they realized that Cheol Mubaek was not alone.

[P38]
“Y-Young Lady.”

[P39]
“We greet Young Lady.”

[P40]
Cheol Mubaek raised his brows at the senior figures hurriedly standing to show their respect. But the “Young Lady” was faster.

[P41]
“I’ll tell the two of you one last time, Iron Sword Squad Leader and Master of the Gatekeeper Pavilion.”

[P42]
The woman who had been hidden behind Cheol Mubaek’s massive frame stepped forward. She was slim and graceful, and the hem of her blue gown rustled whenever it brushed the floor.

[P43]
“Change how you address me. Not Young Lady. Sect Leader.”

[P44]
Those who met her frost-cold gaze remembered one fact they had momentarily forgotten.

[P45]
*Oh. That’s right.*

[P46]
The Blood Wolf Sword, Lee Cheonbaek.

[P47]
Lee Seowol was the child in whom his blood ran strongest.

[P48]
* * *

[P49]
I knew nothing about horseback riding. After coming to Murim, I had ridden only a few times. In the modern world, horseback riding was practically an aristocratic sport reserved for the rich, so I’d never had the chance to try it.

[P50]
But perhaps because my physical abilities were so good and I was riding a well-trained horse, I had enough leisure to look at the System Window even during a furious gallop.

[P51]
*Open Quest Window.*

[P52]
*Ding.*

[P53]
> **System**
>
> **Quest**
>
> **Yesterday’s Enemy, Today’s Ally**
>
> Now that all the truth has been revealed, the Mount Heng Sword Sect is not an enemy but an ally you must join hands with. Invite them to the Jin Family of Taiyuan during the upcoming Lunar New Year.
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Deliver the invitation (Incomplete)
>
> **Reward:** ???
>
> **Failure:** None

[P54]
Quests were fluid. Sometimes sudden Quests appeared depending on the situation, and sometimes, like now, an existing Quest was updated.

[P55]
*The Grade was raised.*

[P56]
The Quest Grade changing from First Rate to Peak meant that the road to the Mount Heng Sword Sect had become anything but easy.

[P57]
For example, the Red Wind Band. Or the Red Wind Band. Probably the Red Wind Band…

[P58]
Never mind. Thinking about it any more would only hurt.

[P59]
*Every day in this place is a walk across thin ice.*

[P60]
I thought I’d finally received an easy Quest for once, but trouble had struck again.

[P61]
The reason I wasn’t as anxious as before was partly because of the reliable presence of Jin Mukyung, but also because I myself had grown stronger.

[P62]
*Open Status Window.*

[P63]
*Ding.*

[P64]
> **System**
>
> **Status Window**
>
> **Level:** 55 — Jin Taekyung
>
> **Class:** First Rate martial artist
>
> **Fame:** 1,300 (+150)
>
> **Titles:** 4 (Title effects active)
>
> — Returnee (All stats +10)
>
> — Sleeping Dragon of Shanxi (All stats +10, Fame +100)
>
> — Scion of a Prestigious Family (All stats +5, Fame +50)
>
> — Gambler (Combat-related stats +10% in one-on-one combat)
>
> **Strength:** 196 (+25)  
> **Stamina:** 195 (+25)
>
> **Agility:** 192 (+25)  
> **Intelligence:** 35 (+25)
>
> **Charm:** 35 (+25)  
> **Internal energy:** 15 years
>
> **Toughness:** 155 (+25)
>
> **Remaining Points:** 0

[P65]
*Ahh, barkeep.*

[P66]
*Look how well I’ve grown. All by myself.*

[P67]
Strength, Agility, and Stamina were each nearing 200. Just looking at them made me feel full, and my Toughness, born from getting beaten by Jin Mukyung, was growing nicely too.

[P68]
*The Title bonuses are hefty, too. This should be enough.*

[P69]
Until now, I had raised my stats just to survive. Every time I advanced a Quest, one crisis after another came crashing down like three waves at once. There was no way I could afford to invest points in Charm or Intelligence.

[P70]
*Even if I raised my Intelligence enough to reach an IQ of 180, it’s not like I’d start thrusting a spear scientifically.*

[P71]
Charm was the same. It wasn’t as though Jopil or the Head Elder would spare me just because I was handsome.

[P72]
Of course, raising them would help me in some way eventually. But with my life hanging by a thread, I hadn’t had the courage to invest in noncombat stats.

[P73]
*I can protect this one life of mine to some extent now.*

[P74]
Once this Quest was over, I planned to pay more attention to my internal energy and noncombat stats.

[P75]
As it happened, the items I had obtained after defeating Jopil—including the Blazing Flame Divine Pill—were sitting untouched in my Inventory.

[P76]
*Of course, if I screw up taking it, I could wind up dead.*

[P77]
At that moment, Wolhwa, who had been riding at the front, spotted a stream and stopped.

[P78]
“We’ll rest for a little while. The horses are too exhausted.”

[P79]
How much time had passed?

[P80]
We had ridden without stopping since leaving the shrine; dawn had broken, and now the sun was high overhead. System messages saying my Strength and Stamina had increased had even appeared twice, so it had definitely been a forced march.

[P81]
“Whew. My butt hurts like hell. If I’d known this would happen, I should’ve been born the son of a coachman instead of a farmer.”

[P82]
While the horses rested, Hyuk Mujin dropped heavily to the ground. Since he was the lowest-level member of the group, his exhaustion was obvious.

[P83]
“Is it hard?”

[P84]
Hyuk Mujin wiped the sweat from his forehead with his sleeve before answering.

[P85]
“To be honest, it is… But strangely, it’s much better than last time.”

[P86]
“Last time?”

[P87]
“You’ve already forgotten? During the scouting mission.”

[P88]
“Ah, I remember.”

[P89]
I had nearly died after encountering Jopil while carrying out a scouting mission for White Tiger Hall. We’d taken horses with us then, too.

[P90]
*Though we ended up abandoning them when the heavy snow came.*

[P91]
Remembering the past, I let out a quiet laugh.

[P92]
“What’s wrong?”

[P93]
“I was thinking about you. You mouthed off to me without knowing what you were doing and got the crap beaten out of you.”

[P94]
“……Do you really have to dredge up the past to feel better?”

[P95]
“You’re the one who asked, punk.”

[P96]
“Anyway, I’m saying it seems much better than back then.”

[P97]
“Really?”

[P98]
“Yes. We’ve ridden much farther than during the scouting mission, but I’m not even that tired. Maybe I’m getting used to riding?”

[P99]
“Maybe… Ah, wait.”

[P100]
“Hm?”

[P101]
Something suddenly occurred to me, so I heightened my Qi Sense.

[P102]
*Ding.*

[P103]
Along with a familiar system notification, a Level Window appeared over Hyuk Mujin’s bewildered face.

[P104]
> **System**
>
> **Level:** 38 — Hyuk Mujin

[P105]
“……Huh?”

[P106]
A breathy sound escaped his open mouth. When had Hyuk Mujin’s Level gotten this high?

[P107]
*Strictly speaking, it wasn’t all that high.*

[P108]
But considering that he had been only Level 20 when we first met, calling it astonishing progress wasn’t enough. At this point, it was practically like he had been reborn.

[P109]
*Come to think of it, his Level did seem to keep rising after we first met.*

[P110]
As I searched my memory, the details came back more clearly.

[P111]
It had been the same when we reunited as a scouting unit. Whenever I heightened my Qi Sense from time to time, Hyuk Mujin’s Level had risen by one or two.

[P112]
And now he was Level 38. In terms of time spent in Murim, he had nearly doubled his Level in only about two months.

[P113]
*Then maybe…?*

[P114]
With a doubtful heart, I stared intently at Hyuk Mujin.

[P115]
What if he received stat points like I did? Could I distribute them for him?

[P116]
*It’s possible.*

[P117]
Judging by how much stronger I was than a Hunter or martial artist of a similar Level, there seemed to be some kind of System enhancement effect…

[P118]
*It’s worth trying once.*

[P119]
“Why are you looking at me like that? Do I have something on my face?”

[P120]
“No. You’re just ugly.”

[P121]
“……Seriously.”

[P122]
I grabbed Hyuk Mujin’s shoulder and shouted inwardly.

[P123]
*Open Status Window!*

[P124]
At that very moment—

[P125]
“What are you doing? My shoulder hurts.”

[P126]
“Oh. Okay.”

[P127]
Nothing happened. I thought at least something would appear.

[P128]
Then again, my main character was still far from reaching the Level cap. Why would my alt character get anything? Still, it was disappointing.

[P129]
*Should I say it out loud?*

[P130]
They would definitely treat me like some kind of weirdo, but it was better than moving on with the feeling of not washing my hands after using the bathroom.

[P131]
I stealthily placed my hand against Hyuk Mujin’s back—lightly, very lightly—and muttered under my breath.

[P132]
“Open Status Window.”

[P133]
“Seriously. What is wrong with you today?”

[P134]
Ignoring him, I sprang to my feet.

[P135]
The system window had appeared with the notification chime I’d been waiting for.

[P136]
“Yes! There it is!”

[P137]
*Ding.*

[P138]
> **System**
>
> The Quest condition **Time Limit** has been added.
>
> Arrive at the Mount Heng Sword Sect within **22:00:00**. If you are late, there will be no going back.

[P139]
“Yes…”

[P140]
My voice faded. My eyes began to tremble.

[P141]
*A time limit? What kind of time limit is this?*

[P142]
*Why are you doing this to me?*

[P143]
As I let out a deep sigh, Wolhwa’s eyes widened and she asked,

[P144]
“Young Master Jin, are you hurt?”

[P145]
“No, it’s not that. Do you know around when we’ll arrive?”

[P146]
“Hmm. At today’s pace, before tomorrow evening?”

[P147]
“Ah.”

[P148]
It was a little past noon now. That meant we would have to ride for more than an entire day.

[P149]
Judging by the Quest Window’s change, it seemed the Red Wind Band bastards would attack the Mount Heng Sword Sect within that time limit…

[P150]
What was I supposed to do?

[P151]
“Shall we get going soon?”

[P152]
“The horses are tired. We need to rest for an hour.”

[P153]
“Horses, you’re all right, aren’t you? You heard that, right? They said they’re fine.”

[P154]
“……”

[P155]
Yeah. I knew you’d look at me like that.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 조필     | **Jopil**          |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 살기     | **killing intent**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 대주     | **Squad Leader** / **Commander**             |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 아가씨 | **Young Lady** | Former address used for Lee Seowol before she demands the title Sect Leader. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 귀환자 | **Returnee** | System Title |
| 승부사 | **Gambler** | System Title |
| 수문각 | **Gate Guard Pavilion** | Jin Family gate complex at the main entrance. |
| 주모 | **Lady of the House** | Title used in Wipeng's remark that Jin Wikyung lacks a wife or household mistress. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 110,
  "passed": true,
  "metrics": {
    "source_characters": 5518,
    "translation_characters": 12378,
    "length_ratio": 2.243,
    "source_paragraphs": 173,
    "translation_paragraphs": 155
  },
  "errors": [],
  "warnings": [
    {
      "code": "numbers",
      "message": "Arabic numerals from the source are absent",
      "details": {
        "values": [
          "1",
          "1300"
        ]
      }
    },
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
        "korean": "진태",
        "preferred": "Jintae"
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
        "korean": "수문각",
        "preferred": "Gate Guard Pavilion"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "주모",
        "preferred": "Lady of the House"
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
