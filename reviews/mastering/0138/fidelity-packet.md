# Fidelity Gate — Chapter 138

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
  1|＃138화
  2|
  3|
  4|
  5|호화로운 육두마차는 거침없이 질주했다.
  6|
  7|척 봐도 정예로 보이는 군사들이 앞에서 길을 텄고, 개미처럼 바글바글하던 사람들은 양옆으로 쫙 갈라서서 바람처럼 달려가는 마차를 지켜봤다.
  8|
  9|“모세가 이런 기분이었구나.”
 10|
 11|내 중얼거림에 청풍이 반응했다.
 12|
 13|“모세요? 그게 뭡니까?”
 14|
 15|“있어요, 그런 사람이.”
 16|
 17|“아, 네.”
 18|
 19|혁무진이었다면 또 이상한 소릴 한다며 한참을 투덜거렸겠지만, 청풍은 달랐다.
 20|
 21|그는 놀이동산에 온 어린애처럼 신난 얼굴로 마차 이곳저곳을 누르고 두드렸다.
 22|
 23|“육두마차는 난생처음 타 봅니다!”
 24|
 25|“……사두마차는요?”
 26|
 27|“사두마차도 안 타 봤어요!”
 28|
 29|“그냥 마차는…….”
 30|
 31|“그냥 마차도 타 보고 싶습니다!”
 32|
 33|“…….”
 34|
 35|지하철이라도 태워 주면 기절하겠는데.
 36|
 37|이쯤 되면 안 해 본 걸 세는 것보다 해 본 걸 세는 게 훨씬 빠르겠다.
 38|
 39|나는 흥분 상태에 접어든 청풍을 물끄러미 바라봤다.
 40|
 41|‘이거 도대체 뭐 하는 놈이야?’
 42|
 43|얘를 순수하다고 해야 할지, 멍청하다고 해야 할지.
 44|
 45|하긴, 평생을 산에서 살았다고 하니 어쩌면 당연한 것일지도 모른다.
 46|
 47|‘다루기가 쉬워서 좋기도 하고.’
 48|
 49|방금 그 표정이 잊히지 않는다. 황족이라는 한 단어에 쌍라이트가 번쩍하던 눈동자도.
 50|
 51|
 52|
 53|‘혹시 황족 본 적 있어요?’
 54|
 55|‘볼래요! 보겠습니다! 보게 해 주세요!’
 56|
 57|
 58|
 59|그의 눈에 담겼던 건 일반적인 양민들이 가지는 황실에 대한 동경 같은 것이 아니었다. 굳이 따지자면 동물원 코끼리를 보러 가는 설렘이랄까.
 60|
 61|‘진짜 특이한 놈일세.’
 62|
 63|나만 그렇게 생각하는 건 아닌가 보다.
 64|
 65|중상인 우진태를 제외한 산서오문의 후기지수들도 해괴한 것을 보는 듯한 표정으로 청풍을 바라보고 있었다.
 66|
 67|“어째 상태가 좀…….”
 68|
 69|“정말 이대로 가도 되는 거야?”
 70|
 71|“괜히 전하 앞에서 말실수라도 하면 우리까지 피 볼 것 같은데.”
 72|
 73|“말실수로 끝나면 다행이지. 황족 처음 봐서 신기하다고 귀라도 잡아당기면 그날로 끝이야, 끝.”
 74|
 75|……제법 그럴듯한 추측인데?
 76|
 77|후기지수들의 수군거림에 함께 마차에 타고 있던 관리도 불안한 얼굴로 귓속말을 건넸다.
 78|
 79|“저기, 진 공자.”
 80|
 81|“네?”
 82|
 83|“저 사람…… 정말 괜찮은 것 맞소?”
 84|
 85|“믿으십쇼. 제가 보증하는 고수라니까요.”
 86|
 87|“아니, 고수고 나발이고 정신이 괜찮냐는 말이오.”
 88|
 89|“아.”
 90|
 91|“차라리 공자와 함께 있던 그 무사를 데려오는 게 더 낫지 않겠소?”
 92|
 93|“누구, 아 혁무진이요?”
 94|
 95|“그런 이름이었던 것 같소. 내 듣자 하니 그 무사도 상당한 무공의 소유자라던데.”
 96|
 97|혁무진이 들었다면 좋아서 펄쩍 뛰었을 얘기다.
 98|
 99|문제는 아침에 나한테 맞은 덕분에 얼굴에 시퍼런 멍이 들어 도저히 함께 갈 수 없다는 거지만.
100|
101|‘그리고 혁무진 정도로는 안 돼.’
102|
103|어린 왕의 심기를 거스르지 않게 하려면 보다 큰 선물을 가져가야 한다.
104|
105|나는 걱정하는 관리를 향해 단호하게 고개를 저어 보였다.
106|
107|“걱정 마십시오. 문제 안 생기도록 제가 책임지고 단속하겠습니다.”
108|
109|내가 누군가, 명망 높은 태원진가의 직계이자 떠오르는 샛별, 산서 무림의 라이징 스타다.
110|
111|내 호언장담에 관리의 얼굴이 약간 밝아졌다.
112|
113|“그럼 본인은 진 공자만 믿겠…….”
114|
115|우둑.
116|
117|“……?”
118|
119|“……?”
120|
121|잠깐만. 이게 무슨 소리야.
122|
123|약속이라도 한 듯이 동시에 고개를 돌린 우리의 시선에, 뭔가를 움켜쥐고 있는 청풍이 보였다.
124|
125|“어, 이게 왜 떨어졌지?”
126|
127|매우 정교하게 만들어진 황금 용을 들고 헤헤 웃는 녀석의 모습에 한참 침묵하던 관리가 나를 바라봤다.
128|
129|“진 공자.”
130|
131|“네.”
132|
133|“정말 괜찮은 것 맞소?”
134|
135|나는 고민 끝에 입을 열었다.
136|
137|“아마도요.”
138|
139|
140|
141|* * *
142|
143|
144|
145|저택이 아니라 성(城)이라고 해도 될 만큼 드넓은 공간. 사내의 발걸음은 거침없었다.
146|
147|굳게 다문 입술과 강건한 눈빛을 마주한 이들은 하나같이 공손히 예를 표했다.
148|
149|“첨사 어른을 뵙습니다.”
150|
151|그는 고개를 끄덕이는 것으로 인사를 대신하고 걸음을 재촉했다.
152|
153|기둥들이 끝없이 늘어선 회랑(回廊)을 지나고 얼마나 걸었을까? 용이 음각된 거대한 철문이 나타나고서야 사내의 발걸음이 멈췄다.
154|
155|“아뢰게.”
156|
157|“충.”
158|
159|그를 향해 군례를 취한 호위군 소속의 장수가 힘차게 외쳤다.
160|
161|“산서성 도지휘첨사(都指揮僉事), 이풍(李灃) 영감 듭시오!”
162|
163|얼마 지나지 않아 그에 응답하는 목소리가 들려왔다.
164|
165|“들라 하라.”
166|
167|“……!”
168|
169|어린아이처럼 앳되지도, 그렇다고 장성한 사내처럼 굵지도 않은 목소리.
170|
171|뭔가를 짐작한 사내, 이풍의 눈썹이 솟구친 그때, 육중한 소리와 함께 철문이 열렸다.
172|
173|그그긍.
174|
175|그곳은 호화롭게 치장된 대전(大殿)이었다. 사방이 금은보화로 번쩍거렸고 수십 명이 앉아도 될 만큼 넓은 탁자는 온갖 산해진미로 가득 차 있었다.
176|
177|다른 사람이라면 입을 딱 벌렸을 만한 광경. 그러나 이풍의 시선은 한곳에 못 박혀 떠날 줄을 몰랐다.
178|
179|‘저자가 어찌.’
180|
181|이풍의 시선 끝, 탁자의 상석(上席)에 앉아 있던 한 사람이 빙긋 웃었다.
182|
183|눈이 부실 만큼 화려한 붉은 비단으로 몸을 휘감은 사내의 입에서 간드러진 목소리가 흘러나왔다.
184|
185|“이게 누구야, 우리 이 첨사 아니에요?”
186|
187|우리 이 첨사?
188|
189|이풍은 지그시 입술을 깨물며 군례를 취했다.
190|
191|“……도지휘동지(都指揮同知)를 뵙습니다.”
192|
193|도지휘동지는 종이품으로 각 성에 두 명밖에 없는 고위직.
194|
195|군 총사령관인 도지휘사와 성주인 상산왕을 제외하면 가장 높은 직책이며, 부사령관인 만큼 실권 또한 막강했다.
196|
197|실제로 알려진 것은 이러하지만, 눈앞의 사내가 가진 권한은 그 이상이었다.
198|
199|‘쳐 죽일 놈 같으니.’
200|
201|간사한 혓바닥과 잔재주로 어린 왕의 눈과 귀를 가리고 제 배만 채우는 간신이자 탐관오리. 그것이 사내에 대한 이풍의 평가였다.
202|
203|그러나 이풍의 곱지 않은 눈길에도 그의 웃음은 여전했다.
204|
205|“이 첨사, 오랜만에 보는데 분위기가 너무 험악한 거 아니에요? 혹시 내가 뭐 섭섭하게 한 거라도?”
206|
207|“……그럴 리가 있습니까. 저는 그저 도지휘동지께서 이런 자리에 계신 것이 뜻밖이라 놀란 것뿐입니다.”
208|
209|“이런 자리라니?”
210|
211|“강호의 무부(武夫)들이 모이는 자리입니다. 워낙 거친 자들이라 도지휘동지께서 불편하시지 않을까 염려되는군요.”
212|
213|말은 위해 주는 것 같지만 속뜻은 다르다. 두 사람 모두 그 사실을 모르지 않았다.
214|
215|“왜요? 나 이런 자리 좋아해. 그리고 아까부터 호칭이 너무 딱딱하다. 그냥 편하게 불러요. 우리 사이인데 뭐 어때.”
216|
217|“우리 사이라…… 그게 무슨 사입니까?”
218|
219|“콩 한 쪽도 나눠 먹는 사이. 전하를 충심으로 보필하는 참된 신하들이지요.”
220|
221|콩 한 쪽도 나눠 먹어? 참된 신하?
222|
223|사내의 말에 이풍이 무뚝뚝하게 물었다.
224|
225|“그럼 편하게 홍 내관이라고 부르면 되겠습니까?”
226|
227|사내, 홍 내관의 웃음이 순간 경직됐다.
228|
229|이풍은 고작 한 단어로 그의 역린을 건드렸다.
230|
231|“그건…… 너무 편한데?”
232|
233|“저야 말씀을 따른 것뿐입니다.”
234|
235|“이거 참, 이 첨사가 나를 그 정도로 편하게 생각하는지는 몰랐네.”
236|
237|“이제라도 제 마음을 알아주시니 몸 둘 바를 모르겠군요.”
238|
239|“이 첨사.”
240|
241|“부르셨습니까, 홍 내관. 아니, 다시 도지휘동지라고 불러 드릴까요?”
242|
243|무겁게 내려앉은 정적.
244|
245|홍 내관의 입이 다시금 열린 것은 한참 후였다.
246|
247|“우리 이 첨사, 많이 늘었다?”
248|
249|“그렇습니까?”
250|
251|“응, 몇 년 전에 비하면 일취월장했는데?”
252|
253|“덕분에 여러 가지 배웠습니다.”
254|
255|“검만 잘 쓰는 줄 알았는데, 오늘 보니 혀도 잘 쓰네. 다시 봤어요.”
256|
257|“누구보다는 아직 한참 모자랍니다.”
258|
259|두 사람의 시선이 허공에서 부딪쳤다. 팽팽하게 조여진 공기 속에서 홍 내관이 부드럽게 웃었다.
260|
261|“뭐, 이 이야기는 나중에 하고…… 내가 뭐 하나만 물어봐도 되려나?”
262|
263|만만치 않은 상대가 한발 물러났다. 여기서 더 물어뜯었다가는 되레 낭패만 볼 뿐이다. 이풍은 묵묵히 고개를 끄덕였다.
264|
265|“하문하십시오.”
266|
267|“이 첨사가 전에 화산파에 있었다고 했죠?”
268|
269|이풍이 멈칫했다. 그에게 있어 화산파는 그리우면서도 아픈 기억이다.
270|
271|화산을 떠난 지 이제 어언 십 년이지만 그곳에서의 기억은 여전히 몸과 마음 깊숙이 남아 있었다.
272|
273|“예. 속가제자였습니다.”
274|
275|“화산파는 섬서에 있고?”
276|
277|그와 홍 내관은 이른바 정적(政敵)이라 할 수 있는 관계였다. 그만큼 오히려 속속들이 잘 알았다.
278|
279|홍 내관은 이런 기본적인 사실을 몰라서 물어볼 만큼 허술하지도, 멍청하지도 않았다.
280|
281|오히려 속에 구렁이가 백 마리는 득실거리는 교활한 놈이다.
282|
283|그렇기에 이풍은 더욱 의아함을 느꼈다.
284|
285|“맞습니다. 그런데 갑자기 그건 왜 물어보시는지?”
286|
287|“내가 이번에 알게 된 지인이 몇 분 있는데, 혹시 이 첨사도 알까 싶어서.”
288|
289|“무림인입니까?”
290|
291|“맞아요. 그것도 섬서 출신.”
292|
293|“설마 화산……?”
294|
295|“에이, 그럼 내가 미리 말을 했겠지.”
296|
297|이풍은 안도의 한숨을 내쉬었다.
298|
299|결국, 스스로 떠나오긴 했지만 평생을 자랑스러워할 사문(師門)이다. 홍 내관 같은 간신배와 엮이지 않았다는 사실이 천만다행이었다.
300|
301|“섬서에 문파가 한둘도 아니고, 저도 본산에서 수련하는 중에는 바깥출입을 하지 않았기 때문에 이름을 들어도 잘 모릅니다.”
302|
303|“그런가? 그럼 얼굴을 보면 알 수도 있겠네?”
304|
305|“……?”
306|
307|이풍의 표정을 본 홍 내관이 탁자에 놓인 젓가락을 집어 들었다.
308|
309|“아까 이 첨사가 물어봤었죠? 내가 왜 이런 자리에 있냐고.”
310|
311|아름답게 세공된 은 젓가락이 술잔을 두드렸다.
312|
313|팅. 맑은 소리가 멀리 퍼져 나갔다. 어리둥절한 이풍에게 홍 내관이 눈웃음을 지어 보였다.
314|
315|“지인을 몇 분 초대했거든. 전하께서 좋아하실 만큼 명성 높고 강한 무인들로.”
316|
317|동시에 철문 밖에서 힘찬 외침이 들려왔다.
318|
319|“섬서의 종남삼수(終南三手)가 뵙기를 청합니다!”
320|
321|“종남삼수…… 종남파!”
322|
323|이풍의 안색이 급변했다.
324|
325|화산파와 종남파는 장장 백 년간 섬서의 패권을 다퉈 온 앙숙 관계.
326|
327|홍 내관의 의도는 지금 짓고 있는 웃음만큼이나 환하기 그지없었다.
328|
329|“같은 섬서 사람이라 자리를 마련해 봤어요. 괜찮죠?”
330|
331|이풍이 주먹을 불끈 움켜쥔 그때, 거대한 철문이 열리고 대전 안으로 장대한 체구의 세 사람이 성큼 들어왔다.
332|
333|그중에 낯익은 얼굴 하나가 끼어 있었다.
334|
335|“이게 누구야. 화산파의 이풍 아닌가?”
336|
337|이풍은 몸을 부르르 떨었다. 놈의 얼굴을 본 순간 십 년 전의 그 치욕스러운 기억이 떠올랐기 때문이었다.
338|
339|“네가 여길 어떻게!”
340|
341|날카로운 눈매의 사내가 천연덕스럽게 대답했다.
342|
343|“어떻게 오긴. 산서성의 도지휘동지께서 불러 주시는데 천 리라도 한달음에 달려와야지. 안 그렇습니까?”
344|
345|“별말씀을. 오히려 초대에 응해 주셔서 감사할 따름이에요.”
346|
347|으드득, 이를 가는 이풍을 향해 종남삼수의 셋째, 공일혁이 씩 웃어 보였다.
348|
349|“그나저나 출세했네. 자네 주제에 도지휘첨사라…… 화산에서 은자깨나 뿌렸겠어. 응?”
350|
351|“네놈이 감히 화산파를 모욕해?”
352|
353|“응? 화산파를 모욕한 건 자네지. 십 년 전, 그 대단한 화산 무공으로 백여 초 만에 무릎을 꿇은 게 누구였나?”
354|
355|“이놈-!”
356|
357|이풍의 입에서 벼락같은 외침이 터져 나왔다.
358|
359|그가 화염이 줄기줄기 쏟아지는 눈동자로 공일혁을 노려보던 그 순간. 철문 밖에서 세 번째 외침이 들려왔다.
360|
361|“산서 무림의 후기지수들이 뵙기를 청합니다!”
```

## Assembled English

```markdown
[P1]
# Chapter 138

[P2]
The luxurious six-horse carriage raced onward without slowing.

[P3]
Elite-looking soldiers cleared the road ahead, while the crowds swarming like ants parted to either side and watched the carriage fly past like the wind.

[P4]
“So this is how Moses felt.”

[P5]
Cheongpung reacted to my mutter.

[P6]
“Moses? Who is that?”

[P7]
“Someone.”

[P8]
“Oh, I see.”

[P9]
If it had been Hyuk Mujin, he would have complained for ages about me saying something weird, but Cheongpung was different.

[P10]
He wore the excited expression of a child at an amusement park as he pressed and tapped every part of the carriage.

[P11]
“This is my first time riding in a six-horse carriage!”

[P12]
“…What about a four-horse carriage?”

[P13]
“I’ve never ridden in one of those, either!”

[P14]
“What about an ordinary carriage…?”

[P15]
“I’d like to ride in one of those, too!”

[P16]
“…”

[P17]
If I put him on a subway, he would probably faint.

[P18]
At this point, it would be much faster to count the things he had done than the things he hadn’t.

[P19]
I stared at the thoroughly excited Cheongpung.

[P20]
*What the hell is this guy?*

[P21]
Was he innocent or stupid?

[P22]
Then again, he had said he had lived his entire life in the mountains. Maybe this was only natural.

[P23]
*At least he’s easy to handle.*

[P24]
I still couldn’t forget the expression he had just made. His eyes had lit up like high beams at the mere mention of the imperial family.

[P25]
*“Have you ever seen a member of the imperial family?”*

[P26]
*“I want to! I’ll see one! Please let me see one!”*

[P27]
What filled his eyes wasn’t the sort of admiration ordinary commoners felt toward the imperial family. If I had to compare it to something, it was more like the excitement of going to see an elephant at the zoo.

[P28]
*He really is a strange one.*

[P29]
Apparently, I wasn’t the only one who thought so.

[P30]
The young prodigies of the Five Gates of Shanxi, excluding the severely injured Woo Jintae, were staring at Cheongpung as if they were looking at something bizarre.

[P31]
“There’s something a little… off about him.”

[P32]
“Can we really go like this?”

[P33]
“If he says something inappropriate in front of His Highness, we might get dragged into it, too.”

[P34]
“We’ll be lucky if that’s all he does. If he gets excited about seeing a member of the imperial family for the first time and pulls on his ear, we’re finished. Completely finished.”

[P35]
…That was a surprisingly plausible prediction.

[P36]
Hearing the young prodigies whispering, the official riding in the carriage with us leaned over anxiously and whispered.

[P37]
“Um, Young Master Jin.”

[P38]
“Yes?”

[P39]
“That man… Are you certain he’s all right?”

[P40]
“Trust me. He’s a master I can vouch for.”

[P41]
“To hell with whether he’s a master. I’m asking whether he’s right in the head.”

[P42]
“Oh.”

[P43]
“Wouldn’t it be better to bring along the martial artist who was with you instead?”

[P44]
“Who? Ah, Hyuk Mujin?”

[P45]
“I believe that was his name. I hear he’s also quite skilled in martial arts.”

[P46]
If Mujin had heard that, he would have jumped for joy.

[P47]
The problem was that he had a dark blue bruise on his face from getting beaten by me that morning, so there was no way he could come along.

[P48]
*Besides, Hyuk Mujin wouldn’t be enough.*

[P49]
To avoid offending the young prince, I needed to bring a more impressive gift.

[P50]
I firmly shook my head at the worried official.

[P51]
“Don’t worry. I’ll take responsibility for keeping him under control.”

[P52]
Who was I? A direct descendant of the prestigious Jin Family of Taiyuan, a rising star, and Shanxi Murim’s newest sensation.

[P53]
My bold assurance brightened the official’s expression a little.

[P54]
“Then I’ll trust Young Master Jin—”

[P55]
*Crack.*

[P56]
“…?”

[P57]
“…?”

[P58]
Wait a second. What was that sound?

[P59]
As if on cue, we all turned our heads at the same time.

[P60]
There was Cheongpung, clutching something in his hands.

[P61]
“Huh? Why did this fall off?”

[P62]
Cheongpung grinned foolishly, holding an exquisitely crafted golden dragon. After a long silence, the official looked at me.

[P63]
“Young Master Jin.”

[P64]
“Yes?”

[P65]
“Are you certain he’s all right?”

[P66]
After thinking it over, I opened my mouth.

[P67]
“Probably.”

[P68]
* * *

[P69]
The space was so vast that it could have been called a castle rather than a residence. A man strode through it without hesitation.

[P70]
Everyone who saw his tightly set lips and resolute gaze paid their respects.

[P71]
“Greetings, Assistant Military Commissioner.”

[P72]
He acknowledged them with a nod and quickened his pace.

[P73]
After passing through a corridor lined with endless pillars, how long had he been walking? The man finally stopped when a massive iron gate engraved with a dragon appeared before him.

[P74]
“Announce me.”

[P75]
“Yes, sir.”

[P76]
A commander of the palace guard saluted him and called out in a powerful voice.

[P77]
“His Excellency Li Feng, Assistant Military Commissioner of Shanxi Province, entering!”

[P78]
Before long, a voice answered from within.

[P79]
“Let him enter.”

[P80]
“…!”

[P81]
The voice was neither as high and childish as a little boy’s nor as deep as a grown man’s.

[P82]
The man—Li Feng—seemed to realize something. His eyebrows shot up just as the iron gate opened with a heavy groan.

[P83]
*Grrrnnng.*

[P84]
Beyond it lay an extravagantly decorated grand hall. Gold and silver treasures glittered in every direction, and a table large enough to seat dozens was laden with every delicacy from land and sea.

[P85]
The sight would have left anyone else gaping. But Li Feng’s gaze remained fixed on a single point.

[P86]
*How is he here?*

[P87]
At the end of Li Feng’s gaze, a man seated at the head of the table smiled faintly.

[P88]
Wrapped in dazzling red silk, the man spoke in a coy, lilting voice.

[P89]
“Well, well. If it isn’t our Assistant Commissioner Li.”

[P90]
*Our Assistant Commissioner Li?*

[P91]
Li Feng bit down on his lips and performed a military salute.

[P92]
“…Greetings, Deputy Military Commissioner.”

[P93]
The Deputy Military Commissioner was a second-rank official, with only two such posts in each province.

[P94]
Aside from the Military Commissioner, the supreme military commander, and Prince Shangshan, the City Lord, it was the highest position in the province. As deputy commander, he also wielded tremendous authority.

[P95]
That was what the public knew. In truth, the man before him possessed even greater power.

[P96]
*That bastard deserves to be beaten to death.*

[P97]
A sycophant and corrupt official who used his glib tongue and petty tricks to blind the young prince’s eyes and ears while lining his own pockets. That was Li Feng’s assessment of him.

[P98]
But even under Li Feng’s hostile gaze, the man’s smile never faltered.

[P99]
“Assistant Commissioner Li, it’s been a while. Isn’t the atmosphere a little too tense? Did I perhaps do something to offend you?”

[P100]
“…Of course not. I was merely surprised to find you in a place like this, Deputy Military Commissioner.”

[P101]
“A place like this?”

[P102]
“It is a gathering of martial artists from the martial world. They are rather rough people, so I was concerned that you might be uncomfortable, Deputy Military Commissioner.”

[P103]
His words sounded considerate, but both men knew what he truly meant.

[P104]
“Why would I? I like places like this. Besides, you’ve been awfully formal with my title. Just call me whatever you like. We’re close enough, aren’t we?”

[P105]
“And what sort of relationship do we have?”

[P106]
“The kind where we’d split even a single bean. True and loyal subjects who serve His Highness with all our hearts.”

[P107]
*Split a bean? True and loyal subjects?*

[P108]
Li Feng asked bluntly, “Then may I call you Eunuch Hong?”

[P109]
Eunuch Hong’s smile stiffened for a moment.

[P110]
With that single word, Li Feng had touched his sore spot.

[P111]
“That’s… a little too familiar, don’t you think?”

[P112]
“I only followed your instructions.”

[P113]
“Well, this is a surprise. I had no idea Assistant Commissioner Li considered me that close.”

[P114]
“I’m overwhelmed that you finally understand how I feel.”

[P115]
“Assistant Commissioner Li.”

[P116]
“Did you call, Eunuch Hong? Or would you prefer that I go back to calling you Deputy Military Commissioner?”

[P117]
A heavy silence settled over the hall.

[P118]
It was a long while before Eunuch Hong spoke again.

[P119]
“Our Assistant Commissioner Li has improved quite a bit, hasn’t he?”

[P120]
“Have I?”

[P121]
“Yes. Compared to a few years ago, you’ve made remarkable progress.”

[P122]
“I’ve learned many things thanks to you.”

[P123]
“I thought you were only good with a sword, but now I see you’re good with your tongue, too. I’ll have to look at you differently.”

[P124]
“I’m still nowhere near as skilled as a certain someone.”

[P125]
Their gazes collided in midair. Amid the taut silence, Eunuch Hong smiled gently.

[P126]
“Well, we can talk about that later… May I ask you one thing?”

[P127]
His opponent was no pushover, but he had taken a step back. If Li Feng kept biting at him, he would only put himself at a disadvantage. He silently nodded.

[P128]
“Ask.”

[P129]
“You said you used to belong to Huashan, didn’t you?”

[P130]
Li Feng paused. Huashan was a place he both missed and remembered with pain.

[P131]
It had been nearly ten years since he had left Mount Hua, but the memories of that time still remained deep in his body and heart.

[P132]
“Yes. I was a lay disciple.”

[P133]
“And Huashan is in Shaanxi?”

[P134]
He and Eunuch Hong were what one might call political enemies. For that very reason, they knew one another inside and out.

[P135]
Eunuch Hong was neither careless nor stupid enough to ask about such a basic fact without a reason.

[P136]
If anything, he was a crafty bastard with a hundred snakes writhing inside him.

[P137]
That only made Li Feng more puzzled.

[P138]
“That’s right. But why are you suddenly asking?”

[P139]
“I’ve come to know a few people recently, and I wondered if you might know them, too.”

[P140]
“Are they martial artists?”

[P141]
“Yes. From Shaanxi, no less.”

[P142]
“Don’t tell me they’re from Huashan…?”

[P143]
“Oh, come on. If they were, I would have told you already.”

[P144]
Li Feng sighed in relief.

[P145]
In the end, he had left of his own accord, but Huashan was still the sect he would be proud of for the rest of his life. It was a tremendous relief that Huashan had not become entangled with a sycophant like Eunuch Hong.

[P146]
“There are more than one or two sects in Shaanxi. And I didn’t go outside while training at the main sect, so even if I heard their names, I might not recognize them.”

[P147]
“Is that so? Then perhaps you would recognize them if you saw their faces?”

[P148]
“…?”

[P149]
At the sight of Li Feng’s expression, Eunuch Hong picked up the chopsticks lying on the table.

[P150]
“You asked earlier why I was here, didn’t you?”

[P151]
The beautifully crafted silver chopsticks tapped against a wine cup.

[P152]
*Ping.*

[P153]
The clear sound spread through the hall.

[P154]
Eunuch Hong smiled with his eyes at the bewildered Li Feng.

[P155]
“I invited a few acquaintances. Famous and powerful martial artists whom His Highness would enjoy meeting.”

[P156]
At that moment, a powerful shout rang out from beyond the iron gate.

[P157]
“The Three Hands of Zhongnan request an audience!”

[P158]
“The Three Hands of Zhongnan… The Zhongnan Sect!”

[P159]
Li Feng’s complexion changed drastically.

[P160]
Huashan and the Zhongnan Sect had been bitter rivals fighting for supremacy in Shaanxi for a full hundred years.

[P161]
Eunuch Hong’s intentions were every bit as clear as the smile on his face.

[P162]
“They’re fellow Shaanxi men, so I thought I’d arrange a gathering. You don’t mind, do you?”

[P163]
Just as Li Feng clenched his fists, the massive iron gate opened and three imposing men strode into the hall.

[P164]
One of them had a familiar face.

[P165]
“Well, well. If it isn’t Li Feng of Huashan?”

[P166]
Li Feng shuddered. The moment he saw that man’s face, the humiliating memory from ten years ago came rushing back.

[P167]
“How did you get here?”

[P168]
The sharp-eyed man answered casually.

[P169]
“How else? When the Deputy Military Commissioner of Shanxi Province invites you, you have to come running even if it’s a thousand li away. Isn’t that right?”

[P170]
“You’re too kind. I’m the one grateful that you accepted the invitation.”

[P171]
Li Feng ground his teeth. Gong Ilhyuk, the third of the Three Hands of Zhongnan, grinned at him.

[P172]
“Anyway, you’ve done well for yourself. Assistant Military Commissioner, someone like you… Huashan must have spread around quite a few silver nyang for you. Hmm?”

[P173]
“How dare you insult Huashan?”

[P174]
“Insult Huashan? You’re the one who insulted it. Ten years ago, who was it that fell to his knees after only a hundred or so exchanges with that magnificent Huashan martial arts?”

[P175]
“You bastard!”

[P176]
A thunderous shout burst from Li Feng’s mouth.

[P177]
At the moment he glared at Gong Ilhyuk with eyes that seemed to pour out streams of flame, a third shout rang out from beyond the iron gate.

[P178]
“The young prodigies of Shanxi Murim request an audience!”
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
# Chapter 138

[P2]
The luxurious six-horse carriage raced onward without slowing.

[P3]
Soldiers who looked like elite troops cleared the road ahead, while the people who had been swarming around like ants split neatly to either side and watched the carriage dash past like the wind.

[P4]
“So this is how Moses felt.”

[P5]
Cheongpung reacted to my mutter.

[P6]
“Moses? Who is that?”

[P7]
“Someone.”

[P8]
“Oh, I see.”

[P9]
If it had been Hyuk Mujin, he would have complained for ages about me saying something strange, but Cheongpung was different.

[P10]
He had the excited expression of a child at an amusement park as he pressed and tapped every part of the carriage.

[P11]
“This is my first time riding in a six-horse carriage!”

[P12]
“…What about a four-horse carriage?”

[P13]
“I’ve never ridden in one of those, either!”

[P14]
“What about an ordinary carriage…?”

[P15]
“I’d like to ride in one of those, too!”

[P16]
“…”

[P17]
If I put him on a subway, he would probably faint.

[P18]
At this point, it would be much faster to count the things he had done than the things he had never done.

[P19]
I stared at Cheongpung, who had entered a state of total excitement.

[P20]
*What the hell is this guy?*

[P21]
Was he innocent or stupid?

[P22]
Then again, he had said he had lived his entire life in the mountains. Maybe this was only natural.

[P23]
*At least he’s easy to handle.*

[P24]
I still couldn’t forget the expression he had just made. His eyes had lit up like high beams at the mere mention of the imperial family.

[P25]
*“Have you ever seen a member of the imperial family?”*

[P26]
*“I want to! I’ll see one! Please let me see one!”*

[P27]
What filled his eyes wasn’t the sort of admiration ordinary commoners felt toward the imperial family. If I had to compare it to something, it was more like the excitement of going to see an elephant at the zoo.

[P28]
*He really is a strange one.*

[P29]
Apparently, I wasn’t the only one who thought so.

[P30]
The young prodigies of the Five Gates of Shanxi, excluding the severely injured Woo Jintae, were staring at Cheongpung as if they were looking at something bizarre.

[P31]
“Is he really all right…?”

[P32]
“Can we really go like this?”

[P33]
“If he says something inappropriate in front of His Highness, we might get dragged into it, too.”

[P34]
“It’ll be lucky if it ends with him saying something inappropriate. If he gets excited about seeing an imperial family member for the first time and pulls on his ear, we’re finished. Completely finished.”

[P35]
…That was a surprisingly plausible prediction.

[P36]
Hearing the young prodigies whispering, the official riding in the carriage with us leaned over and spoke in an anxious voice.

[P37]
“Um, Young Master Jin.”

[P38]
“Yes?”

[P39]
“That person… Is he really all right?”

[P40]
“Believe me. He’s a master I can vouch for.”

[P41]
“To hell with whether he’s a master. I’m asking whether he’s right in the head.”

[P42]
“Oh.”

[P43]
“Wouldn’t it be better to bring along the martial artist who was with you instead?”

[P44]
“Who? Ah, Hyuk Mujin?”

[P45]
“I believe that was his name. I hear he’s also quite skilled in martial arts.”

[P46]
If Mujin had heard that, he would have jumped for joy.

[P47]
The problem was that he had a dark blue bruise on his face from getting beaten by me that morning, so there was no way he could come along.

[P48]
*And Hyuk Mujin wouldn’t be enough.*

[P49]
To avoid offending the young prince, I needed to bring a more impressive gift.

[P50]
I firmly shook my head at the worried official.

[P51]
“Don’t worry. I’ll take responsibility for making sure nothing happens.”

[P52]
Who was I? A direct descendant of the prestigious Jin Family of Taiyuan, a rising star, and Shanxi Murim’s newest sensation.

[P53]
My bold assurance brightened the official’s expression a little.

[P54]
“Then I’ll trust Young Master Jin—”

[P55]
*Crack.*

[P56]
“…?”

[P57]
“…?”

[P58]
Wait a second. What was that sound?

[P59]
As though we had made a pact, we all turned our heads at the same time.

[P60]
There was Cheongpung, clutching something in his hands.

[P61]
“Huh? Why did this fall off?”

[P62]
The official stared at me in silence for a long moment as Cheongpung grinned foolishly while holding an exquisitely crafted golden dragon.

[P63]
“Young Master Jin.”

[P64]
“Yes?”

[P65]
“Is he really all right?”

[P66]
After thinking it over, I opened my mouth.

[P67]
“Probably.”

[P68]
* * *

[P69]
The space was so vast that it could have been called a castle rather than a residence. A man strode through it without hesitation.

[P70]
Everyone who saw his tightly pressed lips and resolute gaze respectfully paid their respects.

[P71]
“Greetings, Assistant Military Commissioner.”

[P72]
He acknowledged them with a nod and quickened his pace.

[P73]
After passing through a corridor lined with endless pillars, how long had he been walking? The man finally stopped when a massive iron gate engraved with a dragon appeared before him.

[P74]
“Announce me.”

[P75]
“Yes, sir.”

[P76]
A commander from the palace guard saluted him and called out in a powerful voice.

[P77]
“His Excellency Li Feng, Assistant Military Commissioner of Shanxi Province, entering!”

[P78]
Before long, a voice answered from within.

[P79]
“Let him enter.”

[P80]
“…”

[P81]
The voice was neither as high and childish as a little boy’s nor as deep as a grown man’s.

[P82]
At the moment the man—Li Feng—seemed to realize something and his eyebrows shot up, the iron gate opened with a heavy groan.

[P83]
*Grrrnnng.*

[P84]
Beyond it was an extravagantly decorated grand hall. Gold and silver treasures glittered in every direction, and a table large enough for dozens of people was covered with every delicacy from land and sea.

[P85]
It was a sight that would have left anyone else gaping. But Li Feng’s gaze remained fixed on a single point.

[P86]
*How is he here?*

[P87]
At the end of Li Feng’s gaze, a man seated at the head of the table smiled faintly.

[P88]
Wrapped in dazzling red silk, the man spoke in a coy, lilting voice.

[P89]
“Well, well. If it isn’t our Assistant Commissioner Li.”

[P90]
*Our Assistant Commissioner Li?*

[P91]
Li Feng bit down on his lips and performed a military salute.

[P92]
“…Greetings, Deputy Military Commissioner.”

[P93]
The Deputy Military Commissioner was a second-rank official, with only two such posts in each province.

[P94]
Aside from the Military Commissioner, who was the commander-in-chief, and the City Lord, Prince Shangshan, it was the highest position there was. As the deputy commander, he also wielded tremendous authority.

[P95]
That was what people knew publicly. In truth, the man before him possessed even greater power.

[P96]
*That bastard deserves to be beaten to death.*

[P97]
A sycophant and corrupt official who used his glib tongue and petty tricks to blind the young prince’s eyes and ears while lining his own pockets. That was Li Feng’s assessment of him.

[P98]
But even beneath Li Feng’s openly hostile gaze, the man continued smiling.

[P99]
“Assistant Commissioner Li, it’s been a while. Isn’t the atmosphere a little too tense? Did I perhaps do something to offend you?”

[P100]
“…Of course not. I was merely surprised to find you in a place like this, Deputy Military Commissioner.”

[P101]
“A place like this?”

[P102]
“It is a gathering of martial artists from the martial world. They are rather rough people, so I was concerned that you might be uncomfortable, Deputy Military Commissioner.”

[P103]
His words sounded considerate, but their true meaning was different. Neither man was unaware of that.

[P104]
“What’s the problem? I like places like this. Besides, you’ve been so stiff with your title since a while ago. Just call me whatever you like. We’re close enough, aren’t we?”

[P105]
“Close enough for what, exactly?”

[P106]
“We’re the kind of people who would split a bean between us. True loyal subjects who serve His Highness with all our hearts.”

[P107]
*Split a bean between us? True loyal subjects?*

[P108]
Li Feng asked bluntly,

[P109]
“Then may I call you Eunuch Hong?”

[P110]
The smile on Eunuch Hong’s face stiffened for a moment.

[P111]
With a single word, Li Feng had touched his sore spot.

[P112]
“That’s… a little too familiar, don’t you think?”

[P113]
“I only followed your instructions.”

[P114]
“Well, this is something. I didn’t realize Assistant Commissioner Li considered me that close.”

[P115]
“I’m overwhelmed that you understand my feelings at last.”

[P116]
“Assistant Commissioner Li.”

[P117]
“Did you call, Eunuch Hong? Or should I go back to calling you Deputy Military Commissioner?”

[P118]
A heavy silence settled over the hall.

[P119]
It was a long while before Eunuch Hong opened his mouth again.

[P120]
“Our Assistant Commissioner Li has improved quite a bit, hasn’t he?”

[P121]
“Have I?”

[P122]
“Yes. Compared to a few years ago, you’ve made remarkable progress.”

[P123]
“I’ve learned many things thanks to you.”

[P124]
“I thought you were only good with a sword, but now I see you’re good with your tongue, too. I’ll have to look at you differently.”

[P125]
“I’m still nowhere near as skilled as someone else.”

[P126]
Their gazes collided in midair. Within the tightly stretched silence, Eunuch Hong smiled gently.

[P127]
“Well, we can talk about that later… May I ask you one thing?”

[P128]
His opponent was no pushover, but he had taken a step back. If he kept biting at him, he would only end up at a disadvantage. Li Feng silently nodded.

[P129]
“Ask.”

[P130]
“You said you used to belong to Huashan, didn’t you?”

[P131]
Li Feng paused. Huashan was a place he both missed and remembered with pain.

[P132]
It had been nearly ten years since he had left Mount Hua, but the memories of that time still remained deep in his body and heart.

[P133]
“Yes. I was a lay disciple.”

[P134]
“And Huashan is in Shaanxi?”

[P135]
He and Eunuch Hong were what one might call political enemies. For that very reason, they knew one another inside and out.

[P136]
Eunuch Hong was neither careless nor stupid enough to ask about such a basic fact without a reason.

[P137]
If anything, he was a crafty man with a hundred snakes writhing inside him.

[P138]
That was why Li Feng was even more puzzled.

[P139]
“That’s right. But why are you suddenly asking?”

[P140]
“I’ve come to know a few people recently, and I wondered if you might know them, too.”

[P141]
“Are they martial artists?”

[P142]
“Yes. And they’re from Shaanxi.”

[P143]
“Don’t tell me they’re from Huashan…?”

[P144]
“Oh, come on. If they were, I would have told you already.”

[P145]
Li Feng let out a sigh of relief.

[P146]
In the end, he had left of his own accord, but Huashan was still the sect he would be proud of for the rest of his life. It was a tremendous relief that he had not been entangled with a sycophant like Eunuch Hong.

[P147]
“There are more than one or two sects in Shaanxi. And I didn’t go outside while training at the main sect, so even if I heard their names, I might not recognize them.”

[P148]
“Is that so? Then perhaps you would recognize them if you saw their faces?”

[P149]
“…?”

[P150]
Seeing Li Feng’s expression, Eunuch Hong picked up the chopsticks lying on the table.

[P151]
“You asked earlier why I was here, didn’t you?”

[P152]
The beautifully crafted silver chopsticks tapped against a wine cup.

[P153]
*Ping.*

[P154]
The clear sound spread through the hall.

[P155]
Eunuch Hong gave the bewildered Li Feng a knowing smile.

[P156]
“I invited a few acquaintances. Famous and powerful martial artists whom His Highness would enjoy meeting.”

[P157]
At that moment, a powerful shout rang out from beyond the iron gate.

[P158]
“The Three Hands of Zhongnan request an audience!”

[P159]
“The Three Hands of Zhongnan… The Zhongnan Sect!”

[P160]
Li Feng’s complexion changed drastically.

[P161]
Huashan and the Zhongnan Sect had been bitter rivals fighting for supremacy in Shaanxi for a full hundred years.

[P162]
Eunuch Hong’s intentions were every bit as clear as the smile on his face.

[P163]
“They’re from Shaanxi, so I thought I’d arrange a gathering. Isn’t that nice?”

[P164]
Just as Li Feng clenched his fists, the massive iron gate opened and three imposing men strode into the hall.

[P165]
One of them had a familiar face.

[P166]
“Well, well. If it isn’t Li Feng of Huashan?”

[P167]
Li Feng’s body trembled. The moment he saw that man’s face, the humiliating memory from ten years ago came rushing back.

[P168]
“How did you get here?”

[P169]
The sharp-eyed man answered casually.

[P170]
“How did I get here? When the Deputy Military Commissioner of Shanxi Province invites you, you have to come running even if it’s a thousand li away. Isn’t that right?”

[P171]
“There’s no need to thank me. I’m the one grateful that you accepted the invitation.”

[P172]
*Grind.*

[P173]
Gong Ilhyuk, the third of the Three Hands of Zhongnan, grinned at Li Feng as he ground his teeth.

[P174]
“Anyway, you’ve done well for yourself. Assistant Military Commissioner, someone like you… Huashan must have spread around quite a bit of silver for you. Hmm?”

[P175]
“How dare you insult Huashan?”

[P176]
“Insult Huashan? You’re the one who insulted it. Ten years ago, who was it that knelt after a little over a hundred exchanges against that magnificent Huashan martial arts?”

[P177]
“You bastard!”

[P178]
A thunderous shout burst from Li Feng’s mouth.

[P179]
At the moment he glared at Gong Ilhyuk with eyes that seemed to pour out streams of flame, a third shout rang out from beyond the iron gate.

[P180]
“The young prodigies of Shanxi Murim request an audience!”
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 공일혁    | **Gong Ilhyuk**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 산서오문   | **Five Gates of Shanxi**         |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 도지휘사 | **Military Commissioner** | Provincial military commander's office |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |
| 은자 | **silver nyang** | Silver currency unit. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 138,
  "passed": true,
  "metrics": {
    "source_characters": 5494,
    "translation_characters": 12298,
    "length_ratio": 2.238,
    "source_paragraphs": 176,
    "translation_paragraphs": 178
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "후기지수",
        "preferred": "young prodigy / rising martial artist"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "상태",
        "preferred": "Status"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "명성",
        "preferred": "Fame"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "중상",
        "preferred": "Severe Injury"
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
        "korean": "내관",
        "preferred": "palace attendant"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "세가",
        "preferred": "great family"
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
