# Fidelity Gate — Chapter 115

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
  1|＃115화
  2|
  3|
  4|
  5|항산호 철무백.
  6|
  7|이미 몇 번 들어 본 이름이다. 월화는 그가 없었다면 항산검문은 진작 적풍단에게 멸문당했을 거라고 했다.
  8|
  9|
 10|
 11|‘혈랑검 이천백과 비견되거나 그 이상이라고 평가받는 절정 고수예요.’
 12|
 13|
 14|
 15|분명히 그랬었는데.
 16|
 17|‘그 대단한 절정 고수가 왜 이 꼴이 되어 있나.’
 18|
 19|기이한 방향으로 꺾여 있는 사지, 상의를 흠뻑 적신 검은 핏물은 심각한 내상의 증거다. 철무백이 흐릿한 눈빛으로 우리를 바라보았다.
 20|
 21|“태원……진가?”
 22|
 23|“어, 알아보시네?”
 24|
 25|나는 억지로 입꼬리를 끌어 올렸다. 위중한 상태인 철무백을 조금이라도 안심시키기 위해서다.
 26|
 27|지금 내 눈앞에 있는 그는 쟁쟁한 위명의 절정 고수가 아닌, 마지막 희망을 발견한 노인에 지나지 않았다.
 28|
 29|“적풍단, 안에, 소월이가 위험…….”
 30|
 31|힘겹게 이어 가는 철무백의 말을 듣지 않았어도 이 자리의 모두는 사태의 심각성을 알고 있다. 시선이 닿는 곳마다 시체와 핏물이 넘쳐 났으니까.
 32|
 33|‘하지만 아직 늦지는 않았어.’
 34|
 35|
 36|
 37|제한 시간 : 00:05:12
 38|
 39|
 40|
 41|아슬아슬하게 시간을 맞췄다. 문제는 항산호 철무백을 이 꼴로 만들어 놓은 놈이 저 안에 있다는 사실이지.
 42|
 43|월화도 나와 같은 생각을 한 모양이다. 그녀가 철무백을 진정시키며 물었다.
 44|
 45|“철 대협, 풍양이 다른 고수와 합공을 했나요?”
 46|
 47|철무백이 미약하게 고개를 저었다.
 48|
 49|“풍양이 단신으로 철 대협을 꺾었다는 말씀이세요?”
 50|
 51|“부, 붉은 단환. 놈을 조심…….”
 52|
 53|붉은 단환?
 54|
 55|더 물어보고 싶었지만 철무백의 한계는 거기까지였다. 소리 없이 입을 벙긋거리던 그의 고개가 푹 꺾이자 혁무진이 헛숨을 들이켰다.
 56|
 57|“주, 죽었다.”
 58|
 59|“……아직 살아 있어.”
 60|
 61|“아, 그러네요. 숨결이 너무 미약해서 그만.”
 62|
 63|산 사람마저 죽이는 혁무진 이 새끼는 도대체…….
 64|
 65|그러나 녀석의 말도 아주 틀린 것은 아니다. 철무백의 가느다란 숨결은 언제 끊길지 모를 정도로 위태로웠다.
 66|
 67|월화가 품 안에서 조그마한 자기병을 꺼낸 것은 그때였다.
 68|
 69|“거기 목 좀 들어 주시겠어요?”
 70|
 71|그녀가 기절한 철무백의 입으로 병을 기울였다.
 72|
 73|정체 모를 녹색 액체가 흘러 들어가자 창백했던 안색에 조금씩 핏기가 도는 것이, 상당히 효과가 좋은 약물인 것 같았다.
 74|
 75|“이걸로 한숨 돌릴 순 있겠지만 말 그대로 임시방편이에요. 지금의 철 대협의 상태로는 어린아이도 감당 못 해요, 아시죠?”
 76|
 77|요컨대 누군가는 남아서 만약의 사태로부터 철무백을 지켜야 한다는 뜻이다. 나는 망설임 없이 고개를 끄덕였다.
 78|
 79|“그럼 무진이가…….”
 80|
 81|“두 사람이 남으시오.”
 82|
 83|“응? 두 사람?”
 84|
 85|이게 무슨 소리야. 나와 시선이 마주친 진무경이 뭐 잘못됐냐는 얼굴로 되물었다.
 86|
 87|“왜?”
 88|
 89|“아니, 우리 둘이 가자고?”
 90|
 91|“문제 있나?”
 92|
 93|“…….”
 94|
 95|당연히 있지.
 96|
 97|‘한가락 하는 절정 고수인 철무백을 반송장으로 만든 풍양에, 그 휘하 마적 놈들까지.’
 98|
 99|고양이 손이라도 빌려야 할 판국인데, 뭐?
100|
101|아직 불안한 수준인 혁무진은 몰라도 월화는 데려가야 한다는 게 내 생각이다.
102|
103|“두 분이서 가능하시겠어요?”
104|
105|월화의 물음에 내가 재빨리 입을 열었다.
106|
107|“그거야 당연히…….”
108|
109|“할 수 있소.”
110|
111|불가능하다고 말하려던 찰나, 진무경의 깊고 검은 눈동자가 나를 응시했다.
112|
113|“할 수 있다고 했다. 날 믿어라.”
114|
115|그 담담하면서도 확신에 찬 한마디에 말문이 막혔다.
116|
117|순간 치기 어린 젊은이의 객기인가 하는 생각도 들었지만, 내심 고개를 가로젓고 있는 스스로를 발견했다.
118|
119|‘진천검. 무공의 천재.’
120|
121|눈앞의 이 녀석은 노력과 재능이 결합해 탄생한 괴물이다. 지금까지 지켜본 바로는 스스로 개죽음을 자처할 만큼 어리석지도 않다.
122|
123|그리고…….
124|
125|
126|
127|제한 시간 : 00:02:21
128|
129|
130|
131|젠장, 더 이상 망설일 시간도 없다.
132|
133|나는 한숨을 푹 내쉬고 진무경을 향해 물었다.
134|
135|“자신 있어?”
136|
137|“이게 최선이다. 어중간한 수준으로는 오히려 짐만 될 뿐이야.”
138|
139|진무경의 대답에 월화가 피식 웃었다.
140|
141|“어머, 너무 솔직하신데요?”
142|
143|“……그 부분은 미안하게 생각하오.”
144|
145|“뭐, 괜찮아요. 틀린 말은 아니니까.”
146|
147|저놈이 누구한테 사과하는 건 처음 보네.
148|
149|다시 보기 힘든 이 희귀한 광경에 혁무진이 끼어들었다.
150|
151|“이공자님, 저도 무인입니다!”
152|
153|“그럼 따라오거라. 단, 살아남는 건 알아서 하고.”
154|
155|“알아서…… 말입니까?”
156|
157|“장담하건대, 싸움이 시작되면 적들은 너부터 노릴 것이다. 무인답게 장렬히 싸우다 죽는 것도 나쁘지 않겠지.”
158|
159|잠깐 침묵하던 혁무진이 결의에 찬 얼굴로 대답했다.
160|
161|“무인으로서, 같은 무도(武道)를 걷는 철 대협을 안전하게 모시고 있겠습니다.”
162|
163|“…….”
164|
165|가끔 보면 저게 사람인가 싶다.
166|
167|‘시간만 있으면 두들겨 패는 건데.’
168|
169|하지만 이 와중에도 시간은 계속해서 흐르고 있었다.
170|
171|
172|
173|제한 시간 : 00:01:09
174|
175|
176|
177|“후우.”
178|
179|미리 꺼내어 둔 창을 단단히 말아 쥐며 진무경에게 말을 건넸다.
180|
181|“내가 조무래기들을 맡을게.”
182|
183|“보통 이런 시점에서는 스스로 우두머리를 맡겠다고 하지 않나?”
184|
185|“응, 그런 고정 관념을 버려.”
186|
187|“웃기는 놈이군.”
188|
189|“분수를 안다고 해 두자.”
190|
191|“투지와 호승심은 무인을 성장시킨다.”
192|
193|“그리고 죽음을 촉진시키겠지. 상대를 봐 가면서 덤비는 건 배웠으니까 그 넘치는 투지와 호승심으로 풍양 좀 처리해 줘.”
194|
195|“말은 청산유수로구나.”
196|
197|“아, 그리고 들어가면 최대한 은밀히 접근한 다음 내가 신호하면 기습하고. 알았지?”
198|
199|“기습?”
200|
201|“기습의 묘리를 살려서 초반에 최대한 큰 피해를 입히고 시작하는 거지. 적들이 우왕좌왕하는 사이에 항산검문주를…….”
202|
203|“그렇군.”
204|
205|“좋아, 오랜만에 말이 통하네.”
206|
207|이걸로 모든 준비는 끝났다. 40초, 39초, 38초.
208|
209|떨어지는 숫자를 보며 문을 향해 걸음을 떼려던 찰나였다.
210|
211|저벅.
212|
213|말리고 자시고 할 시간도 없었다.
214|
215|성큼 안으로 걸어 들어간 진무경이 공력을 실은 외침을 토해 냈다.
216|
217|“풍양-!”
218|
219|띠링.
220|
221|
222|
223|- [제한 시간]이 사라집니다.
224|
225|
226|
227|“…….”
228|
229|진무경 이 개새끼야.
230|
231|
232|
233|* * *
234|
235|
236|
237|“혼인? 차라리 죽음을 택하겠다.”
238|
239|자기 자신의 목에 은장도를 뽑아 겨눈 이소월을 보며 풍양은 혀를 찼다.
240|
241|“어지간히 애먹이는군. 혈랑검의 여식다워.”
242|
243|뛰어난 비도술의 소유자인 풍양이지만 현재로서는 그의 장기를 십분 발휘할 수 없었다.
244|
245|‘망할 노인네…… 결국 잠력단(暫力丹)을 쓰게 만들다니.’
246|
247|풍양에게도 고작 세 개밖에 없는 귀물이다. 그중 하나를 쓴 덕분에 철무백을 쓰러트릴 수 있었지만 후유증이 제법 컸다.
248|
249|그는 사시나무처럼 떨리는 손을 소매 아래로 감추며 말했다.
250|
251|“숨이 붙어 있는 놈들을 모두 끌고 와.”
252|
253|“옛.”
254|
255|명령이 떨어지고 얼마 되지 않아 곧장 포박당한 채 끌려오는 항산검문의 무인들. 이소월의 얼굴에 어둠이 내려앉았다.
256|
257|“무슨 짓을 할 셈이냐?”
258|
259|풍양이 빙긋 웃었다.
260|
261|“대충 짐작하고 있을 텐데? 우선 소저가 보는 앞에서 저들의 사지를 하나씩 자를 거요. 팔, 다리, 뭐 이것저것. 썩 유쾌한 광경은 아니니 눈을 감고 있는 걸 추천하지.”
262|
263|“그런 짓을 했다간…….”
264|
265|“자결하겠다면 말리지는 않겠소. 충성심 깊은 수하들은 그 대가로 도륙을 당하겠지만.”
266|
267|이소월이 이를 악물었다.
268|
269|“당신이 원하는 게 그건 아닐 텐데?”
270|
271|“혼인 상대가 죽어 버리겠다는데 어쩔 수 없지. 그래도 혈랑검의 독문무공과 항산호의 무공 구결 정도면 충분히, 아. 돌아가는 길에 철무백 그 노인네도 데려가야겠군.”
272|
273|“……철 숙부가, 아직 살아 계신다고?”
274|
275|“당연한 소리를. 귀한 무공 구결을 넘겨줄 은인을 그렇게 쉽게 죽일 수야 있나.”
276|
277|“…….”
278|
279|“내 목을 걸고 하나 약속하지. 지금이라도 늦지 않았으니 나와 혼인하시오. 하면 단전을 폐하는 선에서 모두 살려 주리다.”
280|
281|그게 결정타였다. 한동안 속눈썹을 파르르 떨던 이소월이 천천히 손을 내렸다.
282|
283|“약속은 지켜라.”
284|
285|“좋은 선택이오.”
286|
287|풍양의 얼굴에 득의양양한 웃음이 어렸다.
288|
289|오늘부로 그는 세 번째 인생을 살게 됐다.
290|
291|거지 소년에서 마적. 마적에서 비로소 정파의 탈을 뒤집어쓰고 항산검문의 실질적인 주인이 됐다.
292|
293|비록 큰 피해를 입었지만 상관없다. 새 술은 새 부대에 담는 법. 항산검문의 이름으로 무인들을 모집하고 세력을 키워 나갈 것이다.
294|
295|‘삼십여 년 전 혈랑검도 했던 일을 내가 못 하랴.’
296|
297|넘치는 희열에 입꼬리가 솟구친 그 순간이었다.
298|
299|“풍양-!”
300|
301|공력이 담긴 외침이 천지를 뒤흔들었다.
302|
303|이소월과 풍양. 그리고 살아남은 모든 이들이 약속이라도 한 듯이 고개를 틀었다.
304|
305|밤처럼 새카만 흑의(黑衣)를 걸친 청년이 오십여 장 밖에서 걸어오고 있었다.
306|
307|‘고수.’
308|
309|풍양은 청년의 송곳 같은 눈빛에 가슴 한구석이 서늘해졌다.
310|
311|고수다. 그것도 자신과 비교해 결코 떨어지지 않는 절정 고수. 검파를 잡아 가는 손놀림만 봐도 알 수 있었다.
312|
313|‘이 정도로 젊은 절정 고수는 산서성에 둘뿐이지. 특히 검수(劍手)라면…….’
314|
315|답은 바로 나왔다. 진천검 진무경. 불과 약관의 나이에 절정의 경지에 오른 천재.
316|
317|무엇보다 그의 뒤에는 산서제일가로 우뚝 선 태원진가가 버티고 있다.
318|
319|‘그나마 혼자 왔으니 다행이군.’
320|
321|그러나 다음 순간, 진무경이 들어온 성문에서 또 다른 한 사람이 슬쩍 고개를 내밀었다.
322|
323|청년은 남색 무복을 입고 있었다. 복식, 손에 든 묵색 철창, 무엇보다 진무경과 빼다 박은 얼굴이 그가 누구인지를 알려 주었다.
324|
325|“산서잠룡?”
326|
327|누군가의 입에서 튀어나온 별호에 진태경이 움찔하더니 중얼거렸다.
328|
329|“시발, 내 이렇게 될 줄 알았다.”
330|
331|명문가 자제답지 않은 걸쭉한 욕설과 함께 휘적휘적 걸어오는 진태경, 느긋한 걸음걸이의 진무경.
332|
333|두 형제의 발걸음이 향하는 쪽에 풍양이 있었다.
334|
335|‘하필 이럴 때 태원진가라…… 매우 좋지 않아.’
336|
337|오랜 세월 가문이 쌓아 올린 평판과 팔천협 전투로 얻은 명성. 현재 태원진가의 위상은 독보적이었다.
338|
339|그 덕분에 산서성 전역에서 수많은 젊은이가 무인을 꿈꾸며 앞다투어 태원진가로 몰려드는 중이다.
340|
341|그것이 당장 풍양이 항산검문을 삼키더라도 넙죽 엎드린 채 발톱을 숨겨야 하는 이유였다.
342|
343|‘이번 고비만 넘기면 기회는 온다.’
344|
345|이미 항산검문은 무너졌다. 무림은 약육강식의 세계고 풍양은 새로운 강자다. 그는 상대가 태원진가라 해도 자신이 충분히 존중받을 만한 자격을 갖췄다고 생각했다.
346|
347|저벅, 저벅, 저벅.
348|
349|진무경, 진태경 형제가 발걸음을 옮길 때마다 적풍단의 마적들이 분분히 물러섰다.
350|
351|풍양은 어느새 코앞까지 다가온 두 사람을 향해 포권을 취했다.
352|
353|“적풍단주, 풍양이라 하오.”
354|
355|풍양이 그 어느 때라도 경계심을 늦추지 않는 노련한 무림인이 아니었다면, 아직 잠력단의 효능이 미약하게 남아 있지 않았더라면 그 일격을 피하지 못했을 것이다.
356|
357|쉬이이잉-!
358|
359|그는 황급히 몸을 뒤집었다. 목을 스쳐 간 눈부신 검기(劍氣) 한 줄기가 뒤에 있던 마적 셋을 베어 냈다.
360|
361|“이게 태원진가의 뜻이냐!”
362|
363|풍양의 노호성에 이미 가까이 있는 마적들을 쓰러트린 진태경이 중얼거렸다.
364|
365|“난 말로 하고 싶은데.”
366|
367|“이런 개호로…….”
368|
369|쉬이이익! 서걱!
370|
371|말을 끝마치기도 전에 날아온 검기가 풍양의 등을 훑었다. 불에 덴 듯한 통증. 간신히 이어지는 공격을 피한 그는 진무경에 대한 평가를 수정해야 했다.
372|
373|‘나보다 더 강하다.’
374|
375|이 정도라면 철무백에게 비견될 만한 움직임이다. 거기에 더해 수하들을 학살하고 있는 진태경까지.
376|
377|풍양은 자신에게 남은 선택지가 하나밖에 없음을 깨달았다.
378|
379|‘잠력단.’
380|
381|그는 품속에 감춰 뒀던 목곽을 꺼냈다. 진무경을 막기 위해 수하들이 죽어 나가는 사이, 단환을 입 안에 털어 넣었다.
382|
383|쉬이이익!
384|
385|어느새 핏빛으로 물든 풍양의 눈동자에 진무경의 푸른 검기가 비쳤다.
386|
387|서걱!
```

## Assembled English

```markdown
[P1]
# Chapter 115

[P2]
Cheol Mubaek, the Tiger of Mount Heng.

[P3]
I had heard that name several times already. Wolhwa had said that without him, the Mount Heng Sword Sect would have been wiped out by the Red Wind Band long ago.

[P4]
*“He’s considered a Peak master comparable to or even stronger than the Blood Wolf Sword, Lee Cheonbaek.”*

[P5]
She had definitely said that.

[P6]
*Then why has such an incredible Peak master ended up like this?*

[P7]
His limbs were bent at unnatural angles, and the black blood soaking his shirt was proof of severe internal injuries. Cheol Mubaek looked at us through hazy eyes.

[P8]
“Taiyuan… Jin Family?”

[P9]
“Oh, you recognize us?”

[P10]
I forced a smile, hoping to reassure the critically wounded Cheol Mubaek, if only a little.

[P11]
The man before me was no longer a renowned Peak master of formidable reputation. He was nothing more than an old man who had found his last hope.

[P12]
“Red Wind Band… inside… Seowol’s in danger…”

[P13]
Even without hearing Cheol Mubaek’s halting words, everyone here understood how serious the situation was. Everywhere we looked, there were corpses and pools of blood.

[P14]
*But it’s not too late yet.*

[P15]
> **System**  
> **Time Limit:** 00:05:12

[P16]
We had made it just in time. The problem was that the bastard who had reduced the Tiger of Mount Heng to this state was still inside.

[P17]
Wolhwa seemed to be thinking the same thing. She calmed Cheol Mubaek as she asked,

[P18]
“Sir Cheol, did Pung Yang join forces with another master to attack you?”

[P19]
Cheol Mubaek weakly shook his head.

[P20]
“You’re saying Pung Yang defeated you by himself?”

[P21]
“R-red pill. Be careful of that bastard…”

[P22]
A red pill?

[P23]
I wanted to ask more, but Cheol Mubaek had reached his limit. His lips moved soundlessly before his head slumped forward. Hyuk Mujin sucked in a startled breath.

[P24]
“H-he’s dead.”

[P25]
“…He’s still alive.”

[P26]
“Oh. So he is. His breathing was so faint that I…”

[P27]
Hyuk Mujin, you bastard. What kind of person kills even the living?

[P28]
Still, he wasn’t entirely wrong. Cheol Mubaek’s thin breath was so precarious that it could stop at any moment.

[P29]
That was when Wolhwa pulled a small porcelain bottle from inside her robes.

[P30]
“Could you lift his head a little?”

[P31]
She tipped the bottle into the unconscious Cheol Mubaek’s mouth.

[P32]
As an unidentified green liquid trickled down his throat, color gradually returned to his pale face. It seemed to be a remarkably effective medicine.

[P33]
“This will help him catch his breath, but it’s only a temporary measure. In his current condition, he couldn’t even handle a child. You understand, right?”

[P34]
In short, someone had to stay behind to protect Cheol Mubaek in case something happened. I nodded without hesitation.

[P35]
“Then Mujin can—”

[P36]
“Two people stay behind.”

[P37]
“Huh? Two people?”

[P38]
What was he talking about? Jin Mukyung met my gaze, looking as though he couldn’t see what the problem was.

[P39]
“Why?”

[P40]
“No, you mean just the two of us should go?”

[P41]
“Is there a problem?”

[P42]
…

[P43]
Of course there was.

[P44]
*Pung Yang turned a formidable Peak master like Cheol Mubaek into a half-dead wreck, and he still has all those mounted-bandit bastards under his command.*

[P45]
We needed every hand we could get, and he was suggesting this?

[P46]
I didn’t know about Hyuk Mujin, whose abilities were still questionable, but Wolhwa absolutely had to come with us.

[P47]
“Can the two of you manage?” Wolhwa asked.

[P48]
I hurriedly opened my mouth.

[P49]
“Obviously, that’s—”

[P50]
“We can.”

[P51]
Just as I was about to say it was impossible, Jin Mukyung fixed his deep, dark eyes on me.

[P52]
“I said we can. Trust me.”

[P53]
His calm yet confident words left me speechless.

[P54]
For a moment, I wondered if this was merely the reckless bravado of an immature young man. But then I realized I was shaking my head inwardly.

[P55]
*The Heaven Shaking Sword. A martial arts genius.*

[P56]
The guy standing before me was a monster born from the combination of effort and talent. From everything I had seen, he wasn’t foolish enough to throw his life away for nothing.

[P57]
And…

[P58]
> **System**  
> **Time Limit:** 00:02:21

[P59]
Damn it. There was no time left to hesitate.

[P60]
I let out a deep sigh and asked Jin Mukyung,

[P61]
“Are you confident?”

[P62]
“This is the best option. Anyone of middling skill would only become a burden.”

[P63]
Wolhwa let out a quiet laugh.

[P64]
“My, you’re awfully honest.”

[P65]
“…I apologize for that.”

[P66]
“Well, that’s all right. You’re not wrong.”

[P67]
That was the first time I had ever seen him apologize to anyone.

[P68]
Hyuk Mujin interrupted this rare spectacle.

[P69]
“Second Young Master, I’m a martial artist too!”

[P70]
“Then follow us. But you’ll be responsible for staying alive.”

[P71]
“On my own…?”

[P72]
“I guarantee that once the fighting begins, the enemy will target you first. There’s nothing wrong with fighting bravely as a martial artist and dying.”

[P73]
After a brief silence, Hyuk Mujin answered with a resolute expression.

[P74]
“As a martial artist, I will remain here and safely protect Sir Cheol, who walks the same martial path as I do.”

[P75]
…

[P76]
Sometimes I wondered if that guy was even human.

[P77]
*If I had the time, I’d beat the hell out of him.*

[P78]
But even now, time continued to pass.

[P79]
> **System**  
> **Time Limit:** 00:01:09

[P80]
“Whew.”

[P81]
I tightened my grip on the spear I had already taken out and spoke to Jin Mukyung.

[P82]
“I’ll handle the small fry.”

[P83]
“Usually, at a time like this, aren’t you supposed to volunteer to take the leader?”

[P84]
“Yeah. Throw away that stereotype.”

[P85]
“You’re ridiculous.”

[P86]
“Let’s just say I know my place.”

[P87]
“Fighting spirit and competitive pride help a martial artist grow.”

[P88]
“And hasten his death. I’ve learned to pick my opponents carefully, so use all that overflowing fighting spirit and competitive pride to deal with Pung Yang.”

[P89]
“You certainly have a way with words.”

[P90]
“Oh, and when we get inside, approach as quietly as possible. Then ambush them when I give the signal. Got it?”

[P91]
“Ambush?”

[P92]
“Use the essence of an ambush to inflict as much damage as possible at the beginning. While the enemies are thrown into confusion, we’ll get to the Sect Leader of the Mount Heng Sword Sect…”

[P93]
“I see.”

[P94]
“Good. It’s nice to be understood for once.”

[P95]
That took care of the preparations. Forty seconds. Thirty-nine. Thirty-eight.

[P96]
I watched the numbers fall and was about to head for the gate when—

[P97]
Clomp.

[P98]
There wasn’t even time to stop him.

[P99]
Jin Mukyung strode inside and unleashed a shout infused with internal energy.

[P100]
“Pung Yang!”

[P101]
> **System**  
> **Time Limit** has disappeared.

[P102]
…

[P103]
Jin Mukyung, you fucking asshole.

[P104]
* * *

[P105]
“Marriage? I’d rather die.”

[P106]
Pung Yang clicked his tongue as he watched Lee Seowol draw a silver dagger and hold it to her own throat.

[P107]
“You’re making this awfully difficult. You really are the Blood Wolf Sword’s daughter.”

[P108]
Though Pung Yang was highly skilled with throwing knives, he couldn’t make full use of his specialty in his current condition.

[P109]
*Damn old man… He actually forced me to use a Temporary Strength Pill.*

[P110]
Even Pung Yang possessed only three of these precious pills. Using one had allowed him to defeat Cheol Mubaek, but the aftereffects were considerable.

[P111]
He hid his hands, trembling like aspen leaves, beneath his sleeves and said,

[P112]
“Bring everyone who’s still breathing.”

[P113]
“Yes, Leader.”

[P114]
Not long after the order was given, martial artists from the Mount Heng Sword Sect were dragged over, bound hand and foot. Darkness settled over Lee Seowol’s face.

[P115]
“What are you planning to do?”

[P116]
Pung Yang smiled.

[P117]
“You can probably guess. First, I’ll cut off their limbs one by one in front of you. Arms, legs, this and that. It won’t be a pleasant sight, so I recommend closing your eyes.”

[P118]
“If you do that…”

[P119]
“If you intend to kill yourself, I won’t stop you. Your loyal subordinates will be slaughtered in return, though.”

[P120]
Lee Seowol clenched her teeth.

[P121]
“That isn’t what you want, is it?”

[P122]
“If my bride-to-be says she’s going to die, what else can I do? Still, the Blood Wolf Sword’s secret martial art and the Tiger of Mount Heng’s martial arts formula would be enough. Ah, I should take that old man Cheol with me on the way back, too.”

[P123]
“…Uncle Cheol is still alive?”

[P124]
“Of course. How could I kill a Benefactor who’s going to hand over such a precious martial arts formula?”

[P125]
“…”

[P126]
“I’ll stake my life on this promise. It’s not too late even now, so marry me. If you do, I’ll let everyone live. I’ll stop at destroying their dantians.”

[P127]
That was the decisive blow.

[P128]
Lee Seowol’s eyelashes trembled for a while before she slowly lowered her hand.

[P129]
“Keep your promise.”

[P130]
“A wise choice.”

[P131]
A triumphant smile spread across Pung Yang’s face.

[P132]
As of today, he would begin his third life.

[P133]
He had gone from a beggar boy to a mounted bandit. Now he would finally don the mask of the orthodox faction and become the true master of the Mount Heng Sword Sect.

[P134]
Though there had been heavy losses, it didn’t matter. New wine belonged in new wineskins. Under the name of the Mount Heng Sword Sect, he would recruit martial artists and expand his power.

[P135]
*If the Blood Wolf Sword could do it thirty years ago, why can’t I?*

[P136]
Just as the corners of his mouth lifted with overflowing delight—

[P137]
“Pung Yang!”

[P138]
A shout infused with internal energy shook heaven and earth.

[P139]
Lee Seowol, Pung Yang, and every survivor turned their heads as if on cue.

[P140]
A young man dressed in robes as black as night was walking toward them from some fifty *jang* away.[^1]

[P141]
*A master.*

[P142]
The young man’s needle-sharp gaze sent a chill through a corner of Pung Yang’s chest.

[P143]
He was a master. More than that, he was a Peak master in no way inferior to Pung Yang himself. Pung Yang could tell just from the way the young man’s hand moved as it gripped his sword hilt.

[P144]
*There are only two Peak masters this young in Shanxi Province. And if he’s a swordsman…*

[P145]
The answer came immediately.

[P146]
Jin Mukyung, the Heaven Shaking Sword. A genius who had reached the Peak realm at barely twenty years of age.

[P147]
More importantly, behind him stood the Jin Family of Taiyuan, which had risen to become the foremost family in Shanxi.

[P148]
*At least he came alone.*

[P149]
But the next moment, another person cautiously stuck his head out through the fortress gate Jin Mukyung had entered.

[P150]
The young man wore a navy martial robe. His clothing, the dark iron spear in his hand, and above all, his nearly identical face told Pung Yang who he was.

[P151]
“The Sleeping Dragon of Shanxi?”

[P152]
Jin Taekyung flinched at the nickname someone blurted out and muttered, “Fuck. I knew this would happen.”

[P153]
Cursing crudely in a manner unbecoming a scion of a prestigious family, Jin Taekyung came sauntering forward beside the leisurely Jin Mukyung.

[P154]
The two brothers were heading straight toward Pung Yang.

[P155]
*The Taiyuan Jin Family, at a time like this… This is very bad.*

[P156]
The reputation the family had built over many years, combined with the fame it had earned in the battle at Eight Spring Gorge, had left the Jin Family’s current standing unrivaled.

[P157]
As a result, countless young people across Shanxi Province who dreamed of becoming martial artists were flocking to the Jin Family.

[P158]
That was why, even if Pung Yang swallowed the Mount Heng Sword Sect right now, he would still have to bow flat and hide his claws.

[P159]
*Once I get past this hurdle, my opportunity will come.*

[P160]
The Mount Heng Sword Sect had already collapsed. The Murim was a world where the strong preyed on the weak, and Pung Yang was a new power in that world. Even if his opponent was the Taiyuan Jin Family, he believed he had earned the right to be treated with respect.

[P161]
Clomp. Clomp. Clomp.

[P162]
With every step Jin Mukyung and Jin Taekyung took, the Red Wind Band’s mounted bandits scattered out of their way.

[P163]
When the brothers reached him, Pung Yang clasped his hands in salute.

[P164]
“I am Pung Yang, Red Wind Band Leader.”

[P165]
Had Pung Yang not been a seasoned martial artist who never let down his guard—had the effects of the Temporary Strength Pill not still lingered faintly—he would never have evaded that strike.

[P166]
Shiiiiing!

[P167]
He hurriedly twisted aside.

[P168]
A dazzling streak of Sword Energy skimmed past his neck and sliced through three mounted bandits behind him.

[P169]
“Is this the will of the Taiyuan Jin Family?”

[P170]
Jin Taekyung, who had already felled the nearby mounted bandits, muttered, “I’d rather talk it out.”

[P171]
“You fucking bast—”

[P172]
Before Pung Yang could finish speaking, another streak of Sword Energy flew in and grazed his back.

[P173]
Pain seared through him like fire. He barely evaded the attacks that followed and revised his assessment of Jin Mukyung.

[P174]
*He’s stronger than me.*

[P175]
At this level, Jin Mukyung’s movements were comparable to Cheol Mubaek’s. On top of that, Jin Taekyung was slaughtering Pung Yang’s subordinates.

[P176]
Pung Yang realized he had only one option left.

[P177]
*The Temporary Strength Pill.*

[P178]
While his subordinates died one after another trying to stop Jin Mukyung, Pung Yang pulled the wooden case hidden inside his robes and tipped the pill into his mouth.

[P179]
Shiiiiing!

[P180]
Jin Mukyung’s blue Sword Energy was reflected in Pung Yang’s eyes, which had turned blood-red.

[P181]
Slice!

[P182]
[^1]: A *jang* is a traditional unit of distance, roughly three meters.
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
# Chapter 115

[P2]
Cheol Mubaek, the Tiger of Mount Heng.

[P3]
I had heard that name several times already. Wolhwa had said that without him, the Mount Heng Sword Sect would have been wiped out by the Red Wind Band long ago.

[P4]
*“He’s considered a Peak master comparable to or even stronger than the Blood Wolf Sword, Lee Cheonbaek.”*

[P5]
She had definitely said that.

[P6]
*Then why has that incredible Peak master ended up like this?*

[P7]
His limbs were twisted at unnatural angles, and the black blood soaking his shirt was proof of severe internal injuries. Cheol Mubaek looked at us through hazy eyes.

[P8]
“Taiyuan… Jin Family?”

[P9]
“Oh, you recognize us?”

[P10]
I forced the corners of my mouth upward. I wanted to reassure Cheol Mubaek, who was in critical condition, even if only a little.

[P11]
The man before me was no longer the renowned Peak master known throughout the Murim. He was nothing more than an old man who had found his last hope.

[P12]
“Red Wind Band… inside… Seowol’s in danger…”

[P13]
Even without hearing Cheol Mubaek’s halting words, everyone here understood how serious the situation was. Everywhere we looked, there were corpses and pools of blood.

[P14]
*But it’s not too late yet.*

[P15]
> **System**  
> **Time Limit:** 00:05:12

[P16]
We had made it just in time. The problem was that the bastard who had reduced the Tiger of Mount Heng to this state was still inside.

[P17]
Wolhwa seemed to have reached the same conclusion. She calmed Cheol Mubaek and asked,

[P18]
“Sir Cheol, did Pung Yang attack you together with another master?”

[P19]
Cheol Mubaek gave a faint shake of his head.

[P20]
“You’re saying Pung Yang defeated Sir Cheol by himself?”

[P21]
“R-red pill. Be careful of that bastard…”

[P22]
A red pill?

[P23]
I wanted to ask more, but that was the limit of Cheol Mubaek’s strength. His lips moved soundlessly, then his head drooped. Hyuk Mujin sucked in a startled breath.

[P24]
“H-he’s dead.”

[P25]
“…He’s still alive.”

[P26]
“Oh. So he is. His breathing was just so faint…”

[P27]
Hyuk Mujin, you bastard. What kind of person kills even the living?

[P28]
Still, he wasn’t entirely wrong. Cheol Mubaek’s thin breath was so precarious that it could stop at any moment.

[P29]
That was when Wolhwa pulled a small porcelain bottle from inside her robes.

[P30]
“Could you lift his head a little?”

[P31]
She tilted the bottle into the unconscious Cheol Mubaek’s mouth.

[P32]
As an unidentified green liquid trickled down his throat, color gradually returned to his pale face. It seemed to be a remarkably effective medicine.

[P33]
“This will help him catch his breath, but it’s only a temporary measure. In his current condition, even a child would be too much for him to handle. You understand, right?”

[P34]
In short, someone had to stay behind to protect Cheol Mubaek in case something happened. I nodded without hesitation.

[P35]
“Then Mujin can—”

[P36]
“Two people stay behind.”

[P37]
“Huh? Two people?”

[P38]
What was he talking about? Jin Mukyung met my gaze and looked back at me as if he couldn’t understand what the problem was.

[P39]
“Why?”

[P40]
“No, you mean the two of us should go?”

[P41]
“Is there a problem?”

[P42]
…

[P43]
Of course there was.

[P44]
*Pung Yang had turned a formidable Peak master like Cheol Mubaek into a half-dead man, and he still had all those mounted-bandit bastards under his command.*

[P45]
We were at the point where we needed every hand we could get, and he was suggesting this?

[P46]
I didn’t know about Hyuk Mujin, whose abilities were still questionable, but Wolhwa absolutely had to come with us.

[P47]
“Can the two of you manage?” Wolhwa asked.

[P48]
I hurriedly opened my mouth.

[P49]
“Obviously, that’s—”

[P50]
“We can.”

[P51]
Just as I was about to say it was impossible, Jin Mukyung’s deep, dark eyes fixed on me.

[P52]
“I said we can. Trust me.”

[P53]
His calm yet confident words left me speechless.

[P54]
For a moment, I wondered if this was merely the reckless bravado of an immature young man. But then I realized I was shaking my head inwardly.

[P55]
*The Heaven Shaking Sword. A martial arts genius.*

[P56]
The guy standing before me was a monster born from the combination of effort and talent. From everything I had seen, he wasn’t foolish enough to throw his life away for nothing.

[P57]
And then…

[P58]
> **System**  
> **Time Limit:** 00:02:21

[P59]
Damn it. There was no time left to hesitate.

[P60]
I let out a deep sigh and asked Jin Mukyung,

[P61]
“Are you confident?”

[P62]
“This is the best option. Someone of middling skill would only become a burden.”

[P63]
Wolhwa let out a quiet laugh.

[P64]
“My, you’re awfully honest.”

[P65]
“…I apologize for that.”

[P66]
“Well, that’s all right. You’re not wrong.”

[P67]
That was the first time I had ever seen him apologize to anyone.

[P68]
Hyuk Mujin interrupted this rare spectacle.

[P69]
“Second Young Master, I’m a martial artist too!”

[P70]
“Then follow us. But staying alive is your responsibility.”

[P71]
“On my own…?”

[P72]
“I guarantee that once the fighting begins, the enemy will target you first. There’s nothing wrong with fighting bravely as a martial artist and dying.”

[P73]
After a brief silence, Hyuk Mujin answered with a resolute expression.

[P74]
“As a martial artist, I will safely protect Sir Cheol, who walks the same path of martial arts as I do.”

[P75]
…

[P76]
Sometimes, I wondered if that guy was even human.

[P77]
*If I had the time, I’d beat the hell out of him.*

[P78]
But even now, time continued to pass.

[P79]
> **System**  
> **Time Limit:** 00:01:09

[P80]
“Whew.”

[P81]
I gripped the spear I had already taken out and spoke to Jin Mukyung.

[P82]
“I’ll handle the small fry.”

[P83]
“Usually, at a time like this, shouldn’t you say that you’ll take the leader?”

[P84]
“Yeah. Throw away that stereotype.”

[P85]
“You’re ridiculous.”

[P86]
“Let’s just say I know my place.”

[P87]
“Fighting spirit and competitive pride help a martial artist grow.”

[P88]
“And hasten his death. I’ve learned to choose my opponents carefully, so deal with Pung Yang using all that overflowing fighting spirit and competitive pride.”

[P89]
“You certainly have a way with words.”

[P90]
“Oh, and when we get inside, approach as quietly as possible. Then ambush them when I give the signal. Got it?”

[P91]
“Ambush?”

[P92]
“Use the essence of an ambush to inflict as much damage as possible at the beginning. While the enemies are thrown into confusion, we’ll get to the Sect Leader of the Mount Heng Sword Sect…”

[P93]
“I see.”

[P94]
“Good. It’s nice to be understood for once.”

[P95]
That took care of every preparation. Forty seconds. Thirty-nine. Thirty-eight.

[P96]
I watched the numbers fall and was just about to walk toward the door when—

[P97]
Clomp.

[P98]
There wasn’t even time to stop him.

[P99]
Jin Mukyung strode inside and let out a shout infused with internal energy.

[P100]
“Pung Yang!”

[P101]
> **System**  
> **Time Limit** has disappeared.

[P102]
…

[P103]
Jin Mukyung, you fucking asshole.

[P104]
* * *

[P105]
“Marriage? I’d choose death instead.”

[P106]
Pung Yang clicked his tongue as he watched Lee Seowol draw a silver dagger and hold it to her own throat.

[P107]
“You’re making this awfully difficult. You really are the Blood Wolf Sword’s daughter.”

[P108]
Though Pung Yang was a master of throwing knives, he couldn’t fully display his specialty in his current condition.

[P109]
*Damn old man… He actually forced me to use the Temporary Strength Pill.[^1]*

[P110]
Even Pung Yang possessed only three of these precious pills. Using one had allowed him to defeat Cheol Mubaek, but the aftereffects were considerable.

[P111]
He hid his hands, trembling like aspen leaves, beneath his sleeves and said,

[P112]
“Bring everyone who’s still breathing.”

[P113]
“Yes, Leader.”

[P114]
Not long after the order was given, martial artists from the Mount Heng Sword Sect were dragged over, bound hand and foot. Darkness settled over Lee Seowol’s face.

[P115]
“What are you planning to do?”

[P116]
Pung Yang smiled.

[P117]
“You can probably guess. First, I’ll cut off their limbs one by one in front of you. Arms, legs, this and that. It won’t be a pleasant sight, so I recommend closing your eyes.”

[P118]
“If you do that…”

[P119]
“If you’re going to kill yourself, I won’t stop you. But your loyal subordinates will be slaughtered for it.”

[P120]
Lee Seowol clenched her teeth.

[P121]
“That isn’t what you want, is it?”

[P122]
“If my bride-to-be says she’s going to die, what else can I do? Still, the Blood Wolf Sword’s secret martial art and the Tiger of Mount Heng’s martial arts formula would be enough. Ah, I should take that old man Cheol with me on the way back, too.”

[P123]
“…Uncle Cheol is still alive?”

[P124]
“Of course. How could I kill a Benefactor who is going to hand over such a precious martial arts formula?”

[P125]
“…”

[P126]
“I’ll stake my life on this promise. It’s not too late even now, so marry me. If you do, I’ll let everyone live. I’ll stop at destroying their dantians.”

[P127]
That was the decisive blow.

[P128]
Lee Seowol’s eyelashes trembled for a while before she slowly lowered her hand.

[P129]
“Keep your promise.”

[P130]
“A wise choice.”

[P131]
A triumphant smile spread across Pung Yang’s face.

[P132]
From this day forward, he would begin his third life.

[P133]
He had gone from a beggar boy to a mounted bandit. Now, he would finally don the mask of an orthodox faction and become the true master of the Mount Heng Sword Sect.

[P134]
Though there had been heavy losses, it didn’t matter. New wine belonged in new wineskins. Under the name of the Mount Heng Sword Sect, he would recruit martial artists and expand his power.

[P135]
*If the Blood Wolf Sword could do the same thing over thirty years ago, why couldn’t I?*

[P136]
Just as the corners of his mouth lifted with overflowing delight—

[P137]
“Pung Yang!”

[P138]
A shout infused with internal energy shook the heavens and earth.

[P139]
Lee Seowol, Pung Yang, and every surviving person turned their heads as if they had made a pact.

[P140]
A young man dressed in black as dark as night was walking toward them from some fifty jang away.[^2]

[P141]
*A master.*

[P142]
A chill ran through some corner of Pung Yang’s chest beneath the young man’s needle-sharp gaze.

[P143]
He was a master. And not merely a master—he was a Peak master who was in no way inferior to Pung Yang himself. Pung Yang could tell just from the way the young man’s hand moved as it gripped his sword hilt.

[P144]
*There are only two Peak masters this young in Shanxi. And if one of them is a swordsman…*

[P145]
The answer came immediately.

[P146]
Jin Mukyung, the Heaven Shaking Sword. A genius who had reached the Peak realm while still in his early twenties.

[P147]
More importantly, behind him stood the Jin Family of Taiyuan, which had risen to become the foremost family in Shanxi.

[P148]
*At least he came alone.*

[P149]
But the next moment, another person cautiously stuck his head out through the fortress gate Jin Mukyung had entered.

[P150]
The young man wore a navy martial robe. His clothing, the dark iron spear in his hand, and above all, his nearly identical face told Pung Yang who he was.

[P151]
“The Sleeping Dragon of Shanxi?”

[P152]
At the nickname that escaped someone’s mouth, Jin Taekyung flinched and muttered,

[P153]
“Fuck. I knew this would happen.”

[P154]
Jin Taekyung came sauntering forward, cursing crudely in a manner unbecoming a scion of a prestigious family, while Jin Mukyung followed at an easy pace.

[P155]
The two brothers were heading straight toward Pung Yang.

[P156]
*The Taiyuan Jin Family, at a time like this… This is very bad.*

[P157]
The family’s reputation, built over many years, and the fame it had gained through the battle at Eight Spring Gorge had made the Jin Family’s current standing unrivaled.

[P158]
Because of that, countless young people across Shanxi who dreamed of becoming martial artists were flocking to the Jin Family.

[P159]
That was why, even if Pung Yang swallowed the Mount Heng Sword Sect right now, he would still have to bow flat and hide his claws.

[P160]
*Once I get past this hurdle, my opportunity will come.*

[P161]
The Mount Heng Sword Sect had already collapsed. The Murim was a world where the strong preyed on the weak, and Pung Yang was a new power in that world. Even if his opponent was the Taiyuan Jin Family, he believed he had earned the right to be treated with respect.

[P162]
Clomp. Clomp. Clomp.

[P163]
Each time Jin Mukyung and Jin Taekyung took a step, the mounted bandits of the Red Wind Band retreated in confusion.

[P164]
By the time the two men reached him, Pung Yang raised his hands in a formal salute.

[P165]
“I am Pung Yang, Red Wind Band Leader.”

[P166]
If Pung Yang had not been a seasoned martial artist who never lowered his guard, or if the effects of the Temporary Strength Pill had not still lingered faintly, he would never have avoided that strike.

[P167]
Shiiiiing!

[P168]
He hurriedly twisted his body.

[P169]
A dazzling streak of Sword Energy skimmed past his neck and sliced through three mounted bandits behind him.

[P170]
“Is this the will of the Taiyuan Jin Family?”

[P171]
Jin Taekyung, who had already felled the mounted bandits nearby, muttered,

[P172]
“I’d rather talk it out.”

[P173]
“You fucking bast—”

[P174]
Before Pung Yang could finish speaking, another streak of Sword Energy flew in and grazed his back.

[P175]
The pain felt like being burned by fire.

[P176]
He barely avoided the continuing attack, and his assessment of Jin Mukyung had to change.

[P177]
*He’s stronger than me.*

[P178]
At this level, Jin Mukyung’s movements were comparable to Cheol Mubaek’s. On top of that, Jin Taekyung was slaughtering Pung Yang’s subordinates.

[P179]
Pung Yang realized that he had only one option left.

[P180]
*The Temporary Strength Pill.*

[P181]
While his subordinates died one after another trying to stop Jin Mukyung, Pung Yang pulled the wooden case hidden inside his robes and tipped the pill into his mouth.

[P182]
Shiiiiing!

[P183]
Jin Mukyung’s blue Sword Energy was reflected in Pung Yang’s eyes, which had turned blood-red.

[P184]
Slice!

[P185]
[^1]: The pill’s name literally means “Temporary Strength Pill.”

[P186]
[^2]: A jang is a traditional unit of distance, roughly three meters.
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
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 정파     | **orthodox faction**                             |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 은인     | **Benefactor**                               |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 팔천협    | **Eight Spring Gorge** |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 115,
  "passed": true,
  "metrics": {
    "source_characters": 5742,
    "translation_characters": 12962,
    "length_ratio": 2.257,
    "source_paragraphs": 181,
    "translation_paragraphs": 182
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "일격",
        "preferred": "One Strike"
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
        "korean": "대협",
        "preferred": "Great Hero or Sir depending tone"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "소저",
        "preferred": "Young Lady"
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
        "korean": "전하",
        "preferred": "His Highness"
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
