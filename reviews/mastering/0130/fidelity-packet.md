# Fidelity Gate — Chapter 130

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
  1|＃130화
  2|
  3|
  4|
  5|변방의 겨울은 혹독하다. 옷깃을 파고드는 칼바람에 중년 사내가 몸을 부르르 떨었다.
  6|
  7|“어흐으, 더럽게 춥네.”
  8|
  9|사내, 석칠은 산서성 남부에 있는 성운표국(盛運鏢局)의 쟁자수다.
 10|
 11|하루 반나절이 넘게 백 근(斤)이 넘어가는 짐수레를 끌어 온몸이 땀으로 흠뻑 젖었고, 지금처럼 잠시 휴식을 취할 때는 엄청난 한기와 싸워야 했다.
 12|
 13|“형님, 짐수레 얼른 놓고 빨리 와서 불이나 좀 쬐시오. 그러다가 얼어 죽겠네.”
 14|
 15|어느새 모닥불 앞에 쭈그려 앉은 동료 쟁자수가 말했다. 석칠은 퉁명스럽게 대답하며 걸음을 옮겼다.
 16|
 17|“이놈아, 내가 먹여 살려야 할 입이 다섯이다. 죽으려면 한참 멀었어.”
 18|
 19|“그렇지. 여우 같은 마누라와 토끼 같은 자식들 생각하면 못 죽지.”
 20|
 21|“여우는 무슨. 곰이야, 곰.”
 22|
 23|“방금 그거 유언이오? 형수님이 들으면 모가지를 꺾어 버릴 텐데.”
 24|
 25|“없는 데서는 나라님 욕도 하는 법이야. 몰라?”
 26|
 27|석칠은 모닥불 앞으로 바짝 다가갔다.
 28|
 29|말똥을 장작으로 쓰다 보니 고약한 냄새가 사방으로 풍겼지만 이십 년 가까이 쟁자수 일을 해 온 그에게는 밥 짓는 냄새만큼이나 익숙했다.
 30|
 31|“어따, 이제야 좀 살겠다.”
 32|
 33|“그런데 형님, 너무 야박한 거 아니오?”
 34|
 35|“응? 이건 또 무슨 헛소리야?”
 36|
 37|동료 쟁자수가 실실 웃으며 턱짓했다.
 38|
 39|“신참도 데려오셔야지. 혼자만 살겠다고 냅다 오는 법이 어디 있소?”
 40|
 41|꽁꽁 언 손을 녹이던 석칠이 고개를 돌렸다. 그의 시선 끝에 멀뚱멀뚱한 얼굴로 눈 덮인 바위 위에 앉아 있는 한 청년이 보였다.
 42|
 43|‘저놈 저거, 또 저러고 있네.’
 44|
 45|청년은 하남(下南)에서 새로 구한 쟁자수다. 이번 표행의 책임자인 송 표두에게 듣기로는 그럭저럭 밥값은 할 것 같아 받아 줬다고 한다.
 46|
 47|‘뭐, 사람이야 늘 부족하니까.’
 48|
 49|문제는 젊은 놈이 대체 무슨 생각을 하는지, 지금처럼 넋 놓고 있을 때가 많다는 거다.
 50|
 51|쯧쯧 혀를 차는 석칠에게 동료 쟁자수가 물었다.
 52|
 53|“왜요, 좀 이상한 놈입니까?”
 54|
 55|“일은 잘해. 보기보다 힘이 장사더라고.”
 56|
 57|“그럼 됐지, 뭘.”
 58|
 59|“되긴 뭐가 돼. 젊은 놈이 허구한 날 저러고 있으니 답답해서 그렇지. 나 때는 말이야…….”
 60|
 61|“풍운의 꿈을 품고 하루하루 열심히 살았다고 말하고 싶은 거요?”
 62|
 63|“그럼, 사내라면 원대한 목표를 세우고 나아갈 줄 알아야지.”
 64|
 65|“그 원대한 목표라는 게 천하제일의 쟁자수는 아니었을 테고.”
 66|
 67|“이 자식이 아까부터.”
 68|
 69|발끈하는 석칠의 반응에 동료 쟁자수가 화제를 돌렸다.
 70|
 71|“그런데 저 친구, 이름이 뭐요?”
 72|
 73|“청풍(淸風).”
 74|
 75|“아따, 이름 한번 멋있네. 잘 어울리기도 하고.”
 76|
 77|“그건 그래.”
 78|
 79|청년, 청풍을 내심 못마땅하게 생각하던 석칠이지만 그 말에는 십분 공감했다.
 80|
 81|서글서글한 인상과 맑은 눈동자를 보고 있노라면 이상하게 마음이 편안해지고 화도 가라앉았다.
 82|
 83|“이보게, 신참!”
 84|
 85|동료 쟁자수의 말에 청풍이 고개를 돌렸다.
 86|
 87|“저요?”
 88|
 89|“그럼 여기 신참이 자네 말고 누가 있나? 이쪽으로 와서 불이나 좀 쬐게. 거기 앉아 있다가는 궁둥이가 뜯어져 나갈걸.”
 90|
 91|“그런 경험도 나쁘지 않죠.”
 92|
 93|“경험? 무슨 경험?”
 94|
 95|“엉덩이가 뜯겨 나가는 경험이요. 제가 한 번도 그래 본 적이 없어서.”
 96|
 97|잠깐 말이 없던 동료 쟁자수가 석칠에게 속삭였다.
 98|
 99|“저거 뭐 하는 놈입니까?”
100|
101|“몰라, 애가 좀 이상해. 뭘 잘못 먹었나 봐.”
102|
103|청풍이 고개를 갸웃했다.
104|
105|“아침에 만두 두 개 먹었는데요.”
106|
107|“……귀가 밝구먼. 알았으니까 와서 앉기나 하게.”
108|
109|“그럴까요?”
110|
111|터벅터벅 걸어온 청풍이 모닥불 앞에 앉자 으레 하는 질문들이 날아들었다.
112|
113|“어디서 왔나?”
114|
115|“하남에서요.”
116|
117|“하남 사람이었군.”
118|
119|“한 달 전에는 호북에 있었고요.”
120|
121|“음. 호북도 좋지.”
122|
123|“그전에는…….”
124|
125|쟁자수가 석칠에게 말했다.
126|
127|“골 때리네.”
128|
129|“그렇지? 이야기하다 보면 나까지 이상해지는 기분이라니까.”
130|
131|“어떻게 이런 놈을 옆에 끼고 달포씩이나 버티셨소?”
132|
133|“그래서 요즘 말 안 걸어. 마지막으로 대화한 게 사흘쯤 됐나?”
134|
135|청풍이 진지한 얼굴로 대답했다.
136|
137|“나흘 하고도 세 시진이요.”
138|
139|“…….”
140|
141|“…….”
142|
143|두 사람은 청풍의 머리통을 한 대 쥐어박고 싶은 마음을 간신히 억눌렀다.
144|
145|“그래서 어디 사람인가?”
146|
147|“산에서 살았어요.”
148|
149|“내 말은 그게 아니고…… 아닐세, 그거라도 대답해 줘서 고맙네.”
150|
151|“별말씀을요.”
152|
153|해맑게 웃는 청풍의 모습을 보니 신기하게도 화가 수그러든다.
154|
155|종잡을 수 없는 엉뚱한 언행에 아이처럼 순수한 웃음. 난생처음 보는 별종에 관한 호기심이 이어졌다.
156|
157|“한데, 산에서 살았다니?”
158|
159|“말 그대로예요. 어릴 때부터 산에서 농사도 짓고, 약초도 캐고. 그 외에도 이것저것 하면서 살았거든요.”
160|
161|두 사람은 청풍이 화전민 출신임을 지레짐작했다.
162|
163|화전민 중 대부분은 악질 지주의 횡포를 못 견뎌서, 혹은 크고 작은 죄를 지어서 관의 눈을 피해 산으로 들어갔다.
164|
165|“고생이 많았겠군.”
166|
167|“전 재밌었는데요?”
168|
169|“아, 그래?”
170|
171|화전민 생활이 재미있을 수가 있나? 순간 석칠의 머릿속에 그런 생각이 스쳤지만, 굳이 물어볼 필요를 느끼진 못했다.
172|
173|“그럼 하산(下山)하게 된 계기는 뭔가?”
174|
175|“산속 생활이 심심해져서요. 세상 구경도 하고 싶고, 만나고 싶은 사람도 있었거든요.”
176|
177|“그래서 하남에 온 거로군.”
178|
179|“네. 어쩌다 보니 헛걸음을 하게 됐는데…… 지금도 나쁘지 않아요. 표행이란 것도 상당히 재밌어요.”
180|
181|“표행이 재미있다고?”
182|
183|청풍이 활짝 웃으며 대답했다.
184|
185|“사람 구경하는 것도 재밌고, 땅도 보고, 하늘도 보고. 생각하는 것도 재밌어요.”
186|
187|오랜 세월 쟁자수 일을 해 온 석칠에게는 이젠 지긋지긋한 광경이다.
188|
189|피곤과 생계에 대한 고민으로 찌들어 있는 사람들, 축축한 땅과 미친 듯이 불어오는 칼바람. 머릿속엔 그저 이번 표행으로 얼마의 수당을 받을지만 꽉 차 있다.
190|
191|‘하긴, 아직 젊으니까 할 수 있는 소리지.’
192|
193|더군다나 평생 산에서 살아온 화전민 출신이니 그럴 법도 하다.
194|
195|곧 냉정한 현실을 알게 되고 점차 나이를 먹으면 자신과 같은 모습이 되어 가지 않을까?
196|
197|‘나도 저럴 때가 있었는데.’
198|
199|석칠은 부러움과 안타까움이 섞인 눈빛으로 청풍을 바라보다가 입을 열었다.
200|
201|“그냥 헛소리라고 생각하고 듣게.”
202|
203|괜한 오지랖인 건 알지만, 이 순박한 청년에게 현실을 알려 주고 싶었다.
204|
205|쟁자수로 시작해서 쟁자수로 늙어 죽기에는 너무 창창한 인생 아닌가.
206|
207|“할 만한 것도 잠깐이야. 십 년, 이십 년쯤 되면 미래가 잘 보이지 않는다 이 말일세. 쟁자수는 아무리 날고 기어 봐야 쟁자수거든. 차라리 동네 무관(武關)에서 삼류 무공이라도 배워서 표사로 시작하게. 그편이 훨씬 나아.”
208|
209|청풍은 눈을 깜빡였다.
210|
211|“아, 그래요?”
212|
213|“그래요, 가 아니고 그렇게 하란 소리야. 무공을 익히기에는 늦은 나이지만 혹시 아나? 의외로 무재가 뛰어나서 잘나가는 일류 고수가 될지.”
214|
215|“일류 고수…….”
216|
217|가만히 듣고 있던 동료 쟁자수가 혀를 찼다.
218|
219|“거, 너무 헛바람 불어넣는 거 아니오? 일류 고수가 뉘 집 개 이름도 아니고.”
220|
221|“말이 그렇다는 거야, 말이. 저 나이에 쟁자수로 만족한다는 게 말이 돼?”
222|
223|“뭐, 그건 그렇죠. 나도 십 년만 젊었으면 여기서 안 이러고 있지.”
224|
225|“거봐.”
226|
227|석칠이 청풍의 어깨를 두드렸다.
228|
229|“들었지? 일이 년만 알뜰하게 모아서 무관 등록 하는 게 훨씬 나아. 그때까진 내가 옆에서 잘 알려 줌세.”
230|
231|청풍이 고개를 갸웃했다.
232|
233|“일이 년이요?”
234|
235|“왜, 너무 긴가? 자네가 세상 물정을 몰라서 그런가 본데, 무관비가 한두 푼 하는 게 아니야. 아무리 적게 잡아도 일 년은…….”
236|
237|“아뇨, 제가 그 전에 관둘 거라서.”
238|
239|“관둔다고? 언제?”
240|
241|“지금이요.”
242|
243|“응?”
244|
245|“엥?”
246|
247|청풍이 해맑게 웃었다.
248|
249|“제가 산서성까지 가는 길을 몰라서요. 마침 산서로 가는 표행이 있길래 끼워 달라고 한 건데요.”
250|
251|“……그래서?”
252|
253|“이제 하루만 더 가면 태원(太元)이니까 이쯤에서 헤어지려고요.”
254|
255|석칠과 동료 쟁자수는 이게 뭔가 싶은 얼굴로 서로를 마주 보았다.
256|
257|“저놈 뭐야? 송 표두 말로는 일 년짜리 계약서에 수결(手決)했다고 하지 않았나?”
258|
259|“나도 그렇게 알고 있소. 그러니까 최고참인 형님한테 배우라고 붙여 놓은 거였고.”
260|
261|석칠이 혼란스러운 표정으로 청풍에게 물었다.
262|
263|“자네, 하남에서 합류할 때 뭔가에 수결했었지?”
264|
265|“앗, 네.”
266|
267|“그거 갖고 있으면 줘 봐.”
268|
269|청풍이 품에서 누리끼리한 죽간 하나를 꺼내어 보여 줬다.
270|
271|앞으로 일 년간 성운표국에서 쟁자수로 일할 것이며, 도중 이탈 시 위약금을 문다는 내용의 계약서였다.
272|
273|“글은 읽을 줄 알지?”
274|
275|“네 살 때 사서삼경을 땠지요.”
276|
277|“그딴 헛소리는 하지 말고. 거기 읽어 봐. 그래, 그 부분. 소리 내서 크게.”
278|
279|청풍이 또랑또랑한 목소리로 석칠이 알려 준 부분을 읽어 내려갔다.
280|
281|“수결 시 번복할 수 없으며, 무단이탈 시 은자 오십 냥의 위약금 혹은 그에 상응하는 대가를 치르게 될 것.”
282|
283|“은자 오십 냥이 얼마인지는 알 테고. 그에 상응하는 대가라는 게 무슨 뜻인지 아나?”
284|
285|곰곰이 생각에 잠겨 있던 청풍이 이마를 탁 쳤다.
286|
287|“혹시 몸으로 때우라는?”
288|
289|“그래, 이 멍청한 친구야. 표국이 무슨 무골호인들만 모여 있는 곳인 줄 알았어?”
290|
291|석칠은 혈압이 올라 뒷덜미가 당겼다. 이놈의 머릿속에 뭐가 들어 있는지 정수리를 쪼개 보고 싶을 정도였다.
292|
293|‘어떻게 이런 놈이 다 있지? 산에서만 살아서 그런가?’
294|
295|천하를 가로지르며 물건을 운송할 때 겪는 위험은 상상을 초월한다. 마적, 수적, 산적, 온갖 도적 떼와 경쟁 표국의 견제까지.
296|
297|행여 그 모든 장애물을 넘어도 자연재해 한 번 잘못 만나면 표행은 실패로 돌아간다.
298|
299|어지간한 무림 문파만큼, 아니 그 이상으로 철저하고 거친 것이 표국이었다.
300|
301|‘그런데 수결까지 찍어 놓고 뭐? 이쯤에서 헤어지겠습니다?’
302|
303|눈앞의 이 젊은 놈은 세상을 몰라도 너무 모른다.
304|
305|석칠은 애먼 목숨 구한다는 마음으로 입을 열었다.
306|
307|“혹시나 해서 말해 두는데, 도망칠 생각은 일찌감치 접게. 그냥 일 년 동안 돈 번다 생각하고 일하란 말이야. 알겠나?”
308|
309|“일 년은 너무 긴데요. 내일 하루까지는 일할 수 있을 것 같은데.”
310|
311|“야, 이 새끼야!”
312|
313|“형님, 형님 진정하십쇼! 괜히 송 표두가 보기라도 하면 피곤해져요.”
314|
315|“놔! 안 놔?”
316|
317|석칠의 눈이 뒤집힌 그때였다.
318|
319|“어, 이 정도면 위약금으로 충분하지 않나요?”
320|
321|쩔그럭.
322|
323|청풍이 내민 손을 확인한 두 사람이 눈을 부릅떴다.
324|
325|말발굽 모양의 그것은 눈보다 새하얀 은빛으로 번쩍거리고 있었다.
326|
327|“은, 은원보(銀元寶)?”
328|
329|“그것도 두 개나!”
330|
331|은자 오십 냥에 해당하는 은원보가 무려 두 개.
332|
333|은자 백 냥은 일개 쟁자수가 십 년간 뼈 빠지게 일해도 벌기 힘든 엄청난 거금이다.
334|
335|그런 거금이 화전민 청년의 품에서 나올 줄이야.
336|
337|“어, 어, 어, 어떻게.”
338|
339|“집 나오면서 노잣돈을 좀 받았거든요.”
340|
341|청풍의 천진난만한 대답에 두 사람은 입을 딱 벌렸다.
342|
343|도대체 어느 집 자제길래 은자 백 냥을 노잣돈으로 준단 말인가. 심지어 소불알처럼 축 늘어진 전낭을 보니 저게 끝이 아닌 듯했다.
344|
345|“일단 위약금은 이걸로 해결할 수 있을 것 같은데…….”
346|
347|두 사람은 미친 듯이 고개를 끄덕였다.
348|
349|“됩니다. 되고 말고요.”
350|
351|“왜 갑자기 존댓말을 쓰세요?”
352|
353|“그냥 이게 편해서 그럽니다.”
354|
355|“맞습니다. 세상에서 제일 편합니다.”
356|
357|“아, 그러시다면야 뭐.”
358|
359|신기하다는 듯 두 사람을 바라본 청풍이 은원보 두 개를 건넸다.
360|
361|“전 이만 가 볼게요. 이건 위약금이라고 전해 주세요.”
362|
363|“이, 이걸 다 말입니까?”
364|
365|“너무 많은데…….”
366|
367|“남으면 두 분이 나눠 쓰세요. 제가 돈 쓰는 법을 잘 몰라서. 따뜻한 옷이라도 하나씩 사 입으세요. 비싼 털가죽 달린 걸로.”
368|
369|“……!”
370|
371|주섬주섬 봇짐 하나를 둘러메고 떠나려는 청풍의 모습에 석칠이 황급히 입을 열었다.
372|
373|“호, 혹시 성함이?”
374|
375|“청풍이요. 보름 전까지는 하남 사람이었고, 지난달에는 호북, 그전에는 섬서에 살았죠.”
376|
377|대답을 마친 청풍은 태원을 향해 성큼성큼 걷기 시작했다.
378|
379|하늘을 푸르렀고, 축축한 땅 위로는 때 이른 새싹이 돋아나고 있었다.
380|
381|“이번 봄은 좀 일찍 오려나?”
382|
383|그는 활짝 웃으며 생각했다. 이번 봄에도 매화가 흐드러지게 피었으면 좋겠다고.
384|
385|문득 얼마 전 몰래 뛰쳐나온 화산(華山)의 연화봉(蓮花峰)이 생각났다.
```

## Assembled English

```markdown
[P1]
# Chapter 130

[P2]
Winter in the borderlands was harsh. A middle-aged man shivered violently as the knife-sharp wind cut through his collar.

[P3]
“Ugh, it’s cold as hell.”

[P4]
The man, Seokchil, was a porter for the Seongun Escort Bureau in southern Shanxi Province.

[P5]
He had spent more than a day and a half hauling a cart loaded with over a hundred geun of cargo, soaking his entire body in sweat. Whenever he took a brief rest, as he was now, he had to fight against the brutal cold.

[P6]
“Hyung, leave the cart and hurry over. Come warm yourself by the fire before you freeze to death.”

[P7]
A fellow porter, already crouched in front of the campfire, called out. Seokchil answered gruffly as he walked over.

[P8]
“Brat, I have five mouths to feed. I’ve got a long way to go before I can die.”

[P9]
“True. You can’t die with a fox of a wife and rabbit-like children waiting for you.”

[P10]
“What fox? She’s a bear. A bear.”

[P11]
“Were those your last words? If your wife hears you, she’ll wring your neck.”

[P12]
“You can curse the king behind his back. Didn’t you know?”

[P13]
Seokchil moved closer to the campfire.

[P14]
They used horse manure for firewood, so a foul smell spread in every direction. But after nearly twenty years as a porter, Seokchil was as used to it as he was to the smell of cooking rice.

[P15]
“Ah, now I feel alive again.”

[P16]
“But Hyung, aren’t you being a little stingy?”

[P17]
“Huh? What nonsense are you talking about now?”

[P18]
His fellow porter grinned and jerked his chin toward something.

[P19]
“You should bring the rookie over, too. Where’s the sense in rushing over here to save yourself alone?”

[P20]
Seokchil, who had been warming his frozen hands, turned his head. At the end of his gaze sat a young man on a snow-covered rock, staring blankly into space.

[P21]
*That kid’s doing it again.*

[P22]
The young man was a new porter they had picked up in Henan. According to Escort Chief Song, who was in charge of this escort run, the young man seemed capable enough to earn his keep, so they had taken him on.

[P23]
*Well, we’re always short on people.*

[P24]
The problem was that no one could tell what the young man was thinking. He often sat there in a daze, just as he was doing now.

[P25]
As Seokchil clicked his tongue, his fellow porter asked,

[P26]
“Why? Is he a little strange?”

[P27]
“He does his work well. He’s surprisingly strong for someone who doesn’t look like much.”

[P28]
“Then what’s the problem?”

[P29]
“What do you mean, what’s the problem? It’s frustrating to see a young fellow sitting around like that day after day. Back when I was his age…”

[P30]
“You want to say you dreamed of making your mark on the world and worked hard every day?”

[P31]
“Of course. A man should know how to set a grand goal and move toward it.”

[P32]
“I assume that grand goal wasn’t becoming the greatest porter under heaven.”

[P33]
“You little—”

[P34]
At Seokchil’s furious reaction, his fellow porter quickly changed the subject.

[P35]
“By the way, what’s that fellow’s name?”

[P36]
“Cheongpung.”

[P37]
“Now that’s a fine name. Suits him, too.”

[P38]
“That’s true.”

[P39]
Seokchil secretly disliked the young man, Cheongpung, but he had to agree completely.

[P40]
Something about the young man’s open, pleasant features and clear eyes put people strangely at ease and soothed their anger.

[P41]
“Hey, rookie!”

[P42]
At his fellow porter’s shout, Cheongpung turned his head.

[P43]
“Me?”

[P44]
“Who else would I be talking to? Come over here and warm yourself by the fire. If you keep sitting there, your butt will get ripped right off.”

[P45]
“An experience like that wouldn’t be bad.”

[P46]
“An experience? What experience?”

[P47]
“The experience of having my butt ripped off. I’ve never had that happen before.”

[P48]
His fellow porter was silent for a moment before whispering to Seokchil,

[P49]
“What kind of guy is he?”

[P50]
“I don’t know. The kid’s a little strange. Maybe he ate something bad.”

[P51]
Cheongpung tilted his head.

[P52]
“I ate two dumplings this morning.”

[P53]
“…Sharp ears, huh? Fine, just come sit down.”

[P54]
“Should I?”

[P55]
Cheongpung trudged over and sat down in front of the fire. The usual questions immediately began flying at him.

[P56]
“Where are you from?”

[P57]
“Henan.”

[P58]
“So you’re from Henan.”

[P59]
“I was in Hubei a month ago.”

[P60]
“Hmm. Hubei’s nice, too.”

[P61]
“Before that…”

[P62]
The porter turned to Seokchil.

[P63]
“This guy’s unbelievable.”

[P64]
“Right? Talking to him makes me feel like I’m going strange, too.”

[P65]
“How have you put up with him beside you for over a month?”

[P66]
“That’s why I stopped talking to him lately. Has it been about three days since our last conversation?”

[P67]
Cheongpung answered with a serious expression.

[P68]
“Four days and three shichen.”

[P69]
“…”

[P70]
“…”

[P71]
The two men barely suppressed the urge to smack him over the head.

[P72]
“So where are you from?”

[P73]
“I lived in the mountains.”

[P74]
“That’s not what I meant… No, never mind. Thank you for answering that, at least.”

[P75]
“You’re welcome.”

[P76]
Strangely, Cheongpung’s bright smile made their anger subside.

[P77]
His unpredictable, bizarre remarks were paired with an innocent smile like a child’s. Their curiosity about this strange young man, unlike anyone they had ever seen, continued to grow.

[P78]
“But you said you lived in the mountains?”

[P79]
“Just like it sounds. I grew crops and gathered medicinal herbs there from the time I was young. I did all sorts of other things, too.”

[P80]
The two men jumped to the conclusion that Cheongpung was from a slash-and-burn farming community.

[P81]
Most slash-and-burn farmers went into the mountains to escape the cruelty of vicious landlords or to avoid the authorities after committing one crime or another.

[P82]
“You must have had a hard life.”

[P83]
“But I had fun.”

[P84]
“Oh, really?”

[P85]
Could life as a slash-and-burn farmer really be fun? The thought briefly crossed Seokchil’s mind, but he saw no reason to ask.

[P86]
“Then what made you come down from the mountain?”

[P87]
“Life there got boring. I wanted to see the world, and there were people I wanted to meet.”

[P88]
“So that’s why you came to Henan.”

[P89]
“Yes. It turned out to be a wasted trip, but… things aren’t bad now, either. This escort work is pretty interesting, too.”

[P90]
“You find escort work interesting?”

[P91]
Cheongpung answered with a broad smile.

[P92]
“Watching people is interesting. Looking at the land and the sky is interesting, too. Thinking is fun.”

[P93]
To Seokchil, who had spent so many years as a porter, they were all sights he was sick to death of.

[P94]
People worn down by exhaustion and worries about making a living. Damp earth and knife-sharp winds blowing like mad. The only thought filling his head was how much he would be paid for this escort run.

[P95]
*Well, he’s still young. That’s why he can say things like that.*

[P96]
Besides, he had lived in the mountains all his life and came from a slash-and-burn farming community. His attitude was understandable.

[P97]
Wouldn’t he learn about the harsh realities of life soon enough and gradually become just like Seokchil as he grew older?

[P98]
*I used to be like that, too.*

[P99]
Seokchil looked at Cheongpung with a mixture of envy and pity before opening his mouth.

[P100]
“Just listen to this as nonsense.”

[P101]
He knew he was meddling where he wasn’t wanted, but he wanted to tell this innocent young man about the realities of life.

[P102]
Wasn’t his life too promising to start as a porter and grow old and die as one?

[P103]
“Anything seems worthwhile for a while. But after ten or twenty years, you stop seeing much of a future ahead of you. No matter how hard a porter works or how talented he is, he’s still a porter. You should learn even Third Rate martial arts at a local martial arts academy and start working as an escort. You’d be much better off.”

[P104]
Cheongpung blinked.

[P105]
“Oh, really?”

[P106]
“Not ‘oh, really?’ I’m telling you to do it. You’re a little old to start learning martial arts, but who knows? Maybe you have exceptional martial talent and could become a successful First Rate master.”

[P107]
“A First Rate master…”

[P108]
His fellow porter, who had been listening quietly, clicked his tongue.

[P109]
“Isn’t that giving him too much false hope? A First Rate master isn’t some dog’s name.”

[P110]
“I’m speaking hypothetically. What kind of sense does it make for someone his age to be satisfied with being a porter?”

[P111]
“Well, you’re right about that. If I were ten years younger, I wouldn’t be doing this either.”

[P112]
“See?”

[P113]
Seokchil patted Cheongpung on the shoulder.

[P114]
“You heard him, right? Save carefully for a year or two and enroll in a martial arts academy. It’ll be much better for you. Until then, I’ll teach you everything I know.”

[P115]
Cheongpung tilted his head.

[P116]
“A year or two?”

[P117]
“What? Is that too long? You don’t know how the world works, so I suppose you don’t realize how expensive martial arts academy fees are. Even with the lowest estimate, it’ll take at least a year…”

[P118]
“No, because I’m going to quit before then.”

[P119]
“You’re quitting? When?”

[P120]
“Now.”

[P121]
“Huh?”

[P122]
“What?”

[P123]
Cheongpung smiled brightly.

[P124]
“I don’t know the way to Shanxi Province. There happened to be an escort run heading to Shanxi, so I asked them to let me tag along.”

[P125]
“…And?”

[P126]
“We’ll reach Taiyuan after one more day, so I was planning to part ways around then.”

[P127]
Seokchil and the other porter exchanged baffled looks.

[P128]
“What the hell? Didn’t Escort Chief Song say he signed a one-year contract?”

[P129]
“That’s what I heard, too. That’s why they assigned him to you, the most experienced porter, so he could learn from you.”

[P130]
With a confused expression, Seokchil asked Cheongpung,

[P131]
“When you joined us in Henan, you signed something, didn’t you?”

[P132]
“Oh, yes.”

[P133]
“If you have it, show it to me.”

[P134]
Cheongpung pulled a yellowish bamboo slip from inside his clothes and showed it to them.

[P135]
It was a contract stating that he would work as a porter for the Seongun Escort Bureau for one year and pay a penalty if he left before then.

[P136]
“You can read, right?”

[P137]
“I finished the Four Books and Three Classics when I was four.[^1]”

[P138]
“Don’t say stupid things like that. Read this part. Yes, that section. Read it aloud, and make sure I can hear you.”

[P139]
Cheongpung read the section Seokchil indicated in a crisp voice.

[P140]
“Once signed, this contract cannot be revoked. In the event of unauthorized departure, the signer shall pay a penalty of fifty silver nyang or provide compensation of equivalent value.”

[P141]
“You know how much fifty silver nyang is, right? Do you know what ‘compensation of equivalent value’ means?”

[P142]
Cheongpung thought deeply for a moment, then slapped his forehead.

[P143]
“Does it mean I’d have to work it off?”

[P144]
“That’s right, you idiot. Did you think the Escort Bureau was full of nothing but kindhearted saints?”

[P145]
Seokchil’s blood pressure shot up, making the back of his neck throb. He wanted to crack open the top of the kid’s skull and see what was inside.

[P146]
*How can someone like this even exist? Is it because he only ever lived in the mountains?*

[P147]
The dangers of transporting goods across the land were beyond imagination. Mounted bandits, river bandits, mountain bandits, every kind of bandit gang imaginable, not to mention interference from competing Escort Bureaus.

[P148]
Even if they overcame every one of those obstacles, a single natural disaster could doom an escort run.

[P149]
An Escort Bureau was every bit as thorough and hard-edged as most Murim sects, if not more so.

[P150]
*And this kid signed the contract, then says what? “I’m leaving around here”?*

[P151]
The young fool in front of him knew far too little about the world.

[P152]
Seokchil spoke, determined to keep the boy from throwing his life away.

[P153]
“I’m telling you this just in case, so give up any thoughts of running away. Work for a year and think of it as earning money. Understand?”

[P154]
“A year is too long. I think I can work through tomorrow, though.”

[P155]
“You little bastard!”

[P156]
“Hyung, Hyung, calm down! If Escort Chief Song happens to see this, we’ll all be in trouble.”

[P157]
“Let go! I said let go!”

[P158]
It was just then, as Seokchil was about to snap.

[P159]
“Uh, wouldn’t this be enough to cover the penalty?”

[P160]
Clink.

[P161]
The two men’s eyes widened at what Cheongpung held out.

[P162]
The object was shaped like a horse’s hoof and gleamed with a silver light whiter than the snow.

[P163]
“S-silver yuanbao?”

[P164]
“And there are two of them!”

[P165]
Two silver yuanbao, each worth fifty silver nyang.

[P166]
A hundred silver nyang was an enormous sum that an ordinary porter would struggle to earn even after working himself to the bone for ten years.

[P167]
And yet such a fortune had come from the clothes of a young man from a slash-and-burn farming community.

[P168]
“H-how…?”

[P169]
“I was given some traveling money when I left home.”

[P170]
Both men’s mouths fell open at Cheongpung’s innocent reply.

[P171]
What kind of family gave their son a hundred silver nyang as traveling money? And judging from the money pouch hanging limp like a bull’s testicles, this didn’t seem to be all he had.

[P172]
“At least it looks like this should cover the penalty…”

[P173]
The two men nodded frantically.

[P174]
“It can. Of course it can.”

[P175]
“Why did you suddenly start speaking formally?”

[P176]
“It’s just more comfortable this way.”

[P177]
“Exactly. It’s the most comfortable thing in the world.”

[P178]
“Oh. If that’s what you prefer.”

[P179]
Cheongpung looked at the two men as if they were strange and handed over the two silver yuanbao.

[P180]
“I’ll be going, then. Please tell them this is the penalty.”

[P181]
“A-are you giving us both?”

[P182]
“It’s too much…”

[P183]
“If there’s anything left over, you two can split it. I don’t really know how to spend money. Buy yourselves some warm clothes. Something with expensive fur.”

[P184]
“…!”

[P185]
As Cheongpung slung a bundle over his shoulder and prepared to leave, Seokchil hurriedly called after him.

[P186]
“C-could I ask your name?”

[P187]
“Cheongpung. Until half a month ago, I was from Henan. Last month, I lived in Hubei, and before that, I was in Shaanxi.”

[P188]
With that, Cheongpung strode off toward Taiyuan.

[P189]
The sky was blue, and early shoots were already sprouting from the damp earth.

[P190]
“Maybe spring will come a little early this year.”

[P191]
He smiled brightly as he thought about it. He hoped the plum blossoms would bloom in profusion again this spring.

[P192]
Then, without warning, he thought of Lotus Peak on Huashan, from which he had secretly run away not long ago.

[P193]
[^1]: The Four Books and Three Classics are foundational Confucian texts.
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
# Chapter 130

[P2]
Winter in the borderlands was harsh. A middle-aged man shivered violently as the knife-sharp wind cut through his collar.

[P3]
“Ugh, it’s cold as hell.”

[P4]
The man, Seokchil, was a porter for the Seongun Escort Bureau in southern Shanxi Province.

[P5]
He had spent more than a day and a half hauling a cart loaded with over a hundred geun of cargo, soaking his entire body in sweat. Whenever he took a brief rest, as he was now, he had to fight against the brutal cold.

[P6]
“Hyung, hurry up and leave the cart. Come warm yourself by the fire before you freeze to death.”

[P7]
A fellow porter, already crouched in front of the campfire, called out. Seokchil answered gruffly as he walked over.

[P8]
“Brat, I have five mouths to feed. I’ve got a long way to go before I’m ready to die.”

[P9]
“True. You can’t die when you’ve got a fox of a wife and rabbit-like children waiting for you.”

[P10]
“What do you mean, fox? She’s a bear. A bear.”

[P11]
“Was that a deathbed confession? If your wife hears you, she’ll wring your neck.”

[P12]
“You can curse the king behind his back. What, you didn’t know that?”

[P13]
Seokchil moved closer to the campfire.

[P14]
They used horse manure for firewood, so a foul smell spread in every direction. But after nearly twenty years as a porter, Seokchil was as used to it as he was to the smell of cooking rice.

[P15]
“Ah, now I feel like I can live again.”

[P16]
“But Hyung, aren’t you being a little stingy?”

[P17]
“Huh? What kind of nonsense is this?”

[P18]
His fellow porter grinned and jerked his chin toward something.

[P19]
“You should bring the rookie over, too. Where’s the sense in rushing over here to save yourself alone?”

[P20]
Seokchil, who had been warming his frozen hands, turned his head. At the end of his gaze sat a young man on a snow-covered rock, staring blankly into space.

[P21]
*That kid’s doing it again.*

[P22]
The young man was a new porter they had picked up in Henan. Escort Chief Song, the person in charge of this escort run, had said that the young man seemed capable enough to earn his keep, so they had taken him on.

[P23]
*Well, people are always in short supply.*

[P24]
The problem was that the young man often sat around like this, completely lost in thought, and no one had the slightest idea what was going on inside his head.

[P25]
As Seokchil clicked his tongue, his fellow porter asked,

[P26]
“Why? Is he a little strange?”

[P27]
“He does his work well. He’s surprisingly strong for someone who doesn’t look like much.”

[P28]
“Then what’s the problem?”

[P29]
“What do you mean, what’s the problem? It’s frustrating seeing a young fellow sit around like that every day. Back when I was his age…”

[P30]
“You want to say you had dreams of making your mark on the world and worked hard every day?”

[P31]
“Of course. A man should know how to set a grand goal and move toward it.”

[P32]
“I assume that grand goal wasn’t becoming the greatest porter under heaven.”

[P33]
“You little—”

[P34]
At Seokchil’s furious reaction, his fellow porter quickly changed the subject.

[P35]
“By the way, what’s that fellow’s name?”

[P36]
“Cheongpung.”

[P37]
“Wow, what a great name. It suits him, too.”

[P38]
“That’s true.”

[P39]
Seokchil secretly disliked the young man, Cheongpung, but he had to agree completely.

[P40]
There was something about the young man’s open, gentle features and clear eyes that made people feel strangely at ease and calmed their anger.

[P41]
“Hey, rookie!”

[P42]
At his fellow porter’s shout, Cheongpung turned his head.

[P43]
“Me?”

[P44]
“Who else would I be talking to? Come over here and warm yourself by the fire. If you keep sitting there, your butt will get ripped right off.”

[P45]
“An experience like that wouldn’t be bad.”

[P46]
“An experience? What experience?”

[P47]
“The experience of having my butt ripped off. I’ve never had that happen before.”

[P48]
His fellow porter was silent for a moment before whispering to Seokchil,

[P49]
“What kind of guy is he?”

[P50]
“I don’t know. The kid’s a little strange. Maybe he ate something bad.”

[P51]
Cheongpung tilted his head.

[P52]
“I ate two dumplings this morning.”

[P53]
“……You’ve got sharp ears. Fine, just come sit down.”

[P54]
“Should I?”

[P55]
Cheongpung trudged over and sat down in front of the fire. The usual questions immediately began flying at him.

[P56]
“Where are you from?”

[P57]
“Henan.”

[P58]
“So you’re from Henan.”

[P59]
“I was in Hubei a month ago.”

[P60]
“Hmm. Hubei’s nice, too.”

[P61]
“Before that…”

[P62]
The porter turned to Seokchil.

[P63]
“This guy’s unbelievable.”

[P64]
“Right? I feel like I’m becoming strange myself whenever I talk to him.”

[P65]
“How have you lasted over a month with someone like him beside you?”

[P66]
“That’s why I stopped talking to him lately. Has it been about three days since our last conversation?”

[P67]
Cheongpung answered with a serious expression.

[P68]
“Four days and three shichen.”

[P69]
“……”

[P70]
“……”

[P71]
The two men barely managed to suppress their urge to smack Cheongpung over the head.

[P72]
“So where are you from?”

[P73]
“I lived in the mountains.”

[P74]
“That’s not what I meant… No, never mind. Thank you for answering that, at least.”

[P75]
“You’re welcome.”

[P76]
Strangely, Cheongpung’s bright smile made their anger subside.

[P77]
His unpredictable, bizarre remarks were paired with an innocent smile like a child’s. Their curiosity about this strange young man, unlike anyone they had ever seen, continued to grow.

[P78]
“But you said you lived in the mountains?”

[P79]
“I mean exactly what I said. I farmed and gathered medicinal herbs in the mountains from the time I was young. I did various other things, too.”

[P80]
The two men jumped to the conclusion that Cheongpung was from a slash-and-burn farming community.

[P81]
Most slash-and-burn farmers went into the mountains to escape the cruelty of vicious landlords or to avoid the authorities after committing one crime or another.

[P82]
“You must have had a hard life.”

[P83]
“But I had fun.”

[P84]
“Oh, really?”

[P85]
Could life as a slash-and-burn farmer really be fun? The thought briefly crossed Seokchil’s mind, but he saw no reason to ask.

[P86]
“Then what made you come down from the mountain?”

[P87]
“Life in the mountains got boring. I wanted to see the world, and there were people I wanted to meet.”

[P88]
“So that’s why you came to Henan.”

[P89]
“Yes. It turned out to be a wasted trip, but… things aren’t bad now, either. This escort work is pretty interesting, too.”

[P90]
“You find escort work interesting?”

[P91]
Cheongpung answered with a broad smile.

[P92]
“Watching people is interesting. Looking at the land and the sky is interesting, too. Thinking is fun.”

[P93]
To Seokchil, who had worked as a porter for so many years, these were all sights he was sick to death of seeing.

[P94]
People worn down by exhaustion and worries about making a living. Damp earth and knife-sharp winds that blew like mad. His mind was filled with only one thought: how much pay he would receive for this escort run.

[P95]
*Well, he’s still young. That’s the only reason he can say something like that.*

[P96]
Besides, he had lived in the mountains his entire life and came from a slash-and-burn farming community. It made sense that he would feel this way.

[P97]
Wouldn’t he learn about the harsh realities of life soon enough and gradually become just like Seokchil as he grew older?

[P98]
*I used to be like that, too.*

[P99]
Seokchil looked at Cheongpung with a mixture of envy and pity before opening his mouth.

[P100]
“Just listen to this as the ramblings of an old man.”

[P101]
He knew he was meddling where he wasn’t wanted, but he wanted to show this innocent young man the realities of life.

[P102]
Wasn’t his life too promising to begin and end as a porter?

[P103]
“Anything seems worthwhile for a while. But after ten or twenty years, you stop seeing much of a future ahead of you. No matter how hard a porter works or how talented he is, he’s still a porter. You should learn even Third Rate martial arts at a local martial arts academy and start working as an escort. You’d be much better off.”

[P104]
Cheongpung blinked.

[P105]
“Oh, really?”

[P106]
“Not ‘oh, really?’ I’m telling you to do it. You’re a little old to start learning martial arts, but who knows? Maybe you have exceptional talent and could become a successful First Rate master.”

[P107]
“A First Rate master…”

[P108]
His fellow porter, who had been listening quietly, clicked his tongue.

[P109]
“Isn’t that giving him too much false hope? A First Rate master isn’t some dog’s name.”

[P110]
“I’m speaking hypothetically. What kind of sense does it make for someone his age to be satisfied with being a porter?”

[P111]
“Well, you’re right about that. If I were ten years younger, I wouldn’t be sitting here either.”

[P112]
“See?”

[P113]
Seokchil patted Cheongpung on the shoulder.

[P114]
“You heard him, right? Save carefully for a year or two and enroll in a martial arts academy. It’ll be much better for you. Until then, I’ll teach you everything I know.”

[P115]
Cheongpung tilted his head.

[P116]
“A year or two?”

[P117]
“What? Is that too long? You don’t know how the world works, so I suppose you don’t realize that martial arts academy fees aren’t cheap. Even if you take the lowest estimate, it’ll take a year to…”

[P118]
“No, because I’m going to quit before then.”

[P119]
“You’re quitting? When?”

[P120]
“Now.”

[P121]
“Huh?”

[P122]
“What?”

[P123]
Cheongpung smiled brightly.

[P124]
“I don’t know the way to Shanxi Province. There happened to be an escort run heading to Shanxi, so I asked them to let me tag along.”

[P125]
“……And?”

[P126]
“We’ll reach Taiyuan after one more day, so I was planning to part ways around then.”

[P127]
Seokchil and his fellow porter looked at each other with expressions that seemed to ask whether this was some kind of joke.

[P128]
“What the hell? Didn’t Escort Chief Song say he signed a one-year contract?”

[P129]
“That’s what I heard, too. That’s why they assigned him to the most experienced porter, so he could learn from him.”

[P130]
With a confused expression, Seokchil asked Cheongpung,

[P131]
“When you joined us in Henan, you signed something, didn’t you?”

[P132]
“Oh, yes.”

[P133]
“If you have it, show it to me.”

[P134]
Cheongpung pulled a yellowish bamboo slip from inside his clothes and showed it to them.

[P135]
It was a contract stating that he would work as a porter for the Seongun Escort Bureau for one year and pay a penalty if he left before then.

[P136]
“You can read, right?”

[P137]
“I finished studying the Four Books and Three Classics when I was four.[^1]”

[P138]
“Don’t say stupid things like that. Read this part. Yes, that section. Read it aloud, and make sure I can hear you.”

[P139]
In a clear voice, Cheongpung read the section Seokchil pointed out.

[P140]
“Once signed, this contract cannot be revoked. In the event of unauthorized departure, the signer shall pay a penalty of fifty nyang of silver or provide compensation of equivalent value.”

[P141]
“You know how much fifty nyang of silver is, right? Do you know what ‘compensation of equivalent value’ means?”

[P142]
Cheongpung thought deeply for a moment, then slapped his forehead.

[P143]
“Does it mean I’d have to work it off?”

[P144]
“That’s right, you idiot. Did you think the Escort Bureau was full of nothing but kindhearted saints?”

[P145]
Seokchil’s blood pressure rose, and the back of his neck began to ache. He wanted to split the top of this kid’s skull open and see what was inside.

[P146]
*How can someone like this even exist? Is it because he only ever lived in the mountains?*

[P147]
The dangers of transporting goods across the land were beyond imagination. Mounted bandits, river bandits, mountain bandits, every kind of bandit gang imaginable, not to mention interference from competing Escort Bureaus.

[P148]
Even if they overcame all those obstacles, one encounter with a natural disaster could bring an escort run to failure.

[P149]
An Escort Bureau was every bit as thorough and hard-edged as most Murim sects, if not more so.

[P150]
*And this kid signed the contract, then says what? “I’m leaving around here”?*

[P151]
The young fool in front of him knew far too little about the world.

[P152]
Seokchil spoke, determined to keep the boy from throwing his life away.

[P153]
“I’m telling you this just in case, so give up on running away right now. Work for a year and think of it as earning money. Understand?”

[P154]
“A year is too long. I think I can work until tomorrow, though.”

[P155]
“You little bastard!”

[P156]
“Hyung, Hyung, calm down! If Escort Chief Song happens to see this, we’ll all be in trouble.”

[P157]
“Let go! I said let go!”

[P158]
It was just then, as Seokchil was about to snap.

[P159]
“Uh, wouldn’t this be enough to cover the penalty?”

[P160]
Clink.

[P161]
The two men’s eyes widened when they saw what Cheongpung held out.

[P162]
The object was shaped like a horse’s hoof and gleamed with a silver light whiter than the snow.

[P163]
“Is that a silver ingot?”

[P164]
“And there are two of them!”

[P165]
There were two silver ingots, each worth fifty nyang of silver.

[P166]
A hundred nyang of silver was an enormous sum that an ordinary porter would struggle to earn even after working himself to the bone for ten years.

[P167]
And yet such a fortune had come from the clothes of a young man from a slash-and-burn farming community.

[P168]
“H-how?”

[P169]
“I was given some traveling money when I left home.”

[P170]
At Cheongpung’s innocent answer, both men’s mouths fell open.

[P171]
What kind of family gave their son a hundred nyang of silver as traveling money? And judging from the money pouch hanging limp like a bull’s testicles, this didn’t seem to be all he had.

[P172]
“At least it looks like the penalty can be settled with this…”

[P173]
The two men nodded frantically.

[P174]
“It can. Of course it can.”

[P175]
“Why did you suddenly start speaking formally?”

[P176]
“It’s just more comfortable this way.”

[P177]
“Exactly. It’s the most comfortable thing in the world.”

[P178]
“Oh. If that’s what you prefer.”

[P179]
Cheongpung looked at the two men as if they were strange and handed over the two silver ingots.

[P180]
“I’ll be going, then. Please tell them this is the penalty.”

[P181]
“A-are you really giving us both?”

[P182]
“It’s too much…”

[P183]
“If there’s any left over, you two can split it. I don’t really know how to spend money. Buy yourselves some warm clothes. Something with expensive fur on it.”

[P184]
“……!”

[P185]
As Cheongpung slung a bundle over his shoulder and prepared to leave, Seokchil hurriedly spoke.

[P186]
“C-could I ask your name?”

[P187]
“Cheongpung. Until half a month ago, I was from Henan. Last month, I lived in Hubei, and before that, I was in Shaanxi.”

[P188]
After answering, Cheongpung began walking steadily toward Taiyuan.

[P189]
The sky was blue, and early shoots were already sprouting from the damp earth.

[P190]
“Maybe spring will come a little early this year.”

[P191]
He smiled brightly as he thought about it. He hoped the plum blossoms would bloom in profusion again this spring.

[P192]
Then, without warning, he thought of Lotus Peak on Huashan, from which he had secretly run away not long ago.

[P193]
[^1]: The Four Books and Three Classics are foundational Confucian texts.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 청풍     | **Cheongpung**     |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 마적     | **mounted bandits**                              |                                                       |
| 표국     | **Escort Bureau**                            |
| 표사     | **escort**                                   |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 석칠 | **Seokchil** | Middle-aged porter with nearly twenty years of experience. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 연화봉 | **Lotus Peak** | Peak on Huashan from which Cheongpung recently fled. |
| 사서삼경 | **Four Books and Three Classics** | Confucian texts used to describe conventional scholarly learning. |
| 은자 | **silver nyang** | Silver currency unit. |
| 은원보 | **silver yuanbao** | Small silver ingot given to Taekyung as pocket money. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 130,
  "passed": true,
  "metrics": {
    "source_characters": 6091,
    "translation_characters": 13895,
    "length_ratio": 2.281,
    "source_paragraphs": 192,
    "translation_paragraphs": 193
  },
  "errors": [],
  "warnings": [
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
        "korean": "은원",
        "preferred": "gratitude and grudges"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "갑자",
        "preferred": "jiazi"
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
