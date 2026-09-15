# Fidelity Gate — Chapter 67

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
  1|＃67화
  2|
  3|
  4|
  5|“어이구, 삭신이야.”
  6|
  7|혁무진이 앓는 소리를 냈다. 훤히 드러난 상반신은 온통 검붉은색으로 물들어 있었다.
  8|
  9|그 광경에 꼬장꼬장하게 생긴 노인, 약왕당주가 혀를 찼다.
 10|
 11|“이놈 이거 몸뚱이를 어떻게 굴린 거야?”
 12|
 13|챙겨 온 보따리를 풀자 말뚝 같은 대침(大針)들이 모습을 드러냈다. 혁무진이 잔뜩 겁에 질린 목소리로 물었다.
 14|
 15|“그걸 제 몸에 꽂는다고요?”
 16|
 17|“왜, 겁나?”
 18|
 19|“엄청 아플 것 같은데…… 가급적 조금만 놔 주세요.”
 20|
 21|“그러지 뭐.”
 22|
 23|시원시원하게 대답한 약왕당주가 대침 두 개를 꺼내 들었다.
 24|
 25|“백회혈이랑 회음혈에 한 방씩 놔 주마. 죽으면 더 이상 아플 일 없을 테니.”
 26|
 27|“…….”
 28|
 29|“이제야 치료받을 준비가 됐구먼.”
 30|
 31|말 한마디로 혁무진의 입을 닥치게 만든 약왕당주가 부지런히 손을 놀렸다. 눈 깜짝할 사이에 크고 작은 침 수십여 개가 혁무진의 살갗을 파고들었다.
 32|
 33|푸푸푹.
 34|
 35|“악, 악!”
 36|
 37|“젊은 놈이 엄살은. 목청 들어 보니 오십 년은 팔팔하겠다.”
 38|
 39|약왕당주는 고슴도치가 되어 버린 혁무진을 뒤로하고 나에게로 고개를 돌렸다.
 40|
 41|“까 봐.”
 42|
 43|“뭐, 뭘요?”
 44|
 45|“귀먹었어? 웃통 까 보라고.”
 46|
 47|나이 앞에서는 산서잠룡이고 나발이고 없다. 나는 시퍼렇게 빛나는 대침들을 곁눈질하며 상의를 벗었다.
 48|
 49|스르륵.
 50|
 51|“응?”
 52|
 53|내 몸을 본 약왕당주가 눈을 크게 떴다.
 54|
 55|“이건 또 뭐 하는 놈이야?”
 56|
 57|놀라움이 담긴 목소리다. 어제까지만 하더라도 멍투성이였던 몸이 깨끗해졌으니 그럴 만도 했다.
 58|
 59|‘나도 이 정도일 줄은 몰랐지.’
 60|
 61|하룻밤 자고 일어났더니 멍 대부분이 사라지고 시큰거리던 뼈도 멀쩡해졌다.
 62|
 63|‘수면 모드의 힘인가?’
 64|
 65|이제는 잠만 자도 어지간한 타박상은 금방 회복되는 것 같다. 의원 생활로 잔뼈가 굵은 약왕당주도 이런 내가 신기한 듯 한참을 뜯어보았다.
 66|
 67|“간밤에 영약이라도 먹었나?”
 68|
 69|“아뇨. 그냥 온종일 운기조식 하고 푹 잤는데요.”
 70|
 71|“백년설삼의 효능인가? 아냐, 너무 과한데…….”
 72|
 73|약왕당주는 이놈이 또 약재 창고를 털었나, 하는 의심 가득한 눈빛으로 나를 쏘아보다가 고개를 저었다.
 74|
 75|“삼공자는 퇴원해도 좋다.”
 76|
 77|끙끙거리던 혁무진이 반색했다.
 78|
 79|“저는! 저는요?”
 80|
 81|“맹세컨대, 또 허락도 없이 뛰쳐나갔다가는 네놈의 회음혈을 대침으로 쑤셔 버릴 것이다.”
 82|
 83|비쩍 마른 노인네가 음산한 어조로 중얼거리며 대침을 들어 허공을 쑤셔 대는데, 그 모습이 호러 무비가 따로 없다.
 84|
 85|유혈이 낭자한 개통식이 되겠군.
 86|
 87|“삼공자는 나가. 침 맞기 싫으면.”
 88|
 89|고맙다…….
 90|
 91|광기로 번들거리는 눈동자를 피해 벌떡 일어난 순간이었다.
 92|
 93|문득 뇌리를 스치는 한 줄기 깨달음.
 94|
 95|‘이제 어디로 가냐.’
 96|
 97|전각이 무너졌으니 돌아갈 곳이 없다. 졸지에 홈리스가 되어 버린 내가 우물쭈물하던 그때였다.
 98|
 99|“커흠, 약왕당주 안에 계시오?”
100|
101|문밖에서 들려오는 익숙한 목소리. 설마 하며 문을 열자 예상했던 얼굴이 보였다.
102|
103|“형?”
104|
105|진위경이 한 박자 늦게 펄쩍 뛰었다.
106|
107|“아니, 어찌 이곳에 네가! 나는 업무 도중 약왕당주에게 긴히 할 말이 있어 온 것인데 이것 참 우연의 일치로구나!”
108|
109|“…….”
110|
111|애쓴다.
112|
113|
114|
115|* * *
116|
117|
118|
119|내 사정을 들은 진위경은 근엄한 얼굴로 앞장섰다.
120|
121|“한동안 거처로 삼을 만한 곳을 알고 있다. 따라오너라.”
122|
123|다분히 주위의 눈을 의식한 행동이었다. 지금껏 쌓아 온 그의 이미지는 공과 사를 철저히 구분하고, 냉철하며 능력 있는 소가주의 모습이었으니까.
124|
125|문제는…….
126|
127|“소가주님이시다.”
128|
129|“옆에는 삼공자님인데? 두 분이 대낮부터 무슨 일이지?”
130|
131|“한시라도 떨어져 있기 싫으신가 보지. 삼공자라면 껌뻑 죽으시잖아.”
132|
133|이미 알 만한 사람들은 다 알고 있다는 거다. 진위경이 엄청난 동생 바보라는 사실을.
134|
135|‘하긴. 모르는 놈이 비정상이지.’
136|
137|30대 중반인 지금도 이러는데 더 젊었을 때는 오죽했을까 싶다. 더군다나 전투가 끝난 직후에는 기쁨을 못 이겨 나를 목말 태우기까지 했다.
138|
139|
140|
141|‘우리 막내! 내 동생!’
142|
143|
144|
145|수백 명 앞에서 그 난리를 쳤으니 모르려야 모를 수가 없다.
146|
147|내심 한숨을 뱉는 내 귓가로 한 줄기 전음이 파고들었다.
148|
149|- 어떠냐? 형도 한 연기력 하지?
150|
151|발연기 부문이라면 아카데미 주연상도 노려 볼 만하다는 생각에 고개를 끄덕였다.
152|
153|- 몸은 괜찮으냐? 무경이도 악의가 있어서 그런 것은 아니니 네가 이해했으면 좋겠구나.
154|
155|“…….”
156|
157|주먹에는 악의가 흘러넘치던데. 내가 회복력이 빨라서 망정이지, 아니었다면 꼬박 며칠 동안 약왕당 천장만 바라보고 있을 뻔했다.
158|
159|‘웬만하면 마주치지 말아야지.’
160|
161|어린놈이 성질도 더러운데 무공까지 강하니까 답이 없다.
162|
163|등장과 동시에 마음속 경계 대상 1호로 급부상한 진무경이었다.
164|
165|“그래도 자주 보다 보면 정이 들 게다.”
166|
167|자주 보다 보면 멍이 들겠지.
168|
169|내 속마음도 모르는 진위경은 허허 웃으며 걸음을 옮겼다.
170|
171|사람으로 바글바글한 태원진가의 중심부를 지나쳐 계속 걷다 보니 갈수록 인적이 뜸해졌다.
172|
173|‘여긴 또 어디야?’
174|
175|과거의 성세를 말해 주듯 태원진가가 차지하는 면적은 어마어마했다. 멀리에서 봐도 어지간한 축구장 몇 개를 합친 크기였으니 전부 둘러볼 수 없는 것도 당연했다. 아직도 발 닿는 곳마다 낯선 곳 천지다.
176|
177|‘죄다 낡았네.’
178|
179|이제 인적은 완전히 뚝 끊겨 길이 텅 비었다. 드문드문 보이는 전각이며 용도를 알 수 없는 건물들은 낡고 을씨년스러웠다.
180|
181|낮에는 쥐들이 운동회를 열고 밤에는 귀신들이 고스톱 칠 것 같은 분위기.
182|
183|내가 두리번거리니 진위경이 허둥지둥 설명했다.
184|
185|“지금까지의 본가 사정으로는 이 정도 유지하는 것만으로도 벅차서 말이다. 이제 대대적으로 보수를 해야지, 암.”
186|
187|“전 별로 상관없는데.”
188|
189|“정말이냐?”
190|
191|“네.”
192|
193|진심이다.
194|
195|좁아터진 3평짜리 고시원 원룸에서 자그마치 5년을 버틴 나다. 쥐는 잡으면 되고, 귀신은 뭐, 설마 진짜로 나오기야 하겠어?
196|
197|“넓기만 하면, 뭐.”
198|
199|“그럼 어떤 경우건 간에 넓으면 상관없다는 게냐?”
200|
201|전제가 살짝 찜찜했지만 일단 고개를 끄덕이자 진위경의 얼굴이 밝아진다.
202|
203|“잘됐구나. 내심 네가 싫다고 할까 봐 걱정했는데.”
204|
205|“……도대체 어디길래.”
206|
207|“다 왔다. 이 건물이야.”
208|
209|“오.”
210|
211|발걸음이 멈춘 곳은 커다란 3층 전각 앞이었다. 지나오면서 본 다른 건물에 비해 훨씬 깔끔했고, 고풍스러운 멋이 물씬 풍겼다.
212|
213|전각을 에워싼 높은 돌담도 마음에 든다.
214|
215|“좋은데요?”
216|
217|이 정도면 싫다고 할 이유가 전혀 없다.
218|
219|내 반응에 진위경이 흐뭇한 듯 환히 웃었다.
220|
221|“마음에 드느냐?”
222|
223|“네, 생각보다 훨씬 깔끔하고. 일단 엄청 넓어 보이네요.”
224|
225|“그렇지. 연무장을 크게 지었거든.”
226|
227|“연무장!”
228|
229|“날씨가 안 좋을 때를 대비해서 지하에 하나 더 지었다.”
230|
231|“오. 연무장이 두 개!”
232|
233|“나눠서 쓰면 문제없을 게다.”
234|
235|“오오. 나눠서 쓰면 딱 좋은…… 예?”
236|
237|잠깐만. 지금 뭐라고?
238|
239|“저 혼자 쓰는 거 아니었어요?”
240|
241|“아, 그게.”
242|
243|진위경이 어색하게 웃었다.
244|
245|“어차피 넓으니 둘이 써도 괜찮지 않겠느냐? 이참에 사이도 돈독해지고.”
246|
247|“……누군데요?”
248|
249|불안감이 스멀스멀 올라온다.
250|
251|그리고 나쁜 직감은 항상 틀리는 법이 없지.
252|
253|진위경은 대답 대신 전각 안으로 성큼 발을 내디뎠다.
254|
255|“무경아! 형님 왔다!”
256|
257|아, 젠장.
258|
259|
260|
261|* * *
262|
263|
264|
265|“해서, 처소를 다시 지을 때까지만 함께 살았으면 한다.”
266|
267|사정을 들은 진무경이 흔쾌히 고개를 끄덕였다.
268|
269|“그렇게 하시죠.”
270|
271|저놈이 대뜸 수락할 줄이야.
272|
273|예상치 못한 반응에 나는 물론이고 진위경도 깜짝 놀랐다.
274|
275|“헛, 진심이냐?”
276|
277|“예. 대신 내일 사람 한 명만 보내 주십시오.”
278|
279|“물론이다. 안 그래도 너 혼자 연무장에만 틀어박혀 있는 게 마음에 걸렸는데 잘됐구나. 일 잘하고 눈치 빠른 하인으로 구해 주마. 아니, 이참에 숙수도 들일까?”
280|
281|“하인이나 숙수는 필요 없습니다.”
282|
283|“그럼?”
284|
285|진무경이 그윽한 눈빛으로 나를 응시했다.
286|
287|“의원이나 불러 주십시오.”
288|
289|“…….”
290|
291|“…….”
292|
293|그럼 그렇지. 문득 오는 길에 봤던 풍경이 눈앞에 어른거린다.
294|
295|인적 끊긴 거리. 비명 하나 새어 나가지 않을 것 같은 지하 연무장. 범죄를 저지르기에는 최적의 요건이다.
296|
297|‘아주 줘 패려고 작정을 했구나.’
298|
299|오한에 몸을 부르르 떨릴 때, 진위경이 더듬더듬 입을 열었다.
300|
301|“무, 무경아. 아니지? 형이 생각하는 그런 거 아니지?”
302|
303|“생각하시는 그게 맞습니다. 생각 이상이 될 수도 있고요.”
304|
305|“생각 이상이면…….”
306|
307|“의원 말고 장의사를 불러야겠죠.”
308|
309|나는 지체하지 않고 출구를 향해 몸을 날렸다.
310|
311|쉬이이익! 덥썩!
312|
313|이런 니기미.
314|
315|진위경에게 목덜미를 붙잡혀 돌아오는 나를 보며 진무경이 피식 웃었다.
316|
317|“형편없는 경신법이군. 뒷골목 개도 너보다는 빠르겠다.”
318|
319|이번에는 나도 지지 않고 맞받아쳤다.
320|
321|“나보다 빠르면 그게 개냐? 적토마지?”
322|
323|“그렇게 맞고도 정신을 못 차렸군.”
324|
325|“쳐 봐! 쳐 봐!”
326|
327|물론 맞을 생각은 없다. 내게는 든든한 보호자가 있으니까.
328|
329|“그만!”
330|
331|쩌렁쩌렁한 외침이 지하 연무장을 흔들었다. 진위경의 얼굴은 지금까지와는 달리 딱딱하게 굳어 있었다.
332|
333|“둘 다 뭐 하는 짓들이냐?”
334|
335|이런 모습은 처음이다. 착한 사람이 화를 내면 무섭다더니, 딱 지금의 진위경을 보고 하는 말 같다.
336|
337|“형제끼리 우애 좋게 지내지는 못할망정, 내 앞에서 드잡이를 하려고 들어?”
338|
339|매서운 눈초리에 나와 진무경은 입을 다물었다.
340|
341|“반년도, 일 년도 아니고 고작 보름이다. 전각이 다 지어질 때까지만 함께 지내라는 말이다. 그게 그렇게 어려운 부탁이었느냐?”
342|
343|진무경이 움찔했다. 전각을 무너트린 주범이니 찔릴 수밖에 없다.
344|
345|“그건 저 녀석이 버릇없게 굴어서…….”
346|
347|“그렇다고 전각을 무너트리고 아우를 두들겨 패? 그걸 변명이라고 하는 것이냐!”
348|
349|진무경이 고개를 숙였다.
350|
351|“죄송합니다.”
352|
353|이번에는 화살이 내게 향했다.
354|
355|“태경이 너는?”
356|
357|주민등록증이라도 까고 싶었지만 참았다.
358|
359|이 몸은 이제 겨우 스무 살이고 진무경은 세 살 위의 친형이니까.
360|
361|“대답!”
362|
363|“……죄송합니다.”
364|
365|진위경이 준엄한 눈빛으로 우리를 쏘아봤다.
366|
367|“내 심사숙고해서 내린 결정이다. 그렇게 서로가 싫다면 지금 말해라. 너희 뜻을 존중하마.”
368|
369|나와 진무경의 시선이 허공에서 부딪쳤다.
370|
371|동시에 대답이 튀어나왔다.
372|
373|“싫은데요.”
374|
375|“저도 싫습니다.”
376|
377|“…….”
378|
379|무거운 침묵 끝에, 진위경이 가까스로 입을 열었다.
380|
381|“너희가 내 뜻에 따르겠다니 이 형은 기쁘구나.”
382|
383|이 정도면 답정너 아니냐?
```

## Assembled English

```markdown
[P1]
# Chapter 67

[P2]
“Ugh, every bone in my body aches.”

[P3]
Hyuk Mujin groaned. His exposed upper body was stained dark reddish-black all over.

[P4]
At the sight, the crotchety-looking old man—the Medicine King Hall Master—clicked his tongue.

[P5]
“What the hell did you do to your body?”

[P6]
He untied the bundle he had brought with him, revealing acupuncture needles as thick as stakes. Hyuk Mujin asked in a terrified voice, “You’re going to stick those in me?”

[P7]
“What, scared?”

[P8]
“They look like they’ll hurt like hell… Please go easy on me.”

[P9]
“Sure, why not.”

[P10]
The Medicine King Hall Master answered readily and took out two large needles.

[P11]
“I’ll put one in the crown of your head and one in your perineum. If you die, you won’t have to worry about pain anymore.”

[P12]
“……”

[P13]
“Now you’re finally ready to be treated.”

[P14]
After silencing Hyuk Mujin with a single sentence, the Medicine King Hall Master got to work. In the blink of an eye, dozens of large and small needles pierced Hyuk Mujin’s skin.

[P15]
Thuk-thuk-thuk.

[P16]
“Argh! Argh!”

[P17]
“A young punk like you, making such a fuss. From the sound of that voice, you’ll be hale and hearty for another fifty years.”

[P18]
Leaving Hyuk Mujin, who had turned into a porcupine, behind, the Medicine King Hall Master turned to me.

[P19]
“Strip.”

[P20]
“What, what?”

[P21]
“Are you deaf? Take off your shirt.”

[P22]
When it came to age, to hell with being the Sleeping Dragon of Shanxi or anything else. I shot a sidelong glance at the blue-glinting needles and took off my top.

[P23]
Rustle.

[P24]
“Hm?”

[P25]
The Medicine King Hall Master’s eyes widened when he saw my body.

[P26]
“What the hell are you?”

[P27]
His voice was full of astonishment, and understandably so. Until yesterday, my body had been covered in bruises, but now it was clean.

[P28]
*I didn’t expect this much either.*

[P29]
After a single night’s sleep, most of the bruises had disappeared, and even my aching bones felt perfectly fine.

[P30]
*Is this the power of Sleep Mode?*

[P31]
It seemed that simply sleeping now let me recover quickly from most ordinary bruises. Even the Medicine King Hall Master, a physician seasoned by years of experience, found me fascinating and examined me for quite some time.

[P32]
“Did you take an elixir last night?”

[P33]
“No. I just circulated my qi all day and got a good night’s sleep.”

[P34]
“Is it the effect of the hundred-year snow ginseng? No, that’s too much…”

[P35]
The Medicine King Hall Master glared at me suspiciously, as if wondering whether I had raided the medicine storeroom again, then shook his head.

[P36]
“The Third Young Master may be discharged.”

[P37]
Hyuk Mujin, who had been groaning, brightened.

[P38]
“What about me? What about me?”

[P39]
“I swear, if you run off again without permission, I’ll ram one of these needles into your perineum.”

[P40]
The gaunt old man muttered in a sinister voice, jabbing a large needle through the air. He looked like something straight out of a horror movie.

[P41]
*That’ll be one bloody opening ceremony.*

[P42]
“Third Young Master, get out. Unless you want the needles too.”

[P43]
*Thanks…*

[P44]
That was the moment I jumped to my feet to escape those eyes gleaming with madness.

[P45]
A sudden flash of insight crossed my mind.

[P46]
*Where am I supposed to go now?*

[P47]
The pavilion had collapsed, leaving me with nowhere to return to. I had become homeless overnight, and as I stood there hesitating—

[P48]
“Ahem. Medicine King Hall Master, are you inside?”

[P49]
A familiar voice came from beyond the door. Wondering if it could really be him, I opened it and found exactly the face I had expected.

[P50]
“Hyung?”

[P51]
Jin Wikyung jumped a beat too late.

[P52]
“No, what are you doing here? I came because I had something urgent to discuss with the Medicine King Hall Master during my duties. What an incredible coincidence!”

[P53]
“……”

[P54]
*Nice try.*

[P55]
* * *

[P56]
After hearing about my situation, Jin Wikyung led the way with a solemn expression.

[P57]
“I know of a place you can use as a residence for a while. Follow me.”

[P58]
He was clearly conscious of the people watching us. After all, the image he had built over the years was that of a coolheaded, capable Lesser Family Head who kept public and private matters strictly separate.

[P59]
The problem was…

[P60]
“It’s the Lesser Family Head.”

[P61]
“Isn’t that the Third Young Master beside him? What are those two doing together in broad daylight?”

[P62]
“Maybe he can’t bear to be apart from him for even a moment. You know how he dotes on the Third Young Master.”

[P63]
Anyone who paid attention already knew: Jin Wikyung was a complete fool for his little brother.

[P64]
*Of course they did. Anyone who didn’t know would be the abnormal one.*

[P65]
He was still like this in his mid-thirties. I could only imagine how bad he had been when he was younger. Right after the battle, he had even been so overcome with joy that he carried me around on his shoulders.

[P66]
*My youngest! My little brother!*

[P67]
After making such a spectacle in front of hundreds of people, there was no way anyone could have missed it.

[P68]
As I sighed inwardly, a thread of Sound Transmission slipped into my ear.

[P69]
—How was that? Hyung can act too, huh?

[P70]
I nodded. If there were an Academy Award for terrible acting, he might have had a shot at Best Actor.

[P71]
—Are you all right? Mukyung didn’t do it out of malice, so I hope you’ll understand.

[P72]
“……”

[P73]
His fists had been overflowing with malice. It was only thanks to my rapid recovery that I hadn’t spent several days staring at the Medicine King Hall ceiling.

[P74]
*I should avoid running into him whenever possible.*

[P75]
That kid had a nasty temper, and the martial arts to back it up. There was no dealing with him.

[P76]
The moment Jin Mukyung appeared, he had shot straight to the top of my internal watch list.

[P77]
“Still, see him often enough and you’ll grow fond of him.”

[P78]
*See him often enough and I’ll grow black-and-blue.*

[P79]
Oblivious to my thoughts, Jin Wikyung laughed heartily and continued walking.

[P80]
We passed through the bustling heart of the Jin Family of Taiyuan and kept going. The farther we went, the fewer people we saw.

[P81]
*Where are we now?*

[P82]
The sheer size of the Jin Family of Taiyuan’s estate spoke to its former glory. Even from a distance, it looked as large as several soccer fields combined, so it was only natural that I couldn’t see everything. There were still unfamiliar places everywhere my feet took me.

[P83]
*Everything’s run-down.*

[P84]
By now, the people had disappeared completely, leaving the road deserted. The occasional pavilion and other buildings whose purposes I couldn’t identify were old and gloomy.

[P85]
It had the kind of atmosphere where rats held sports festivals during the day and ghosts played go-stop at night.[^1]

[P86]
When I looked around, Jin Wikyung hurriedly began to explain.

[P87]
“Given how things have been for our family, even maintaining this much has been more than we could manage. We’ll need to carry out extensive renovations now, of course.”

[P88]
“I don’t really mind.”

[P89]
“Really?”

[P90]
“Yes.”

[P91]
I meant it.

[P92]
I had lasted five whole years in a cramped, three-pyeong goshiwon studio.[^2] Rats could be caught, and as for ghosts… Well, it wasn’t as if real ghosts would actually show up.

[P93]
“As long as it’s spacious, I don’t mind.”

[P94]
“So, no matter what the circumstances are, you don’t care as long as it’s spacious?”

[P95]
The premise sounded slightly ominous, but I nodded anyway. Jin Wikyung’s face brightened.

[P96]
“That’s a relief. I was worried you might dislike it.”

[P97]
“Where exactly is this place?”

[P98]
“We’re here. This is the building.”

[P99]
“Oh.”

[P100]
We stopped in front of a large three-story pavilion. Compared to the other buildings we had passed, it was much cleaner and had a distinctly elegant, old-fashioned charm.

[P101]
I also liked the tall stone wall surrounding it.

[P102]
“It’s nice.”

[P103]
There was no reason at all to dislike a place like this.

[P104]
Jin Wikyung smiled brightly, looking pleased by my reaction.

[P105]
“Do you like it?”

[P106]
“Yes. It’s much cleaner than I expected. And it looks incredibly spacious.”

[P107]
“That’s right. I had the training ground built large.”

[P108]
“A training hall!”

[P109]
“I had another one built underground in case the weather was bad.”

[P110]
“Oh. Two training halls!”

[P111]
“If we divide them up, there shouldn’t be any problem.”

[P112]
“Whoa. If we divide them up, that’d be perfect… Huh?”

[P113]
Wait. What had he just said?

[P114]
“I’m not supposed to use it alone?”

[P115]
“Oh, well…”

[P116]
Jin Wikyung gave an awkward smile.

[P117]
“It’s spacious enough for two people to use it together, isn’t it? You might grow closer while you’re at it.”

[P118]
“Who is it?”

[P119]
Unease began to creep up my spine.

[P120]
And bad premonitions were never wrong.

[P121]
Instead of answering, Jin Wikyung strode into the pavilion.

[P122]
“Mukyung! Your big brother’s here!”

[P123]
*Oh, damn it.*

[P124]
* * *

[P125]
“So, I’d like you two to live together until his residence is rebuilt.”

[P126]
After hearing the situation, Jin Mukyung readily nodded.

[P127]
“Very well.”

[P128]
I hadn’t expected him to accept so readily.

[P129]
His unexpected response surprised both me and Jin Wikyung.

[P130]
“Wait, are you serious?”

[P131]
“Yes. But please send me one person tomorrow.”

[P132]
“Of course. I was worried about you shutting yourself away in the training ground all alone anyway, so this works out well. I’ll find you a capable servant who’s quick on the uptake. Or should I bring in a cook while I’m at it?”

[P133]
“A servant or a cook is unnecessary.”

[P134]
“Then what?”

[P135]
Jin Mukyung gave me a long, meaningful look.

[P136]
“Please call a physician.”

[P137]
“……”

[P138]
“……”

[P139]
The scenery I had seen on the way here suddenly rose before my eyes.

[P140]
An empty street with no people around. An underground training ground where not even a scream could escape. The perfect conditions for committing a crime.

[P141]
*He’s really made up his mind to beat me senseless.*

[P142]
As I shivered with a chill, Jin Wikyung stammered, “M-Mukyung. No, that’s not it, right? It’s not what I’m thinking, right?”

[P143]
“It’s exactly what you’re thinking. It might be worse.”

[P144]
“If it’s worse…”

[P145]
“Then you’ll need to call an undertaker instead of a physician.”

[P146]
I threw myself toward the exit without delay.

[P147]
Whoosh! Grab!

[P148]
*Goddammit.*

[P149]
Jin Wikyung caught me by the nape and hauled me back. Jin Mukyung let out a short laugh as he watched.

[P150]
“What a pathetic movement technique. Even a back-alley dog would be faster than you.”

[P151]
This time I fired back without backing down.

[P152]
“If something’s faster than me, is it really a dog? It’s Red Hare, isn’t it?”[^3]

[P153]
“Even after taking that beating, you still haven’t come to your senses.”

[P154]
“Hit me! Come on, hit me!”

[P155]
Of course, I had no intention of actually being hit. I had a dependable protector on my side.

[P156]
“Enough!”

[P157]
The booming shout shook the underground training ground. Unlike before, Jin Wikyung’s face had hardened.

[P158]
“What do you two think you’re doing?”

[P159]
I had never seen him like this. They said it was frightening when a kind person got angry, and Jin Wikyung now showed me exactly what that meant.

[P160]
“Instead of getting along as brothers, you’re trying to start a fight in front of me?”

[P161]
Under his fierce glare, Jin Mukyung and I both fell silent.

[P162]
“It isn’t half a year or a year. It’s only fifteen days. I’m asking you to live together just until the pavilion is finished. Was that such a difficult request?”

[P163]
Jin Mukyung flinched. As the one responsible for demolishing the pavilion, he couldn’t help feeling guilty.

[P164]
“That was because that brat was being rude…”

[P165]
“And that gives you the right to demolish a pavilion and beat up your little brother? You call that an excuse?”

[P166]
Jin Mukyung lowered his head.

[P167]
“I’m sorry.”

[P168]
This time, the arrow turned toward me.

[P169]
“Taekyung, what about you?”

[P170]
I wanted to whip out my ID card, but I held myself back.

[P171]
This body was only twenty now, and Jin Mukyung was my blood brother, three years older than me.

[P172]
“Answer!”

[P173]
“……I’m sorry.”

[P174]
Jin Wikyung glared sternly at both of us.

[P175]
“This is a decision I reached after careful consideration. If you dislike each other that much, say so now. I’ll respect your wishes.”

[P176]
Jin Mukyung and I locked eyes in midair.

[P177]
Our answers burst out at the same time.

[P178]
“I don’t want to.”

[P179]
“Nor do I.”

[P180]
“……”

[P181]
After a heavy silence, Jin Wikyung finally managed to speak.

[P182]
“I’m glad you two are willing to follow your big brother’s wishes.”

[P183]
*Why ask when he’d already decided on the answer?*

[P184]
[^1]: Go-stop is a Korean card game commonly played with hwatu cards.

[P185]
[^2]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement; three pyeong is roughly ten square meters.

[P186]
[^3]: Red Hare is the legendary swift horse associated with the historical warlord Lü Bu.
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
# Chapter 67

[P2]
“Ugh, every bone in my body hurts.”

[P3]
Hyuk Mujin groaned. His exposed upper body was stained dark reddish-black all over.

[P4]
At the sight, the cantankerous-looking old man—the Medicine King Hall Master—clicked his tongue.

[P5]
“What the hell did you do to your body?”

[P6]
When he untied the bundle he had brought with him, stake-like acupuncture needles were revealed. Hyuk Mujin asked in a trembling voice:

[P7]
“You’re going to stick those in me?”

[P8]
“What, scared?”

[P9]
“They look like they’ll hurt like hell… Please go easy, if possible.”

[P10]
“Sure, why not.”

[P11]
The Medicine King Hall Master answered cheerfully and took out two large needles.

[P12]
“I’ll put one in the crown of your head and one in your perineum. If you die, you won’t have to worry about pain anymore.”

[P13]
“……”

[P14]
“Now you’re finally ready to be treated.”

[P15]
After silencing Hyuk Mujin with a single sentence, the Medicine King Hall Master got to work. In the blink of an eye, dozens of large and small needles pierced Hyuk Mujin’s skin.

[P16]
Thuk-thuk-thuk.

[P17]
“Argh! Argh!”

[P18]
“A young punk like you, making such a fuss. From the sound of that voice, you’ll be hale for another fifty years.”

[P19]
Leaving Hyuk Mujin, who had turned into a porcupine, behind, the Medicine King Hall Master turned his head toward me.

[P20]
“Take it off.”

[P21]
“What, what?”

[P22]
“Are you deaf? Take off your shirt.”

[P23]
When it came to age, to hell with being the Sleeping Dragon of Shanxi or anything else. I shot a sidelong glance at the blue-glinting needles and took off my top.

[P24]
Rustle.

[P25]
“Hm?”

[P26]
The Medicine King Hall Master’s eyes widened when he saw my body.

[P27]
“What are you made of?”

[P28]
His voice was filled with astonishment. It was understandable. Until yesterday, my body had been covered in bruises, but now it was clean.

[P29]
*I didn’t expect this much, either.*

[P30]
After sleeping through the night, most of the bruises had disappeared, and even the bones that had been aching felt fine.

[P31]
*Is this the power of Sleep Mode?*

[P32]
It seemed that simply sleeping now let me recover quickly from most ordinary bruises. Even the Medicine King Hall Master, who had spent years as a physician, found me fascinating and examined me for quite some time.

[P33]
“Did you take an elixir during the night?”

[P34]
“No. I just circulated my qi all day and slept deeply.”

[P35]
“Is it the effect of the hundred-year snow ginseng? No, that’s too much…”

[P36]
The Medicine King Hall Master glared at me suspiciously, as if wondering whether I had raided the medicine storeroom again, then shook his head.

[P37]
“The Third Young Master may be discharged.”

[P38]
Hyuk Mujin, who had been groaning, brightened.

[P39]
“What about me? What about me?”

[P40]
“I swear, if you run off again without permission, I’ll jab your perineum with a large needle.”

[P41]
The gaunt old man muttered in a sinister voice as he raised a large needle and stabbed it through the air. He looked like something straight out of a horror movie.

[P42]
*That’s going to be one bloody opening ceremony.*

[P43]
“Third Young Master, get out. Unless you want to be needled.”

[P44]
*Thanks…*

[P45]
That was the moment I jumped to my feet to escape those eyes gleaming with madness.

[P46]
A sudden flash of insight crossed my mind.

[P47]
*Where am I supposed to go now?*

[P48]
The pavilion had collapsed, so I had nowhere to return to. I had become homeless overnight, and was hesitating when—

[P49]
“Ahem. Medicine King Hall Master, are you inside?”

[P50]
A familiar voice came from outside the door. I opened it, half expecting the impossible, and saw the face I had anticipated.

[P51]
“Hyung?”

[P52]
Jin Wikyung jumped a beat late.

[P53]
“No, what are you doing here? I came because I had something urgent to discuss with the Medicine King Hall Master during my duties. What an incredible coincidence!”

[P54]
“……”

[P55]
*Nice try.*

[P56]
* * *

[P57]
After hearing my situation, Jin Wikyung led the way with a solemn expression.

[P58]
“I know of a place you can use as a residence for a while. Follow me.”

[P59]
His behavior was clearly influenced by the eyes around us. The image he had built over the years was that of a cold, capable Lesser Family Head who strictly separated public and private affairs.

[P60]
The problem was…

[P61]
“The Lesser Family Head!”

[P62]
“Isn’t that the Third Young Master beside him? What are those two doing together in broad daylight?”

[P63]
“Maybe he can’t stand being apart from him for even an instant. He absolutely dotes on the Third Young Master.”

[P64]
Anyone who paid attention already knew: Jin Wikyung was a complete fool for his little brother.

[P65]
*Of course they did. Anyone who didn’t know would be the abnormal one.*

[P66]
He was still like this in his mid-thirties. I could only imagine what he had been like when he was younger. After the battle ended, he had even been so happy that he carried me around on his shoulders.

[P67]
*My youngest! My little brother!*

[P68]
After making such a spectacle in front of hundreds of people, there was no way anyone could have missed it.

[P69]
As I sighed inwardly, a thread of Sound Transmission slipped into my ear.

[P70]
—How was that? Hyung can act, too, huh?

[P71]
I nodded, thinking that if there were an Academy Award for terrible acting, he might even contend for Best Actor.

[P72]
—Are you all right? Mukyung didn’t do it out of malice, so I hope you’ll understand him.

[P73]
“……”

[P74]
His fists had been overflowing with malice. It was only thanks to my rapid recovery that I had not spent several days staring at the Medicine King Hall ceiling.

[P75]
*I should avoid running into him whenever possible.*

[P76]
That kid had a nasty temper, and the martial arts to back it up. There was no dealing with him.

[P77]
Jin Mukyung had shot straight up to the number-one spot on my internal watch list the moment he appeared.

[P78]
“Still, see him often enough and you’ll grow fond of him.”

[P79]
*See him often enough and I’ll grow black-and-blue.*

[P80]
Jin Wikyung, unaware of my inner thoughts, laughed heartily and continued walking.

[P81]
We passed through the bustling center of the Jin Family of Taiyuan and kept going. The farther we went, the fewer people we saw.

[P82]
*Where are we now?*

[P83]
The area occupied by the Jin Family of Taiyuan was enormous, a reminder of its former glory. Even from a distance, it looked as though several soccer fields had been joined together, so it was only natural that I couldn’t see everything. There were still unfamiliar places everywhere my feet took me.

[P84]
*Everything’s run-down.*

[P85]
Now the people had disappeared completely, leaving the road empty. The occasional pavilion and the buildings whose purposes I couldn’t identify were old and gloomy.

[P86]
It had the kind of atmosphere where rats could hold a sports festival during the day and ghosts could play go-stop at night.[^1]

[P87]
When I looked around, Jin Wikyung hurriedly began to explain.

[P88]
“Given how things have been for our family, even maintaining this much has been more than we could manage. We’ll need to carry out extensive renovations now, of course.”

[P89]
“I don’t really care.”

[P90]
“Really?”

[P91]
“Yes.”

[P92]
I meant it.

[P93]
I had lasted five whole years in a cramped, three-pyeong goshiwon studio.[^2] Rats could be dealt with, and ghosts… Well, it wasn’t as if real ghosts would actually show up.

[P94]
“As long as it’s spacious, I don’t mind.”

[P95]
“So, no matter what the circumstances are, you don’t care as long as it’s spacious?”

[P96]
The premise sounded slightly ominous, but I nodded anyway. Jin Wikyung’s face brightened.

[P97]
“That’s a relief. I was worried you might dislike it.”

[P98]
“Where exactly is this place?”

[P99]
“We’re here. This is the building.”

[P100]
“Oh.”

[P101]
We stopped in front of a large three-story pavilion. Compared to the other buildings we had passed, it was much cleaner and had a distinctly elegant, old-fashioned charm.

[P102]
I also liked the tall stone wall surrounding it.

[P103]
“It’s nice.”

[P104]
There was no reason at all to dislike a place like this.

[P105]
Jin Wikyung smiled brightly, looking pleased by my reaction.

[P106]
“Do you like it?”

[P107]
“Yes. It’s much cleaner than I expected. And it looks incredibly spacious.”

[P108]
“That’s right. I had the training hall built large.”

[P109]
“A training hall!”

[P110]
“I had another one built underground in case the weather was bad.”

[P111]
“Oh. Two training halls!”

[P112]
“If we divide them up, there shouldn’t be any problem.”

[P113]
“Whoa. If we divide them up, that’d be perfect… Huh?”

[P114]
Wait. What had he just said?

[P115]
“I’m not supposed to use it alone?”

[P116]
“Oh, well…”

[P117]
Jin Wikyung gave an awkward smile.

[P118]
“It’s spacious enough for two people to use it together, isn’t it? You might grow closer while you’re at it.”

[P119]
“Who?”

[P120]
Unease began to creep up my spine.

[P121]
And a bad premonition was never wrong.

[P122]
Instead of answering, Jin Wikyung strode into the pavilion.

[P123]
“Mukyung! Your big brother’s here!”

[P124]
*Oh, damn it.*

[P125]
* * *

[P126]
“So, I’d like you to live together until your residence is rebuilt.”

[P127]
After hearing the situation, Jin Mukyung readily nodded.

[P128]
“Let’s do that.”

[P129]
I hadn’t expected him to accept so readily.

[P130]
His unexpected response surprised both me and Jin Wikyung.

[P131]
“Wait, are you serious?”

[P132]
“Yes. But please send one person tomorrow.”

[P133]
“Of course. I was worried about you shutting yourself away in the training hall all alone anyway, so this works out well. I’ll find you a capable servant who’s quick on the uptake. Or should I hire a cook while I’m at it?”

[P134]
“A servant or a cook is unnecessary.”

[P135]
“Then what?”

[P136]
Jin Mukyung gazed at me with deep, intent eyes.

[P137]
“Please call a physician.”

[P138]
“……”

[P139]
“……”

[P140]
The scenery I had seen on the way here suddenly rose before my eyes.

[P141]
An empty street with no people around. An underground training hall where not even a scream could escape. The perfect conditions for committing a crime.

[P142]
*He’s really made up his mind to beat me senseless.*

[P143]
As I shivered, Jin Wikyung stammered out:

[P144]
“M-Mukyung. No, that’s not it, right? It’s not what I’m thinking, right?”

[P145]
“It’s exactly what you’re thinking. It might be worse.”

[P146]
“If it’s worse…”

[P147]
“Then you’ll need to call an undertaker instead of a physician.”

[P148]
I threw myself toward the exit without delay.

[P149]
Whoosh! Grab!

[P150]
*Goddammit.*

[P151]
Jin Wikyung caught me by the nape and dragged me back. Jin Mukyung gave a short laugh as he watched.

[P152]
“What a pathetic movement technique. Even a back-alley dog would be faster than you.”

[P153]
This time, I fired back without holding anything in.

[P154]
“If something’s faster than me, is it really a dog? It’s Red Hare, isn’t it?”[^3]

[P155]
“Even after taking that beating, you still haven’t come to your senses.”

[P156]
“Hit me! Come on, hit me!”

[P157]
Of course, I had no intention of actually being hit. I had a dependable protector on my side.

[P158]
“Enough!”

[P159]
The booming shout shook the underground training hall. Unlike before, Jin Wikyung’s face had hardened.

[P160]
“What do you two think you’re doing?”

[P161]
I had never seen him like this. They said it was frightening when a good person got angry, and looking at Jin Wikyung now, I understood exactly what they meant.

[P162]
“Instead of getting along as brothers, you’re trying to start a fight in front of me?”

[P163]
Under his fierce glare, both Jin Mukyung and I fell silent.

[P164]
“It isn’t half a year or a year. It’s only fifteen days. I’m asking you to live together just until the pavilion is finished. Was that such a difficult request?”

[P165]
Jin Mukyung flinched. As the one who had demolished the pavilion, he had every reason to feel guilty.

[P166]
“That was because that guy was being rude…”

[P167]
“And that gives you the right to demolish a pavilion and beat up your little brother? You call that an excuse?”

[P168]
Jin Mukyung lowered his head.

[P169]
“I’m sorry.”

[P170]
This time, the arrow turned toward me.

[P171]
“Taekyung, what about you?”

[P172]
I wanted to whip out my ID card, but I held myself back.

[P173]
This body was only twenty, and Jin Mukyung was my blood brother, three years older than me.

[P174]
“Answer!”

[P175]
“……I’m sorry.”

[P176]
Jin Wikyung glared at us with a stern expression.

[P177]
“This was a decision I reached after careful consideration. If you dislike each other that much, say so now. I’ll respect your wishes.”

[P178]
Jin Mukyung and I locked eyes in midair.

[P179]
Our answers came out at the same time.

[P180]
“But I don’t want to.”

[P181]
“I don’t want to either.”

[P182]
“……”

[P183]
After a heavy silence, Jin Wikyung finally managed to speak.

[P184]
“I’m glad you two are willing to follow your big brother’s wishes.”

[P185]
*Was that even a question? He’d already decided on the answer.*

[P186]
[^1]: Go-stop is a Korean card game commonly played with hwatu cards.

[P187]
[^2]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement; three pyeong is roughly ten square meters.

[P188]
[^3]: Red Hare is the legendary swift horse associated with the historical warlord Lü Bu.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 신법     | **movement technique**                           |                                                       |
| 영약     | **elixir**                                       |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 사숙     | **Martial Uncle**                            |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 공자      | **Young Master**                                                |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 적토마 | **Red Hare** | Famous horse used in Hyuk Mujin's exaggerated comparison. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 67,
  "passed": true,
  "metrics": {
    "source_characters": 5162,
    "translation_characters": 12260,
    "length_ratio": 2.375,
    "source_paragraphs": 185,
    "translation_paragraphs": 186
  },
  "errors": [],
  "warnings": [
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
        "korean": "사숙",
        "preferred": "Martial Uncle"
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
