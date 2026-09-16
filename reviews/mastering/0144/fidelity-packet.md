# Fidelity Gate — Chapter 144

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
  1|＃144화
  2|
  3|
  4|
  5|나한테 사인을 해 달란다. 그것도 왕이.
  6|
  7|‘뭐여, 이게.’
  8|
  9|이런 시나리오는 내 예상에 없었는데?
 10|
 11|황당함에 말을 잇지 못하는 나를 큼지막한 눈동자가 물끄러미 바라본다.
 12|
 13|“과인이 너무 무리한 부탁을 한 것인가?”
 14|
 15|“아뇨, 그건 아닌데…… 제 서명을 받아서 뭐 하시려고.”
 16|
 17|“음, 싫으면 안 해도 되네.”
 18|
 19|사극에서나 나올 법한 고풍스러운 말투 속에는 보이지 않는 간절함이 숨겨져 있다.
 20|
 21|강아지처럼 연무장 바닥을 긁는 발끝과 연신 꼼지락거리는 양손이 그 증거다.
 22|
 23|‘짜식, 귀엽기는.’
 24|
 25|아직은 어린아이. 아무리 왕이라 해도 나이는 못 속인다.
 26|
 27|위엄 어린 표정과는 달리 정직한 몸을 본 나는 피식 실소가 흘러나왔다.
 28|
 29|“왜 웃는 거지?”
 30|
 31|“아무것도 아닙니다. 그럼 이 목판에 제 이름을 새기면 되는 거죠?”
 32|
 33|순간 어린 왕의 입가가 씰룩였다.
 34|
 35|“가급적이면 별호도 함께.”
 36|
 37|이게 뭐라고 또 진지하게 대답해 준다. 나는 터져 나오는 웃음을 참으며 단검을 들었다.
 38|
 39|사각, 사각, 사각.
 40|
 41|산서잠룡 진태경. 무릎에 목판을 대고 일곱 글자를 정성스럽게 새겨 나가던 그때 주표가 불쑥 물었다.
 42|
 43|“검기를 사용하면 더 편하지 않겠나?”
 44|
 45|“그렇죠.”
 46|
 47|“그런데 왜 쓰지 않지?”
 48|
 49|“안 쓰는 게 아니라 못 쓰는 겁니다.”
 50|
 51|“검기를 못 쓴다니?”
 52|
 53|“말 그대롭니다. 아직 절정 고수가 아니라서 검기를 못 써요.”
 54|
 55|“절정 고수가…… 아니야?”
 56|
 57|슬쩍 고개를 들어 보니 주표가 충격받은 얼굴로 나를 바라보고 있었다.
 58|
 59|“그대는 산서잠룡이 아닌가.”
 60|
 61|“네, 저 맞는데요.”
 62|
 63|“한데 검기를 못 쓴다니, 절정 고수가 아니라니!”
 64|
 65|“……그럴 수도 있죠.”
 66|
 67|“아닐세, 그럴 수 없어!”
 68|
 69|와, 살짝 상처받으려고 하네.
 70|
 71|가뜩이나 근래 들어 자주 등장하는 검기 때문에 상대적 박탈감을 느끼고 있었는데, 난생처음 보는 꼬맹이가 속을 뒤집어 놓는다.
 72|
 73|‘검기 못 쓰는 것도 죄냐.’
 74|
 75|나는 나대로 상처받고, 주표의 어린 팬심에도 금이 갔다.
 76|
 77|괜한 서러움에 코를 훔치던 그때였다.
 78|
 79|“절정 고수도 아니면서 어찌 그리 강할 수 있단 말인가!”
 80|
 81|“예?”
 82|
 83|“일문일살 조필, 화양검 진백양, 마지막으로 얼마 전의 적풍단주 풍양까지. 지금까지 그대가 쓰러트린 적들은 모두 고강한 절정 고수들이었지 않은가?”
 84|
 85|저 중에서 온전히 내 힘으로 쓰러트렸다고 할 만한 자는 조필밖에 없지만, 일단 고개를 끄덕였다.
 86|
 87|“그렇죠.”
 88|
 89|“도대체 어떻게 그런 일이 가능하지?”
 90|
 91|“그야.”
 92|
 93|인벤토리가 개꿀입니다. 그리고 다구리 앞에는 장사 없어요.
 94|
 95|도저히 안 되겠다 싶을 때는 인벤토리를 뒤져 보세요. 반 갑자짜리 영약과 만년한철 무기가 나올 수도 있으니까요.
 96|
 97|‘……이렇게 대답할 수는 없지.’
 98|
 99|이미지는 스스로가 만들어 가는 법.
100|
101|나는 잔잔한 미소와 함께 입을 열었다.
102|
103|“제가 더 강했기 때문 아니겠습니까.”
104|
105|“오오!”
106|
107|“무림에는 이런 말이 있습니다. 강자가 살아남는 것이 아니다, 살아남는 자가 강자다.”
108|
109|“오오오!”
110|
111|“지금까지 세 명의 절정 고수와 싸웠습니다. 일류 고수 수십 명의 습격을 받은 적도 있지요.”
112|
113|“그럴 수가!”
114|
115|주표가 작은 주먹을 꼭 쥔 채 탄성을 내질렀다.
116|
117|리액션이 혜자다 보니 말할 맛이 난다. 나는 지금까지 헤쳐 온 위기의 순간을 떠올리며 말을 이어 갔다.
118|
119|“하지만 저는 매번 죽을힘을 다해 싸웠고, 살아남았습니다. 절정 고수? 검기? 그런 것은 중요하지 않습니다.”
120|
121|“검기가 중요하지 않다니, 진심인가?”
122|
123|“물론입니다.”
124|
125|사실 존나게 중요하다. 만나는 놈들마다 검기를 가래떡마냥 줄줄 뽑아 대는데 나만 못 써.
126|
127|한 번씩 싸울 때마다 이게 사람 목숨인지 파리 목숨인지 헷갈릴 정도다.
128|
129|‘넌 영약 든든히 먹고 다녀라. 검기가 없으면 몸이 고생해.’
130|
131|나는 무엄하게도 어린 왕의 어깨에 손을 올렸다. 그리고 속삭였다.
132|
133|“이기고자 하는 마음. 끝까지 포기하지 않는 불굴의 의지가 지금의 산서잠룡을 만든 것이지요.”
134|
135|“불굴의 의지……!”
136|
137|주표의 작은 몸이 부르르 떨렸다. 이윽고 뜨거운 한숨을 내쉰 그가 입을 열었다.
138|
139|“과인도 그대처럼 될 수 있을까?”
140|
141|“할 수 있습니다. 방금 수련하시는 모습을 보니 금방 고수가 되실 것 같던데요.”
142|
143|“그, 그 말이 정말인가?”
144|
145|아니, 시스템 없으면 힘들걸.
146|
147|‘하지만 자라나는 새싹에게는 물을 줘야지.’
148|
149|반짝반짝 빛나는 큼지막한 눈동자를 향해 고개를 끄덕여 준 나는, 이미 완성된 목판에 몇 글자를 더 새긴 뒤 건네주었다.
150|
151|“힘들 때마다 이걸 보면서 힘을 내십시오.”
152|
153|“이건…….”
154|
155|목판을 확인한 어린 왕이 활짝 웃었다.
156|
157|“정말 고맙네. 내 이 목판을 크게 만들어 산서성부의 현판에 걸어 두지.”
158|
159|“……저걸요?”
160|
161|“아무렴. 이곳을 드나드는 모두가 그대의 명문(名文)을 읽게 될 걸세.”
162|
163|나는 목판을 흐뭇하게 바라보는 주표를 보며 생각했다.
164|
165|‘저걸 산서성부 현판에 걸어 둔다고?’
166|
167|
168|
169|꿈☆은 이루어진다.
170|
171|-산서잠룡 진태경-
172|
173|
174|
175|……저걸?
176|
177|
178|
179|* * *
180|
181|
182|
183|다시 돌아온 대전은 언제 그랬냐는 듯 깔끔하게 원상 복구 된 상태였다.
184|
185|하인들이 새로 들여놓은 탁자 위를 산해진미로 가득 채우자 상석에 앉아 있던 상산왕 주표가 입을 열었다.
186|
187|“과인의 부름에 기꺼이 응해 준 그대들에게 감사를 표하네. 자, 이제 마음껏 드시게.”
188|
189|띠링.
190|
191|
192|
193|- 퀘스트 조건, [성주가 주최하는 오찬에 참석]을 충족시켰습니다!
194|
195|- 퀘스트 보상은 오찬이 끝난 이후 지급됩니다.
196|
197|
198|
199|이어지는 분위기는 화기애애했다. 아무래도 주최자이자 이 자리의 주인인 어린 왕이 싱글벙글 웃고 있으니 안 좋으려야 안 좋을 수가 없다.
200|
201|“과인이 듣기로는 일문일살 조필은 아주 악독한 놈이라 들었는데, 어떤 자였는지 알려 줄 수 있겠나?”
202|
203|“아, 그놈 아주 지독한 놈이었죠. 그러니까 그게…….”
204|
205|“화양검 진백양은 중원에까지 이름이 알려진 절정 고수였다지? 얼마나 강하던가?”
206|
207|“개쎕니다. 미쳤어요.”
208|
209|“진 소협, 전하께서 듣고 계십니다. 부디 언행에 좀 주의를.”
210|
211|“아, 죄송합니다. 아무튼, 그때 이야기를 해 보자면…….”
212|
213|한참 썰을 풀고 나니 진이 빠졌다. 나는 계속해서 말을 거는 주표에게 청풍을 던져 주고 슬쩍 엉덩이를 뺐다.
214|
215|“산서잠룡, 어딜 가는가?”
216|
217|“검성 매종학 아시죠? 이 친구가 그분 제잡니다.”
218|
219|“검성!”
220|
221|“그리고 절정 고수예요. 검기 가르쳐 달라고 해 보세요.”
222|
223|산타클로스를 만난 아이처럼 행복해하는 주표를 남겨 두고 옆으로 빠졌다.
224|
225|말 한마디 못 꺼내 보고 꾸역꾸역 음식만 먹고 있는 산서오문의 후기지수들과 제법 진지한 분위기로 대화를 나누는 두 사람이 보였다.
226|
227|전자와 후자, 둘 다 딱히 끼어들고 싶은 대화 상대는 아니다.
228|
229|‘밥이나 먹자.’
230|
231|하지만 고기를 몇 점 집어먹기도 전에 간드러진 목소리가 귓가를 파고들었다.
232|
233|“진 소혀엽.”
234|
235|“……왜요?”
236|
237|저 목소리를 들으니까 갑자기 입맛이 뚝 떨어지네.
238|
239|“거기서 혼자 뭐 해요? 우리 같이 이야기나 하죠.”
240|
241|“싫습니다. 배고파요.”
242|
243|“태원진가에 관련된 이야기인데?”
244|
245|“저는 가문 일에는 관여 안 합니다. 우리 큰형님이랑 따로 얘기해 보세요.”
246|
247|“아쉽네. 그럼 성운표국 쪽에 맡기는 수밖에.”
248|
249|성운표국? 어디서 들어 본 이름이다 싶었는데, 어제 홍화객잔에서 흠씬 두들겨 패 준 녀석의 집안이다.
250|
251|그놈이 아마 성운표국의 소국주인가 그랬지?
252|
253|“성운표국이 왜요?”
254|
255|홍진이 입꼬리를 말아 올렸다.
256|
257|“아니에요. 식사마저 들어요. 개도 안 건드린다는데 산서잠룡을 건드리면 쓰나.”
258|
259|“…….”
260|
261|“호호, 농담인데 정색하기는, 어서 와서 앉아요.”
262|
263|홍진이 옆자리 의자를 빼 주었고, 나는 못 이기는 척 자리에 앉았다. 물론 이풍의 옆자리에.
264|
265|다시 한번 말하지만 내 엉덩이는 소중하니까.
266|
267|“무슨 얘긴지 들어나 보죠. 이쪽은 영 문외한이라 별 소용없을 수도 있겠지만.”
268|
269|섭섭한 척 입술을 삐죽 내밀고 있던 홍진이 입을 열었다.
270|
271|“진 소협이 이 자리에서 결정하지 않아도 상관없어요. 소가주께 전달만 해 드리면 되니까. 그럼 이 첨사?”
272|
273|이풍이 말을 받았다.
274|
275|“이번 일에 태원진가의 힘을 빌리고 싶소.”
276|
277|“이번 일이라면…….”
278|
279|“섬서와 산서를 중점적으로 연결하는 것에 대해서는 알고 계실 거라 생각하오.”
280|
281|“원래 종남파와 하려고 했던 그거요?”
282|
283|지켜보고 있던 홍진이 고개를 끄덕였다.
284|
285|“사실 종남파도 나쁘지 않은 상대예요. 구파일방에 속할 만큼 거대 문파인 데다 문주인 풍운검군을 포함한 수뇌부도 실리적인 성향이거든요. 비교적 폐쇄적인 다른 무림 문파들과는 다르죠.”
286|
287|“그럼 굳이 바꿀 필요가 있었나요? 처음부터 화산파와 할 게 아니었다면 그냥 두는 게 더 나을 수도 있었을 텐데.”
288|
289|“나름 심사숙고해서 내린 결정이에요. 오늘 뒤엎긴 했지만.”
290|
291|홍진이 빙긋 웃으며 말을 이었다.
292|
293|“나는 무림인은 아니지만 검성이 무림에서 어떤 위치를 차지하고 있는지는 잘 알고 있거든.”
294|
295|“…….”
296|
297|“하지만 검성이 모습을 감춘 지 삼십여 년이에요. 지금까지 화산에 남아 후인을 양성하고 있었다는 사실을 진작 알았다면 종남파를 선택하지 않았겠죠.”
298|
299|말을 끝낸 홍진이 이풍을 향해 눈을 흘겼다.
300|
301|보아하니 10년 전부터 검성과 청풍의 존재를 알고 있었으면서 입도 벙긋 안 한 모양이다.
302|
303|“도지휘동지. 다시 말씀드리지만 그건 본문의 대외비였습니다. 청풍 사숙이 하산한 이상 감출 필요가 없어졌을 뿐.”
304|
305|침착하게 대꾸한 이풍이 나를 향해 고개를 돌렸다.
306|
307|“본론부터 말씀드리겠소. 표국, 섬서를 시작으로 중원까지 진출할 수 있을 만한 표국이 필요하오.”
308|
309|아하, 대충 감이 잡힌다.
310|
311|이들은 태원진가에 물적, 혹은 인적 자원을 지원해 달라고 부탁하고 있는 것이다.
312|
313|“표국을 만들 생각이신 건가요?”
314|
315|“비슷하오. 다만 우리는 태원진가의 이름을 빌리고 싶소. 대신 절반의 자금과 최대한의 편의를 제공하지.”
316|
317|이건 대놓고 밀어주겠다는 소린데? 이럴 바에야 본인들 스스로 표국을 만드는 게 더 낫지 않나?
318|
319|의아함을 느끼던 그때, 문득 며칠 전 진무경이 해 준 말이 떠올랐다.
320|
321|‘지금의 황제도 형인 황태자를 암살하고 황위에 올랐다고 했지. 분명히.’
322|
323|확인되지 않은 소문일 뿐이지만 두 사람이 몸을 사리는 걸 봐서는 영 근거 없는 말도 아닌 모양이다.
324|
325|하나뿐인 아우를 굳이 변방 취급받는 산서성으로 보낸 이유도 황제의 경계심에서 비롯된 것이 아닐까?
326|
327|‘음. 이것도 어째 쎄한데?’
328|
329|잘못 얽힌 거 아닌지 고민하는 내게 두 사람이 말했다.
330|
331|“이에 관해서는 일간 자리를 마련할 테니 진 소가주께 잘 말씀드려 주시오.”
332|
333|“진 공자, 이거 좋은 제안인 거 알죠?”
334|
335|“알죠, 아는데…….”
336|
337|이것도 어떻게 보면 남의 집안싸움이다. 평범한 형제 사이라면 아이스크림 하나 더 먹겠다고 싸우다가 코피가 터지고 끝나겠지만, 이쪽은 아이스크림이 아니라 황위다.
338|
339|코피 터지는 정도로 끝날 일이 아니라는 것이다.
340|
341|“일단 큰형님께는 잘 전달해 드릴게요.”
342|
343|일부러 말을 아꼈다. 어차피 결정은 진위경이 내릴 건데 내가 고민할 이유가 없다. 그가 먼저 내 의견을 물어본다면 모를까.
344|
345|“그 정도면 충분해요. 진 공자가 말하는데 흘려듣진 않겠지. 진 소가주가 아우들 아끼는 거야 우리도 익히 들었으니까.”
346|
347|아주 동네방네 소문이 다 났구나.
348|
349|무안한 얼굴로 술잔을 쭉 들이켜는데, 한참 떨어진 탁자 끝자리에서 체할 것 같은 얼굴로 앉아 있는 사인방과 시선이 딱 마주쳤다.
350|
351|아, 맞다. 하나 깜빡할 뻔했네.
352|
353|“저기요. 위원장 동지. 아니 도지휘동지.”
354|
355|“네?”
356|
357|“표국 그거, 간판만 바꿔 달아도 충분하지 않아요?”
358|
359|어리둥절한 이풍과는 달리 홍진은 씩 웃어 보였다.
360|
361|“생각해 둔 곳 있어요?”
362|
363|“아까 두 분이 얘기하시던 그곳.”
364|
365|“성운표국? 거기 너무 만만하게 보지 마요. 명색이 산서 제일 표국이야. 한입에 소화하기 힘들어.”
366|
367|“그러니까 꼭꼭 씹어 먹어야죠.”
368|
369|소국주 보니까 견적이 딱 나온다. 지금의 태원진가에 홍진과 이풍이 도와준다면 뼈 채로 씹어 먹어도 소화할 수 있다.
```

## Assembled English

```markdown
[P1]
# Chapter 144

[P2]
He wanted my autograph. A king, no less.

[P3]
*What the hell is this?*

[P4]
I never saw this scenario coming.

[P5]
As I stood there speechless with bewilderment, a pair of large eyes gazed steadily at me.

[P6]
“Have I asked too much of you?”

[P7]
“No, it’s not that… What are you planning to do with my signature?”

[P8]
“Hmm. If you don’t want to, you don’t have to.”

[P9]
Beneath the archaic speech straight out of a historical drama lurked an eagerness he couldn’t quite hide.

[P10]
The tips of his feet scraped at the training ground floor like a puppy, and both his hands kept fidgeting restlessly. Those were proof enough.

[P11]
*The little guy is cute, though.*

[P12]
He was still a child. King or not, he couldn’t hide his age.

[P13]
His expression was full of dignity, but his body was honest. A quiet laugh escaped me.

[P14]
“Why are you laughing?”

[P15]
“It’s nothing. So I just carve my name into this wooden tablet?”

[P16]
The young king’s lips twitched.

[P17]
“Preferably with your alias as well.”

[P18]
Why was he answering so seriously over something like this? I held back my laughter and picked up the dagger.

[P19]
*Scritch, scritch, scritch.*

[P20]
Sleeping Dragon of Shanxi, Jin Taekyung. I rested the wooden tablet on my knee and carefully carved the seven characters into it.

[P21]
That was when Zhu Bao suddenly asked, “Wouldn’t it be easier if you used Sword Energy?”

[P22]
“It would.”

[P23]
“Then why aren’t you using it?”

[P24]
“It’s not that I won’t. I can’t.”

[P25]
“You can’t use Sword Energy?”

[P26]
“I mean exactly what I said. I’m not a Peak master yet, so I can’t use Sword Energy.”

[P27]
“You’re… not a Peak master?”

[P28]
I raised my head slightly. Zhu Bao was staring at me with a shocked expression.

[P29]
“Aren’t you the Sleeping Dragon of Shanxi?”

[P30]
“Yes, that’s me.”

[P31]
“And yet you can’t use Sword Energy? You’re not a Peak master?”

[P32]
“…That can happen.”

[P33]
“No, it can’t!”

[P34]
Wow. He almost sounded hurt.

[P35]
I’d already been feeling inadequate with all the Sword Energy I’d been seeing lately. Now a little kid I had never seen before was twisting the knife.

[P36]
*Is being unable to use Sword Energy a crime?*

[P37]
I was hurt in my own way, and the young prince’s fandom had taken a hit too.

[P38]
I was wiping my nose in wounded frustration when he exclaimed, “How can you be so strong when you aren’t even a Peak master?”

[P39]
“What?”

[P40]
“One Question, One Kill Jopil, Blade of Flowers Jin Baekyang, and most recently Pung Yang, the Red Wind Band Leader. Weren’t all the enemies you defeated powerful Peak masters?”

[P41]
Jopil was the only one I could honestly claim to have defeated entirely through my own strength, but I nodded anyway.

[P42]
“That’s right.”

[P43]
“How was such a thing possible?”

[P44]
“Well…”

[P45]
*The Inventory is fucking amazing. And nobody can withstand a group beating.*

[P46]
*Whenever things look hopeless, try digging through your Inventory. You might find an elixir worth half a jiazi or a weapon made of Ten-Thousand-Year Cold Iron.*

[P47]
*…I can’t exactly answer that way.*

[P48]
An image was something you built for yourself.

[P49]
I opened my mouth with a gentle smile.

[P50]
“Isn’t it because I was stronger?”

[P51]
“Wow!”

[P52]
“There’s a saying in Murim. The strong do not survive. Those who survive are strong.”

[P53]
“Wow!”

[P54]
“I’ve fought three Peak masters so far. I was once even attacked by dozens of First Rate masters.”

[P55]
“How could that be!”

[P56]
Zhu Bao clenched his tiny fists and gasped in admiration.

[P57]
He gave such great reactions that it made me want to keep talking. I continued, recalling the moments of crisis I had fought my way through.

[P58]
“But every time, I fought with everything I had and survived. Peak masters? Sword Energy? Those things aren’t important.”

[P59]
“Sword Energy isn’t important? Do you mean that?”

[P60]
“Of course.”

[P61]
*It’s fucking important.*

[P62]
Every bastard I met kept drawing out Sword Energy like endless strands of rice cake, and I was the only one who couldn’t use it.

[P63]
Every fight left me wondering whether I had a human life or a fly’s.

[P64]
*Make sure you eat plenty of elixirs. Without Sword Energy, your body will suffer.*

[P65]
With outrageous disrespect, I placed a hand on the young king’s shoulder and whispered, “The desire to win. The unbreakable will to never give up until the very end. That is what made the Sleeping Dragon of Shanxi who he is today.”

[P66]
“An unbreakable will…!”

[P67]
Zhu Bao’s small body trembled. Then, after letting out a heated sigh, he asked, “Can I become like you?”

[P68]
“You can. From what I just saw of your training, you look like you’ll become a master in no time.”

[P69]
“D-Do you really mean that?”

[P70]
*It’ll be tough without the System.*

[P71]
*But you have to water a growing sprout.*

[P72]
I nodded at his enormous, sparkling eyes, carved a few more characters into the finished tablet, and handed it to him.

[P73]
“Whenever things get hard, look at this and take heart.”

[P74]
“What is this…?”

[P75]
The young king examined the tablet and broke into a radiant smile.

[P76]
“Thank you very much. I shall have this tablet enlarged and hang it on the signboard of the Shanxi Provincial Office.”

[P77]
“…That?”

[P78]
“Of course. Everyone who enters or leaves this place shall read your celebrated words.”

[P79]
I looked at Zhu Bao, who was gazing fondly at the wooden tablet, and thought,

[P80]
*He’s going to hang that on the signboard of the Shanxi Provincial Office?*

[P81]
*Dreams☆come true.*

[P82]
—Sleeping Dragon of Shanxi, Jin Taekyung—

[P83]
*…That?*

[P84]
* * *

[P85]
When we returned to the grand hall, it had been restored to pristine condition as though nothing had ever happened.

[P86]
Once the servants filled the newly placed tables with delicacies from land and sea, Prince Shangshan Zhu Bao, seated at the seat of honor, spoke.

[P87]
“I thank you all for willingly answering my summons. Now, please eat your fill.”

[P88]
*Ding.*

[P89]
> **System**
>
> Quest condition, **Attend the luncheon hosted by the City Lord**, has been fulfilled!
>
> The Quest Reward will be issued after the luncheon ends.

[P90]
The atmosphere that followed was warm and cheerful. With the young king, both host and master of the gathering, grinning from ear to ear, how could it not have been?

[P91]
“I have heard that One Question, One Kill Jopil was an exceptionally vicious man. Could you tell me what he was like?”

[P92]
“Oh, that bastard was absolutely brutal. Well, you see…”

[P93]
“I’ve heard that Blade of Flowers Jin Baekyang was a Peak master whose name was known even in the Central Plains. How strong was he?”

[P94]
“Fucking strong. The man was insane.”

[P95]
“Young Hero Jin, His Highness is listening. Please mind your language.”

[P96]
“Ah, sorry. Anyway, to tell you about what happened then…”

[P97]
After telling stories for quite some time, I was exhausted. I tossed Cheongpung to Zhu Bao, who continued asking me questions, and quietly began edging away.

[P98]
“Sleeping Dragon of Shanxi, where are you going?”

[P99]
“You know the Sword Saint, Mae Jonghak, right? This guy is his disciple.”

[P100]
“The Sword Saint!”

[P101]
“And he’s a Peak master, too. Ask him to teach you Sword Energy.”

[P102]
Leaving Zhu Bao as delighted as a child meeting Santa Claus, I slipped off to one side.

[P103]
I spotted the young prodigies of the Five Gates of Shanxi silently cramming food into their mouths and two men engaged in a rather serious discussion.

[P104]
Neither group was particularly inviting company.

[P105]
*I’ll just eat.*

[P106]
But before I could manage more than a few pieces of meat, a syrupy voice wormed into my ear.

[P107]
“Young Hero Jiiin.”

[P108]
“…What?”

[P109]
Hearing that voice killed my appetite on the spot.

[P110]
“What are you doing over there all by yourself? Come talk with us.”

[P111]
“No, thank you. I’m hungry.”

[P112]
“It’s about the Jin Family of Taiyuan.”

[P113]
“I don’t get involved in family affairs. Talk to my eldest brother separately.”

[P114]
“What a shame. Then I suppose we’ll have no choice but to entrust it to the Seongun Escort Bureau.”

[P115]
The Seongun Escort Bureau? The name sounded familiar. Then I remembered—it belonged to the family of the guy I’d beaten black and blue at Honghwa Inn yesterday.

[P116]
Hadn’t that guy been the Seongun Escort Bureau’s Young Bureau Head?

[P117]
“Why the Seongun Escort Bureau?”

[P118]
Hong Jin curled up the corners of his mouth.

[P119]
“Oh, nothing. Please eat your meal. They say even a dog is left alone while it’s eating, so how could I bother the Sleeping Dragon of Shanxi?”

[P120]
“…”

[P121]
“Hee-hee. I was joking. Don’t look so serious. Come over and sit down.”

[P122]
Hong Jin pulled out the chair beside him. I sat down as though I had no choice.

[P123]
Beside Li Feng, of course.

[P124]
I’ll say it again: my ass is precious.

[P125]
“Let’s hear what this is about. I’m not very knowledgeable in this area, so I may not be much help.”

[P126]
Hong Jin had been pouting in feigned disappointment. Now he spoke.

[P127]
“It doesn’t matter if Young Hero Jin doesn’t make a decision here. You only need to pass the matter along to the Lesser Family Head. Now, Assistant Commissioner Li?”

[P128]
Li Feng took over.

[P129]
“We would like to borrow the strength of the Jin Family of Taiyuan for this matter.”

[P130]
“This matter being…?”

[P131]
“I believe you’re aware of our plan to focus on connecting Shaanxi and Shanxi.”

[P132]
“The thing you originally intended to do with the Zhongnan Sect?”

[P133]
Hong Jin, who had been watching us, nodded.

[P134]
“To be honest, the Zhongnan Sect isn’t a bad partner. It’s a massive sect belonging to the Nine Sects and One Gang, and its leadership, including the Sect Leader, the Wind-and-Cloud Sword Lord, has a practical nature. They’re different from the other, relatively closed-off Murim sects.”

[P135]
“Then was there really any need to switch partners? If you hadn’t intended to work with Huashan from the start, leaving things as they were might have been better.”

[P136]
“It was a decision I reached after giving it a great deal of thought. Although we overturned it today.”

[P137]
Hong Jin smiled faintly and continued.

[P138]
“I’m not a martial artist, but I’m well aware of the Sword Saint’s standing in Murim.”

[P139]
“…”

[P140]
“But it has been more than thirty years since the Sword Saint disappeared. If we had known sooner that he had remained at Huashan and was raising successors, we wouldn’t have chosen the Zhongnan Sect.”

[P141]
When he finished speaking, Hong Jin shot Li Feng a reproachful look.

[P142]
Apparently, Li Feng had known about the Sword Saint and Cheongpung for the past ten years without breathing a word of it.

[P143]
“Deputy Military Commissioner, I’ll say it again: that was classified information belonging to our sect. There was simply no longer any reason to conceal it once Martial Uncle Cheongpung descended the mountain.”

[P144]
Li Feng replied calmly, then turned to me.

[P145]
“I’ll get straight to the point. We need an Escort Bureau capable of expanding into the Central Plains, starting with Shaanxi.”

[P146]
*Ah.*

[P147]
I had a rough idea of what was going on.

[P148]
They were asking the Jin Family of Taiyuan to provide material or human resources.

[P149]
“Are you planning to create an Escort Bureau?”

[P150]
“Something similar. However, we would like to borrow the name of the Jin Family of Taiyuan. In return, we’ll provide half the funding and every possible convenience.”

[P151]
They were openly offering to back us. Wouldn’t it be better for them to create an Escort Bureau themselves at this point?

[P152]
As I wondered about that, I suddenly remembered what Jin Mukyung had told me a few days ago.

[P153]
*He said that the current Emperor also assassinated his older brother, the Crown Prince, and ascended the throne. I’m sure of it.*

[P154]
It was only an unconfirmed rumor, but judging by how cautiously these two were acting, it didn’t seem entirely baseless.

[P155]
Could the Emperor’s wariness have been the reason he sent his only younger brother to Shanxi Province, a region treated as a frontier?

[P156]
*Hmm. Something about this smells fishy too.*

[P157]
As I wondered whether I had gotten myself entangled in something dangerous, the two men spoke to me.

[P158]
“We’ll arrange a meeting regarding this matter in the coming days. Please put in a good word with the Lesser Family Head.”

[P159]
“Young Master Jin, you know this is a good offer, right?”

[P160]
“I know. I do, but…”

[P161]
Looked at one way, this was someone else’s family feud. Ordinary brothers might fight over who got an extra ice cream, give each other bloody noses, and call it a day.

[P162]
But this wasn’t ice cream. It was the imperial throne.

[P163]
A bloody nose wouldn’t be the end of it.

[P164]
“I’ll make sure to pass it along to my eldest brother.”

[P165]
I deliberately kept my answer noncommittal. Jin Wikyung would be the one making the decision anyway, so there was no reason for me to worry about it—unless he asked for my opinion first.

[P166]
“That will be enough. He won’t simply dismiss something Young Master Jin tells him. We’ve heard plenty about how much the Lesser Family Head cherishes his younger brothers.”

[P167]
*So the whole neighborhood knows.*

[P168]
I drained my cup of liquor with an embarrassed look, only to meet the eyes of the four of them sitting at the far end of a table some distance away. They all looked as though they were about to get indigestion.

[P169]
Oh, right. I’d almost forgotten something.

[P170]
“Excuse me. Comrade Chairman—no, Deputy Military Commissioner.”

[P171]
“Yes?”

[P172]
“That Escort Bureau business. Wouldn’t it be enough to simply change the sign?”

[P173]
Unlike the bewildered Li Feng, Hong Jin grinned.

[P174]
“You have a place in mind?”

[P175]
“The one the two of you were talking about earlier.”

[P176]
“The Seongun Escort Bureau? Don’t take them too lightly. It’s the foremost Escort Bureau in Shanxi, after all. They’ll be difficult to swallow in one bite.”

[P177]
“That’s why we have to chew thoroughly.”

[P178]
One look at their Young Bureau Head had told me exactly what we were dealing with. With Hong Jin and Li Feng backing the Jin Family of Taiyuan as it now stood, we could chew them up bones and all—and still digest them.
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
# Chapter 144

[P2]
He was asking me for an autograph. A king, no less.

[P3]
*What the hell is this?*

[P4]
I never saw this scenario coming.

[P5]
As I struggled to continue speaking in my bewilderment, a pair of large eyes stared at me quietly.

[P6]
“Have I asked too much of you?”

[P7]
“No, it’s not that… What are you planning to do with my signature?”

[P8]
“Hmm. If you don’t want to, you don’t have to.”

[P9]
Hidden beneath his archaic, historical-drama way of speaking was a desperate eagerness he was trying to conceal.

[P10]
The tips of his feet scraped at the training ground floor like a puppy, and both his hands kept fidgeting restlessly. Those were proof enough.

[P11]
*The little guy is cute, though.*

[P12]
He was still a child. No matter how much of a king he was, he couldn’t hide his age.

[P13]
His expression was dignified, but his body language was honest. I let out a quiet laugh.

[P14]
“Why are you laughing?”

[P15]
“It’s nothing. So I just carve my name into this wooden tablet?”

[P16]
The young king’s lips twitched.

[P17]
“If possible, include your alias as well.”

[P18]
Why was he answering so seriously over something like this? I held back my laughter and picked up the dagger.

[P19]
Scritch, scritch, scritch.

[P20]
Sleeping Dragon of Shanxi, Jin Taekyung. I rested the wooden tablet on my knee and carefully carved the seven characters into it.

[P21]
That was when Zhu Bao suddenly asked,

[P22]
“Wouldn’t it be easier if you used Sword Energy?”

[P23]
“It would.”

[P24]
“Then why aren’t you using it?”

[P25]
“It’s not that I’m choosing not to. I can’t.”

[P26]
“You can’t use Sword Energy?”

[P27]
“I mean exactly what I said. I can’t use Sword Energy because I’m not a Peak master yet.”

[P28]
“You’re… not a Peak master?”

[P29]
I raised my head slightly. Zhu Bao was staring at me with a shocked expression.

[P30]
“Aren’t you the Sleeping Dragon of Shanxi?”

[P31]
“Yes, that’s me.”

[P32]
“And yet you can’t use Sword Energy? You’re not a Peak master?”

[P33]
“…That can happen.”

[P34]
“No, it can’t!”

[P35]
Wow. He almost sounded hurt.

[P36]
I had already been feeling a sense of relative deprivation because Sword Energy had been appearing so often lately. Now a little kid I had never seen before was twisting the knife.

[P37]
*Is being unable to use Sword Energy a crime?*

[P38]
I was hurt in my own way, and the young prince’s fandom had taken a hit too.

[P39]
I was wiping my nose in wounded frustration when he suddenly exclaimed,

[P40]
“How can you be so strong if you aren’t even a Peak master?”

[P41]
“What?”

[P42]
“One Question, One Kill Jopil, Blade of Flowers Jin Baekyang, and finally Pung Yang, the Red Wind Band Leader, not long ago. Weren’t all the enemies you’ve defeated powerful Peak masters?”

[P43]
Jopil was the only one I could honestly say I had defeated entirely with my own strength, but I nodded for the time being.

[P44]
“That’s right.”

[P45]
“How was such a thing possible?”

[P46]
“Well…”

[P47]
*The Inventory is unbelievably useful. And no one can beat a group attack.*

[P48]
*When things seem impossible, try rummaging through your Inventory. You might find an elixir worth half a jiazi or a weapon made of Ten-Thousand-Year Cold Iron.*

[P49]
*…I can’t exactly answer that way.*

[P50]
An image was something you built for yourself.

[P51]
I opened my mouth with a gentle smile.

[P52]
“Isn’t it because I was stronger?”

[P53]
“Wow!”

[P54]
“There’s a saying in Murim. The strong do not survive. Those who survive are strong.”

[P55]
“Wow!”

[P56]
“I’ve fought three Peak masters so far. I’ve even been attacked by dozens of First Rate masters.”

[P57]
“How could that be!”

[P58]
Zhu Bao clenched his tiny fists and let out an admiring gasp.

[P59]
He gave such great reactions that it made me want to keep talking. I continued, recalling the moments of crisis I had fought my way through.

[P60]
“But every time, I fought with everything I had and survived. Peak masters? Sword Energy? Those things aren’t important.”

[P61]
“Sword Energy isn’t important? Do you mean that?”

[P62]
“Of course.”

[P63]
*It’s fucking important.*

[P64]
Every person I met kept drawing out Sword Energy like endless strings of rice cake, and I was the only one who couldn’t use it.

[P65]
Every fight left me wondering whether I had a human life or a fly’s.

[P66]
*Make sure you eat plenty of elixirs. Without Sword Energy, your body will suffer.*

[P67]
I shamelessly placed a hand on the young king’s shoulder and whispered,

[P68]
“The desire to win. The unbreakable will to never give up until the very end. That is what made the Sleeping Dragon of Shanxi who he is today.”

[P69]
“An unbreakable will…!”

[P70]
Zhu Bao’s small body trembled. Then, after letting out a heated sigh, he opened his mouth.

[P71]
“Can I become like you?”

[P72]
“You can. From what I just saw of your training, you look like you’ll become a master in no time.”

[P73]
“D-Do you really mean that?”

[P74]
*Without the System, it would be difficult.*

[P75]
*But you have to water a growing sprout.*

[P76]
I nodded at those enormous, sparkling eyes. Then I added a few more characters to the completed wooden tablet and handed it over.

[P77]
“Look at this whenever things get difficult, and let it give you strength.”

[P78]
“What is this…?”

[P79]
The young king examined the tablet and broke into a radiant smile.

[P80]
“Thank you very much. I shall have this tablet enlarged and hang it on the signboard of the Shanxi Provincial Office.”

[P81]
“…That?”

[P82]
“Of course. Everyone who enters and leaves this place will read your famous words.”

[P83]
I looked at Zhu Bao, who was gazing fondly at the wooden tablet, and thought,

[P84]
*He’s going to hang that on the signboard of the Shanxi Provincial Office?*

[P85]
*Dreams☆come true.*

[P86]
—Sleeping Dragon of Shanxi, Jin Taekyung—

[P87]
*…That?*

[P88]
* * *

[P89]
When we returned to the grand hall, it had been restored to pristine condition as though nothing had ever happened.

[P90]
Once the servants filled the newly placed tables with all kinds of delicacies, Prince Shangshan Zhu Bao, seated at the head of the table, spoke.

[P91]
“I thank you all for willingly answering my summons. Now, please eat your fill.”

[P92]
*Ding.*

[P93]
> **System**
>
> Quest condition, **Attend the luncheon hosted by the City Lord**, has been fulfilled!
>
> The Quest Reward will be issued after the luncheon ends.

[P94]
The atmosphere that followed was warm and cheerful. With the young king, the host and master of the gathering, grinning from ear to ear, it could hardly have been otherwise.

[P95]
“I have heard that One Question, One Kill Jopil was an exceptionally vicious man. Could you tell me what he was like?”

[P96]
“Oh, that bastard was absolutely brutal. Well, you see…”

[P97]
“I’ve heard that Blade of Flowers Jin Baekyang was a Peak master whose name was known even in the Central Plains. How strong was he?”

[P98]
“He was insanely strong. Completely crazy.”

[P99]
“Young Hero Jin, His Highness is listening. Please be more mindful of your language.”

[P100]
“Ah, sorry. Anyway, to tell you about what happened then…”

[P101]
After telling stories for quite some time, I was exhausted. I handed Cheongpung over to Zhu Bao, who continued asking me questions, and quietly withdrew.

[P102]
“Sleeping Dragon of Shanxi, where are you going?”

[P103]
“You know the Sword Saint, Mae Jonghak, right? This guy is his disciple.”

[P104]
“The Sword Saint!”

[P105]
“And he’s a Peak master, too. Ask him to teach you Sword Energy.”

[P106]
I left Zhu Bao behind, happy as a child who had met Santa Claus, and slipped away to the side.

[P107]
I saw the young prodigies of the Five Gates of Shanxi forcing food down without managing to say a word, as well as two people engaged in a fairly serious conversation.

[P108]
Neither the former nor the latter made for company I particularly wanted to join.

[P109]
*I’ll just eat.*

[P110]
But before I could take more than a few pieces of meat, a syrupy voice wormed into my ears.

[P111]
“Young Hero Jiiin.”

[P112]
“…What?”

[P113]
The moment I heard that voice, my appetite vanished.

[P114]
“What are you doing all by yourself over there? Come over and talk with us.”

[P115]
“No, thank you. I’m hungry.”

[P116]
“It’s about the Jin Family of Taiyuan.”

[P117]
“I don’t get involved in family affairs. Talk to my eldest brother instead.”

[P118]
“That’s unfortunate. In that case, I suppose we’ll have no choice but to entrust it to the Seongun Escort Bureau.”

[P119]
Seongun Escort Bureau? The name sounded familiar. Then I remembered—it was the family of the man I had thoroughly beaten at Honghwa Inn yesterday.

[P120]
That guy had been the Young Bureau Head of the Seongun Escort Bureau, hadn’t he?

[P121]
“Why the Seongun Escort Bureau?”

[P122]
Hong Jin curled up the corners of his mouth.

[P123]
“Oh, nothing. Please eat your meal. They say even a dog is left alone while it’s eating, so how could I bother the Sleeping Dragon of Shanxi?”

[P124]
“…”

[P125]
“Hee-hee. I was joking. Don’t look so serious. Come over and sit down.”

[P126]
Hong Jin pulled out the chair beside him. I sat down as though I had no choice.

[P127]
Beside Li Feng, of course.

[P128]
As I’ve said before, my backside is precious.

[P129]
“Let’s hear what this is about. I’m not very knowledgeable in this area, so I may not be much help.”

[P130]
Hong Jin, who had been pretending to sulk with his lips stuck out, spoke.

[P131]
“It doesn’t matter if Young Hero Jin doesn’t make a decision here. You only need to pass the matter along to the Lesser Family Head. Now, Assistant Commissioner Li?”

[P132]
Li Feng took over.

[P133]
“We would like to borrow the strength of the Jin Family of Taiyuan for this matter.”

[P134]
“This matter being…?”

[P135]
“I believe you’re aware of our plan to establish a primary connection between Shaanxi and Shanxi.”

[P136]
“The thing you originally intended to do with the Zhongnan Sect?”

[P137]
Hong Jin, who had been watching us, nodded.

[P138]
“To be honest, the Zhongnan Sect isn’t a bad partner. It’s a massive sect belonging to the Nine Sects and One Gang, and its leadership, including the Sect Leader, the Wind-and-Cloud Sword Lord, has a practical nature. They’re different from the other, relatively closed-off Murim sects.”

[P139]
“Then was there really any need to change partners? If you weren’t going to work with Huashan from the beginning, it might have been better to leave things as they were.”

[P140]
“It was a decision I reached after giving it a great deal of thought. Although we overturned it today.”

[P141]
Hong Jin continued with a faint smile.

[P142]
“I’m not a martial artist, but I know very well what position the Sword Saint occupies in Murim.”

[P143]
“…”

[P144]
“But it has been more than thirty years since the Sword Saint disappeared. If we had known from the beginning that he had remained in Huashan and was raising successors, we wouldn’t have chosen the Zhongnan Sect.”

[P145]
When he finished speaking, Hong Jin shot Li Feng a reproachful look.

[P146]
Apparently, Li Feng had known about the Sword Saint and Cheongpung for the past ten years and hadn’t said a word.

[P147]
“Deputy Military Commissioner, I’ll say it again: that was classified information belonging to our sect. There was simply no longer any reason to conceal it once Martial Uncle Cheongpung descended the mountain.”

[P148]
Li Feng answered calmly, then turned toward me.

[P149]
“I’ll get straight to the point. We need an Escort Bureau capable of expanding into the Central Plains, beginning with Shaanxi.”

[P150]
“Ah.”

[P151]
I had a rough idea of what was going on.

[P152]
They were asking the Jin Family of Taiyuan to provide material or human resources.

[P153]
“Are you planning to create an Escort Bureau?”

[P154]
“Something similar. However, we would like to borrow the name of the Jin Family of Taiyuan. In return, we’ll provide half the funding and every possible convenience.”

[P155]
They were practically offering to back us outright. Wouldn’t it be better for them to create their own Escort Bureau at this point?

[P156]
As I wondered about that, I suddenly remembered what Jin Mukyung had told me several days ago.

[P157]
*He said that the current Emperor also assassinated his older brother, the Crown Prince, and ascended the throne. I’m sure of it.*

[P158]
It was only an unconfirmed rumor, but judging by how cautiously these two were acting, it didn’t seem entirely baseless.

[P159]
Could the Emperor’s wariness have been the reason he sent his only younger brother to Shanxi Province, a place regarded as a frontier region?

[P160]
*Hmm. This feels suspicious too.*

[P161]
As I wondered whether I had gotten myself entangled in something dangerous, the two men spoke to me.

[P162]
“We’ll arrange a meeting soon regarding this matter, so please speak well of it to the Lesser Family Head.”

[P163]
“Young Master Jin, you know this is a good offer, right?”

[P164]
“I know. I do, but…”

[P165]
In a way, this was someone else’s family feud. If they were ordinary brothers, they might fight over who got to eat one more ice cream, end up with a bloody nose, and leave it at that.

[P166]
But this wasn’t ice cream. It was the imperial throne.

[P167]
That meant it wouldn’t end with a bloody nose.

[P168]
“I’ll make sure to pass it along to my eldest brother.”

[P169]
I deliberately kept my answer vague. Jin Wikyung would be the one making the decision anyway, so there was no reason for me to worry about it. Unless he asked for my opinion first, that was.

[P170]
“That’s enough. He won’t ignore what Young Master Jin says. We’ve heard plenty about how much the Lesser Family Head cares for his younger brothers.”

[P171]
*So everyone in the neighborhood has heard about it.*

[P172]
I drained my cup of liquor with an embarrassed expression, and my eyes met the four of them sitting at the far end of a table some distance away, all looking as though they were about to get indigestion.

[P173]
Oh, right. I almost forgot something.

[P174]
“Hey. Comrade Chairman—no, Deputy Military Commissioner.”

[P175]
“Yes?”

[P176]
“That Escort Bureau business. Wouldn’t it be enough to simply change the sign?”

[P177]
Unlike the bewildered Li Feng, Hong Jin grinned.

[P178]
“You have a place in mind?”

[P179]
“The one the two of you were talking about earlier.”

[P180]
“The Seongun Escort Bureau? Don’t take them too lightly. It’s the most prestigious Escort Bureau in Shanxi, after all. They’ll be difficult to swallow in one bite.”

[P181]
“That’s why we have to chew thoroughly.”

[P182]
I could tell exactly what we were dealing with from the Young Bureau Head. If Hong Jin and Li Feng helped the Jin Family of Taiyuan as it stood now, we could chew through the whole thing—bones and all—and still digest it.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 진백양    | **Jin Baekyang**   |
| 조필     | **Jopil**          |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 화양검    | **Blade of Flowers**          | Jin Baekyang   |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 산서오문   | **Five Gates of Shanxi**         |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 영약     | **elixir**                                       |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 표국     | **Escort Bureau**                            |
| 소국주    | **Young Bureau Head**                        |
| 사숙     | **Martial Uncle**                            |
| 큰형     | **eldest brother**                           |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 본문      | **our sect / this sect**                                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 황태자 | **Crown Prince** | The Emperor's older brother in Taekyung's recollection. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 144,
  "passed": true,
  "metrics": {
    "source_characters": 5859,
    "translation_characters": 13386,
    "length_ratio": 2.285,
    "source_paragraphs": 178,
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
        "korean": "인도",
        "preferred": "Human Butcher"
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
        "korean": "고자",
        "preferred": "eunuch"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "기해",
        "preferred": "qi sea"
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
