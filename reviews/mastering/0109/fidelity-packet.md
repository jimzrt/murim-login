# Fidelity Gate — Chapter 109

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
  1|＃109화
  2|
  3|
  4|
  5|전서응(全書鷹).
  6|
  7|태원진가에도 두 마리밖에 없다는 연락용 매다.
  8|
  9|훈련시키기 어렵다 보니 중요한 정보를 전달하는 데에만 쓰인다고 들었는데…….
 10|
 11|‘누가 보낸 거지?’
 12|
 13|전서응을 향해 다가가려는 나를 붙잡은 건 월화의 목소리였다.
 14|
 15|“물러서는 게 좋을걸요? 경계심이 심한 녀석이라 진 공자가 잡으려고 들면 도망칠 테니까.”
 16|
 17|“아, 혹시?”
 18|
 19|“본문에서 보낸 전서응이에요. 특정한 추종향(追從香)을 쫓아오도록 훈련되어 있죠.”
 20|
 21|월화가 품에서 자그마한 주머니를 꺼내 흔들자, 전서응이 슬금슬금 다가와 부리를 비빈다.
 22|
 23|그 틈에 어느새 밖으로 나온 하오문도가 전서응의 발목에 묶인 원통을 풀었다.
 24|
 25|“어디야?”
 26|
 27|“하루 전 삭주지부에서 지부장님 앞으로 보낸 전서입니다.”
 28|
 29|“이리 줘.”
 30|
 31|전서를 건네받아 읽는 월화의 표정이 오묘했다.
 32|
 33|굳게 다물어져 있던 입술이 열린 것은 잠시 후였다.
 34|
 35|“적풍단주…… 생각 이상인데.”
 36|
 37|“또 적풍단에 관련된 겁니까?”
 38|
 39|작게 고개를 끄덕인 월화가 내게 전서를 내밀었다.
 40|
 41|읽어 보라는데 굳이 마다할 필요가 있나, 쭈뼛거리던 진무경과 혁무진도 슬쩍 고개를 들이밀었다.
 42|
 43|
 44|
 45|적풍단, 고원을 넘어 남하 중. 숫자는 대략 이백으로 추정.
 46|
 47|
 48|
 49|짤막한 한 줄이 의미하는 바는 명백했다.
 50|
 51|“다시 한번 항산검문을 치려는 거군요.”
 52|
 53|“틀림없어요. 하루 전 소식이니 그만큼, 아니 그 이상으로 거리가 좁혀졌을 거고요.”
 54|
 55|현재 항산검문까지 남은 거리는 하루하고도 반나절.
 56|
 57|마적단인 만큼 뛰어난 기동력으로 목적지를 향해 진군하고 있을 것이다.
 58|
 59|“안타깝게도 저희 지부는 북부에 제대로 된 정보망을 갖추지 못했어요. 그나마 다행인 건…….”
 60|
 61|월화의 시선이 적풍단의 마적들을 향했다. 이미 오래전 전의를 상실한 그들은 움찔하며 고개를 숙였다.
 62|
 63|“여기 소중한 정보원들이 있다는 거죠. 쓸 만한 정보를 갖고 있을지는 모르겠지만.”
 64|
 65|마적들을 훑어보던 그녀가 돌연 한 사람을 지목했다.
 66|
 67|“너, 일어나.”
 68|
 69|“……저, 저 말입니까?”
 70|
 71|잔뜩 겁먹은 얼굴로 일어난 그는 생각 이상으로 젊은 청년이었다. 마적 중 가장 어리고 약한 그 녀석은 월화의 시선을 정면으로 쳐다보지도 못했다.
 72|
 73|“나이가?”
 74|
 75|“오, 올해 약관을 넘겼습니다.”
 76|
 77|“약관? 어리네. 하긴, 어리다고 마적이 될 수 없는 건 아니니까.”
 78|
 79|“전 마적이 아닙니다! 얼마 전에 낭인이 되었는데 한몫 단단히 챙겨 준다는 말에 그만…….”
 80|
 81|“아, 지난번 습격 때 적풍단주가 끌어모은 낭인 중 하나구나?”
 82|
 83|“예, 예! 제가 아는 사실은 모두 말씀드리겠습니다!”
 84|
 85|“아냐, 괜찮아.”
 86|
 87|“예?”
 88|
 89|“별로 아는 것도 없어 보이는데 뭘. 안 그러니, 춘삼아?”
 90|
 91|지금까지 묵묵히 마부를 자처하던 하오문도.
 92|
 93|그가 대답 대신 품에서 꺼낸 소도(小刀)를 청년의 가슴에 박아 넣었다.
 94|
 95|푹-
 96|
 97|일류 무인의 빠르고 정확한 일격이 심장을 갈랐다. 비명도 지르지 못한 채 입을 벙긋거리던 청년이 실 끊어진 인형처럼 쓰러졌다.
 98|
 99|쿵.
100|
101|싸늘한 적막이 장내를 짓눌렀다. 경악과 공포로 물든 마적들의 시선 속에서, 월화의 가느다란 손가락이 다시 한번 움직였다.
102|
103|“너.”
104|
105|“마, 말하겠소! 전부 다 말하겠소! 나는 적풍단에 일 년째 몸담고 있는…….”
106|
107|“춘삼아.”
108|
109|쐐애애액! 서걱!
110|
111|“크륵, 그르륵.”
112|
113|마적이 피가래 끓는 소리와 함께 뒷걸음질 쳤다. 쩍 벌어진 목을 막아 보지만 손가락 사이로 뿜어져 나오는 피분수를 막을 수는 없다.
114|
115|“단 두 가지만 명심하면 돼.”
116|
117|머리부터 발끝까지.
118|
119|선홍빛 핏물을 뒤집어쓴 월화가 건조한 어조로 말을 이었다.
120|
121|“대답은 묻는 말에만, 있는 사실 그대로.”
122|
123|“……!”
124|
125|우리는 불과 촌각(寸刻) 만에 적풍단에 관한 모든 정보를 얻을 수 있었다.
126|
127|
128|
129|* * *
130|
131|
132|
133|한시가 급하다는 걸 알게 된 우리는 마차를 버리고 말을 한 마리씩 골라잡았다. 나, 진무경, 혁무진, 그리고 월화.
134|
135|하오문도는 오색귀와 생존한 마적들을 데리고 가까운 하오문 지부에서 상황을 전달할 것이다.
136|
137|“너무 잔인했나요?”
138|
139|월화가 말안장을 올리며 건넨 물음에 나는 턱을 긁적였다.
140|
141|“솔직히, 조금 놀라긴 했어요.”
142|
143|항상 여유롭고 장난기 넘치는 모습만 봐서 잠시 잊고 있었다. 그녀도 무림인이라는 사실을.
144|
145|‘그것도 경륜 있는 무림인이지.’
146|
147|월화의 나이가 어떻게 되더라?
148|
149|물어본 적이 없어 잘은 모르지만 서른은 넘지 않을 것이다.
150|
151|그런 젊은 나이에 산서성 전체를 총괄하는 지부장이 되었다는 것은 그에 걸맞은 결단력을 갖췄다는 뜻이다.
152|
153|‘잔인하지만 효과적인 방법이었어.’
154|
155|망설임 없이 두 명을 죽였다. 그것도 파리 잡듯 간단하게.
156|
157|진무경이 우두머리를 상대로 보여 준 모습도 마적들에겐 두려웠겠지만 죽음에 대한 공포는 그 이상이다.
158|
159|벼랑 끝으로 내몰린 그들은 필사적으로 정보를 쏟아 내는 수밖에 없었다.
160|
161|“저라도 술술 불었을 것 같은데요.”
162|
163|“진 공자가 오해할까 봐 말해 두는데, 살생에는 취미 없어요. 상대가 선량한 양민들도 아니었고…… 아, 이놈의 피는 닦아도 끝이 없네.”
164|
165|주르륵 흘러내리는 피는 두 번째로 죽은 마적의 것이다.
166|
167|콧잔등을 찡그리는 그녀를 향해 천 조각을 내미는 한 사람이 있었다.
168|
169|“이, 이걸로 닦으시오.”
170|
171|“어머.”
172|
173|“엥?”
174|
175|“흐음.”
176|
177|월화와 나, 그리고 혁무진의 반응에 진무경이 헛기침을 연발했다.
178|
179|“그, 필요할 것 같아서.”
180|
181|“고마워요, 진 소협. 마침 딱 필요했는데.”
182|
183|“별것 아니오.”
184|
185|말과는 달리 표정은 상당히 뿌듯해 보이는데?
186|
187|저놈 저거 설마…….
188|
189|‘여자한테만 잘해 주는 타입이구나.’
190|
191|어딜 가나 저런 놈이 꼭 하나씩 있지. 천하의 진천검도 별다른 것 없던 모양이다. 그때 피를 닦아 낸 월화가 품에서 돌돌 만 가죽을 꺼내어 펼쳤다.
192|
193|“산서성 전역을 대략으로 표기한 지도에요. 우리 위치는 지금 여기. 적풍단은 아마…… 쉬지 않고 이동했다면 이미 대동(大同)을 돌파했을지도 모르겠네요.”
194|
195|“저희보다 빠르군요.”
196|
197|“지금으로선 반나절. 하지만 우리가 가는 길에는 관도가 잘 정비되어 있으니 밤낮없이 달린다면 충분히 격차를 좁힐 수 있을 거예요.”
198|
199|요컨대 쉴 생각은 하지 말라는 뜻이다. 나는 사람들을 따라 말안장 위로 훌쩍 뛰어올랐다.
200|
201|‘어째 오자마자 일이 터지냐.’
202|
203|내심 한숨이 나왔지만, 별수 있나. 한두 번 고생하는 것도 아니고 이젠 그러려니 해야지.
204|
205|‘이거 되게 간단한 퀘스트였던 것 같은데.’
206|
207|띠링.
208|
209|
210|
211|- 퀘스트 난이도가 [절정]으로 변경되었습니다.
212|
213|
214|
215|“…….”
216|
217|어, 그래. 이젠 아니구나.
218|
219|
220|
221|* * *
222|
223|
224|
225|여우를 닮은 사내였다. 뾰족한 턱과 귀, 날카롭게 찢어진 눈동자는 주위의 모든 것들을 감시하는 동시에 관찰했다.
226|
227|“크아아악!”
228|
229|“죽여라, 싸그리 다 죽여!”
230|
231|“꺄아아아아!”
232|
233|커다란 장원에서 솟구치는 연기, 그리고 비명.
234|
235|말에 올라 언덕 아래를 응시하던 사내, 적풍단주 풍양(風陽)의 입이 열린 것은 장원이 잠잠해진 후였다.
236|
237|“끝났나?”
238|
239|보고를 위해 막 언덕을 올라온 마적이 대답했다.
240|
241|“사내놈들은 전부 죽였고, 아이와 여자들은 한데 모아 뒀습니다.”
242|
243|“왜?”
244|
245|“예? 그야 당연히 고원의 전통대로…….”
246|
247|마차 바퀴보다 큰 사내는 아이라도 가차 없이 죽이고, 여인은 취하거나 노예로 팔아 버린다. 그것이 유목민들로부터 전해져 내려오는 전통 아닌 전통이었다.
248|
249|마적의 말에 풍양은 조용히 손가락을 까딱였다.
250|
251|“이리 가까이 와 보게.”
252|
253|주춤주춤 다가온 마적이 조심스럽게 물었다.
254|
255|“단주, 제가 혹시 큰 실수라도…….”
256|
257|“원래 어디 소속이었나?”
258|
259|“얼마 전까지 토호단에 부단주로 있었습니다.”
260|
261|“토호단? 아, 기억나. 거기 부단주가 자네였군.”
262|
263|“예, 옛! 단주의 고강한 무공과 훌륭한 인품에 반해 충성스러운 수하가 되기로 맹세했습니다!”
264|
265|풍양은 미묘한 얼굴로 코를 긁적였다.
266|
267|그랬던가? 그가 기억하는 건 서른 명쯤 되는 부하를 데리고 단주랍시고 거들먹거리는 쓰레기를 일 합에 죽인 것뿐이었다.
268|
269|“내 기억과는 좀 다르지만 어쨌든 고맙네.”
270|
271|“아닙니다, 영광입니다!”
272|
273|“그런데 말이야. 토호단은 어땠을지 모르지만, 이곳 적풍단은 좀 달라. 고원의 전통이라든지 하는 자질구레한 것들 말일세.”
274|
275|“아, 미처 몰랐습니다.”
276|
277|“단주인 내 명령이 최우선이야. 알겠나?”
278|
279|“앞으로 명심, 또 명심하겠습니다!”
280|
281|“아마 저 친구들도 몰라서 고원의 전통을 지킨 모양이야. 다들 자네처럼 새로 합류한 이들이거든. 그러니 가서 내 뜻을 전해 줄 수 있겠나?”
282|
283|“존명. 한 놈도 살려 두지 않겠습니다.”
284|
285|마적답지 않게 어설픈 군례까지 갖추는 그를 향해 풍양은 손을 내저었다.
286|
287|“그래, 어서 가 보게.”
288|
289|“옛!”
290|
291|말을 몰아 떠나는 그의 뒷모습을 응시하던 풍양이 돌연 소매를 떨쳤다.
292|
293|쉭, 바람이 갈라지는 소리와 함께 뻗어 나간 빛줄기가 십 장(약 30m) 밖에서 목표를 관통했다.
294|
295|푹! 털썩.
296|
297|말은 계속해서 내달렸다.
298|
299|이미 숨이 끊긴 주인이 등자에 발이 걸려 지금 이 순간에도 너덜너덜해지고 있다는 사실을 모른 채.
300|
301|“가서 전해. 포로는 없다고. 다 죽이고 불태우라고.”
302|
303|“예, 단주님.”
304|
305|풍양의 수하가 떠나고 얼마 지나지 않아 장원 전체가 화염에 휩싸였다. 금세 타들어 가는 현판(懸板)을 확인한 그의 입가에 슬쩍 웃음이 맺혔다.
306|
307|항산검문 대동지부.
308|
309|적풍단이 다시 한번 고원을 넘은 순간이었다.
310|
311|
312|
313|* * *
314|
315|
316|
317|넓은 대전.
318|
319|갑론을박을 벌이던 사람들은 전령의 보고에 숨이 턱 막혔다.
320|
321|“놈들이 대동을 돌파했습니다!”
322|
323|“버, 벌써?”
324|
325|“대동지부는? 경계를 위해 나가 있던 인원들은 어찌 되었나?”
326|
327|“전멸, 전멸입니다. 대동지부는 잿더미가 되었고 생존자는 한 명도 없습니다.”
328|
329|“뭣이?”
330|
331|“혹 소식이 잘못 전해진 건 아닌가? 놈들도 지난번에 큰 타격을 입었을 터인데 어찌 이리 빨리……!”
332|
333|“다른 마적단을 흡수한 듯합니다. 최소 이백 명, 혹은 그 이상입니다.”
334|
335|“그 말이 사실인가?”
336|
337|“예, 틀림없습니다.”
338|
339|“그, 그럼 도대체 언제쯤 여기까지……?”
340|
341|“빠르면 하루, 늦어도 이틀 안에 놈들의 공격이 시작될 것으로 예상됩니다.”
342|
343|“끝장이군.”
344|
345|누군가의 중얼거림은 이 자리에 모인 대부분의 마음과 크게 다르지 않았다.
346|
347|열 명 남짓한 그들은 모두 항산검문의 주요 직책을 맡은 중진. 그러나 누구 하나 빠지지 않고 마음속으로는 이미 패배라는 단어를 만지작거리는 중이었다.
348|
349|“철검대주, 이 싸움 자신 있어?”
350|
351|“각주씩이나 되는 양반이 왜 나한테 물어? 여기서 무인이 나밖에 없나.”
352|
353|대항산검문의 대주. 당주, 혹은 각주.
354|
355|한때는 분명 그 위치에 오르길 간절하게 소망한 적이 있었다. 한때는, 말이다.
356|
357|‘대항산검문은 얼어 죽을. 이제 와서 승진시켜 주면 뭐 하나, 문파가 이 꼴인데.’
358|
359|‘가만히 둬도 망할 판국에 마적단까지 와서 난장을 피우는군. 어디 보자, 남아 있는 놈들을 박박 긁어모으면 한 백 명 되려나?’
360|
361|태원진가와의 전쟁으로 팔 할에 가까운 전력을 상실했다.
362|
363|공들여 키운 정예 무인들과 풍진강호를 헤쳐 온 노련한 중진들, 무엇보다 문파가 가진 힘을 상징하는 절정 고수들과 금력(金力)의 상실이 가장 뼈아프다.
364|
365|“제기랄, 문주라도 살아 있었다면.”
366|
367|일개 낭인으로 시작하여 지금의 항산검문을 키워 낸 이천백. 그의 무공과 수완이라면 이 사태를 뒤집을 수 있을 것이다.
368|
369|그러나 혈랑검 이천백은 이미 죽고 없다. 그의 핏줄 중 살아남은 이는 오직 한 사람뿐이다.
370|
371|“이런 상황에 약관도 안 된 어린 계집을 문주라고 모셔야 하다니.”
372|
373|누군가 홧김에 말을 내뱉은 그 순간.
374|
375|쾅!
376|
377|굳게 닫혀 있던 대전의 문이 폭발했다.
```

## Assembled English

```markdown
[P1]
# Chapter 109

[P2]
A messenger eagle.

[P3]
I’d heard that even the Jin Family of Taiyuan had only two of these birds. They were so difficult to train that they were used only to deliver important information…

[P4]
*Who sent it?*

[P5]
Just as I was about to approach the messenger eagle, Wolhwa's voice stopped me.

[P6]
“You’d better keep your distance. It’s extremely wary. If you try to catch it, Young Master Jin, it’ll fly away.”

[P7]
“Ah, could it be?”

[P8]
“It’s a messenger eagle from our sect. It’s trained to follow a specific tracking scent.”

[P9]
Wolhwa pulled a small pouch from her robes and shook it. The messenger eagle cautiously approached and rubbed its beak against the pouch.

[P10]
While it was distracted, a Lower District Sect member who had already slipped outside untied the cylinder bound to its ankle.

[P11]
“Where’s it from?”

[P12]
“It was sent to you from the Sakju Branch yesterday, Branch Leader.”

[P13]
“Give it to me.”

[P14]
Wolhwa accepted the letter and read it, her expression turning inscrutable.

[P15]
After a moment, her tightly pressed lips parted.

[P16]
“The Red Wind Band Leader… He’s more than I expected.”

[P17]
“Is this about the Red Wind Band again?”

[P18]
Wolhwa nodded slightly and handed me the letter.

[P19]
She wanted me to read it, so there was no reason to refuse. Jin Mukyung and Hyuk Mujin, who had been hanging back, cautiously leaned in as well.

[P20]
> The Red Wind Band is heading south across Gaoyuan. Their numbers are estimated at approximately two hundred.

[P21]
The meaning of that single terse line was clear.

[P22]
“They’re planning to attack the Mount Heng Sword Sect again.”

[P23]
“There’s no doubt about it. This news is already a day old, so they must have closed the distance by at least that much, if not more.”

[P24]
We were currently a day and a half away from the Mount Heng Sword Sect.

[P25]
As mounted bandits, they would be advancing on their destination at remarkable speed.

[P26]
“Unfortunately, our branch doesn’t have a proper intelligence network in the north. The one fortunate thing is…”

[P27]
Wolhwa’s gaze shifted toward the Red Wind Band’s mounted bandits. They had lost the will to fight long ago, and they flinched and lowered their heads.

[P28]
“We have some valuable sources of information right here. Whether they know anything useful is another matter.”

[P29]
She looked over the mounted bandits, then abruptly pointed at one of them.

[P30]
“You. Stand up.”

[P31]
“…M-me?”

[P32]
The terrified young man rose. He was younger than I had expected. The youngest and weakest of the mounted bandits, he couldn’t even meet Wolhwa’s eyes.

[P33]
“How old are you?”

[P34]
“I-I turned twenty this year.”

[P35]
“Twenty? You’re young. Then again, being young doesn’t stop someone from becoming a mounted bandit.”

[P36]
“I’m not a mounted bandit! I only became a wandering martial artist recently, but then they said they’d give me a big cut, so I…”

[P37]
“Ah, so you’re one of the wandering martial artists the Red Wind Band Leader gathered for the last attack?”

[P38]
“Y-yes! I’ll tell you everything I know!”

[P39]
“No, it’s all right.”

[P40]
“Pardon?”

[P41]
“You don’t look like you know much anyway. What would be the point? Isn’t that right, Chunsam?”

[P42]
The Lower District Sect member who had silently played the part of our carriage driver until now.

[P43]
Instead of answering, he pulled a small knife from his robes and drove it into the young man’s chest.

[P44]
*Thunk—*

[P45]
The swift, precise One Strike of a First Rate martial artist split his heart. The young man’s mouth opened and closed soundlessly before he collapsed like a puppet with its strings cut.

[P46]
*Thud.*

[P47]
A frigid silence pressed down on the scene. While the mounted bandits stared in horror and fear, Wolhwa’s slender finger moved once more.

[P48]
“You.”

[P49]
“I-I’ll talk! I’ll tell you everything! I’ve been with the Red Wind Band for a year…”

[P50]
“Chunsam.”

[P51]
*Whoosh! Slash!*

[P52]
“Grrk… Gurg…”

[P53]
The mounted bandit staggered backward, making a wet, blood-choked sound. He tried to cover his gaping throat, but couldn’t stop the fountain of blood spraying between his fingers.

[P54]
“You only need to remember two things.”

[P55]
Covered from head to toe in bright-red blood, Wolhwa continued in a dry voice.

[P56]
“Answer only what you’re asked, and tell the truth exactly as it is.”

[P57]
“…!”

[P58]
In mere moments, we learned everything there was to know about the Red Wind Band.

[P59]
* * *

[P60]
Once we realized there wasn’t a moment to lose, we abandoned the carriage and each chose a horse—me, Jin Mukyung, Hyuk Mujin, and Wolhwa.

[P61]
Chunsam would take the Five-Colored Ghosts and the surviving mounted bandits to the nearest Lower District Sect branch and report the situation.

[P62]
“Was that too cruel?”

[P63]
Wolhwa asked as she saddled her horse. I scratched my chin.

[P64]
“To be honest, I was a little surprised.”

[P65]
I’d only ever seen her relaxed and playful, so I had briefly forgotten that she was a martial artist too.

[P66]
*And an experienced one at that.*

[P67]
How old was Wolhwa, anyway?

[P68]
I’d never asked, so I couldn’t be sure, but she couldn’t have been over thirty.

[P69]
Becoming the Branch Leader in charge of all Shanxi Province at such a young age meant she possessed the decisiveness the position demanded.

[P70]
*Cruel, but effective.*

[P71]
She had killed two people without hesitation. Just as casually as swatting flies.

[P72]
Jin Mukyung’s display against the leader must have terrified the mounted bandits, but the fear of death was even greater.

[P73]
Driven to the edge of a cliff, they had no choice but to pour out information desperately.

[P74]
“I think I would’ve spilled everything too.”

[P75]
“I’m saying this in case Young Master Jin gets the wrong idea, but I don’t enjoy killing people. They weren’t innocent commoners, either… Ah, this bastard’s blood just won’t stop, even when I wipe it.”

[P76]
The blood streaming down her belonged to the second mounted bandit she had killed.

[P77]
As she wrinkled her nose, someone held out a piece of cloth.

[P78]
“U-use this to wipe it off.”

[P79]
“Oh my.”

[P80]
“Huh?”

[P81]
“Hmm.”

[P82]
At the reactions from Wolhwa, me, and Hyuk Mujin, Jin Mukyung cleared his throat repeatedly.

[P83]
“I thought you might need it.”

[P84]
“Thank you, Young Hero Jin. This is exactly what I needed.”

[P85]
“It’s nothing.”

[P86]
He said that, but he looked awfully pleased with himself.

[P87]
*No way. Is he…*

[P88]
*The type who’s only nice to women?*

[P89]
There was always at least one guy like that wherever you went. Even the Heaven Shaking Sword wasn’t any different, apparently.

[P90]
After wiping away the blood, Wolhwa pulled a rolled-up piece of leather from her robes and spread it out.

[P91]
This is a rough map covering all of Shanxi Province. We're here. The Red Wind Band has probably… If they've been moving without rest, they may already have broken through Datong.

[P92]
“They’re faster than us.”

[P93]
“By half a day, for now. But the official roads along our route are well maintained. If we ride day and night, we should be able to close the gap.”

[P94]
In short, we shouldn’t expect any rest.

[P95]
I followed the others and vaulted into the saddle.

[P96]
*Why does trouble always break out the moment I arrive?*

[P97]
I sighed inwardly, but what could I do? This wasn't my first hardship—or my second. By now I just had to accept it.

[P98]
*Wasn’t this supposed to be a really simple Quest?*

[P99]
*Ding.*

[P100]
> **System**
>
> Quest difficulty has changed to **Peak**.

[P101]
“…”

[P102]
Right. Not anymore, I guess.

[P103]
* * *

[P104]
He was a man who resembled a fox. His pointed chin and ears, along with his sharp, slanted eyes, watched and observed everything around him at once.

[P105]
“Graaah!”

[P106]
“Kill them! Kill every last one of them!”

[P107]
“Aaaah!”

[P108]
Smoke billowed from a large manor, accompanied by screams.

[P109]
Pung Yang, the Red Wind Band Leader, sat astride his horse atop a hill and watched the scene below. He didn’t speak until the manor had fallen silent.

[P110]
“Is it over?”

[P111]
A mounted bandit who had just ridden up the hill to report answered him.

[P112]
“We killed all the men and gathered the women and children together.”

[P113]
“Why?”

[P114]
“Pardon? Why, it’s the tradition of Gaoyuan…”

[P115]
Any male taller than a cartwheel—even a child—was killed without mercy, while the women were taken or sold as slaves. It was a tradition—or something close to one—passed down from the nomads.

[P116]
At the mounted bandit’s words, Pung Yang quietly crooked one finger.

[P117]
“Come closer.”

[P118]
The mounted bandit approached hesitantly and asked carefully,

[P119]
“Leader, did I perhaps make some serious mistake…”

[P120]
“Who were you with before?”

[P121]
“Until recently, I was the deputy leader of the Earth Tiger Band.”

[P122]
“The Earth Tiger Band? Ah, I remember. You were their deputy leader.”

[P123]
“Y-yes! I was so impressed by your formidable martial arts and noble character that I swore to become your loyal subordinate!”

[P124]
Pung Yang scratched his nose with an ambiguous expression.

[P125]
*Was that so?*

[P126]
All he remembered was killing a piece of trash in a single strike—the man who had swaggered around calling himself a bandit leader while commanding some thirty subordinates.

[P127]
“My memory differs a little, but thank you anyway.”

[P128]
“Not at all! It’s an honor!”

[P129]
“Still, whatever the Earth Tiger Band may have been like, things are different in the Red Wind Band. Petty matters like the traditions of Gaoyuan, for instance.”

[P130]
“Ah, I didn’t realize.”

[P131]
“My orders as leader take priority. Do you understand?”

[P132]
“I’ll keep that in mind—over and over again!”

[P133]
“Those fellows probably followed Gaoyuan’s traditions because they didn’t know any better. They all joined recently, just like you. Would you go and tell them what I want?”

[P134]
“Your command is my law. I won’t leave a single one alive.”

[P135]
The mounted bandit even gave an awkward military salute, though there was nothing military about a mounted bandit. Pung Yang waved him away.

[P136]
“Yes, go on.”

[P137]
“Yes, Leader!”

[P138]
Pung Yang watched him ride away, then suddenly flicked his sleeve.

[P139]
*Whoosh!*

[P140]
A streak of light split the air and pierced its target ten jang—about thirty meters—away.

[P141]
*Thnk! Thud.*

[P142]
The horse kept galloping.

[P143]
It had no idea that its rider was already dead, his foot caught in the stirrup and his body being battered to pieces against the ground.

[P144]
“Go and tell them. There are no prisoners. Kill them all and burn the place.”

[P145]
“Yes, Leader.”

[P146]
Not long after Pung Yang’s subordinate departed, the entire manor was engulfed in flames. As he watched the signboard burn away in an instant, a faint smile touched the corners of his mouth.

[P147]
Mount Heng Sword Sect, Datong Branch.

[P148]
It was the moment the Red Wind Band crossed Gaoyuan once more.

[P149]
* * *

[P150]
The messenger’s report left the people arguing in the spacious main hall breathless.

[P151]
“They’ve broken through Datong!”

[P152]
“A-already?”

[P153]
“What about the Datong Branch? What happened to the men who went out to stand guard?”

[P154]
“Wiped out. They were all wiped out. The Datong Branch was reduced to ashes, and there wasn’t a single survivor.”

[P155]
“What?”

[P156]
“Could the report be wrong? They must have suffered heavy losses last time, so how could they have come this far so quickly…?”

[P157]
“They appear to have absorbed another mounted-bandit group. At least two hundred men—possibly more.”

[P158]
“Is that certain?”

[P159]
“Yes, without a doubt.”

[P160]
“Th-then when will they reach us…?”

[P161]
“If they’re fast, the attack will begin within a day. At the latest, we expect it within two days.”

[P162]
“We’re finished.”

[P163]
The muttered words were not much different from what most of the people gathered there were thinking.

[P164]
There were a little over ten of them, all senior figures holding important positions in the Mount Heng Sword Sect. Yet every one of them was already turning the word *defeat* over in their minds.

[P165]
“Iron Sword Squad Leader, are you confident in this fight?”

[P166]
“Why are you asking me, when you’re a Pavilion Leader? Am I the only martial artist here?”

[P167]
They were squad leaders, hall leaders, and pavilion leaders of the great Mount Heng Sword Sect.

[P168]
There had been a time when he had desperately wanted to rise to that position. Once upon a time, that was.

[P169]
To hell with the great Mount Heng Sword Sect. What good is a promotion now, with the sect in this state?

[P170]
*We were already on the verge of collapse, and now a mounted-bandit group has come to raise hell. Let’s see… If we scrape together everyone we have left, we might reach a hundred.*

[P171]
The war with the Jin Family of Taiyuan had cost them nearly eighty percent of their strength.

[P172]
They had lost the elite martial artists they had painstakingly trained and the seasoned senior figures who had weathered countless trials in the martial world. Most painful of all was the loss of the Peak masters who embodied the sect’s power—and of its financial resources.

[P173]
“Damn it. If only the Sect Leader were still alive.”

[P174]
Lee Cheonbaek had started as a mere wandering martial artist and built the Mount Heng Sword Sect into what it was now. With his martial arts and resourcefulness, he could have turned this situation around.

[P175]
But the Blood Wolf Sword, Lee Cheonbaek, was already dead. Of his bloodline, only one person remained alive.

[P176]
“To think we have to serve some little girl who isn’t even twenty as Sect Leader at a time like this.”

[P177]
The moment someone spat out those words in anger—

[P178]
*Boom!*

[P179]
The tightly closed doors of the main hall exploded.
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
# Chapter 109

[P2]
A messenger hawk.

[P3]
I’d heard the Jin Family of Taiyuan had only two of them. They were messenger birds, but difficult to train, so they were used only to deliver important information…

[P4]
*Who sent it?*

[P5]
Just as I was about to approach the messenger hawk, Wolhwa called out to me.

[P6]
“You’d better keep your distance. It’s a very wary bird. If Young Master Jin tries to catch it, it’ll fly away.”

[P7]
“Ah, could it be?”

[P8]
“It’s a messenger hawk sent from our sect. It was trained to follow a specific tracking scent.”

[P9]
Wolhwa pulled a small pouch from her robes and shook it. The messenger hawk cautiously approached and rubbed its beak against it.

[P10]
In that moment, a Lower District Sect member who had somehow already slipped outside untied the cylinder from the hawk’s ankle.

[P11]
“Where’s it from?”

[P12]
“A letter sent yesterday from the Sakju Branch to the Branch Leader.”

[P13]
“Give it to me.”

[P14]
Wolhwa accepted the letter and read it. Her expression turned complicated.

[P15]
It took a while before her tightly closed lips finally parted.

[P16]
“The Red Wind Band Leader… He’s more than I expected.”

[P17]
“Is this about the Red Wind Band again?”

[P18]
Wolhwa gave a small nod and handed me the letter.

[P19]
There was no reason to refuse when she was telling me to read it. Jin Mukyung and Hyuk Mujin, who had been hesitating nearby, cautiously leaned in as well.

[P20]
The Red Wind Band is moving south across the plateau. Their numbers are estimated at approximately two hundred.

[P21]
The short line made its meaning clear.

[P22]
“They’re planning to attack the Mount Heng Sword Sect again.”

[P23]
“There’s no doubt about it. This news is already a day old, so they must have narrowed the distance by that much—or more.”

[P24]
We were currently a day and a half away from the Mount Heng Sword Sect.

[P25]
As a mounted-bandit group, they would be advancing toward their destination with exceptional mobility.

[P26]
“Unfortunately, our branch doesn’t have a proper intelligence network in the northern region. The one fortunate thing is…”

[P27]
Wolhwa’s gaze shifted toward the mounted bandits of the Red Wind Band. They had lost the will to fight long ago, and flinched as they lowered their heads.

[P28]
“We have valuable sources of information right here. I don’t know whether they have any useful information, though.”

[P29]
After looking over the mounted bandits, she suddenly pointed at one of them.

[P30]
“You. Stand up.”

[P31]
“……M-me?”

[P32]
The man rose with a thoroughly terrified expression. He was younger than I expected. The youngest and weakest of the mounted bandits, he couldn’t even meet Wolhwa’s gaze.

[P33]
“How old are you?”

[P34]
“I-I passed twenty this year.”

[P35]
“Twenty? You’re young. Then again, being young doesn’t stop someone from becoming a mounted bandit.”

[P36]
“I’m not a mounted bandit! I only became a wandering martial artist recently, but then they said they’d give me a big cut, so I…”

[P37]
“Ah, so you’re one of the wandering martial artists the Red Wind Band Leader gathered for the last attack?”

[P38]
“Y-yes! I’ll tell you everything I know!”

[P39]
“No, it’s all right.”

[P40]
“Pardon?”

[P41]
“You don’t look like you know much anyway. What would be the point? Isn’t that right, Chunsam?”

[P42]
The Lower District Sect member who had silently played the part of our carriage driver until now.

[P43]
Instead of answering, he pulled a small knife from his robes and drove it into the young man’s chest.

[P44]
*Thunk—*

[P45]
A First Rate martial artist’s fast, precise One Strike split the young man’s heart. He opened and closed his mouth soundlessly before collapsing like a puppet with its strings cut.

[P46]
*Thud.*

[P47]
A frigid silence pressed down on the scene. While the mounted bandits stared in horror and fear, Wolhwa’s slender finger moved once more.

[P48]
“You.”

[P49]
“I-I’ll talk! I’ll tell you everything! I’ve been with the Red Wind Band for a year…”

[P50]
“Chunsam.”

[P51]
*Whoosh! Slash!*

[P52]
“Grrk… Gurg…”

[P53]
The mounted bandit staggered backward, making a wet, blood-choked sound. He tried to cover his gaping throat, but couldn’t stop the fountain of blood spraying between his fingers.

[P54]
“You only need to remember two things.”

[P55]
From head to toe, Wolhwa was covered in crimson blood. She continued in a dry tone.

[P56]
“Answer only what you’re asked, and tell the truth exactly as it is.”

[P57]
“……!”

[P58]
In mere moments, we learned everything there was to know about the Red Wind Band.

[P59]
* * *

[P60]
Once we learned that every second mattered, we abandoned the carriage and each chose a horse. Me, Jin Mukyung, Hyuk Mujin, and Wolhwa.

[P61]
The Lower District Sect member would take the Five-Colored Ghosts and the surviving mounted bandits to a nearby Lower District Sect branch and report what had happened.

[P62]
“Was that too cruel?”

[P63]
Wolhwa asked as she lifted a saddle onto her horse. I scratched my chin.

[P64]
“To be honest, I was a little surprised.”

[P65]
I had temporarily forgotten because I had only ever seen her relaxed and playful. She was a martial artist too.

[P66]
*And an experienced one at that.*

[P67]
How old was Wolhwa, anyway?

[P68]
I’d never asked, so I didn’t know for sure, but she couldn’t have been over thirty.

[P69]
To become the Branch Leader overseeing all of Shanxi at such a young age, she had to possess the decisiveness to match the position.

[P70]
*Cruel, but effective.*

[P71]
She had killed two people without hesitation. Just as casually as swatting flies.

[P72]
Jin Mukyung’s display against the leader must have terrified the mounted bandits, but the fear of death was even greater.

[P73]
Driven to the edge of a cliff, they had no choice but to pour out information desperately.

[P74]
“I think I would’ve spilled everything too.”

[P75]
“I’m saying this in case Young Master Jin gets the wrong idea, but I don’t enjoy killing people. They weren’t innocent commoners, either… Ah, this bastard’s blood just won’t stop, even when I wipe it.”

[P76]
The blood streaming down her belonged to the second mounted bandit she had killed.

[P77]
As she wrinkled her nose, someone held out a piece of cloth to her.

[P78]
“U-use this to wipe it off.”

[P79]
“Oh my.”

[P80]
“Huh?”

[P81]
“Hmm.”

[P82]
At the reactions from Wolhwa, me, and Hyuk Mujin, Jin Mukyung cleared his throat repeatedly.

[P83]
“I thought you might need it.”

[P84]
“Thank you, Young Hero Jin. I needed it.”

[P85]
“It’s nothing.”

[P86]
His expression, however, looked quite pleased.

[P87]
*No way. Is he…*

[P88]
*The type who’s only nice to women?*

[P89]
There was always at least one guy like that wherever you went. Even the Heaven Shaking Sword wasn’t any different, apparently.

[P90]
After wiping away the blood, Wolhwa pulled a rolled-up piece of leather from her robes and spread it out.

[P91]
“This is a rough map of the entire Shanxi region. Our location is here. The Red Wind Band has probably… If they’ve been moving without rest, they may have already broken through Datong.”

[P92]
“They’re faster than us.”

[P93]
“By half a day for now. But the roads along our route are well maintained, so if we ride day and night, we can narrow the gap enough.”

[P94]
In short, she was telling us not to expect any rest.

[P95]
I followed the others and leaped onto my saddle.

[P96]
*Why does something always happen the moment I arrive?*

[P97]
I wanted to sigh, but what could I do? It wasn’t as though this was my first hardship—or my second. I’d just have to accept it.

[P98]
*Wasn’t this supposed to be a really simple Quest?*

[P99]
*Ding.*

[P100]
> **System**
>
> Quest difficulty has changed to **Peak**.

[P101]
“……”

[P102]
Right. I guess it wasn’t simple anymore.

[P103]
* * *

[P104]
He was a man who resembled a fox. His pointed chin and ears, along with his sharp, slanted eyes, watched and observed everything around him at once.

[P105]
“Graaah!”

[P106]
“Kill them! Kill every last one of them!”

[P107]
“Aaaah!”

[P108]
Smoke billowed from a large manor, accompanied by screams.

[P109]
The man sitting on horseback and gazing down from the hill was Pung Yang, the Red Wind Band Leader. He didn’t speak until the manor had fallen silent.

[P110]
“Is it over?”

[P111]
A mounted bandit who had just climbed the hill to deliver his report answered.

[P112]
“We killed all the men and gathered the women and children together.”

[P113]
“Why?”

[P114]
“Pardon? Why, because it’s the plateau’s tradition, of course…”

[P115]
Any male taller than a cartwheel—even a child—was killed without mercy, while the women were taken or sold as slaves. It was a tradition—or something close to one—passed down from the nomads.

[P116]
At the mounted bandit’s words, Pung Yang quietly crooked one finger.

[P117]
“Come closer.”

[P118]
The mounted bandit approached hesitantly and asked carefully,

[P119]
“Leader, did I perhaps make some serious mistake…”

[P120]
“Where did you belong before?”

[P121]
“Until recently, I was the deputy leader of the Toho Band.”

[P122]
“The Toho Band? Ah, I remember. You were their deputy leader.”

[P123]
“Y-yes! I was so impressed by your formidable martial arts and noble character that I swore to become your loyal subordinate!”

[P124]
Pung Yang scratched his nose with an ambiguous expression.

[P125]
*Was that so?*

[P126]
All he remembered was killing a piece of trash in a single strike—the man who had swaggered around calling himself a bandit leader while commanding some thirty subordinates.

[P127]
“My memory differs a little, but thank you anyway.”

[P128]
“Not at all! It’s an honor!”

[P129]
“However, the Earth Tiger Band may have been different. The Red Wind Band has its own way. Those petty matters about plateau traditions, for example.”

[P130]
“Ah, I didn’t realize.”

[P131]
“My orders as leader take priority. Do you understand?”

[P132]
“I’ll keep that in mind—over and over again!”

[P133]
“Those fellows probably followed the plateau’s traditions because they didn’t know any better. They all joined recently, just like you. So go and convey my wishes to them, will you?”

[P134]
“Understood. I won’t leave a single one alive.”

[P135]
The mounted bandit even gave an awkward military salute, though there was nothing military about a mounted bandit. Pung Yang waved him away.

[P136]
“Yes, go on.”

[P137]
“Yes, Leader!”

[P138]
Pung Yang watched him ride away, then suddenly flicked his sleeve.

[P139]
With a sharp sound as the air split, a streak of light shot out and pierced its target ten jang away—about thirty meters.

[P140]
*Thud!*

[P141]
*Clatter.*

[P142]
The horse continued racing forward.

[P143]
Its rider was already dead, but his foot remained caught in the stirrup. Unaware that his body was being dragged and battered to shreds, the horse galloped on.

[P144]
“Go and tell them. There are no prisoners. Kill them all and burn the place.”

[P145]
“Yes, Leader.”

[P146]
Not long after Pung Yang’s subordinate departed, the entire manor was engulfed in flames. As he watched the signboard burn away in an instant, a faint smile touched the corners of his mouth.

[P147]
The Datong Branch of the Mount Heng Sword Sect.

[P148]
The moment the Red Wind Band crossed the plateau once more.

[P149]
* * *

[P150]
The people gathered in the spacious main hall had been arguing back and forth when the messenger’s report left them speechless.

[P151]
“They’ve broken through Datong!”

[P152]
“A-already?”

[P153]
“What about the Datong Branch? What happened to the men who went out to stand guard?”

[P154]
“Everyone was wiped out. Everyone. The Datong Branch was reduced to ashes, and there were no survivors.”

[P155]
“What?”

[P156]
“Could the report be wrong? They must have suffered heavy losses last time, so how could they have come this far so quickly…?”

[P157]
“They appear to have absorbed another mounted-bandit group. At least two hundred men—possibly more.”

[P158]
“Is that certain?”

[P159]
“Yes, without a doubt.”

[P160]
“Th-then when will they reach us…?”

[P161]
“If they’re fast, the attack will begin within a day. At the latest, we expect it within two days.”

[P162]
“We’re finished.”

[P163]
The muttered words were not much different from what most of the people gathered there were thinking.

[P164]
There were a little over ten of them, all senior figures holding important positions in the Mount Heng Sword Sect. Yet every one of them was already turning the word *defeat* over in their minds.

[P165]
“Iron Sword Squad Leader, are you confident in this fight?”

[P166]
“Why are you asking me, when you’re a Pavilion Leader? Am I the only martial artist here?”

[P167]
They were squad leaders, hall leaders, and pavilion leaders of the great Mount Heng Sword Sect.

[P168]
There had been a time when he had desperately wanted to rise to that position. Once upon a time, that was.

[P169]
*To hell with being a commander of the Mount Heng Sword Sect. What good is a promotion now, with the sect in this state?*

[P170]
*We were already doomed if left alone, and now a mounted-bandit group has come to make a mess of everything. Let’s see… If we scrape together every man we have left, there might be a hundred of them.*

[P171]
The war with the Jin Family of Taiyuan had cost them nearly eighty percent of their strength.

[P172]
The loss of the elite martial artists they had painstakingly trained and the seasoned senior figures who had weathered the martial world was painful enough. Most devastating of all was the loss of the Peak masters who represented the sect’s power—and its financial resources.

[P173]
“Damn it. If only the Sect Leader were still alive.”

[P174]
Lee Cheonbaek had started as a mere wandering martial artist and built the Mount Heng Sword Sect into what it was now. With his martial arts and resourcefulness, he could have turned this situation around.

[P175]
But the Blood Wolf Sword, Lee Cheonbaek, was already dead. Of his bloodline, only one person remained alive.

[P176]
“To think we have to serve some little girl who isn’t even twenty as Sect Leader at a time like this.”

[P177]
At that moment, someone spat out the words in a fit of anger.

[P178]
*Boom!*

[P179]
The tightly closed doors of the main hall exploded.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 월화     | **Wolhwa**         |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 대주     | **Squad Leader** / **Commander**             |
| 지부장    | **Branch Leader**                            |
| 일격     | **One Strike**                         |
| 퀘스트              | **Quest**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본문      | **our sect / this sect**                                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 삭주 | **Sakju** | Jin Family branch location |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 토호단 | **Earth Tiger Band** | Mounted-bandit group formerly led by Pung Yang's subordinate. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 109,
  "passed": true,
  "metrics": {
    "source_characters": 5665,
    "translation_characters": 12915,
    "length_ratio": 2.28,
    "source_paragraphs": 178,
    "translation_paragraphs": 179
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "무림",
        "preferred": "Murim"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "돌파",
        "preferred": "break through / breakthrough"
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
