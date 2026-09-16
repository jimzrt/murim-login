# Fidelity Gate — Chapter 121

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
  1|＃121화
  2|
  3|
  4|
  5|시체가 산을 이루고 피가 강이 되어 흐를 정도로 치열한 전투였으나 항산검문의 건축물들은 대부분 멀쩡하게 그 형태를 유지하고 있었다. 지금 이 전각처럼.
  6|
  7|나는 의자에 쓰러지듯이 몸을 기댔다.
  8|
  9|“으, 죽겠다.”
 10|
 11|지금 같은 큰 전투를 치른 후에는 늘 피로가 뒤따른다.
 12|
 13|몸의 피로야 레벨 업으로 회복할 수 있다지만 정신적인 피로까지는 어쩌지 못하는 법이니까.
 14|
 15|오늘처럼 죽음의 문턱을 오고 간 뒤라면 훨씬 더하다.
 16|
 17|‘진짜 위험했다.’
 18|
 19|조필, 대장로, 풍양.
 20|
 21|절정 고수라는 놈들과 엮여서 좋은 꼴을 본 적이 없다. 목숨이 다섯 개쯤 있으면 좋겠다는 생각이 들 때가 한두 번이 아니니까.
 22|
 23|“조장님, 고생하셨습니다.”
 24|
 25|“오냐.”
 26|
 27|“어휴, 어깨가 심하게 뭉치셨네요.”
 28|
 29|혁무진이 살살거리며 다가와 어깨를 주물렀다.
 30|
 31|외부에서 철무백을 지키던 월화와 혁무진은 일이 어느 정도 마무리된 생존자 수색 작업 때 합류했다.
 32|
 33|“제가 있었으면 풍양 그놈을 아주 확 그냥, 아시죠?”
 34|
 35|“그럼, 당연히 알지. 확 그냥 죽어 버렸을 거라는 거.”
 36|
 37|“…….”
 38|
 39|“뭐, 인마. 좀 더 세게 주물러 봐.”
 40|
 41|혁무진은 구시렁거리면서도 힘을 줘 내 어깨를 꾹꾹 주물렀다.
 42|
 43|“진무경, 아니 둘째 형은?”
 44|
 45|“이미 따로 모셨습니다. 의원들 말로는 걱정 없을 거라더군요. 다른 부상자들도 빠르게 회복 중이랍니다.”
 46|
 47|“그래? 그럼 다행이고.”
 48|
 49|“돌팔이들 아닐까요? 이공자님도 그렇고, 철무백 대협도 제법 큰 내상을 입으신 거로 아는데.”
 50|
 51|“하오문에서 보낸 사람들이잖아. 실력을 믿어 보자고.”
 52|
 53|사실 내가 믿는 건 의원들이 아니라 아이템의 효능이다.
 54|
 55|어지간한 상처는 며칠 안에 아물게 해 준다는 [뛰어난 금창약]과 내상 치유에 탁월한 효과가 있는 [십년하수오]가 아니었다면 저들 중 몇 명은 벌써 요단강 건넜을 거다.
 56|
 57|‘최소한의 응급 처치는 했으니 나머진 의원들이 알아서 해 주겠지.’
 58|
 59|하오문, 아니 월화는 우리도 모르는 새에 발 빠르게 움직였다. 며칠 전 사당에서 수하를 돌려보내면서 인근에 있는 지부에 소집령을 내렸단다.
 60|
 61|모든 전투가 끝나고 반나절 후에 도착한 하오문의 지원군은 곧장 뒷수습을 시작했다.
 62|
 63|‘모두가 앞만 바라볼 때 뒤를 생각한 거지.’
 64|
 65|하오문의 지원군은 전투가 아닌 구호를 목적으로 꾸려져 있었다.
 66|
 67|의원은 물론이고, 숙수에 일꾼들까지 데려왔을 정도니 그 선견지명과 준비성 하나만큼은 혀를 내두를 지경이다.
 68|
 69|‘역시 보통 사람이 아니야.’
 70|
 71|하오문은 천하 어디에나 있는 정보 단체인 동시에 무림 문파라고 했다.
 72|
 73|그 정도 규모의 문파에서 20대 중후반의 나이에 지부장이라는 자리를 맡은 월화도 결코 평범한 사람은 아닐 거다.
 74|
 75|‘그러고 보니 월화라는 이름도 가명이지.’
 76|
 77|기감으로 파악했던 월화의 실제 이름은 은소월이었다. 굳이 우리에게 이름을 숨기는 이유는 글쎄, 첩보 영화의 코드네임과 비슷한 거 아닐까 싶다.
 78|
 79|확실한 건 저 정도 수완가를 적으로 돌리면 피곤해진다는 사실이다.
 80|
 81|‘너무 가까이는 말고 적당히 선을 지키면서. 그래, 그 정도가 딱 적당해.’
 82|
 83|다행히 그리 어렵지 않은 일이다. 월화는 처음부터 내게 이유 모를 호의와 호기심을 갖고 있었으니까.
 84|
 85|그것이 순수한 감정인지, 베테랑 정보 상인으로서의 호기심인지는 좀 더 지켜봐야 알 것 같다.
 86|
 87|“무진아.”
 88|
 89|“더 세게 주무를까요?”
 90|
 91|“아니, 그거 말고. 월화 소저에 대해 어떻게 생각하냐?”
 92|
 93|“예쁘죠.”
 94|
 95|“그리고?”
 96|
 97|곰곰이 생각하던 혁무진이 대답했다.
 98|
 99|“엄청 예쁘죠.”
100|
101|“……어깨 말고 팔뚝 주물러.”
102|
103|저 자식한테 뭘 물어본 내가 병신이지.
104|
105|혁무진이 상처받은 얼굴로 뭐라 대꾸하려던 그때, 가벼운 발소리가 서서히 가까워져 오더니 문 앞에서 멈췄다.
106|
107|‘월화?’
108|
109|아니다. 문밖에서 느껴지는 기는 월화에 비해 턱없이 작고 약했다. 잠깐의 침묵 끝에 뜻밖의 손님이 입을 열었다.
110|
111|“진 공자, 들어가도 될까요?”
112|
113|맑고 또렷한 목소리. 이소월이었다.
114|
115|
116|
117|* * *
118|
119|
120|
121|혁무진이 전각을 나가자 이소월과 단둘이 남겨졌다. 나는 창밖으로 슬슬 어두워지는 하늘을 바라보며 괜한 헛기침을 내뱉었다.
122|
123|“큼. 커흠.”
124|
125|이 시간에 여자, 그것도 기가 막힌 미인과 단둘이 마주 보고 있으려니까 고역이 따로 없다.
126|
127|심지어 얼마 전까지만 해도 철천지원수처럼 싸우던 항산검문의 문주 아닌가.
128|
129|새 술은 새 부대에 담는다고 하지만 그녀는 태원진가를 무너뜨리려던 이천백의 하나뿐인 딸이며 나와는 추문(醜聞)으로 엮인 사이다.
130|
131|‘이거 도대체 무슨 말을 해야 하나.’
132|
133|삼가 고인의 명복을 빕니다? 아냐, 이건 너무 분위기가 무거워져. 얼마 전에 일가(一家)를 떠나보낸 거로도 모자라 풍양과의 전투에서 수하의 대부분을 잃은 그녀다.
134|
135|나는 고민 끝에 입을 뗐다.
136|
137|“식사는 하셨어요?”
138|
139|“…….”
140|
141|“힘드신 일 겪으신 건 알지만 이럴 때일수록 속이 든든해야…… 죄송합니다.”
142|
143|시바, 그냥 입 다물고 있을걸.
144|
145|마음속 깊이 후회하고 있을 때 이소월이 자리에서 일어나 내게 절을 올렸다.
146|
147|“항산검문의 이소월이 은공께 인사 올립니다.”
148|
149|말릴 새도 없이 벌어진 일. 당황한 나는 황급히 그녀를 일으켜 세웠다.
150|
151|은공이라니. 맞는 말이지만 낯간지럽다.
152|
153|“아이고, 왜 이러세요. 은공은 무슨.”
154|
155|“아닙니다. 사람이라면 응당 은혜를 입고 감사할 줄 알아야 하는 법. 은공께서는 부디 저를 부끄럽게 만들지 말아 주세요.”
156|
157|워낙 결의에 찬 말투라 더 이상 말릴 수도 없다.
158|
159|‘틀린 말도 아니고.’
160|
161|나와 진무경이 아니었다면 항산검문은 오늘부로 문 닫았을 거다. 큰절이 아니라 우리의 동상을 세워도 부족하긴 하지.
162|
163|오늘 날짜를 ‘산서잠룡 오신 날’로 지정해서 매년 항산검문의 공휴일로…… 이건 너무 나갔지만 아무튼.
164|
165|“이제 진정하고 자리에 앉으세요.”
166|
167|“은공의 말씀을 따르겠습니다.”
168|
169|“그 은공 소리는 안 하면 안 될까요?”
170|
171|“예, 은공.”
172|
173|미치겠네. 침착한 얼굴로 대답한 이소월이 자리에 앉고 나서야 비로소 나를 찾아온 이유를 들을 수 있었다.
174|
175|“서신에 대한 답을 들려 드리러 왔어요.”
176|
177|“서신? 아.”
178|
179|초대장에 관한 이야기다. 곧 다가오는 새해 첫날 태원진가에서 밥 한 끼 하자는, 정중한 초대의 탈을 쓴 소집령.
180|
181|태원진가가 산서 무림을 틀어쥔 지금, 초대에 응하지 않는 문파는 앞으로의 행보가 재미없을 거라는 사실은 불 보듯 뻔하다.
182|
183|그건 간신히 궤멸을 면한 항산검문도 예외가 아니다.
184|
185|“그래서 대답은요?”
186|
187|“귀문의 제의에 기쁘게 응하겠습니다.”
188|
189|충분히 예상했던 대답이다.
190|
191|그러나 이소월은 거기서 멈추지 않고 말을 이어 나갔다.
192|
193|“더불어 지난 일에 대한 사죄로 본 문이 갖고 있는 모든 권리를 태원진가에게 양도하겠습니다.”
194|
195|“권리?”
196|
197|“네. 본 문의 차지하고 있는 영역에 대한 일체의 권리 모두를요.”
198|
199|그 말인즉슨, 산서 북부를 통째로 태원진가에 넘기겠다는 뜻인데…….
200|
201|‘이렇게까지?’
202|
203|항산검문이 태원진가에게 머리를 숙였다는 건 이미 기정사실이다. 그 과정에서 진위경이 배상금 명목으로 상당히 많은 걸 요구하겠지만 그렇다고 완전히 통째로 집어삼키지는 못한다.
204|
205|월화도 지난 대화에서 비슷한 얘기를 했었고.
206|
207|‘그런데 알아서 떠먹여 주네.’
208|
209|은공, 은공 하더니 아주 헛말은 아닌 모양이다.
210|
211|그래. 역시 감사라는 건 말로 끝내서는 안 되는 법이지. 음.
212|
213|“감사합니다. 저희 큰형님이 흡족해하시겠네요.”
214|
215|“거기에 더해서.”
216|
217|뭐야, 아직 안 끝났어?
218|
219|이소월이 품에서 꺼내 들어 내게 내민 것은 세 권의 책이었다. 나는 겉표지에 적힌 제목을 천천히 읽어 내려갔다.
220|
221|“혈랑검법, 혈랑보법. 그리고.”
222|
223|“수라멸권(修羅滅拳). 검법과 보법은 아버님께서 직접 창안하신 무공이고, 수라멸권은 철 숙부의 비전절기예요. 하나같이 빼어난 절정 무공이죠.”
224|
225|“절정 무공…….”
226|
227|마른침이 절로 넘어간다.
228|
229|무림에서 뼈저리게 깨달은 것 중 하나가 바로 무공의 중요성이다. 시스템을 이용해서 그 부족함을 간신히 메꾸고 있는 나도 이럴진대, 다른 평범한 무림인들에게는 더 말할 것도 없다.
230|
231|무인들에게 있어 훌륭한 절정 무공은 값어치를 매길 수 없는 무가지보(無價之寶)인 것이다.
232|
233|‘산서 북부에 대한 권리, 그 이상.’
234|
235|항산검문이 소유한 권리가 나무의 가지라면 지금 눈앞에 놓인 세 권의 비급은 뿌리다.
236|
237|이소월은 지금 아버지의 유산이자 항산검문이 가진 가장 값진 것들을 저울에 올려놓은 것이다.
238|
239|“이것도 선물입니까?”
240|
241|“아뇨, 이건 거래예요.”
242|
243|역시. 그럴 줄 알았지.
244|
245|거래라. 진위경이라면 무슨 수를 써서라도 그 거래를 받아들일 것이다. 자그마치 세 개의 절정 무공이 걸려 있으니까.
246|
247|‘도대체 뭘 요구하려는 거지?’
248|
249|재물? 안전 보장? 아니면 또 다른 무언가?
250|
251|현재 이소월은, 아니 항산검문은 절박하다 못해 절망적인 상황이다. 아무리 무공들을 헐값에 내놓았다 한들 그 또한 어려운 요구일 것이 분명했다. 나는 슬쩍 발을 뺐다.
252|
253|“무슨 거래일지 궁금하긴 한데…… 아실지는 모르겠지만 저한텐 그 정도 권한이 없어서요.”
254|
255|이소월이 호수처럼 맑은 눈동자로 나를 물끄러미 응시했다.
256|
257|“그런가요?”
258|
259|“네, 딱히 직책도 없고. 나중에 큰형님이랑 따로 상의해 보시는 게 맞는 것 같네요.”
260|
261|“제 생각은 은공과 다른데요.”
262|
263|“예?”
264|
265|“은공께서 충분히 결정하실 수 있는 거래예요. 물론 많은 이야기가 오고 가야겠지만.”
266|
267|“세 개의 절정 무공과 바꿀 만한 거래라…… 그럼 저희 쪽에서는 뭘 줘야 하는 거죠?”
268|
269|“사람이요.”
270|
271|“사람?”
272|
273|순간 이소월의 입가에 미소가 스쳤다.
274|
275|두 번째로 보는 그녀의 웃음이었고, 이번에는 결코 착각이 아니었다.
276|
277|“저와 혼인해 주세요.”
278|
279|
280|
281|* * *
282|
283|
284|
285|“그럼 이만.”
286|
287|전각 앞마당에 서성이던 혁무진은 등 뒤에서 들려오는 여인의 목소리에 돌아섰다. 보는 것만으로도 가슴 한구석이 간질거리는 미녀가 전각의 계단을 내려오는 중이었다.
288|
289|‘허어, 절색이로다.’
290|
291|수십 보(步)는 떨어져 있건만, 한겨울 찬 바람에 꽃향기가 섞여 불어오는 것 같기도 했다.
292|
293|‘하여간 우리 조장은 복도 많아.’
294|
295|잘생긴 얼굴, 자타 공인 산서제일가(山西第一家)인 태원진가의 막내 도련님인 데다가 무공도 뛰어나다.
296|
297|월화와 함께 있을 때는 선남선녀라는 말이 딱 어울렸다.
298|
299|거기에 이제는 항산검문의 문주까지 추가되다니.
300|
301|혁무진은 저 멀리 사라지는 이소월의 뒷모습을 보며 한숨을 푹 내쉬었다.
302|
303|‘잠깐이지만 사랑했소, 이 소저.’
304|
305|다시 전각으로 돌아간 혁무진이 발견한 것은 반쯤 넋이 나가 있는 진태경이었다.
306|
307|“조장, 왜 그러세요?”
308|
309|“…….”
310|
311|“조장. 정신 좀 차려 보세요!”
312|
313|어깨를 붙잡고 흔들자 그제야 풀려 있던 눈동자가 또렷해졌다. 혁무진이 걱정스러운 얼굴로 물었다.
314|
315|“무슨 일 있었습니까? 갑자기 왜 그러세요?”
316|
317|꿀꺽. 마른침을 삼킨 진태경이 간신히 입을 뗐다.
318|
319|“무진아.”
320|
321|“예.”
322|
323|“이소월, 몇 살인지 아냐?”
324|
325|“이소월이 뭡니까, 이소월이. 문주나 소저라고 해야죠.”
326|
327|“고(故) 혁무진이라고 불리기 싫으면 닥치고 대답해.”
328|
329|“……몇 살이었더라? 슬슬 혼인할 나이긴 했던 것 같은데.”
330|
331|곰곰이 생각하던 혁무진이 이마를 탁 쳤다.
332|
333|“아, 생각났어요.”
334|
335|“며, 몇 살인데?”
336|
337|“열일곱이요.”
338|
339|진태경이 입을 딱 벌렸다.
340|
341|“시발, 급식이었어?”
```

## Assembled English

```markdown
[P1]
# Chapter 121

[P2]
It had been a fierce battle—fierce enough to leave mountains of corpses and rivers of blood—yet most of the Mount Heng Sword Sect’s buildings remained largely intact.

[P3]
Like this pavilion, for instance.

[P4]
I collapsed into a chair and leaned back.

[P5]
“Ugh. I’m dying.”

[P6]
Exhaustion always followed a major battle like the one we had just fought.

[P7]
Leveling up could restore my physical fatigue, but it couldn’t do anything about mental fatigue.

[P8]
And after skirting the brink of death like I had today, it was even worse.

[P9]
*That was seriously dangerous.*

[P10]
Jopil. The Head Elder. Pung Yang.

[P11]
Nothing good had ever come from getting tangled up with Peak masters. More than once, I’d found myself wishing I had about five lives.

[P12]
“Squad Leader, thank you for your hard work.”

[P13]
“Yeah, yeah.”

[P14]
“Whew, your shoulders are really tense.”

[P15]
Hyuk Mujin sidled up and began massaging my shoulders.

[P16]
Wolhwa and Hyuk Mujin had been protecting Cheol Mubaek outside before joining the survivor search once things had more or less settled down.

[P17]
“If I’d been there, I would’ve really laid into that bastard Pung Yang. You know what I mean, right?”

[P18]
“Of course. You would’ve gotten yourself killed on the spot.”

[P19]
“……”

[P20]
“What? Come on, massage a little harder.”

[P21]
Hyuk Mujin grumbled, but he put more strength into his hands and kneaded my shoulders.

[P22]
“What about Jin Mukyung? I mean, my second brother?”

[P23]
“We’ve already moved him elsewhere. The physicians said there’s no need to worry. They also said the other wounded are recovering quickly.”

[P24]
“Really? That’s a relief.”

[P25]
“Aren’t they quacks? I heard the Second Young Master and Great Hero Cheol Mubaek both suffered fairly serious Internal Injuries.”

[P26]
“They were sent by the Lower District Sect. Let’s trust their skills.”

[P27]
In truth, it wasn’t the physicians I trusted. It was the efficacy of the Items.

[P28]
If not for the **Superior Wound Medicine**, which could heal most wounds within a few days, and the **Ten-Year He Shouwu**, which was exceptionally effective at treating Internal Injuries, some of them would already have crossed the River Jordan.

[P29]
*I’ve given them the minimum emergency treatment. The physicians can take care of the rest.*

[P30]
The Lower District Sect—or rather, Wolhwa—had moved quickly without any of us realizing it. Several days ago, when she sent one of her subordinates back from the shrine, she had apparently issued a mobilization order to a nearby branch.

[P31]
The Lower District Sect’s support force arrived half a day after the battle ended and immediately began dealing with the aftermath.

[P32]
*While everyone else was looking ahead, she was thinking about what came after.*

[P33]
The Lower District Sect’s support force had been organized for relief work, not combat.

[P34]
They had brought physicians, cooks, and even laborers. Their foresight and preparation were enough to make me marvel.

[P35]
*She really isn’t an ordinary person.*

[P36]
The Lower District Sect was both an information organization found throughout the land and a Murim sect.

[P37]
Wolhwa had become a Branch Leader in a sect of that size while still in her mid-to-late twenties. There was no way she was ordinary.

[P38]
*Come to think of it, Wolhwa isn’t even her real name.*

[P39]
The name I’d discovered through Qi Sense was Eun Sowol. As for why she had gone out of her way to hide it from us, I figured it was something like using a code name in a spy movie.

[P40]
One thing was certain: making an enemy of someone that capable would be exhausting.

[P41]
*Don’t get too close. Keep a reasonable distance and maintain proper boundaries. Yeah, that should be about right.*

[P42]
Fortunately, that wouldn’t be too difficult. Wolhwa had shown me inexplicable goodwill and curiosity from the very beginning.

[P43]
Whether those were genuine feelings or simply the curiosity of a veteran information merchant was something I would have to watch a little longer to determine.

[P44]
“Mujin-ah.”

[P45]
“Should I massage harder?”

[P46]
“No, not that. What do you think of Young Lady Wolhwa?”

[P47]
“She’s pretty.”

[P48]
“And?”

[P49]
Hyuk Mujin thought hard before answering.

[P50]
“She’s extremely pretty.”

[P51]
“……”

[P52]
“Massage my forearms instead of my shoulders.”

[P53]
I was the idiot for asking that guy anything.

[P54]
Hyuk Mujin looked wounded and was about to retort when light footsteps slowly approached and stopped in front of the door.

[P55]
*Wolhwa?*

[P56]
No. The qi I sensed outside the door was far weaker and smaller than Wolhwa’s.

[P57]
After a brief silence, an unexpected guest spoke.

[P58]
“Young Master Jin, may I come in?”

[P59]
The voice was clear and distinct.

[P60]
It was Lee Seowol.

[P61]
* * *

[P62]
Once Hyuk Mujin left the pavilion, Lee Seowol and I were alone.

[P63]
I gazed out the window at the slowly darkening sky and cleared my throat for no reason.

[P64]
“Ahem. Ahem.”

[P65]
Being alone with a woman at this hour—especially a stunning beauty—was a trial in itself.

[P66]
Worse yet, she was the Sect Leader of the Mount Heng Sword Sect, whom we had been fighting like sworn enemies until recently.

[P67]
They said new wine belonged in new wineskins, but she was the only daughter of Lee Cheonbaek, the man who had tried to bring down the Jin Family of Taiyuan, and she and I were already entangled in a scandal.

[P68]
*What the hell am I supposed to say?*

[P69]
*May the deceased rest in peace?*

[P70]
No. That would make the atmosphere far too heavy. As if losing her family recently hadn’t been enough, she had also lost most of her subordinates in the battle against Pung Yang.

[P71]
After agonizing over it, I finally opened my mouth.

[P72]
“Have you eaten?”

[P73]
“……”

[P74]
“I know you’ve been through something difficult, but it’s even more important to keep your strength up at times like this, so……”

[P75]
I stopped myself.

[P76]
“Sorry.”

[P77]
*Damn it. I should’ve just kept my mouth shut.*

[P78]
As I was regretting my words from the bottom of my heart, Lee Seowol rose from her seat and bowed deeply to me.

[P79]
“Lee Seowol of the Mount Heng Sword Sect pays her respects to her benefactor.”

[P80]
It happened before I could stop her. Flustered, I hurriedly helped her to her feet.

[P81]
*Benefactor?*

[P82]
It was accurate, but hearing it made me cringe.

[P83]
“Oh, come on. What are you doing? You don’t have to call me your benefactor.”

[P84]
“No. A person ought to receive kindness and know how to be grateful for it. Please do not make me feel ashamed, Benefactor.”

[P85]
Her tone was so resolute that I couldn’t stop her anymore.

[P86]
*She’s not wrong.*

[P87]
If not for Jin Mukyung and me, the Mount Heng Sword Sect would have shut its doors today. A deep bow wasn’t enough. They could have erected statues of us and it still wouldn’t have been sufficient.

[P88]
Maybe they could designate today as the Day the Sleeping Dragon of Shanxi Came and make it an annual Mount Heng Sword Sect holiday—

[P89]
*That might be taking things too far.*

[P90]
“Now, calm down and sit.”

[P91]
“I will follow my benefactor’s instructions.”

[P92]
“Could you stop calling me that?”

[P93]
“Yes, Benefactor.”

[P94]
*This is driving me crazy.*

[P95]
Only after Lee Seowol answered with a calm expression and sat down was I finally able to hear why she had come to see me.

[P96]
“I came to give you my answer regarding the letter.”

[P97]
“The letter? Oh.”

[P98]
She meant the invitation.

[P99]
The polite invitation to have a meal at the Jin Family of Taiyuan on New Year’s Day, which was fast approaching—a summons disguised as a dinner invitation.

[P100]
Now that the Jin Family of Taiyuan had Shanxi Murim firmly in its grasp, it was obvious that any sect refusing the invitation would face an unpleasant future.

[P101]
The Mount Heng Sword Sect, which had only narrowly escaped annihilation, was no exception.

[P102]
“So what’s your answer?”

[P103]
“We will gladly accept your sect’s proposal.”

[P104]
It was the answer I had expected.

[P105]
But Lee Seowol didn’t stop there. She continued speaking.

[P106]
“Furthermore, as an apology for what happened, I will transfer every right held by our sect to the Jin Family of Taiyuan.”

[P107]
“Rights?”

[P108]
“Yes. All rights to the territory currently occupied by our sect.”

[P109]
In other words, she was saying that she would hand over all of northern Shanxi to the Jin Family of Taiyuan.

[P110]
*She’s going this far?*

[P111]
The fact that the Mount Heng Sword Sect had bowed its head to the Jin Family of Taiyuan was already a given. Jin Wikyung would demand a great deal in compensation, but even he couldn’t completely swallow the sect whole.

[P112]
Wolhwa had said something similar during our previous conversation.

[P113]
*And now she’s serving it up to us without even being asked.*

[P114]
After calling me her benefactor over and over, it seemed she hadn’t just been paying lip service.

[P115]
Right. Gratitude shouldn’t end with words. Hm.

[P116]
“Thank you. My eldest brother will be pleased.”

[P117]
“There’s more.”

[P118]
*What? She isn’t finished yet?*

[P119]
Lee Seowol took three books from inside her robes and held them out to me.

[P120]
I slowly read the titles on their covers.

[P121]
“Blood Wolf Sword Technique, Blood Wolf Footwork. And……”

[P122]
“Shura Annihilating Fist. The sword technique and footwork technique were created by my father himself. The Shura Annihilating Fist is Uncle Cheol’s secret ultimate technique. Every one of them is an outstanding Peak martial art.”

[P123]
“Peak martial arts…”

[P124]
I swallowed hard.

[P125]
One of the things I had learned painfully in the Murim was the importance of martial arts. Even I was barely able to make up for my deficiencies by relying on the System. For ordinary martial artists, it went without saying.

[P126]
To them, an outstanding Peak martial art was a priceless treasure.

[P127]
*These are worth more than the rights to northern Shanxi.*

[P128]
If those rights were the branches of a tree, the three martial arts manuals before me were its roots.

[P129]
Lee Seowol had placed her father’s legacy—the most valuable possessions of the Mount Heng Sword Sect—on the scales.

[P130]
“Is this a gift too?”

[P131]
“No. This is a transaction.”

[P132]
*I knew it.*

[P133]
A transaction.

[P134]
If it was Jin Wikyung, he would accept the deal by any means necessary. Three Peak martial arts were at stake, after all.

[P135]
*What on earth is she going to demand?*

[P136]
Wealth? A guarantee of safety? Or something else?

[P137]
Lee Seowol—or rather, the Mount Heng Sword Sect—was in a situation beyond desperate. Even if they were offering their martial arts at a bargain price, whatever they wanted in return was certain to be a difficult demand.

[P138]
I cautiously distanced myself from the matter.

[P139]
“I’m curious what kind of transaction this is, but I don’t know if you’re aware—I don’t have that kind of authority.”

[P140]
Lee Seowol gazed steadily at me with eyes as clear as a lake.

[P141]
“Is that so?”

[P142]
“Yes. I don’t have a particular position, either. I think it would be best for you to discuss this separately with my eldest brother later.”

[P143]
“My thoughts differ from yours, Benefactor.”

[P144]
“Excuse me?”

[P145]
“This is a transaction you are fully capable of deciding. Of course, there would need to be many discussions.”

[P146]
“A transaction worth trading three Peak martial arts for…… Then what would our side have to give?”

[P147]
“A person.”

[P148]
“A person?”

[P149]
For an instant, a smile flickered across Lee Seowol’s lips.

[P150]
It was the second time I had seen her smile, and this time, I knew I hadn’t imagined it.

[P151]
“Please marry me.”

[P152]
* * *

[P153]
“Well, I’ll be going.”

[P154]
Hyuk Mujin, who had been pacing around the pavilion’s front courtyard, turned at the sound of a woman’s voice behind him.

[P155]
A beauty who made his chest tickle just by looking at her was descending the pavilion steps.

[P156]
*Good heavens. She’s breathtaking.*

[P157]
Though she was dozens of paces away, it almost seemed as if the cold midwinter wind carried the scent of flowers.

[P158]
*Our squad leader sure is lucky.*

[P159]
He had a handsome face, was the youngest Young Master of the Jin Family of Taiyuan—the universally acknowledged foremost family in Shanxi—and possessed excellent martial arts.

[P160]
When he was with Wolhwa, the words *a celestial beauty and a handsome man* fit them perfectly.

[P161]
And now the Sect Leader of the Mount Heng Sword Sect had been added to the list.

[P162]
Hyuk Mujin let out a deep sigh as he watched Lee Seowol’s back disappear into the distance.

[P163]
*I loved you, however briefly, Young Lady Lee.*

[P164]
When Hyuk Mujin returned to the pavilion, he found Jin Taekyung sitting there half out of his mind.

[P165]
“Squad Leader, what’s wrong?”

[P166]
“……”

[P167]
“Squad Leader. Please come to your senses!”

[P168]
Only after Hyuk Mujin grabbed him by the shoulders and shook him did his unfocused eyes finally clear.

[P169]
Hyuk Mujin asked with a worried expression, “Did something happen? Why are you suddenly acting like this?”

[P170]
*Gulp.*

[P171]
Jin Taekyung swallowed hard and barely managed to open his mouth.

[P172]
“Mujin.”

[P173]
“Yes.”

[P174]
“Do you know how old Lee Seowol is?”

[P175]
“What do you mean, ‘Lee Seowol’? You should call her Sect Leader or Young Lady.”

[P176]
“Unless you want people calling you the late Hyuk Mujin, shut up and answer.”

[P177]
“……”

[P178]
Hyuk Mujin thought for a moment.

[P179]
“How old was she again? I think she was about the age when people started getting married.”

[P180]
He suddenly slapped his forehead.

[P181]
“Oh, I remember.”

[P182]
“H-How old is she?”

[P183]
“Seventeen.”

[P184]
Jin Taekyung’s mouth fell open.

[P185]
“Fuck, she was still a high schooler?”
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
# Chapter 121

[P2]
It had been a fierce battle—fierce enough for corpses to pile up into mountains and blood to flow like rivers—yet most of the Mount Heng Sword Sect’s buildings remained standing, largely undamaged.

[P3]
Like this pavilion, for instance.

[P4]
I collapsed into a chair and leaned back.

[P5]
“Ugh. I’m dying.”

[P6]
A major battle like the one we had just fought always left exhaustion in its wake.

[P7]
Leveling up could restore the fatigue in my body, but there was nothing I could do about mental exhaustion.

[P8]
And after skirting the brink of death like I had today, it was even worse.

[P9]
*That was seriously dangerous.*

[P10]
Jopil. The Head Elder. Pung Yang.

[P11]
I had never come out ahead after getting tangled up with Peak masters. More than once, I had wished I had about five lives.

[P12]
“Squad Leader, you worked hard.”

[P13]
“Yeah, yeah.”

[P14]
“Oh, your shoulders are really tense.”

[P15]
Hyuk Mujin approached with an ingratiating smile and began massaging my shoulders.

[P16]
Wolhwa and Hyuk Mujin had been protecting Cheol Mubaek outside before joining the survivor search once things had more or less settled down.

[P17]
“If I’d been there, I would’ve really laid into that bastard Pung Yang. You know what I mean, right?”

[P18]
“Of course I do. You would’ve gotten yourself killed on the spot.”

[P19]
“……”

[P20]
“What? Come on, massage a little harder.”

[P21]
Hyuk Mujin grumbled, but he put more strength into his hands and kneaded my shoulders.

[P22]
“What about Jin Mukyung? I mean, my second brother?”

[P23]
“We’ve already moved him elsewhere. The physicians said there’s no need to worry. They also said the other wounded are recovering quickly.”

[P24]
“Really? That’s a relief.”

[P25]
“Aren’t they quacks? I heard the Second Young Master and Great Hero Cheol Mubaek both suffered fairly serious Internal Injuries.”

[P26]
“They were sent by the Lower District Sect. Let’s trust their skills.”

[P27]
In truth, it wasn’t the physicians I trusted. It was the efficacy of the Items.

[P28]
If not for the **Superior Wound Medicine**, which could heal most wounds within a few days, and the **Ten-Year He Shouwu**, which was exceptionally effective at treating Internal Injuries, some of them would already have crossed the River Jordan.

[P29]
*I’ve given them the minimum emergency treatment. The physicians can take care of the rest.*

[P30]
The Lower District Sect—or rather, Wolhwa—had moved quickly without any of us realizing it. Several days ago, when she sent one of her subordinates back from the shrine, she had apparently issued a mobilization order to a nearby branch.

[P31]
The Lower District Sect’s support force arrived half a day after the battle ended and immediately began dealing with the aftermath.

[P32]
*While everyone else was looking ahead, she was thinking about what came after.*

[P33]
The Lower District Sect’s support force had been organized for rescue work, not combat.

[P34]
They had brought not only physicians, but cooks and laborers as well. Their foresight and preparation were enough to make me whistle in admiration.

[P35]
*She really isn’t an ordinary person.*

[P36]
The Lower District Sect was an information organization found throughout the land, but it was also a Murim sect.

[P37]
And Wolhwa, who had taken on the position of Branch Leader in a sect of that size while still in her mid-to-late twenties, was certainly no ordinary person.

[P38]
*Come to think of it, Wolhwa isn’t even her real name.*

[P39]
The name I had sensed through Qi Sense was Eun Sowol. As for why she had gone out of her way to hide her name from us, I supposed it was something like a code name in a spy movie.

[P40]
One thing was certain: making an enemy of someone that capable would be exhausting.

[P41]
*Don’t get too close. Keep a reasonable distance and stay within proper boundaries. Yes, that sounds about right.*

[P42]
Fortunately, that wouldn’t be too difficult. Wolhwa had shown me inexplicable goodwill and curiosity from the very beginning.

[P43]
Whether those were genuine feelings or simply the curiosity of a veteran information merchant was something I would have to watch a little longer to determine.

[P44]
“Mujin-ah.”

[P45]
“Should I massage harder?”

[P46]
“No, not that. What do you think about Young Lady Wolhwa?”

[P47]
“She’s pretty.”

[P48]
“And?”

[P49]
Hyuk Mujin thought hard before answering.

[P50]
“She’s extremely pretty.”

[P51]
“……”

[P52]
“Massage my forearms instead of my shoulders.”

[P53]
I was the idiot for asking that guy anything.

[P54]
Hyuk Mujin looked wounded and was about to say something when light footsteps slowly approached and stopped in front of the door.

[P55]
*Wolhwa?*

[P56]
No. The qi I sensed outside the door was far weaker and smaller than Wolhwa’s.

[P57]
After a brief silence, an unexpected guest spoke.

[P58]
“Young Master Jin, may I come in?”

[P59]
Her voice was clear and distinct.

[P60]
It was Lee Seowol.

[P61]
* * *

[P62]
Once Hyuk Mujin left the pavilion, I was alone with Lee Seowol.

[P63]
I gazed out the window at the sky slowly darkening and gave a pointless cough.

[P64]
“Ahem. Ahem.”

[P65]
Being alone with a woman at this hour—especially a stunning beauty—was a trial in itself.

[P66]
To make matters worse, she was the Sect Leader of the Mount Heng Sword Sect, which I had been fighting like a sworn enemy only a short while ago.

[P67]
They said new wine belonged in new wineskins, but she was the only daughter of Lee Cheonbaek, the man who had tried to bring down the Jin Family of Taiyuan, and she and I were already connected by a scandal.

[P68]
*What the hell am I supposed to say?*

[P69]
*May the deceased rest in peace?*

[P70]
No. That would make the atmosphere far too heavy. It wasn’t enough that she had lost her family recently—she had also lost most of her subordinates in the battle against Pung Yang.

[P71]
After agonizing over it, I finally opened my mouth.

[P72]
“Have you eaten?”

[P73]
“……”

[P74]
“I know you’ve been through something difficult, but it’s even more important to keep your strength up at times like this, so……”

[P75]
I stopped myself.

[P76]
“Sorry.”

[P77]
*Damn it. I should’ve just kept my mouth shut.*

[P78]
As I was regretting my words from the bottom of my heart, Lee Seowol rose from her seat and bowed deeply to me.

[P79]
“Lee Seowol of the Mount Heng Sword Sect pays her respects to her benefactor.”

[P80]
It happened before I had a chance to stop her.

[P81]
Flustered, I hurriedly helped her back to her feet.

[P82]
*Benefactor?*

[P83]
It was accurate, but hearing it made me cringe.

[P84]
“Oh, come on. What are you doing? You don’t have to call me your benefactor.”

[P85]
“No. A person ought to receive kindness and know how to be grateful for it. Please do not make me feel ashamed, Benefactor.”

[P86]
Her tone was so resolute that I couldn’t stop her anymore.

[P87]
*She’s not wrong.*

[P88]
If not for Jin Mukyung and me, the Mount Heng Sword Sect would have shut its doors today. A deep bow wasn’t enough. They could have erected statues of us and it still wouldn’t have been sufficient.

[P89]
Maybe they could designate today as the day the Sleeping Dragon of Shanxi came to visit and make it an annual holiday for the Mount Heng Sword Sect—

[P90]
*That might be taking things too far.*

[P91]
“Now, calm down and sit.”

[P92]
“I will follow my benefactor’s instructions.”

[P93]
“Could you not call me that?”

[P94]
“Yes, Benefactor.”

[P95]
*This is driving me crazy.*

[P96]
Only after Lee Seowol answered with a calm expression and sat down was I finally able to hear why she had come to see me.

[P97]
“I came to give you my answer regarding the letter.”

[P98]
“The letter? Oh.”

[P99]
She was talking about the invitation.

[P100]
The polite invitation to have a meal at the Jin Family of Taiyuan on New Year’s Day, which was fast approaching—a summons disguised as a dinner invitation.

[P101]
Now that the Jin Family of Taiyuan had Shanxi Murim firmly in its grasp, it was obvious that things would not go well for any sect that refused the invitation.

[P102]
The Mount Heng Sword Sect, which had only barely escaped annihilation, was no exception.

[P103]
“So what’s your answer?”

[P104]
“We will gladly accept your sect’s proposal.”

[P105]
It was the answer I had expected.

[P106]
But Lee Seowol didn’t stop there. She continued speaking.

[P107]
“Additionally, as an apology for what happened, I will transfer all the rights held by our sect to the Jin Family of Taiyuan.”

[P108]
“Rights?”

[P109]
“Yes. All rights to the territory currently occupied by our sect.”

[P110]
In other words, she was saying that she would hand over all of northern Shanxi to the Jin Family of Taiyuan.

[P111]
*She’s going this far?*

[P112]
The fact that the Mount Heng Sword Sect had bowed its head to the Jin Family of Taiyuan was already a given. Jin Wikyung would demand a great deal in compensation, but even he couldn’t completely swallow the sect whole.

[P113]
Wolhwa had said something similar during our previous conversation.

[P114]
*And now she’s serving it up to us without even being asked.*

[P115]
After calling me her benefactor over and over, it seemed she hadn’t just been paying lip service.

[P116]
Yes. Gratitude shouldn’t end with words. Hm.

[P117]
“Thank you. My eldest brother will be pleased.”

[P118]
“There’s more.”

[P119]
*What? She isn’t finished yet?*

[P120]
Lee Seowol took three books from inside her robes and held them out to me.

[P121]
I slowly read the titles written on their covers.

[P122]
“Blood Wolf Sword Technique, Blood Wolf Footwork. And……”

[P123]
“Shura Annihilating Fist. The sword technique and footwork technique were created by my father himself. The Shura Annihilating Fist is Uncle Cheol’s secret ultimate technique. Every one of them is an outstanding Peak martial art.”

[P124]
“Peak martial arts……”

[P125]
I swallowed hard.

[P126]
One of the things I had learned painfully in the Murim was the importance of martial arts. Even I was barely able to make up for my deficiencies by relying on the System. For ordinary martial artists, it went without saying.

[P127]
To martial artists, an excellent Peak martial art was a priceless treasure.

[P128]
*These are worth more than the rights to northern Shanxi.*

[P129]
If the rights to northern Shanxi were the branches of a tree, then the three martial arts manuals lying before me were its roots.

[P130]
Lee Seowol had placed her father’s legacy—the most valuable things possessed by the Mount Heng Sword Sect—on the scale.

[P131]
“Is this a gift too?”

[P132]
“No. This is a transaction.”

[P133]
*I knew it.*

[P134]
A transaction.

[P135]
If it was Jin Wikyung, he would accept the deal by any means necessary. Three Peak martial arts were at stake, after all.

[P136]
*What on earth is she going to demand?*

[P137]
Wealth? A guarantee of safety? Or something else entirely?

[P138]
Lee Seowol—or rather, the Mount Heng Sword Sect—was in a situation so desperate that it had nearly become hopeless. Even if they were offering their martial arts at a bargain price, whatever they wanted in return was certain to be a difficult demand.

[P139]
I cautiously backed away.

[P140]
“I am curious what kind of transaction you have in mind, but I don’t know if you’re aware of this—I don’t have that kind of authority.”

[P141]
Lee Seowol gazed steadily at me with eyes as clear as a lake.

[P142]
“Is that so?”

[P143]
“Yes. I don’t have a particular position, either. I think it would be best for you to discuss this separately with my eldest brother later.”

[P144]
“My thoughts differ from yours, Benefactor.”

[P145]
“Excuse me?”

[P146]
“This is a transaction you are fully capable of deciding. Of course, there would need to be many discussions.”

[P147]
“A transaction worth trading three Peak martial arts for…… Then what would our side have to give?”

[P148]
“A person.”

[P149]
“A person?”

[P150]
For an instant, a smile flickered across Lee Seowol’s lips.

[P151]
It was the second time I had seen her smile, and this time, I knew I hadn’t imagined it.

[P152]
“Please marry me.”

[P153]
* * *

[P154]
“Well, I’ll be going.”

[P155]
Hyuk Mujin, who had been pacing around the pavilion’s front courtyard, turned at the sound of the woman’s voice behind him.

[P156]
A beauty who made one’s chest tickle just by looking at her was descending the pavilion steps.

[P157]
*Good heavens. She’s breathtaking.*

[P158]
Though she was dozens of paces away, it almost seemed as if the cold midwinter wind carried the scent of flowers with it.

[P159]
*Our squad leader sure is lucky.*

[P160]
He had a handsome face, was the youngest Young Master of the Jin Family of Taiyuan—the universally acknowledged First Family of Shanxi—and possessed excellent martial arts.

[P161]
When he was with Wolhwa, the words *a celestial beauty and a handsome man* fit them perfectly.

[P162]
And now the Sect Leader of the Mount Heng Sword Sect had been added to the list.

[P163]
Hyuk Mujin let out a deep sigh as he watched Lee Seowol’s back disappear into the distance.

[P164]
*I loved you for a moment, Young Lady Lee.*

[P165]
When Hyuk Mujin returned to the pavilion, he found Jin Taekyung sitting there half out of his mind.

[P166]
“Squad Leader, what’s wrong?”

[P167]
“……”

[P168]
“Squad Leader. Please come to your senses!”

[P169]
Only after Hyuk Mujin grabbed him by the shoulders and shook him did the unfocused eyes finally clear.

[P170]
Hyuk Mujin asked with a worried expression.

[P171]
“Did something happen? Why are you suddenly acting like this?”

[P172]
*Gulp.*

[P173]
Jin Taekyung swallowed hard and barely managed to open his mouth.

[P174]
“Mujin.”

[P175]
“Yes.”

[P176]
“Do you know how old Lee Seowol is?”

[P177]
“What do you mean, ‘Lee Seowol’? You should call her Sect Leader or Young Lady.”

[P178]
“If you don’t want me to start calling you the late Hyuk Mujin, shut up and answer me.”

[P179]
“……”

[P180]
Hyuk Mujin thought for a moment.

[P181]
“How old was she again? I think she was about the age when people started getting married.”

[P182]
He suddenly slapped his forehead.

[P183]
“Oh, I remember.”

[P184]
“H-How old is she?”

[P185]
“Seventeen.”

[P186]
Jin Taekyung’s mouth fell open.

[P187]
“Fuck, she was still a high schooler?”
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 조필     | **Jopil**          |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 검법     | **sword technique**                              |                                                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 지부장    | **Branch Leader**                            |
| 큰형     | **eldest brother**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 아이템              | **Item**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 귀문      | **your sect**                                                   |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 은소월 | **Eun Sowol** |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 하수오 | **He Shou Wu** | Traditional medicinal herb; a thirty-year-old specimen is offered to Jang Taebo. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 121,
  "passed": true,
  "metrics": {
    "source_characters": 5501,
    "translation_characters": 12858,
    "length_ratio": 2.337,
    "source_paragraphs": 166,
    "translation_paragraphs": 185
  },
  "errors": [],
  "warnings": [
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
        "korean": "내상",
        "preferred": "Internal Injury"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "조장",
        "preferred": "Captain"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "갑자",
        "preferred": "jiazi"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "하수오",
        "preferred": "He Shou Wu"
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
