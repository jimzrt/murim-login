# Fidelity Gate — Chapter 37

Audit the complete assembled English chapter against the Korean source.
Report only genuine source-fidelity defects: wrong action, subject, object,
causality, quantity, mechanism, terminology, ambiguity, joke logic, register,
or physical detail. Check repeated UI labels and counters against how they
behave across the whole scene. Interpret idioms by their function, not by
translating their component words. Do not report optional stylistic rewrites.

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
  1|＃37화
  2|
  3|
  4|
  5|이동은 순조로웠다. 지난번 정찰 임무 때 내린 폭설은 녹아 없어진 지 오래였고 지휘부는 병력의 힘을 최대한 비축시키며 이동했다.
  6|
  7|“지금 속도라면 늦어도 내일 정양(定壤)에 도착하겠군요.”
  8|
  9|어쩐지 낯익은 남자의 말에 나는 눈을 껌뻑거렸다.
 10|
 11|“누구신지?”
 12|
 13|복색을 보아하니 태원진가 쪽 사람은 아니다. 내가 있는 후미에는 정찰조원들을 제외하면 새로 합류한 중소 문파의 무사들이 대다수였으니 당연했다.
 14|
 15|“삼도문의 곽준이라 합니다. 일전에 한 번 인사를 드렸었는데…… 손도 잡았었죠.”
 16|
 17|삼도문의 곽준? 기억이 날 듯 말 듯 한데.
 18|
 19|명성치 올리려고 잡은 손이 한 둘이냐. 아마 그들 중 하나였겠지.
 20|
 21|“죄송합니다. 제가 기억력이 좀 안 좋아서.”
 22|
 23|“사실 기대도 안 했습니다. 하하.”
 24|
 25|친근한 웃음을 지어 보인 곽준이 재차 입을 열었다
 26|
 27|“사실 처음에는 후미에 배치되었다는 사실에 실망했습니다.”
 28|
 29|“왜요?”
 30|
 31|“공을 세울 기회가 적어지니까요. 저 같은 무명 소졸이 이름을 알릴 기회 아니겠습니까?”
 32|
 33|“아, 예.”
 34|
 35|이런 경우는 둘 중 하나다. 정말 많은 전투를 겪어서 강심장이 됐거나, 겁이 없는 놈이거나. 나는 [기감]을 끌어올렸다.
 36|
 37|띠링.
 38|
 39|
 40|
 41|[Lv.40 곽준]
 42|
 43|
 44|
 45|오, 한가락 하는데?
 46|
 47|40레벨이면 최소 일류다. 나 고수라고 큰소리 뻥뻥 치지는 못해도 후미에만 처박혀 있는 게 억울할 정도는 된다.
 48|
 49|“적들의 병력 중 절반은 급하게 충원된 자들입니다. 별의별 쭉정이들까지 끌어들인 데다 본대에 합류하기 위해 강행군을 했을 테니 태원진가와 삼도문의 정예들에게는 상대도 안 되겠지요.”
 50|
 51|말은 제법 그럴듯하다. 삼도문이 정예라는 걸 빼면.
 52|
 53|나는 건성으로 고개를 끄덕였다.
 54|
 55|“그렇군요.”
 56|
 57|“적들보다 뛰어난 절정 고수들도 있지요. 소가주님과 위 대협도 계시지만 화양검(火魎檢)의 무명은 중원 전체에 퍼져 있지 않습니까.”
 58|
 59|화양검. 처음 듣는 별호였지만 누군지 짐작할 수 있었다.
 60|
 61|태원진가의 절정 고수는 셋이고 진위경과 위팽을 제외한다면 남는 건 한 사람뿐이니까.
 62|
 63|‘대장로.’
 64|
 65|그 노인네가 그 정도였나?
 66|
 67|이어지는 곽준의 말은 찬양 일색이었다. 수십 년 전, 젊은 시절의 대장로가 베어 넘긴 고수들의 별호와 이름이 수도 없이 흘러나왔다.
 68|
 69|“정마대전이 낳은 영웅이셨죠.”
 70|
 71|과거의 전쟁 영웅이라. 곽준의 말만 들어 보면 정의를 사랑하고 불의를 보면 못 참는 협객 중의 협객인데…….
 72|
 73|‘난 왜 볼 때마다 찝찝할까.’
 74|
 75|첫인상 때문인지 몰라도 나는 대장로가 싫었다.
 76|
 77|특유의 분위기와 상대방을 뚫어 보는 묘한 눈빛. 진위경에 맞서 정치적 파벌을 이루고 있다는 것까지.
 78|
 79|하지만 그 후로 대장로는 진위경을 전폭적으로 지지해 주었고, 태원진가는 안팎으로 똘똘 뭉칠 수 있었다.
 80|
 81|‘하긴, 외적이 침입하면 집안싸움도 멈춰야지.’
 82|
 83|현재 대장로는 진위경과 함께 선두를 이끌고 있다. 그가 소문만큼의 고수라면 내일의 전투가 한층 수월해질 것이다.
 84|
 85|“내일 화양검 대협께서 전장을 휩쓸 모습을 생각하니 벌써부터 가슴이 뛰는군요.”
 86|
 87|곽준은 사흘 만에 소변본 사람처럼 몸을 부르르 떨었다.
 88|
 89|이 자식은 긴장감이란 걸 모르나? 더군다나 우리가 이길 거라는 자신감은 어디서 나온 건지 모르겠다.
 90|
 91|“승리를 확신하시는군요.”
 92|
 93|“지면 큰일이죠.”
 94|
 95|“예?”
 96|
 97|큰일이 아니라 끝장나는 거 아니냐. 항산검문이 지금까지 해 왔던 짓을 보면 태원진가는 물론이고 우리 쪽에 가담한 중소 문파들까지 쑥대밭으로 만들 것 같은데.
 98|
 99|“그게 무슨…….”
100|
101|“농담입니다.”
102|
103|이 자식도 또라이네. 어이없어하는 내게 곽준이 씩 웃어 보였다.
104|
105|“이깁니다. 우리가.”
106|
107|확신에 찬 한마디였다.
108|
109|곽준이 그 말을 끝으로 멀어지자 혁무진이 다가와 물었다.
110|
111|“누굽니까?”
112|
113|“40레벨.”
114|
115|“예?”
116|
117|“있어. 자신감 넘치는 놈이.”
118|
119|여러모로 마음에 안 드는 놈이다. 뭐, 이제 대화를 나눌 일도 없겠지만.
120|
121|
122|
123|* * *
124|
125|
126|
127|시간은 빠르게 흘렀다. 진군을 시작한 지 이틀째 되는 밤, 우리는 혼주에 도착했고 진위경은 지휘부를 모아 회의를 열었다. 그의 손에는 작은 종이가 쥐어져 있었다.
128|
129|“하오문에서 보낸 전서요. 이틀 전 적들의 원군이 오태산을 넘었다는군.”
130|
131|“그렇다면…….”
132|
133|“지금쯤, 혹은 내일 중에 본대와 합류할 가능성이 높소.”
134|
135|뭐지? 이해할 수가 없다. 원군이 합류하기 전에 본대를 쳤다면 훨씬 수월한 싸움이 됐을 텐데.
136|
137|‘생각해 둔 게 있겠지.’
138|
139|아니나 다를까, 이어지는 진위경의 말이 있었다.
140|
141|“새로 합류한 적들의 원군은 지쳐 있고 식량은 바닥을 드러내고 있소. 내일 우리가 앞서 정양의 유리한 고지를 점하면 항산검문주는 고민할 거요. 물러서느냐. 부딪치느냐.”
142|
143|다음 순간 진위경의 시선이 나를 향했다.
144|
145|“그가 어떤 선택을 할까?”
146|
147|순간 당황했지만 답은 나와 있다. 이제 와서 물러설 위인이었다면 이미 한참 전에 물러났겠지.
148|
149|“부딪칠 것 같은데요.”
150|
151|두 배에 달하는 병력, 절정 고수의 숫자도 밀리지 않는다. 적으로서는 속전속결로 이 싸움을 끝내려 할 것이다.
152|
153|“바로 보았다.”
154|
155|흐뭇하게 웃은 진위경이 탁자에 놓인 지형도를 짚어 나갔다.
156|
157|“적들이 정양으로 진입할 수 있는 길은 네 곳. 허나 식량 사정이 여의찮은 그들은 가장 빠른 길을 선택하겠지.”
158|
159|손가락이 멈춘 곳에는 팔천협(八天峽)이라는 지명이 적혀 있었다. 그때, 조용히 자리를 지키고 있던 대장로가 처음으로 말문을 열었다.
160|
161|“팔천협이라. 항아리 모양에 입구가 좁고 가파른 곳이지. 마적 떼들은 애마를 버려야겠구려.”
162|
163|“목숨도 버리고 가야지요.”
164|
165|“적들도 목숨을 불사하고 싸울 터, 이 정도로는 부족하오.”
166|
167|“협곡 위 절벽에 각궁 백여 자루를 숨겨 두었습니다.”
168|
169|“허어.”
170|
171|막사 안이 술렁였다. 나도 입을 벌리고 진위경을 바라봤다.
172|
173|아니, 도대체 그건 언제 숨겨 뒀대?
174|
175|“혼주에서의 승리 직후였습니다. 수완 좋은 조력자 덕분이지요.”
176|
177|진위경이 나를 똑바로 바라보며 말했다.
178|
179|‘하오문. 월화구나.’
180|
181|보이지 않는 곳에서 끊임없이 도움을 주고 있다. 물론 이 정도까지 큰 그림을 그린 진위경도 대단하다.
182|
183|‘존나 멋있어.’
184|
185|저 인간 분쇄기 같은 덩치에 명석한 두뇌라니. 갑자기 형이라고 부르고 싶어진다.
186|
187|“오오.”
188|
189|“소가주……!”
190|
191|시커먼 사내놈들의 뜨거운 시선에 막사가 후끈 달아오른다.
192|
193|진위경이 묵직한 눈빛으로 좌중을 훑었다.
194|
195|“이제 결착을 냅시다.”
196|
197|이견은 없었다. 가장 먼저 자리에서 일어난 대장로가 진위경을 향해 포권을 취했다.
198|
199|“존명.”
200|
201|그렇게 회의가 끝났다. 막사를 나오는 내 귓가로 익숙한 목소리가 파고들었다.
202|
203|- 어제 했던 말, 잊지 말거라.
204|
205|순간 몸이 굳는다. 하지만 이내 작게 고개를 끄덕여 보였다.
206|
207|그리고 그날 새벽, 태원진가의 무사 삼백과 중소 문파의 지원군 백오십. 도합 사백오십의 병력이 협곡을 향해 떠났다.
208|
209|‘그래도 마지막인데, 인사도 제대로 못 했네.’
210|
211|나는 언덕에 올라 굽이치는 횃불을 하염없이 바라보았다.
212|
213|
214|
215|* * *
216|
217|
218|
219|다음 날 아침, 나를 본 혁무진이 흠칫 놀라며 물러났다.
220|
221|“깜짝이야. 무슨 일이에요?”
222|
223|“뭐가?”
224|
225|“뭐긴요. 얼굴이 산송장 같아요. 안 주무셨어요?”
226|
227|“아냐. 조금 잤어.”
228|
229|거짓말이다. 사실 한숨도 못 잤다. 바위에 틀어 앉아 밤이 새도록 시스템창만 들여다보고 있었다.
230|
231|마침내 코앞으로 다가온 그 순간을 손꼽아 기다리며.
232|
233|
234|
235|명성 500 달성 (497 / 500)
236|
237|
238|
239|숫자 1이 이렇게 소중하게 느껴질 줄이야.
240|
241|나는 부쩍 늙어 버린 목소리로 중얼거렸다.
242|
243|“간다, 간다, 이제 집 간다…….”
244|
245|“이제는 혼잣말까지 하네. 실성했어요?”
246|
247|쯧쯧. 혀를 차던 혁무진이 눈을 동그랗게 떴다.
248|
249|“그건 뭐예요? 못 보던 물건인데.”
250|
251|“이거?”
252|
253|나는 바위에 올려 둔 낡은 서책과 조그마한 함을 차례대로 가리켰다.
254|
255|“하나는 비급. 하나는 영단.”
256|
257|“헉. 진짜요?”
258|
259|반쯤 눈이 튀어나온 녀석에게 힘없이 설명해 주었다.
260|
261|“비급은 초절정 무공이고, 영단은 잘만 흡수하면 반 갑자.”
262|
263|“예?”
264|
265|“그런데 영단 잘못 먹으면 타 죽는다더라. 너 먹을래?”
266|
267|“아, 예에…….”
268|
269|시큰둥한 얼굴과 댓 발 튀어나온 주둥이를 보아하니 내 말을 쥐뿔도 안 믿는 것 같다.
270|
271|하긴, 난데없이 초절정 무공에 반 갑자짜리 파이어볼 영단이라고 하니 장난으로 생각할 만도 하지.
272|
273|“진짜 안 먹어? 좋은 건데.”
274|
275|“어이구, 됐습니다. 초절정 무공 많이 익히시고 영단 꼭꼭 씹어 드십쇼.”
276|
277|“난 이제 이런 거 필요 없어.”
278|
279|“그럼요. 잠룡이신데.”
280|
281|평소 같았으면 뒤통수라도 한 대 후려쳐 줬을 텐데. 지금은 별 느낌 없다.
282|
283|‘이게 말년 병장의 기분인가?’
284|
285|동시에 기분이 이상해졌다. 워낙 많은 일을 겪은 후유증인가? 한 달 남짓인데 일 년은 있었던 것처럼 아련하다.
286|
287|나는 과거의 기억을 더듬어 나갔다.
288|
289|‘처음 홍화루에서 눈을 떴지.’
290|
291|그곳에서 월화를 처음 만났고 이 게임에 갇혔다는 사실을 깨달았다. 그때만 생각하면 지금도 소름이 끼친다.
292|
293|‘진짜 미쳐 버리는 줄 알았는데.’
294|
295|태원진가에 오기로 결심하는 데만 사흘이 걸렸다. 거기서 만난 게 이 녀석, 혁무진이다.
296|
297|빡!
298|
299|“억! 왜 때려요?”
300|
301|“음. 그냥 옛날 생각이 나서.”
302|
303|“옛날 언제요?”
304|
305|“안 돼. 안 알려 줘. 빨리 돌아가.”
306|
307|“무슨 뒷골목 파락호예요? 무공 좀 세다고 이렇게 사람을 핍박해도 되는 겁니까?”
308|
309|혁무진이 길길이 날뛰자 사람들의 시선이 우리를 향해 쏠렸다. 강 건너 불구경하던 정찰조원들까지 끼어들었다.
310|
311|“두 분이서 무슨 얘기 중이에요?”
312|
313|“몰라. 부조장이 잘못했겠지.”
314|
315|“야, 난 아무것도 안 했어!”
316|
317|“무림이잖아. 약한 게 죄야.”
318|
319|“그런데 우리 이러고 있어도 되는 겁니까?”
320|
321|누군가의 말에 순간 침묵이 흘렀다.
322|
323|“그러게. 여기서 대기하는 게 우리 임무긴 한데…….”
324|
325|억지웃음으로 억누르고 있던 긴장과 두려움이 감돈다. 곧 현실로 돌아갈 나조차 진위경의 모습이 어른거려 찝찝한 마당에 이 녀석들이야 오죽하겠나. 내가 해 줄 말은 하나밖에 없다.
326|
327|“난 형님을 믿는다.”
328|
329|형님. 이번만큼은 그 단어에 진심을 실었다. 이곳에서 내게 가장 큰 힘이 되어 주었던 진위경이다. 이렇게라도 찝찝함을 털어 내고 싶었던 것일지도 모르겠다.
330|
331|잠깐 굳어 있던 사람들의 얼굴이 풀렸다.
332|
333|“저희도 마찬가집니다.”
334|
335|혁무진도 슬쩍 끼어들었다.
336|
337|“전 조장을 더 믿습니다.”
338|
339|“와, 부조장 줄 갈아타는 솜씨가 아주.”
340|
341|“이 자식들이. 여기 조장한테 목숨 빚지지 않은 놈 있어?”
342|
343|“에이, 그렇게 말씀하시면 또 할 말이 없죠.”
344|
345|“저도 조장 믿습니다. 사실 전 조장이 망나니 행세할 때도 다 알고 있었어요. 아, 저 사람은 잠룡이구나. 딱 감이 왔죠.”
346|
347|기분이 묘했다. 마른오징어도 짜면 물이 나온다더니, 게임에서 NPC들을 상대로 이런 감정을 느낄 줄이야.
348|
349|‘뭐, 솔직히…… 기분이 나쁘진 않네.’
350|
351|문득 저 산 너머에 있을 진위경이 궁금했다. 전투가 시작됐는지, 시작됐다면 어느 쪽이 이기고 있는지.
352|
353|그리고 그런 생각을 한 것은 나 혼자만이 아니었다.
354|
355|“지금쯤이면 전투가 시작됐겠군요.”
356|
357|삼도문의 곽준이다. 지금까지와는 달리 그는 흑색 무복을 걸치고 있었다.
358|
359|‘저 녀석이 원래 저 옷이었던가?’
360|
361|내 시선에 곽준이 어깨를 으쓱했다.
362|
363|“전 이런 게 좋더라고요. 움직이기에도 편하고, 피 좀 튀어도 티도 안 나고. 자네들도 그렇지?”
364|
365|마지막 질문은 우리를 향한 것이 아니었다. 곽준이 이끄는 삼도문의 무사들. 빠짐없이 흑의로 갈아입은 그들이 과묵하게 고개를 끄덕였다.
366|
367|“그렇다는군요.”
368|
369|만족스럽게 웃은 곽준이 내게 고개를 돌렸다.
370|
371|“자, 이제 저희도 출발해 볼까요?”
372|
373|이 새끼가 지금 뭐라는 거지?
```

## Assembled English

```markdown
[P1]
# Chapter 37

[P2]
The march went smoothly. The heavy snow that had fallen during our last reconnaissance mission had melted away long ago, and command moved us while conserving as much of the troops’ strength as possible.

[P3]
“At this rate, we’ll arrive in Jeongyang by tomorrow at the latest.”

[P4]
I blinked at the oddly familiar man’s words.

[P5]
“And you are?”

[P6]
Judging by his clothes, he wasn’t from the Jin Family of Taiyuan. Aside from the reconnaissance squad, most of the rear guard consisted of martial artists from the newly allied small and mid-sized sects, so that made sense.

[P7]
“I’m Gwak Jun of the Three Paths Sect. We met once before… We even shook hands.”

[P8]
Gwak Jun of the Three Paths Sect? I almost remembered him. Almost.

[P9]
*It wasn’t as if I’d shaken only one or two hands trying to raise my Fame.*

[P10]
He was probably one of them.

[P11]
“Sorry. My memory isn’t very good.”

[P12]
“I wasn’t expecting you to remember, honestly. Haha.”

[P13]
Gwak Jun gave me a friendly smile and went on.

[P14]
“To be honest, I was disappointed at first when I found out we’d been assigned to the rear guard.”

[P15]
“Why?”

[P16]
“Because there’d be fewer chances to distinguish ourselves. Isn’t this the chance for an unknown grunt like me to make a name for himself?”

[P17]
“Ah. Right.”

[P18]
There were two possibilities in cases like this. Either he’d been through so many battles that he’d developed nerves of steel, or he simply had no fear.

[P19]
I raised my **Qi Sense**.

[P20]
Ding.

[P21]
> **System**
>
> **Lv.40 Gwak Jun**

[P22]
*Oh. He’s got some skill.*

[P23]
At Level 40, he was at least First Rate. He couldn’t exactly go around bragging he was a master, but it was more than enough to feel wronged about being stuck in the rear.

[P24]
“Half of the enemy troops were recruited in a hurry. They’ve dragged in every kind of deadweight, and they must have force-marched to join the main force. They won’t stand a chance against the elites of the Jin Family of Taiyuan and the Three Paths Sect.”

[P25]
His words sounded plausible enough.

[P26]
*Except for the part about the Three Paths Sect being elite.*

[P27]
I nodded half-heartedly.

[P28]
“I see.”

[P29]
“And we have Peak masters superior to the enemy’s as well. There’s the Lesser Family Head and Great Hero Wipeng, of course, but the reputation of the Blade of Flowers has spread throughout the Central Plains, hasn’t it?”

[P30]
The Blade of Flowers. It was the first time I’d heard the title, but I could guess who he meant.

[P31]
The Jin Family of Taiyuan had three Peak masters. Exclude Jin Wikyung and Wipeng, and only one person was left.

[P32]
*The Head Elder.*

[P33]
*Was that old man really that strong?*

[P34]
Gwak Jun’s next words were nothing but praise. Title after title, name after name of masters the Head Elder had cut down in his youth, decades ago, came spilling out.

[P35]
“He was a hero born of the Great Faction War.”

[P36]
A war hero from the past. Listening to Gwak Jun, he sounded like a chivalrous hero among chivalrous heroes—a man who loved justice and couldn’t stand to see injustice go unpunished…

[P37]
*Then why do I feel so uneasy every time I see him?*

[P38]
Maybe it was the first impression, but I disliked the Head Elder.

[P39]
That peculiar air of his. The strange gaze that bored straight through people. The fact that he had formed a political faction against Jin Wikyung.

[P40]
And yet after that, the Head Elder had thrown his full support behind Jin Wikyung, and the Jin Family of Taiyuan had been able to pull tight together, inside and out.

[P41]
*Well, when an outside enemy invades, even family feuds have to stop.*

[P42]
The Head Elder was currently leading the vanguard alongside Jin Wikyung. If he really was as skilled as the rumors claimed, tomorrow’s battle would be that much easier.

[P43]
“Just thinking of Great Hero Blade of Flowers sweeping the battlefield tomorrow already has my heart racing.”

[P44]
Gwak Jun shuddered like a man finally taking a piss after holding it for three days.

[P45]
*Does this bastard not know what tension is?*

[P46]
And where was he getting the confidence that we were going to win?

[P47]
“You’re certain of victory.”

[P48]
“If we lose, we’re in big trouble.”

[P49]
“Excuse me?”

[P50]
*Not big trouble. We’d be finished.*

[P51]
Judging by everything the Mount Heng Sword Sect had done so far, they would lay waste not only to the Jin Family of Taiyuan but also to the small and mid-sized sects allied with us.

[P52]
“What do you mean by—”

[P53]
“I’m joking.”

[P54]
*This bastard’s a lunatic too.*

[P55]
As I stared at him, speechless, Gwak Jun flashed me a grin.

[P56]
“We’ll win. We will.”

[P57]
One sentence, packed with conviction.

[P58]
When Gwak Jun left it at that and moved away, Hyuk Mujin came up and asked,

[P59]
“Who was that?”

[P60]
“Level 40.”

[P61]
“What?”

[P62]
“There’s this guy. Overflowing with confidence.”

[P63]
I didn’t like him, in more ways than one.

[P64]
*Well, it wasn’t as though I’d have to talk to him again.*

[P65]
* * *

[P66]
Time passed quickly. On the second night of the march, we reached Honju, and Jin Wikyung gathered the command staff for a meeting. He was holding a small slip of paper.

[P67]
“A dispatch from the Lower District Sect. The enemy reinforcements crossed Mount Otae two days ago.”

[P68]
“Then…”

[P69]
“They’re likely to join the main force around now, or sometime tomorrow.”

[P70]
*What?*

[P71]
I couldn’t understand it. If we had attacked the main force before the reinforcements joined them, the fight would have been much easier.

[P72]
*He must have something in mind.*

[P73]
Sure enough, Jin Wikyung went on.

[P74]
“The enemy reinforcements that just joined them are exhausted, and their food is running out. If we take Jeongyang’s high ground first tomorrow, the Mount Heng Sword Sect Leader will have a choice to make. Fall back, or clash.”

[P75]
The next moment, Jin Wikyung’s gaze shifted to me.

[P76]
“What choice do you think he’ll make?”

[P77]
I was caught off guard, but the answer was already there. If he were the kind of man to fall back at this point, he would have done so long ago.

[P78]
“I think he’ll clash.”

[P79]
Twice our numbers, and they weren’t behind us in Peak masters either. From the enemy’s side, they would want to end this fight as fast as possible.

[P80]
“Exactly.”

[P81]
Jin Wikyung smiled, pleased, and traced a finger across the topographic map on the table.

[P82]
“There are four routes the enemy can take into Jeongyang. But with their food situation as it is, they’ll choose the fastest one.”

[P83]
His finger stopped on a place labeled Eight Spring Gorge. The Head Elder, who had been sitting quietly until then, spoke for the first time.

[P84]
“Eight Spring Gorge. Jar-shaped, with a narrow, steep mouth. The mounted bandits will have to abandon their prized horses.”

[P85]
“They’ll have to abandon their lives too.”

[P86]
“The enemy will fight with their lives on the line as well. This much won’t be enough.”

[P87]
“I’ve hidden about a hundred horn bows on the cliffs above the gorge.”

[P88]
“Hoh.”

[P89]
A stir ran through the tent. I stared at Jin Wikyung with my mouth open.

[P90]
*When the hell did he hide those?*

[P91]
“Right after our victory at Honju. Thanks to a resourceful ally.”

[P92]
Jin Wikyung looked straight at me as he said it.

[P93]
*The Lower District Sect. Wolhwa.*

[P94]
She had been helping us constantly from places we couldn’t see. Of course, Jin Wikyung was impressive too, for drawing a picture this big.

[P95]
*That’s fucking cool.*

[P96]
A build like a human meat grinder, and a sharp mind to go with it. Suddenly I wanted to call him my big brother.

[P97]
“Oh!”

[P98]
“The Lesser Family Head…!”

[P99]
The tent went hot under the burning gazes of those dark, burly men.

[P100]
Jin Wikyung swept a heavy look over everyone assembled.

[P101]
“Let’s settle this.”

[P102]
No one objected. The Head Elder was the first to rise, then gave Jin Wikyung a fist-in-palm salute.

[P103]
“By your command.”

[P104]
That was the end of the meeting. As I left the tent, a familiar voice bored into my ear.

[P105]
—Don’t forget what I told you yesterday.

[P106]
I stiffened for a moment. Then I gave a small nod.

[P107]
And at dawn that day, three hundred martial artists from the Jin Family of Taiyuan and one hundred fifty reinforcements from the small and mid-sized sects—four hundred fifty in all—set out for the gorge.

[P108]
*Still, this was the last time, and I hadn’t even said a proper goodbye.*

[P109]
I climbed a hill and stared endlessly at the winding line of torches.

[P110]
* * *

[P111]
The next morning, Hyuk Mujin flinched when he saw me and stepped back.

[P112]
“You startled me. What’s going on?”

[P113]
“What?”

[P114]
“What do you mean, what? You look like a living corpse. Didn’t you sleep?”

[P115]
“Nah. I slept a little.”

[P116]
That was a lie. I hadn’t slept a wink. I had planted myself on a rock and stared at the System Window all night.

[P117]
Counting down to the moment that had finally come right up to my nose.

[P118]
> **System**
>
> Achieve Fame 500 (497/500)

[P119]
I never thought the number 1 could feel this precious.

[P120]
In a voice that had aged all of a sudden, I muttered,

[P121]
“I’m going, I’m going, going home now…”

[P122]
“Now you’re even talking to yourself. Have you lost your mind?”

[P123]
Hyuk Mujin clicked his tongue, then his eyes went round.

[P124]
“What’s that? I’ve never seen those before.”

[P125]
“This?”

[P126]
I pointed in turn at the old book and the small case sitting on the rock.

[P127]
“One’s a martial arts manual. The other’s an elixir.”

[P128]
“Whoa. Really?”

[P129]
I explained in a drained voice to the guy whose eyes were halfway out of his head.

[P130]
“The manual’s a Supreme Peak martial art, and if you absorb the elixir properly, it’ll give you thirty years of internal energy.”

[P131]
“What?”

[P132]
“But they say if you take the elixir wrong, you’ll burn to death. You want it?”

[P133]
“Uh, right…”

[P134]
Judging by that unimpressed face and the snout sticking out a good five feet, he didn’t believe a damn word I was saying.

[P135]
*Well, if someone suddenly came at me with a Supreme Peak martial art and a thirty-year Fireball elixir, I’d figure it was a joke too.*

[P136]
“You really won’t eat it? It’s good stuff.”

[P137]
“Oh, I’m fine. Learn plenty of that Supreme Peak martial art, and be sure to chew your elixir thoroughly.”

[P138]
“I don’t need this kind of thing anymore.”

[P139]
“Of course. You’re the Sleeping Dragon.”

[P140]
Normally I would have smacked him in the back of the head. Right now I didn’t feel much of anything.

[P141]
*Is this how a short-timer sergeant feels?[^1]*

[P142]
At the same time, I felt strange. Was it the aftereffect of everything I’d been through? It had only been a little over a month, but it felt hazy and distant, as if I’d been here a year.

[P143]
I started tracing back through old memories.

[P144]
*I first opened my eyes at Honghwaru.*

[P145]
That was where I met Wolhwa for the first time and realized I was trapped in this game. Even now, thinking about that moment gave me goose bumps.

[P146]
*I really thought I was going to lose my mind.*

[P147]
It had taken me three days just to decide to go to the Jin Family of Taiyuan. And the guy I met there was this one—Hyuk Mujin.

[P148]
Smack!

[P149]
“Argh! Why did you hit me?”

[P150]
“Hmm. Just thought of the old days.”

[P151]
“What old days?”

[P152]
“Nope. Not telling. Get back already.”

[P153]
“What are you, some back-alley thug? Just because your martial arts are a bit strong, you think you can oppress people like this?”

[P154]
As Hyuk Mujin threw a fit, everyone’s eyes turned toward us. Even the reconnaissance-squad members who had been watching like it was none of their business jumped in.

[P155]
“What are you two talking about?”

[P156]
“Dunno. The deputy squad leader must have done something wrong.”

[P157]
“Hey, I didn’t do anything!”

[P158]
“This is Murim. Being weak is a crime.”

[P159]
“But should we even be doing this?”

[P160]
At someone’s words, silence fell for a moment.

[P161]
“True. Waiting here is our mission, but…”

[P162]
The tension and fear they had been suppressing with forced smiles hung in the air. Even I, who would soon be returning to the real world, felt uneasy with Jin Wikyung’s face flickering through my mind. How much worse must it be for these guys?

[P163]
There was only one thing I could say.

[P164]
“I trust my big brother.”

[P165]
*Big brother.*

[P166]
This time, I put my heart into the word.

[P167]
Jin Wikyung had been the greatest source of strength I’d had in this place. Maybe I simply wanted to shake off that unease, even if only like this.

[P168]
The faces that had stiffened for a moment relaxed.

[P169]
“We feel the same.”

[P170]
Hyuk Mujin slipped in as well.

[P171]
“I trust the squad leader more.”

[P172]
“Wow. Deputy squad leader, that side-switching of yours is really something.”

[P173]
“You little bastards. Is there anyone here who doesn’t owe the squad leader their life?”

[P174]
“Well, when you put it that way, what can we say?”

[P175]
“I trust the squad leader too. Honestly, I knew all along, even when you were playing the thug. I thought, *Ah, that man is the Sleeping Dragon.* I could tell right away.”

[P176]
I felt strange.

[P177]
*They say even dried squid gives water if you squeeze it. Who knew I’d feel something like this toward NPCs in a game?*

[P178]
*Well, honestly… it doesn’t feel bad.*

[P179]
Suddenly I wondered about Jin Wikyung, somewhere beyond those mountains. Had the battle started? If so, which side was winning?

[P180]
And I wasn’t the only one thinking that.

[P181]
“By now, the battle must have started.”

[P182]
It was Gwak Jun of the Three Paths Sect. Unlike before, he was wearing black martial robes.

[P183]
*Was that what this guy originally wore?*

[P184]
At my look, Gwak Jun shrugged.

[P185]
“I like this sort of thing. Easy to move in, and even if a little blood splatters, it doesn’t show. You fellows feel the same, right?”

[P186]
That last question wasn’t aimed at us. It was for the martial artists of the Three Paths Sect under his command. Every last one of them had changed into black, and they nodded without a word.

[P187]
“Apparently so.”

[P188]
Gwak Jun smiled, satisfied, then turned to me.

[P189]
“Well, shall we set out too?”

[P190]
*What the fuck is this bastard talking about right now?*

[P191]
[^1]: A conscript sergeant in the last stretch of mandatory service, coasting toward discharge.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 37

[P2]
The march went smoothly. The heavy snow that had fallen during our last reconnaissance mission had melted away long ago, and command moved us while conserving as much of the troops’ strength as possible.

[P3]
“At this rate, we’ll arrive in Jeongyang by tomorrow at the latest.”

[P4]
I blinked at the oddly familiar man’s words.

[P5]
“Who are you?”

[P6]
Judging by his clothes, he wasn’t from the Jin Family of Taiyuan. Aside from the reconnaissance squad, most of the people in the rear guard were martial artists from the newly allied small and mid-sized sects, so that made sense.

[P7]
“I’m Gwak Jun of the Three Paths Sect. We met once before… We even shook hands.”

[P8]
Gwak Jun of the Three Paths Sect? It was on the tip of my tongue.

[P9]
*It wasn’t as if I’d shaken only one or two hands trying to raise my Fame.*

[P10]
He was probably one of them.

[P11]
“Sorry. My memory isn’t very good.”

[P12]
“I wasn’t expecting you to remember, honestly. Haha.”

[P13]
Gwak Jun gave me a friendly smile and went on.

[P14]
“To be honest, I was disappointed at first when I found out we’d been assigned to the rear guard.”

[P15]
“Why?”

[P16]
“Because there’d be fewer chances to distinguish ourselves. Isn’t this the chance for an unknown grunt like me to make a name for himself?”

[P17]
“Ah. Right.”

[P18]
There were two possibilities in cases like this. Either he’d been through so many battles that he’d grown nerves of steel, or he was simply fearless.

[P19]
I raised my **Qi Sense**.

[P20]
Ding.

[P21]
> **System**
>
> **Lv.40 Gwak Jun**

[P22]
*Oh. He’s got some skill.*

[P23]
At Level 40, he was at least First Rate. He couldn’t exactly go around bragging he was a master, but it was more than enough to feel wronged about being stuck in the rear.

[P24]
“Half of the enemy troops were recruited in a hurry. They’ve dragged in every kind of deadweight, and they must have force-marched to join the main force. They won’t stand a chance against the elites of the Jin Family of Taiyuan and the Three Paths Sect.”

[P25]
His words sounded plausible enough.

[P26]
*If you leave out the part about the Three Paths Sect being elite.*

[P27]
I nodded half-heartedly.

[P28]
“I see.”

[P29]
“And we have Peak masters superior to the enemy’s as well. There’s the Lesser Family Head and Great Hero Wipeng, of course, but the reputation of the Blade of Flowers has spread throughout the Central Plains, hasn’t it?”

[P30]
The Blade of Flowers. It was the first time I’d heard the title, but I could guess who he meant.

[P31]
The Jin Family of Taiyuan had three Peak masters. Exclude Jin Wikyung and Wipeng, and only one person was left.

[P32]
*The Head Elder.*

[P33]
*Was that old man really that strong?*

[P34]
Gwak Jun’s next words were nothing but praise. Title after title, name after name of masters the Head Elder had cut down in his youth, decades ago, came spilling out.

[P35]
“He was a hero born of the Great Faction War.”

[P36]
A war hero from the past. Listening to Gwak Jun, he sounded like a chivalrous hero among chivalrous heroes—a man who loved justice and couldn’t stand to see injustice go unpunished…

[P37]
*Then why do I feel so uneasy every time I see him?*

[P38]
Maybe it was the first impression, but I disliked the Head Elder.

[P39]
That peculiar air of his. The strange gaze that bored straight through people. The fact that he had formed a political faction against Jin Wikyung.

[P40]
And yet after that, the Head Elder had thrown his full support behind Jin Wikyung, and the Jin Family of Taiyuan had been able to pull tight together, inside and out.

[P41]
*Well, when an outside enemy invades, even family feuds have to stop.*

[P42]
The Head Elder was currently leading the vanguard alongside Jin Wikyung. If he really was as skilled as the rumors claimed, tomorrow’s battle would be that much easier.

[P43]
“Just thinking of Great Hero Blade of Flowers sweeping the battlefield tomorrow already has my heart racing.”

[P44]
Gwak Jun shuddered like a man taking a piss after three days.

[P45]
*Does this bastard not know what tension is?*

[P46]
And where was he getting the confidence that we were going to win?

[P47]
“You’re certain of victory.”

[P48]
“If we lose, we’re in big trouble.”

[P49]
“Excuse me?”

[P50]
*Not big trouble. We’d be finished.*

[P51]
Judging by everything the Mount Heng Sword Sect had done so far, they would turn not only the Jin Family of Taiyuan but the small and mid-sized sects allied with us into a wasteland.

[P52]
“What do you mean by—”

[P53]
“I’m joking.”

[P54]
*This bastard’s a lunatic too.*

[P55]
As I stared at him, speechless, Gwak Jun flashed me a grin.

[P56]
“We’ll win. We will.”

[P57]
One sentence, packed with conviction.

[P58]
When Gwak Jun left it at that and moved away, Hyuk Mujin came up and asked,

[P59]
“Who was that?”

[P60]
“Level 40.”

[P61]
“What?”

[P62]
“There’s this guy. Overflowing with confidence.”

[P63]
I didn’t like him, in more ways than one.

[P64]
*Well, it wasn’t as though I’d have to talk to him again.*

[P65]
* * *

[P66]
Time passed quickly. On the second night after we began the march, we reached Honju, and Jin Wikyung gathered the command staff for a meeting. He was holding a small slip of paper.

[P67]
“A letter from the Lower District Sect. The enemy reinforcements crossed Mount Otae two days ago.”

[P68]
“Then…”

[P69]
“They’re likely to join the main force around now, or sometime tomorrow.”

[P70]
*What?*

[P71]
I couldn’t understand it. If we had attacked the main force before the reinforcements joined them, the fight would have been much easier.

[P72]
*He must have something in mind.*

[P73]
Sure enough, Jin Wikyung went on.

[P74]
“The enemy reinforcements that just joined them are exhausted, and their food is running out. If we take Jeongyang’s high ground first tomorrow, the Mount Heng Sword Sect Leader will have a choice to make. Fall back, or clash.”

[P75]
The next moment, Jin Wikyung’s gaze shifted to me.

[P76]
“What choice do you think he’ll make?”

[P77]
I was caught off guard, but the answer was already there. If he were the kind of man to fall back at this point, he would have done so long ago.

[P78]
“I think he’ll clash.”

[P79]
Twice our numbers, and they weren’t behind us in Peak masters either. From the enemy’s side, they would want to end this fight as fast as possible.

[P80]
“Exactly.”

[P81]
Jin Wikyung smiled, pleased, and traced a finger across the topographic map on the table.

[P82]
“There are four routes the enemy can take into Jeongyang. But with their food situation as it is, they’ll choose the fastest one.”

[P83]
His finger stopped on a place labeled Eight Spring Gorge. The Head Elder, who had been sitting quietly until then, spoke for the first time.

[P84]
“Eight Spring Gorge. Jar-shaped, with a narrow, steep mouth. The mounted bandits will have to abandon their prized horses.”

[P85]
“They’ll have to abandon their lives too.”

[P86]
“The enemy will fight with their lives on the line as well. This much won’t be enough.”

[P87]
“I’ve hidden some hundred horn bows on the cliffs above the gorge.”

[P88]
“Hoh.”

[P89]
A stir ran through the tent. I stared at Jin Wikyung with my mouth open.

[P90]
*When the hell did he hide those?*

[P91]
“Right after our victory at Honju. Thanks to a resourceful ally.”

[P92]
Jin Wikyung looked straight at me as he said it.

[P93]
*The Lower District Sect. Wolhwa.*

[P94]
She had been helping us constantly from places we couldn’t see. Of course, Jin Wikyung was impressive too, for drawing a picture this big.

[P95]
*That’s fucking cool.*

[P96]
A build like a human meat grinder, and a sharp mind to go with it. Suddenly I wanted to call him big brother.

[P97]
“Oh!”

[P98]
“The Lesser Family Head…!”

[P99]
The tent went hot under the burning gazes of those dark, burly men.

[P100]
Jin Wikyung swept a heavy look over everyone assembled.

[P101]
“Let’s settle this.”

[P102]
No one objected. The Head Elder was the first to rise, then gave Jin Wikyung a fist-in-palm salute.

[P103]
“By your command.”

[P104]
That was the end of the meeting. As I left the tent, a familiar voice bored into my ear.

[P105]
—Don’t forget what I told you yesterday.

[P106]
I stiffened for a moment. Then I gave a small nod.

[P107]
And at dawn that day, three hundred martial artists from the Jin Family of Taiyuan and one hundred fifty reinforcements from the small and mid-sized sects—four hundred fifty in all—set out for the gorge.

[P108]
*Still, this was the end, and I hadn’t even said a proper goodbye.*

[P109]
I climbed a hill and stared endlessly at the winding line of torches.

[P110]
* * *

[P111]
The next morning, Hyuk Mujin flinched when he saw me and stepped back.

[P112]
“You startled me. What’s going on?”

[P113]
“What?”

[P114]
“What do you mean, what? You look like a living corpse. Did you not sleep?”

[P115]
“Nah. I slept a little.”

[P116]
That was a lie. I hadn’t slept a wink. I had planted myself on a rock and stared at the System Window all night.

[P117]
Counting down to the moment that had finally come right up to my nose.

[P118]
> **System**
>
> Achieve Fame 500 (497/500)

[P119]
I never thought the number 1 could feel this precious.

[P120]
In a voice that had aged all of a sudden, I muttered,

[P121]
“I’m going, I’m going, going home now…”

[P122]
“Now you’re even talking to yourself. Have you lost your mind?”

[P123]
Hyuk Mujin clicked his tongue, then his eyes went round.

[P124]
“What’s that? I’ve never seen those before.”

[P125]
“This?”

[P126]
I pointed in turn at the old book and the small case sitting on the rock.

[P127]
“One’s a martial arts manual. The other’s an elixir.”

[P128]
“Hah. Really?”

[P129]
I explained it weakly to the guy whose eyes were halfway out of his head.

[P130]
“The manual’s a Supreme Peak martial art, and if you absorb the elixir right, it’s thirty years.”

[P131]
“What?”

[P132]
“But they say if you take the elixir wrong, you’ll burn to death. You want it?”

[P133]
“Ah. Sure…”

[P134]
Judging by that unimpressed face and the snout sticking out a good few feet, he didn’t believe a damn word I was saying.

[P135]
*Well, if someone suddenly came at me with a Supreme Peak martial art and a thirty-year Fireball elixir, I’d figure it was a joke too.*

[P136]
“You really won’t eat it? It’s good stuff.”

[P137]
“Oh, I’m fine. Learn plenty of that Supreme Peak martial art, and be sure to chew your elixir thoroughly.”

[P138]
“I don’t need this kind of thing anymore.”

[P139]
“Of course. You’re the Sleeping Dragon.”

[P140]
Normally I would have smacked him in the back of the head. Right now I didn’t feel much of anything.

[P141]
*Is this how a short-timer sergeant feels?[^1]*

[P142]
At the same time, I felt strange. Was it the aftereffect of everything I’d been through? It had only been a little over a month, but it felt distant, as if I’d been here a year.

[P143]
I started tracing back through old memories.

[P144]
*I first opened my eyes at Honghwaru.*

[P145]
That was where I met Wolhwa for the first time and realized I was trapped in this game. Even now, thinking about that moment gave me goose bumps.

[P146]
*I really thought I was going to lose my mind.*

[P147]
It had taken me three days just to decide to go to the Jin Family of Taiyuan. And the guy I met there was this one—Hyuk Mujin.

[P148]
Smack!

[P149]
“Argh! Why did you hit me?”

[P150]
“Hmm. Just thought of the old days.”

[P151]
“What old days?”

[P152]
“Nope. Not telling. Get back already.”

[P153]
“What am I, some back-alley punk? Just because your martial arts are a bit strong, you think you can oppress people like this?”

[P154]
As Hyuk Mujin threw a fit, everyone’s eyes turned toward us. Even the reconnaissance-squad members who had been watching like it was none of their business jumped in.

[P155]
“What are you two talking about?”

[P156]
“Dunno. The deputy squad leader must have done something wrong.”

[P157]
“Hey, I didn’t do anything!”

[P158]
“This is Murim. Being weak is a crime.”

[P159]
“But should we even be doing this?”

[P160]
At someone’s words, silence fell for a moment.

[P161]
“True. Waiting here is our mission, but…”

[P162]
The tension and fear they had been holding down with forced smiles hung in the air. Even I, who would soon be going back to the real world, felt uneasy with Jin Wikyung’s face flickering through my mind. How much worse must it be for these guys?

[P163]
There was only one thing I could say.

[P164]
“I trust my big brother.”

[P165]
*Big brother.* This time, I put my heart into the word.

[P166]
Jin Wikyung had been the greatest source of strength I’d had in this place. Maybe I simply wanted to shake off that unease, even if only like this.

[P167]
The faces that had stiffened for a moment eased.

[P168]
“We feel the same.”

[P169]
Hyuk Mujin slipped in as well.

[P170]
“I trust the squad leader more.”

[P171]
“Wow. Deputy squad leader, that side-switching of yours is really something.”

[P172]
“You little bastards. Is there anyone here who doesn’t owe the squad leader their life?”

[P173]
“Well, when you put it that way, what can we say?”

[P174]
“I trust the squad leader too. Honestly, I knew all along, even when you were playing the thug. I thought, *Ah, that man is the Sleeping Dragon.* I could tell right away.”

[P175]
I felt strange.

[P176]
*They say even dried squid gives water if you squeeze it. Who knew I’d feel something like this toward NPCs in a game?*

[P177]
*Well, honestly… it doesn’t feel bad.*

[P178]
Suddenly I wondered about Jin Wikyung, somewhere beyond those mountains. Had the battle started? If it had, which side was winning?

[P179]
And I wasn’t the only one thinking that.

[P180]
“By now, the battle must have started.”

[P181]
It was Gwak Jun of the Three Paths Sect. Unlike before, he was wearing black martial robes.

[P182]
*Was that what this guy originally wore?*

[P183]
At my look, Gwak Jun shrugged.

[P184]
“I like this sort of thing. Easy to move in, and even if a little blood splatters, it doesn’t show. You all feel the same, right?”

[P185]
That last question wasn’t aimed at us. It was for the martial artists of the Three Paths Sect whom he led. Every last one of them had changed into black, and they nodded without a word.

[P186]
“Apparently so.”

[P187]
Gwak Jun smiled, satisfied, then turned to me.

[P188]
“Well, shall we set out too?”

[P189]
*What the fuck is this bastard talking about right now?*

[P190]
[^1]: A conscript sergeant in the last stretch of mandatory service, coasting toward discharge.
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 37,
  "passed": true,
  "metrics": {
    "source_characters": 5716,
    "translation_characters": 13444,
    "length_ratio": 2.352,
    "source_paragraphs": 178,
    "translation_paragraphs": 191
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
