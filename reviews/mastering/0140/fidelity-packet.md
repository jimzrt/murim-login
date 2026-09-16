# Fidelity Gate — Chapter 140

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
  1|＃140화
  2|
  3|
  4|
  5|종남삼수(終南三手) 공일혁은 떨떠름한 표정으로 눈앞의 청년을 바라봤다.
  6|
  7|‘뭐지, 이놈은?’
  8|
  9|산서잠룡 진태경. 불과 몇 달 만에 섬서성까지 슬금슬금 이름을 알리고 있는 돌풍의 주역이다.
 10|
 11|공일혁은 속으로 진태경이 했던 말을 곱씹었다.
 12|
 13|‘군림…… 뭐라고?’
 14|
 15|분명히 무슨 말을 하려다 말았던 것 같은데.
 16|
 17|처음 종남파의 이름을 들었을 때 보여 줬던 열광적인 반응과 달리, 놈은 지금 김이 팍 샌 얼굴로 한숨만 푹푹 내쉬고 있었다.
 18|
 19|“휴우.”
 20|
 21|“……웬 한숨인가?”
 22|
 23|“아닙니다. 아무것도 아니에요.”
 24|
 25|“아니긴 뭐가 아닌가? 그러지 말고 마저 말해 보게.”
 26|
 27|공일혁은 슬슬 기분이 나빠지기 시작했다. 자신의 사문이 어떤 곳인가, 바로 그 유명한 종남파(終南派)다.
 28|
 29|수백 년의 역사와 뿌리 깊은 무맥을 바탕으로 당당히 구파일방(九派一幇)에 이름을 올린 무림의 거목 중 하나란 말이다.
 30|
 31|그런데…….
 32|
 33|‘알아봐 주는 것에 감사하지는 못할망정 한숨을 내쉬어?’
 34|
 35|태원진가가 아무리 잘나가 봐야 아직은 변방의 일개 가문에 불과하다.
 36|
 37|구파일방인 종남파와 비교하면 태양 앞의 반딧불 같은 존재. 출신 배경으로나, 개인의 명성으로나 까마득한 애송이 녀석이다.
 38|
 39|‘시건방진 놈.’
 40|
 41|종남파의 제자라는 자부심으로 평생을 살아 온 그다. 기분이 나쁜 것도 당연했다.
 42|
 43|공일혁과 함께 종남삼수로 불리는 다른 두 사람 역시 진태경을 보는 시선이 곱지 않았다.
 44|
 45|“크흠.”
 46|
 47|“젊은 친구가 말을 하다가 마는 버릇이 있군.”
 48|
 49|분위기가 영 텁텁해지자 진태경이 손을 내저었다.
 50|
 51|“아뇨, 그런 게 아니고요. 그냥 혼자 착각했던 것뿐입니다.”
 52|
 53|공일혁이 애써 너그러운 말투로 입을 열었다.
 54|
 55|“무슨 착각? 말해 보게. 내 다 대답해 줄 터이니.”
 56|
 57|“진짜 별거 아닌데…….”
 58|
 59|“아, 말해 보라고!”
 60|
 61|“엥, 왜 소리를 지르고 그러세요?”
 62|
 63|공일혁은 호흡을 가다듬었다.
 64|
 65|내일모레면 그의 나이 불혹이다. 그런데 이제 겨우 약관밖에 안 된 어린놈에게 이렇게 흥분하다니.
 66|
 67|이상하게 저놈의 잘생긴 얼굴을 보고 있으면 약이 오르는 기분이다.
 68|
 69|“그게 아니고…… 후우, 어쨌든 말해 보게.”
 70|
 71|“으음.”
 72|
 73|진태경이 어쩔 수 없다는 듯이 입을 열었다.
 74|
 75|“그럼 하나만 여쭤봐도 되겠습니까?”
 76|
 77|“뭐든지.”
 78|
 79|“지금 종남파 회장님, 아니 장문인 존함이 어떻게 되시는지?”
 80|
 81|“응? 장문인의 존함 말인가?”
 82|
 83|“네.”
 84|
 85|이게 무슨 뜬금없는 질문이란 말인가? 공일혁은 의아함을 느끼며 대답했다.
 86|
 87|“공씨 성에 일 자, 중 자 쓰시네.”
 88|
 89|“아아, 네.”
 90|
 91|마치 그게 누구냐는 듯 심드렁한 대답이다. 공일혁을 포함한 세 사람의 이마에 핏대가 섰다.
 92|
 93|“장문인의 존함을 들어 본 적 없나?”
 94|
 95|진태경이 뒤통수를 긁적였다.
 96|
 97|“글쎄요, 들어 본 것 같기도 하고. 아닌 것 같기도 하고…….”
 98|
 99|“……그, 그럼 풍운검군(風雲劍君)이라는 별호는?”
100|
101|“풍운검군 공일중, 풍운검군 공일중…… 쓰읍, 잘 모르겠는데요.”
102|
103|기가 찰 노릇이다. 구파일방, 오대세가의 장문인과 가주들은 모두 천하에 이름이 쟁쟁한 고수들. 무림인이라면 모를 수 없는 존재다.
104|
105|하물며 얼뜨기 무인도 아니고 태원진가의 자제라는 놈이 종남파 장문인을 모르다니.
106|
107|심지어 제 친구라도 되는 마냥 이름을 불러 댄다.
108|
109|‘이놈이 지금 종남파를 우롱하는 건가?’
110|
111|공일혁이 충격으로 머리가 띵해 있는데, 문득 진태경이 고개를 들어 그를 바라봤다.
112|
113|“어? 그러고 보니 이름이 비슷하시네요. 공일중, 공일혁.”
114|
115|그나마 최소한의 눈치는 있는 놈이군. 공일혁의 심기가 살짝 누그러졌다.
116|
117|“집안 어른이시네.”
118|
119|“오, 집안 어른! 그럼 혹시 관계가…….”
120|
121|“오촌 당숙 되시지.”
122|
123|“오촌 당숙!”
124|
125|눈이 휘둥그레진 진태경을 보자 공일혁의 어깨에 힘이 들어갔다.
126|
127|다른 사람도 아니고 풍운검군이다. 종남파의 장문인과 한집안 사람이라는 건 엄청난 영광 아닌가.
128|
129|“크흠, 너무 소문내지는 말아 주게. 아무래도 이 사실이 널리 알려지면 사람들이 날 대하는 태도가 달라질 테니 말일세.”
130|
131|실제론 이 사실이 누구보다 알려지길 원하는 건 공일혁 본인이다.
132|
133|그는 지금까지 풍운검군의 이름을 앞세워 온갖 혜택을 누려 왔다. 뛰어난 무공과 영약, 그리고 종남삼수라는 별호까지.
134|
135|이대로만 승승장구를 거듭한다면 종남파의 요직을 꿰차는 것도 시간문제였다.
136|
137|“내 말, 잘 알아들었지? 정 말하고 싶다면 가까운 벗 몇 명한테만…….”
138|
139|진태경이 손을 내저었다.
140|
141|“에이, 절대 말 안 합니다. 공 대협 평판에 누가 될 게 뻔한데. 연줄 믿고 여기까지 올라온 놈, 어이쿠. 죄송합니다. 어쨌든 그런 식으로 소문나면 곤란하잖아요.”
142|
143|공일혁은 헛기침을 내뱉었다. 스스로 생각하기에도 아주 틀린 얘기는 아니었기 때문이다.
144|
145|“크흠. 딱히 누가 될 것까지야 있겠나. 내 말은, 혹 나에 대해 궁금해하는 사람이 있을 수 있으니…….”
146|
147|“궁금해하는 사람이요? 저 친구 한 명도 없어서 딱히 말해 줄 사람이 없는데.”
148|
149|“……자네 큰형님인 진 소가주나, 아니면 진천검 소협이 궁금해할 수도 있지 않겠나?”
150|
151|“아, 저희 가문 사정 잘 모르시는구나. 큰형님 지금 엄청 바빠요. 둘째 형은 무공 아니면 별 관심도 없고.”
152|
153|“……그래?”
154|
155|“예.”
156|
157|그렇다는데 더 할 말도 없다. 언짢은 헛기침만 연발하는 그를 보며 진태경이 해맑게 웃었다.
158|
159|“그리고 그거 말해 봤자 뭐해요. 오촌 당숙이면 거의 남이나 다름없는데. 저는 또 무슨 부자지간이라도 되시는 줄.”
160|
161|“……!”
162|
163|
164|
165|* * *
166|
167|
168|
169|역시 웃는 얼굴로 엿 먹이는 게 세상에서 제일 짜릿하다.
170|
171|특히 거만 떠는 놈들한테는 제대로 먹이기만 하면 쾌감은 두 배가 된다.
172|
173|‘아, 중독될 것 같아.’
174|
175|종남삼수라고 했나?
176|
177|처음부터 마음에 안 들었던 놈들이다. 위에서 내려다보는 듯한 눈빛도, 대문파랍시고 거들먹거리는 태도도.
178|
179|‘역시 소설이랑은 다르네.’
180|
181|고등학교 다닐 때는 종남파 제자가 되는 게 꿈이었는데, 역시 현실은 시궁창이다.
182|
183|나는 주먹을 부르르 떠는 공일혁을 보며 새어 나오는 웃음을 참았다.
184|
185|‘귀여운 자식, 놀리는 맛이 쏠쏠하네.’
186|
187|더 놀려 주고 싶지만 이쯤 해 둬야 한다. 태원진가가 지역구라면 저쪽은 전국구. 시비 붙어서 좋을 게 없으니까.
188|
189|다행히 불쑥 끼어든 목소리가 분위기를 환기시켰다.
190|
191|“너무 그쪽 분들만 대화하시는 거 아니에요? 다른 분들 외로우시겠다. 아직 소개도 다 못 했는데.”
192|
193|콧소리가 듬뿍 들어간 간드러진 목소리에 한 번.
194|
195|나를 보며 찡긋 웃는 미중년의 모습에 두 번 소름이 돋는다.
196|
197|“아직 내 소개를 못 했죠? 산서성 도지휘동지, 홍진이라고 해요.”
198|
199|“도지휘……뭐요?”
200|
201|“도지휘동지요. 아, 무림인이시라 이런 직책은 처음 들어 보시는구나?”
202|
203|“네.”
204|
205|위원장 동지는 들어 봤어도 도지휘동지는 처음 들어 보네.
206|
207|눈만 껌뻑이는 나를 보며 홍진이 까르르 웃었다. 세상에, 중년 남성이 까르르 웃다니.
208|
209|“표정이 왜 그래요? 무슨 안 좋은 일이라도?”
210|
211|“……아뇨. 너무 행복해서.”
212|
213|“행복? 호호호, 너무 귀여우시다. 안 그래요, 이 첨사?”
214|
215|귀엽대 시발, 저 새끼가 나한테 귀엽대.
216|
217|간신히 구역질을 참고 있는데 앞서 스치듯이 본 이풍이라는 사내가 무뚝뚝하게 인사를 건넸다.
218|
219|“산서성 도지휘첨사 이풍이오. 산서성부 소속 군사들의 훈련을 맡고 있지.”
220|
221|“그리고 내 직속 부하죠. 그렇지 않나요, 이 첨사?”
222|
223|순간 이풍의 굵은 눈썹이 꿈틀거렸다. 만난 지 5분도 안 됐지만 하나는 알겠다.
224|
225|이풍이 홍진을 싫어한다는 것.
226|
227|그거 하나만으로도 예의를 갖출 만한 상대다. 나는 공손히 포권을 취했다.
228|
229|“태원진가의 진태경이라고 합니다.”
230|
231|“위명은 익히 들었소. 산서 무림에 큰 신성이 떠올랐다고.”
232|
233|“신성이라뇨, 과찬의 말씀이십니다.”
234|
235|이풍이 진지한 얼굴로 고개를 저었다.
236|
237|“아니오. 소문이라는 것이 왕왕 과장되기 마련인데, 내 오늘 진 소협을 보니 모두 사실임을 알겠소.”
238|
239|오는 말이 고우면 가는 말도 고운 법.
240|
241|나도 오는 길에 봤던 군사들 이야기를 꺼냈다.
242|
243|“저야말로 군사들 수준이 상당히 뛰어나서 깜짝 놀랐습니다. 어떤 분이 훈련시켰는지 궁금했는데…… 역시는 역시네요.”
244|
245|엄지를 척 치켜세워 주자 이풍의 입가에 웃음이 스친다.
246|
247|이런 정상적이고 훈훈한 대화가 얼마 만인지, 감개가 무량할 지경이다.
248|
249|“결례가 안 된다면 다른 분들도 소개해 주시겠소?”
250|
251|“어이구, 그럼요. 이쪽은…….”
252|
253|“안녕하십니까! 존경하는 무림의 선배님들과 불철주야 나라를 위해 힘쓰시는…….”
254|
255|“…….”
256|
257|대기업 면접이야, 뭐야.
258|
259|호시탐탐 기회만 엿보고 있던 산서오문의 후기지수들이 앞다투어 과장된 자기소개와 아부를 한바탕 쏟아 내자 남은 한 사람에게 시선이 쏠렸다.
260|
261|“그래, 거기 계신 후배님은 어디에서 온 누구신가?”
262|
263|한껏 선배뽕에 취한 공일혁의 질문에 청풍이 눈을 깜빡였다.
264|
265|“저요?”
266|
267|“그럼 자네 말고 누가 있나?”
268|
269|“하나, 둘, 셋, 넷…… 저 말고도 많은데요.”
270|
271|공일혁의 이마에 핏대가 섰다.
272|
273|“그거 말고! 아직 소개 안 한 건 자네뿐이잖아!”
274|
275|“아하, 그렇군요. 후배라고 하시기에 제가 아닌 줄 알았어요.”
276|
277|“어허, 원래 무림은 동도! 다 선후배지간인 걸 왜 모르는가!”
278|
279|나 같았으면 잔뜩 비꼬았겠지만, 청풍은 역시 청풍.
280|
281|일반인과는 클라스가 다르다.
282|
283|“우와, 저 후배 처음 해 봐요! 잘 부탁드립니다!”
284|
285|“……아니, 뭐 이런 놈이.”
286|
287|가끔은 적당히 때 묻은 어른들보다 순수한 어린아이가 훨씬 대하기 어렵다. 청풍이 해맑은 웃음과 함께 입을 열었다.
288|
289|“저는 산서에 살고 있는 청풍이라고 합니다.”
290|
291|말문이 막혔던 공일혁이 그제야 정신을 차리고 더듬더듬 물었다.
292|
293|“커, 커험. 그럼 자네도 산서오문의 후기지수겠군.”
294|
295|“어? 아닌데요?”
296|
297|“아니라고?”
298|
299|“네. 전 하남에서 왔는데.”
300|
301|“방금은 산서 사람이라며?”
302|
303|“산서에 살고 있으니 산서 사람이지요. 헤헤.”
304|
305|“그…… 후우우.”
306|
307|공일혁의 이마에 골이 패었다. 당장이라도 주먹을 휘두르고 싶은데, 자리가 자리인 만큼 참는 기색이 역력했다.
308|
309|“좋아, 그럼 하남 어느 문파 출신인가? 철혈문? 오호검문?”
310|
311|“거기가 어디예요?”
312|
313|“하남 출신이라면서 철혈문과 오호검문을 모르는 게 말이 되나? 응? 그럼 자네가 소림사 출신이라도 돼?”
314|
315|“아, 하남에서는 보름 정도 머무르다가 산서로 넘어와서 잘 모릅니다.”
316|
317|“하남 출신이라며?”
318|
319|“하남에서 온 건 맞는데, 그전에는 섬서에…….”
320|
321|“야, 이 새끼야! 차라리 그냥 천하가 네 고향이라고 해라!”
322|
323|결국 폭발한 공일혁이 고함과 함께 청풍의 멱살을 붙잡았다. 아니, 붙잡으려던 찰나였다.
324|
325|덥석.
326|
327|너무나 간단하게 잡혀 버린 손목. 공일혁이 헛웃음을 흘렸다.
328|
329|“허, 이놈 봐라. 한 수 재간은 있다, 이거지?”
330|
331|“어어, 본능적으로 그만. 죄송합니다, 선배님.”
332|
333|“본능적으로? 죄송해?”
334|
335|울상이 된 얼굴로 사과하는 청풍을 보며 공일혁이 피식 웃었다.
336|
337|“아니다. 놓을 것 없다. 사과할 것도 없고.”
338|
339|“정말요?”
340|
341|“그래, 그 대신 만용의 대가는 톡톡히 치러야겠지?”
342|
343|“예? 그게 무슨.”
344|
345|“이제부터 알게 될 거다.”
346|
347|내가 끼어든 것은 바로 그 순간이었다. 몸을 날려 청풍의 앞을 막아선 나를, 공일혁이 건조한 눈빛으로 응시했다.
348|
349|“비키시게, 후배님.”
350|
351|“잠시 실례하겠습니다. 선배님.”
352|
353|“실례라…… 본문의 행사에 태원진가가 반하겠다는 뜻으로 받아들이면 되겠나?”
354|
355|나는 태연하게 대답했다.
356|
357|“천만에요. 그저 문제가 커지는 걸 막고 싶을 뿐입니다.”
358|
359|“문제? 무슨 문제?”
360|
361|“곧 전하께서 오시지 않습니까? 여긴 보는 눈도 많고요.”
362|
363|“보는 눈이라. 도지휘동지, 어떻게 생각하십니까?”
364|
365|공일혁의 등 뒤로 빙긋 웃는 홍진의 얼굴이 보였다. 간드러진 목소리가 뒤를 잇는다.
366|
367|“글쎄요, 제 생각엔 별문제 없을 것 같은데요?”
368|
369|이풍이 즉시 반발했다.
370|
371|“이곳은 대전입니다. 작은 소동도 용납할 수 없습니다.”
372|
373|“이 첨사, 용납이라는 말은 듣기 거북하네? 누가 들으면 내 상관이라도 되는 줄 알겠어.”
374|
375|“도지휘동지!”
376|
377|“왜요, 도지휘첨사?”
378|
379|홍진의 말이 떨어지기가 무섭게 종남삼수에 속한 다른 두 명이 슬그머니 이풍의 앞을 막아선다.
380|
381|종남파라는 이름답게 각각 최소 초일류의 고수들. 이풍은 입술을 질끈 깨물더니 나를 보며 중얼거렸다.
382|
383|“미안하오.”
384|
385|공일혁이 득의양양하게 웃었다.
386|
387|“자, 이제 어쩔 텐가?”
388|
389|어쩌긴 뭘 어째. 어깨를 한번 으쓱하고 물러나자 공일혁의 웃음이 진해졌다.
390|
391|“현명한 선택이야.”
392|
393|“저는 문제가 커지는 걸 막고 싶었을 뿐입니다. 아시죠?”
394|
395|“알다마다. 여기 있는 모두가 똑똑히 기억할 걸세.”
396|
397|“그랬으면 좋겠네요.”
398|
399|청풍은 멀뚱멀뚱 나를 쳐다봤다.
400|
401|“은인, 혹시 제가 뭘 잘못했나요?”
402|
403|내 대답보다 공일혁이 한발 빨랐다.
404|
405|“뭐라? 잘못?”
406|
407|찢어 죽일 듯한 눈빛이 청풍을 향했다.
408|
409|“네가 지금 나와 종남파를 능멸하는 것이냐?”
410|
411|“그게 아니고요. 저는 그저…….”
412|
413|“그 입 닥치지 못할까!”
414|
415|청풍의 얼굴 위로 복잡 미묘한 감정이 떠올랐다. 그리고 공혁일의 이성을 잃게 만들기에 충분한 한마디가 이어졌다.
416|
417|“와, 저 누구한테 욕먹는 거 처음이에요. 신기하다.”
418|
419|“이런 쳐 죽일……!”
420|
421|후웅!
422|
423|묵직한 파공성. 공혁일의 일권(一拳)이 눈부신 속도로 청풍의 옆구리를 향해 쏘아진 다음 순간이었다.
424|
425|퍽, 우두둑.
426|
427|“……!”
428|
429|“……!”
430|
431|소리 없는 경악 속, 한 사람이 고통으로 입을 딱 벌렸다.
432|
433|으스러진 주먹과 팔뚝 살을 찢고 뛰어나온 뼈, 피투성이가 된 공혁일이 떨리는 목소리로 물었다.
434|
435|“이, 이게 무슨. 도대체 어떤 권법…….”
436|
437|그가 아니었다면 내가 물어봤을 거다. 이미 예상한 결과이기는 했지만, 이 정도일 줄이야.
438|
439|청풍은 단 한 번 맞받아치는 것만으로 70레벨이 넘는 공일혁을 저항 불능으로 만들어 버렸다.
440|
441|그리고…….
442|
443|“권법이 아니었어.”
444|
445|내 중얼거림에 청풍이 금방이라도 토할 것 같은 얼굴로 대답했다.
446|
447|“은인 말씀이 맞아요. 권법이 아니라 태을미리장(太乙迷離掌)이라는 장법이에요. 그런데 선배님, 피가 너무 나요. 피 냄새 때문에 속 울렁거려요. 우욱!”
448|
449|이런 미친놈.
450|
451|공일혁을 내팽개치고 헛구역질을 시작하는 녀석을 보며 헛웃음을 흘리던 그때였다.
452|
453|“태, 태을미리장!”
454|
455|이풍이 부릅뜬 눈으로 물었다.
456|
457|“지금 태을미리장이라고 했소? 정말 틀림없소?”
458|
459|“우욱, 네. 저희 할아버지께서 가르쳐 주셨어요.”
460|
461|“호, 혹시 그분의 존함을 여쭤봐도 되겠소?”
462|
463|“우욱, 매종학, 우웨에에엑!”
464|
465|촤아아악!
466|
467|나는 청풍이 곧 왕이 도착할 자리에 토를 했다는 사실에 놀랐지만, 이풍은 아닌 듯했다.
468|
469|벼락을 맞은 것처럼 부들부들 떨던 그가 목소리를 쥐어짜 냈다.
470|
471|“검성……!”
```

## Assembled English

```markdown
[P1]
# Chapter 140

[P2]
Gong Ilhyuk of the Three Hands of Zhongnan stared dubiously at the young man before him.

[P3]
*What’s with this guy?*

[P4]
Jin Taekyung, the Sleeping Dragon of Shanxi. He was the driving force behind a whirlwind that had quietly spread his name as far as Shaanxi in the span of only a few months.

[P5]
Gong Ilhyuk mulled over what Jin Taekyung had said.

[P6]
*“The Reign…” What was it?*

[P7]
It definitely seemed as though he had been about to say something before stopping himself.

[P8]
Unlike his enthusiastic reaction when he first heard the name of the Zhongnan Sect, he now looked completely deflated and let out one deep sigh after another.

[P9]
“Whew.”

[P10]
“…What’s with the sighing?”

[P11]
“It’s nothing. Really.”

[P12]
“What do you mean, nothing? Go on. Finish what you were saying.”

[P13]
Gong Ilhyuk was beginning to feel irritated. What kind of sect was his? It was none other than the famous Zhongnan Sect.

[P14]
It was one of the great pillars of Murim, a sect that had proudly earned its place among the Nine Sects and One Gang on the strength of centuries of history and deeply rooted martial traditions.

[P15]
And yet…

[P16]
*Instead of being grateful that I acknowledged him, he sighs?*

[P17]
No matter how successful the Jin Family of Taiyuan had become, it was still merely a family from the frontier.

[P18]
Compared to the Zhongnan Sect, one of the Nine Sects and One Gang, it was a firefly before the sun. In both background and personal fame, Jin Taekyung was an insignificant greenhorn far beneath him.

[P19]
*Arrogant bastard.*

[P20]
Gong Ilhyuk had spent his entire life taking pride in being a disciple of the Zhongnan Sect. Naturally, he was offended.

[P21]
The other two members of the Three Hands of Zhongnan also regarded Jin Taekyung with displeasure.

[P22]
“Ahem.”

[P23]
“Young friend, you have a habit of stopping halfway when you speak.”

[P24]
As the atmosphere grew increasingly sour, Jin Taekyung waved a hand.

[P25]
“No, it’s not like that. I just misunderstood something on my own.”

[P26]
Gong Ilhyuk forced himself to speak magnanimously.

[P27]
“What did you misunderstand? Tell me. I’ll answer everything.”

[P28]
“It’s really nothing…”

[P29]
“Ah, just tell me!”

[P30]
“Huh? Why are you shouting?”

[P31]
Gong Ilhyuk took a deep breath.

[P32]
He was almost forty years old. Yet here he was, getting worked up over a brat barely twenty.

[P33]
For some reason, just looking at that handsome face got under his skin.

[P34]
“It’s not that… Whew. Anyway, tell me.”

[P35]
“Hmm.”

[P36]
Jin Taekyung finally spoke, as though he had no other choice.

[P37]
“Then may I ask you one thing?”

[P38]
“Anything.”

[P39]
“What is the name of the current chairman of the Zhongnan Sect—or rather, the Sect Leader?”

[P40]
“Hm? You mean the Sect Leader’s name?”

[P41]
“Yes.”

[P42]
What kind of question was that? Puzzled, Gong Ilhyuk answered.

[P43]
“His family name is Gong. His given name is Iljung.”

[P44]
“Ah. Yes.”

[P45]
His indifferent response made it sound as though he had no idea who that was. Veins bulged on the foreheads of all three men.

[P46]
“Have you never heard the Sect Leader’s name?”

[P47]
Jin Taekyung scratched the back of his head.

[P48]
“I might have. Or maybe not…”

[P49]
“…Then what about his title, the Wind-and-Cloud Sword Lord?”

[P50]
“Wind-and-Cloud Sword Lord Gong Iljung. Wind-and-Cloud Sword Lord Gong Iljung… Hmm. Doesn’t ring a bell.”

[P51]
It was beyond absurd.

[P52]
The Sect Leaders and Family Heads of the Nine Sects and One Gang and the Five Great Families were all renowned masters whose names resounded throughout the world. No martial artist could possibly be unaware of them.

[P53]
Yet this fellow, a member of the Jin Family of Taiyuan rather than some half-baked martial artist, didn’t even know the Sect Leader of the Zhongnan Sect.

[P54]
Worse, he casually repeated the man’s name as though they were friends.

[P55]
*Is this bastard mocking the Zhongnan Sect?*

[P56]
Gong Ilhyuk’s head was still reeling from the shock when Jin Taekyung suddenly looked up at him.

[P57]
“Oh? Come to think of it, your names are similar. Gong Iljung, Gong Ilhyuk.”

[P58]
At least he had some basic social awareness. Gong Ilhyuk’s irritation eased slightly.

[P59]
“He’s an elder of my family.”

[P60]
“Oh, a family elder! Then are you two…?”

[P61]
“He’s my father’s cousin.”

[P62]
“Your father’s cousin!”

[P63]
Seeing Jin Taekyung’s eyes widen, Gong Ilhyuk squared his shoulders.

[P64]
It wasn’t just anyone. He was the Wind-and-Cloud Sword Lord. Being related to the Sect Leader of the Zhongnan Sect was an immense honor.

[P65]
“Ahem. Don’t spread it around too much. If this became widely known, people would start treating me differently.”

[P66]
In truth, no one wanted that fact widely known more than Gong Ilhyuk himself.

[P67]
He had enjoyed all manner of benefits by invoking the Wind-and-Cloud Sword Lord’s name: superior martial arts, elixirs, and even the title of Three Hands of Zhongnan.

[P68]
If he continued advancing at this rate, it was only a matter of time before he seized an important position within the Zhongnan Sect.

[P69]
“You understand what I mean, don’t you? If you truly must tell someone, limit it to a few close friends…”

[P70]
Jin Taekyung waved him off.

[P71]
“No way. I’d never tell anyone. It would obviously hurt Great Hero Gong’s reputation. People would say, ‘That bastard only made it this far because of his connections.’ Oops. Sorry. Anyway, that kind of rumor would be troublesome, wouldn’t it?”

[P72]
Gong Ilhyuk gave a dry cough. Even he had to admit that the boy wasn’t entirely wrong.

[P73]
“Ahem. It’s not as though it would hurt me that much. I only meant that there might be people who are curious about me…”

[P74]
“Curious about you? I don’t have a single friend, so there’s no one I could tell.”

[P75]
“…Your eldest brother, the Lesser Family Head of the Jin Family, might be curious. Or Young Hero Heaven Shaking Sword.”

[P76]
“Oh, you don’t know much about my family situation. My eldest brother is incredibly busy right now. My second brother isn’t interested in much besides martial arts.”

[P77]
“…Is that so?”

[P78]
“Yes.”

[P79]
There was nothing more Gong Ilhyuk could say.

[P80]
As Gong Ilhyuk continued giving irritated coughs, Jin Taekyung smiled brightly.

[P81]
“Besides, what would be the point of telling anyone? If he’s only your father’s cousin, you’re practically strangers. Here I thought you might be father and son or something.”

[P82]
“……!”

[P83]
* * *

[P84]
Nothing in the world was more exhilarating than screwing someone over with a smile.

[P85]
It was especially satisfying with arrogant bastards. Land the blow properly, and the rush was twice as sweet.

[P86]
*Ah, I could get addicted to this.*

[P87]
The Three Hands of Zhongnan, was it?

[P88]
I hadn’t liked them from the start. Not the way they looked down on everyone, nor the way they strutted around because they belonged to some great sect.

[P89]
*So it really is different from the novel.*

[P90]
Back in high school, I’d dreamed of becoming a disciple of the Zhongnan Sect.

[P91]
But as expected, reality was a cesspool.

[P92]
I held back my laughter as I watched Gong Ilhyuk’s fists tremble.

[P93]
*Cute bastard. He’s so much fun to tease.*

[P94]
I wanted to keep going, but this was probably enough. If the Jin Family of Taiyuan was a local player, these guys were national-level. Nothing good would come of picking a fight with them.

[P95]
Fortunately, a voice suddenly cut in and lightened the atmosphere.

[P96]
“Aren’t you gentlemen monopolizing the conversation a little? The other guests must feel lonely. We haven’t even finished the introductions.”

[P97]
The nasal, lilting voice gave me goose bumps once.

[P98]
Then the pretty middle-aged man looked at me and winked, giving me goose bumps all over again.

[P99]
“I haven’t introduced myself yet, have I? I’m Hong Jin, the Deputy Military Commissioner of Shanxi Province.”

[P100]
“Deputy Military… what?”

[P101]
“The Deputy Military Commissioner. Ah, you’re a martial artist, so I suppose this is your first time hearing of the office?”

[P102]
“Yes.”

[P103]
*I’d heard of Comrade Chairman, but Comrade Deputy Military Commissioner was a new one.*

[P104]
Hong Jin giggled as he looked at me blinking.

[P105]
Good heavens. A middle-aged man was giggling.

[P106]
“Why that expression? Did something bad happen?”

[P107]
“…No. I’m just so happy.”

[P108]
“Happy? Ho ho ho, you’re adorable. Don’t you agree, Assistant Commissioner Li?”

[P109]
*He called me cute. Fuck, that bastard called me cute.*

[P110]
I barely managed to suppress my nausea as the man I had glimpsed earlier greeted me bluntly.

[P111]
“I am Li Feng, Assistant Military Commissioner of Shanxi Province. I oversee the training of the soldiers attached to the Shanxi Provincial Office.”

[P112]
“And he’s my direct subordinate. Isn’t that right, Assistant Commissioner Li?”

[P113]
Li Feng’s thick eyebrow twitched.

[P114]
We had known each other for less than five minutes, but I already knew one thing.

[P115]
Li Feng hated Hong Jin.

[P116]
That alone made him worthy of courtesy. I offered him a respectful fist-and-palm salute.

[P117]
“My name is Jin Taekyung of the Jin Family of Taiyuan.”

[P118]
“I have heard much of your reputation. A great new star has risen in the martial world of Shanxi.”

[P119]
“A new star? You flatter me.”

[P120]
Li Feng shook his head gravely.

[P121]
“No. Rumors are often exaggerated, but after seeing Young Hero Jin today, I can tell they were all true.”

[P122]
Kind words deserved kind words in return.

[P123]
I brought up the soldiers I had seen on the way here.

[P124]
“I was surprised by how skilled the soldiers were. I wondered who had trained them, but I suppose it was only natural that it would be you.”

[P125]
I gave him a firm thumbs-up, and a smile flickered across Li Feng’s lips.

[P126]
It had been so long since I’d had a normal, pleasant conversation that I was almost moved.

[P127]
“If it would not be discourteous, could you introduce the others as well?”

[P128]
“Of course. This is…”

[P129]
“Greetings! To the respected Seniors of Murim and those who toil day and night for the sake of the nation…”

[P130]
“……”

[P131]
What was this, a job interview at a conglomerate?

[P132]
The young prodigies of the Five Gates of Shanxi had been waiting for their chance. They fell over one another to deliver extravagant introductions and lavish everyone with flattery.

[P133]
That left only one person.

[P134]
“All right. Junior, where are you from, and who are you?”

[P135]
At Gong Ilhyuk’s question, delivered with all the smugness of someone high on his seniority, Cheongpung blinked.

[P136]
“Me?”

[P137]
“Who else would I mean?”

[P138]
“One, two, three, four… There are plenty of people besides me.”

[P139]
A vein bulged on Gong Ilhyuk’s forehead.

[P140]
“Not that! You’re the only one who hasn’t introduced himself!”

[P141]
“Oh, I see. You called me Junior, so I didn’t think you meant me.”

[P142]
“Good heavens! In Murim, we all share the same path! We’re all seniors and juniors to one another. How do you not know that?”

[P143]
If it had been me, I would have laid the sarcasm on thick.

[P144]
But Cheongpung was Cheongpung.

[P145]
He was in a different class from ordinary people.

[P146]
“Wow, I’ve never been anyone’s junior before! Please take good care of me!”

[P147]
“…What kind of person is this?”

[P148]
Sometimes, a pure child was much harder to deal with than an adult who had been properly tainted by the world.

[P149]
Cheongpung spoke with a bright smile.

[P150]
“My name is Cheongpung, and I live in Shanxi.”

[P151]
Gong Ilhyuk had been left speechless, but he finally came to his senses and stammered out a question.

[P152]
“Ahem. Then you must also be one of the young prodigies of the Five Gates of Shanxi.”

[P153]
“Huh? No.”

[P154]
“You’re not?”

[P155]
“No. I came from Henan.”

[P156]
“You just said you were from Shanxi.”

[P157]
“I live in Shanxi, so that makes me a Shanxi man. Hehe.”

[P158]
“You… Whew.”

[P159]
A furrow appeared in Gong Ilhyuk’s forehead.

[P160]
He clearly wanted to throw a punch right then and there, but the occasion forced him to hold himself back.

[P161]
“Fine. Then which sect in Henan are you from? The Iron Blood Sect? The Five Tigers Sword Sect?”

[P162]
“Where are those?”

[P163]
“You’re from Henan, yet you’ve never heard of the Iron Blood Sect or the Five Tigers Sword Sect? How does that make any sense? What, are you from Shaolin Temple?”

[P164]
“Oh, I only stayed in Henan for about two weeks before moving to Shanxi, so I don’t know much about it.”

[P165]
“You said you were from Henan!”

[P166]
“I did come from Henan, but before that, I was in Shaanxi…”

[P167]
“You little bastard! Just say the whole world is your hometown!”

[P168]
Gong Ilhyuk finally exploded. With a roar, he reached for Cheongpung’s collar—or tried to.

[P169]
Grab.

[P170]
His wrist was caught with absurd ease.

[P171]
Gong Ilhyuk let out a hollow laugh.

[P172]
“Well, look at you. You know at least one trick, huh?”

[P173]
“Ah, I just reacted on instinct. I’m sorry, Senior.”

[P174]
“On instinct? And you’re apologizing?”

[P175]
Seeing Cheongpung apologize with a miserable expression, Gong Ilhyuk gave a short laugh.

[P176]
“No. There’s no need to let go. No need to apologize, either.”

[P177]
“Really?”

[P178]
“Yes. But you’ll pay dearly for your reckless bravado.”

[P179]
“What? What does that mean?”

[P180]
“You’re about to find out.”

[P181]
I stepped in at that exact moment.

[P182]
I threw myself in front of Cheongpung, and Gong Ilhyuk regarded me coldly.

[P183]
“Move aside, Junior.”

[P184]
“Pardon me, Senior.”

[P185]
“Pardon you… Should I take this to mean the Jin Family of Taiyuan intends to oppose the actions of our sect?”

[P186]
I answered calmly.

[P187]
“Not at all. I only want to stop this from becoming a bigger problem.”

[P188]
“A problem? What problem?”

[P189]
“His Highness will be arriving soon, won’t he? And there are plenty of eyes on us.”

[P190]
“Plenty of eyes. Deputy Military Commissioner, what do you think?”

[P191]
I could see Hong Jin smiling behind Gong Ilhyuk.

[P192]
His lilting voice followed.

[P193]
“Well, I don’t think it will be much of a problem.”

[P194]
Li Feng immediately objected.

[P195]
“This is the grand hall. We cannot tolerate even a minor disturbance.”

[P196]
“Assistant Commissioner Li, I find the word ‘tolerate’ unpleasant. Anyone listening might think you were my superior.”

[P197]
“Deputy Military Commissioner!”

[P198]
“Why, Assistant Military Commissioner?”

[P199]
No sooner had Hong Jin finished speaking than the other two members of the Three Hands of Zhongnan quietly stepped in front of Li Feng.

[P200]
True to the Zhongnan Sect’s reputation, both were at least advanced First Rate masters.

[P201]
Li Feng bit down hard on his lip, then looked at me and muttered,

[P202]
“I’m sorry.”

[P203]
Gong Ilhyuk smiled triumphantly.

[P204]
“Well? What will you do now?”

[P205]
What else could I do?

[P206]
I shrugged once and stepped back. Gong Ilhyuk’s smile deepened.

[P207]
“A wise choice.”

[P208]
“I only wanted to prevent the problem from getting bigger. You understand, right?”

[P209]
“Of course. Everyone here will remember it clearly.”

[P210]
“I hope so.”

[P211]
Cheongpung stared blankly at me.

[P212]
“Benefactor, did I do something wrong?”

[P213]
Gong Ilhyuk answered before I could.

[P214]
“What? Wrong?”

[P215]
His murderous gaze swung toward Cheongpung.

[P216]
“Are you insulting me and the Zhongnan Sect right now?”

[P217]
“That’s not it. I was just…”

[P218]
“Can’t you shut that mouth of yours?”

[P219]
A complicated, subtle expression appeared on Cheongpung’s face.

[P220]
Then he said the one thing more than enough to make Gong Ilhyuk lose his reason.

[P221]
“Wow, no one’s ever sworn at me before. This is fascinating.”

[P222]
“You goddamn bastard…!”

[P223]
Whoosh!

[P224]
A heavy sound split the air.

[P225]
Gong Ilhyuk’s fist shot toward Cheongpung’s ribs at blinding speed.

[P226]
Then—

[P227]
Crack. Crunch.

[P228]
“……!”

[P229]
“……!”

[P230]
Amid the stunned silence, one man’s mouth fell open in agony.

[P231]
His fist had been crushed. Bone jutted through the torn flesh of his forearm, and Gong Ilhyuk, drenched in blood, asked in a trembling voice,

[P232]
“Wh-what is this? What kind of fist technique…?”

[P233]
If he hadn’t asked, I would have.

[P234]
I had expected this result, but not to this extent.

[P235]
With a single counter, Cheongpung had rendered Gong Ilhyuk, a master above Level 70, completely helpless.

[P236]
And…

[P237]
“That wasn’t a fist technique.”

[P238]
At my mutter, Cheongpung answered with a face that looked ready to vomit.

[P239]
“Benefactor is right. It wasn’t a fist technique. It was a palm technique called the Taeeul Miri Palm. But Senior, you’re bleeding too much. The smell of blood is making my stomach churn. Urk!”

[P240]
What a lunatic.

[P241]
I let out a hollow laugh as Cheongpung flung Gong Ilhyuk aside and began to dry-heave.

[P242]
That was when—

[P243]
“Ta-Taeeul Miri Palm!”

[P244]
Li Feng asked with his eyes wide.

[P245]
“Did you just say Taeeul Miri Palm? Are you certain?”

[P246]
“Urk, yes. My grandfather taught me.”

[P247]
“M-May I ask his name?”

[P248]
“Urk, Mae Jonghak—bleeegh!”

[P249]
Splash!

[P250]
I was shocked that Cheongpung had vomited in the very place where the king was about to arrive, but Li Feng seemed unfazed.

[P251]
He trembled as though he had been struck by lightning, then squeezed out a single word.

[P252]
“The Sword Saint…!”
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
# Chapter 140

[P2]
Gong Ilhyuk of the Three Hands of Zhongnan stared at the young man in front of him with a dubious expression.

[P3]
*What is this guy?*

[P4]
Jin Taekyung, the Sleeping Dragon of Shanxi. He was the driving force behind a whirlwind that had quietly spread his name as far as Shaanxi in the span of only a few months.

[P5]
Gong Ilhyuk mulled over what Jin Taekyung had said.

[P6]
*“The Reign…” What was it?*

[P7]
It definitely seemed as though he had been about to say something before stopping himself.

[P8]
Unlike his enthusiastic reaction when he first heard the name of the Zhongnan Sect, he now looked completely deflated and let out one deep sigh after another.

[P9]
“Whew.”

[P10]
“…What’s with the sighing?”

[P11]
“It’s nothing. Really.”

[P12]
“What do you mean, nothing? Go on and finish what you were saying.”

[P13]
Gong Ilhyuk was beginning to feel irritated. What kind of sect was his? It was none other than the famous Zhongnan Sect.

[P14]
It was one of the great pillars of Murim, a sect that had proudly earned its place among the Nine Sects and One Gang on the strength of centuries of history and deeply rooted martial traditions.

[P15]
And yet…

[P16]
*Can’t he at least be grateful that I acknowledged him? Why is he sighing?*

[P17]
No matter how successful the Jin Family of Taiyuan was, it was still merely a family from the frontier.

[P18]
Compared to the Zhongnan Sect, one of the Nine Sects and One Gang, it was like a firefly before the sun. In terms of both background and personal fame, Jin Taekyung was a hopelessly insignificant greenhorn.

[P19]
*What an arrogant bastard.*

[P20]
Gong Ilhyuk had lived his entire life with pride in being a disciple of the Zhongnan Sect. It was only natural that he felt offended.

[P21]
The other two men known alongside him as the Three Hands of Zhongnan were also looking at Jin Taekyung with displeasure.

[P22]
“Ahem.”

[P23]
“Young friend, you have a habit of stopping halfway when you speak.”

[P24]
As the atmosphere grew increasingly unpleasant, Jin Taekyung waved his hand.

[P25]
“No, it’s not like that. I just misunderstood something on my own.”

[P26]
Gong Ilhyuk opened his mouth, deliberately adopting a generous tone.

[P27]
“What did you misunderstand? Tell me. I’ll answer everything.”

[P28]
“It’s really nothing…”

[P29]
“Ah, just tell me!”

[P30]
“Why are you shouting?”

[P31]
Gong Ilhyuk took a deep breath.

[P32]
He was almost forty years old. Yet here he was, getting worked up over a brat barely twenty.

[P33]
For some reason, looking at that handsome face made his blood boil.

[P34]
“It’s not that… Whew. Anyway, tell me.”

[P35]
“Hmm.”

[P36]
Jin Taekyung finally opened his mouth, as though he had no choice.

[P37]
“Then may I ask you one thing?”

[P38]
“Anything.”

[P39]
“What is the name of the current chairman of the Zhongnan Sect—or rather, the Sect Leader?”

[P40]
“Hm? You mean the Sect Leader’s name?”

[P41]
“Yes.”

[P42]
What kind of question was that? Gong Ilhyuk answered with a puzzled look.

[P43]
“Gong Iljung.”

[P44]
“Ah. Yes.”

[P45]
Jin Taekyung’s response was so indifferent that it was as though he had no idea who that was.

[P46]
The veins on the foreheads of all three men began to bulge.

[P47]
“Have you never heard the Sect Leader’s name?”

[P48]
Jin Taekyung scratched the back of his head.

[P49]
“I think I have. Or maybe not…”

[P50]
“…Then what about the title Wind-and-Cloud Sword Lord?”

[P51]
“Wind-and-Cloud Sword Lord Gong Iljung. Wind-and-Cloud Sword Lord Gong Iljung… Hmm. I’m not sure.”

[P52]
It was beyond absurd.

[P53]
The Sect Leaders and Family Heads of the Nine Sects and One Gang and the Five Great Families were all renowned masters whose names were known throughout the world. No martial artist could possibly be unaware of them.

[P54]
And yet this fellow, who was supposedly a member of the Jin Family of Taiyuan—not some half-baked martial artist—didn’t know the Sect Leader of the Zhongnan Sect.

[P55]
He even called him by his given name, as though they were friends.

[P56]
*Is this bastard making a mockery of the Zhongnan Sect?*

[P57]
Gong Ilhyuk’s head was spinning from the shock when Jin Taekyung suddenly looked up at him.

[P58]
“Oh? Now that I think about it, your names are similar. Gong Iljung, Gong Ilhyuk.”

[P59]
At least he had some basic social awareness. Gong Ilhyuk’s irritation eased slightly.

[P60]
“He’s a family elder.”

[P61]
“Oh, a family elder! Then are you two…?”

[P62]
“He’s my father’s cousin.”

[P63]
“Your father’s cousin!”

[P64]
Seeing Jin Taekyung’s eyes widen, Gong Ilhyuk straightened his shoulders.

[P65]
It wasn’t just anyone. He was the Wind-and-Cloud Sword Lord. Being related to the Sect Leader of the Zhongnan Sect was an immense honor.

[P66]
“Ahem. Don’t spread it around too much. If this became widely known, people’s attitudes toward me would change.”

[P67]
In reality, Gong Ilhyuk wanted this fact to become known more than anyone.

[P68]
He had enjoyed all kinds of benefits by putting the Wind-and-Cloud Sword Lord’s name out front: superior martial arts, elixirs, and even the title of Three Hands of Zhongnan.

[P69]
If he continued advancing at this rate, it was only a matter of time before he seized an important position within the Zhongnan Sect.

[P70]
“You understand what I mean, right? If you absolutely have to tell someone, just tell a few close friends…”

[P71]
Jin Taekyung waved his hand.

[P72]
“No way. I’d never tell anyone. It would obviously hurt Great Hero Gong’s reputation. People would say, ‘He’s a guy who climbed this high by relying on connections.’ Oops. Sorry. Anyway, that kind of rumor would be troublesome, wouldn’t it?”

[P73]
Gong Ilhyuk gave a dry cough. Even he had to admit that the boy wasn’t entirely wrong.

[P74]
“Ahem. It’s not as though it would hurt me that much. I only meant that there might be people who are curious about me…”

[P75]
“People curious about you? I don’t have a single friend, so there’s no one I could tell.”

[P76]
“…Your eldest brother, the Lesser Family Head of the Jin Family, might be curious. Or Young Hero Heaven Shaking Sword.”

[P77]
“Oh, you don’t know much about my family situation. My eldest brother is incredibly busy right now. My second brother isn’t interested in much besides martial arts.”

[P78]
“…Really?”

[P79]
“Yes.”

[P80]
There was nothing more to say after that.

[P81]
As Gong Ilhyuk continued giving irritated coughs, Jin Taekyung smiled brightly.

[P82]
“And what good would it do to tell anyone? If he’s only your father’s cousin, you’re practically strangers. I thought you two were father and son or something.”

[P83]
“……!”

[P84]
* * *

[P85]
There was nothing more exhilarating than screwing someone over while smiling.

[P86]
Especially when it was someone who acted arrogant. If I managed to get one over on them properly, the rush doubled.

[P87]
*Ah. I think I could get addicted to this.*

[P88]
Were they called the Three Hands of Zhongnan?

[P89]
I hadn’t liked them from the moment I met them. Not their gazes, which seemed to look down on everyone, nor their swaggering attitude as members of a great sect.

[P90]
*So it really is different from the novel.*

[P91]
When I was in high school, becoming a disciple of the Zhongnan Sect had been one of my dreams.

[P92]
As expected, reality was a cesspool.

[P93]
I held back my laughter as I watched Gong Ilhyuk trembling with rage.

[P94]
*What a cute bastard. He’s so much fun to tease.*

[P95]
I wanted to keep going, but this was probably enough. If the Jin Family of Taiyuan was a local player, these people were national-level.

[P96]
There was nothing to gain from picking a fight with them.

[P97]
Fortunately, a voice suddenly cut in and lightened the atmosphere.

[P98]
“Aren’t you gentlemen monopolizing the conversation a little? The other guests must be lonely. You haven’t even finished introducing yourselves.”

[P99]
I got goose bumps once at the nasal, lilting voice.

[P100]
Then I got them a second time when the pretty middle-aged man looked at me and winked.

[P101]
“I haven’t introduced myself yet, have I? I’m Hong Jin, the Deputy Military Commissioner of Shanxi Province.”

[P102]
“Deputy Military Commissioner… what?”

[P103]
“The Deputy Military Commissioner. Ah, you’re a martial artist, so I suppose this is your first time hearing of the office?”

[P104]
“Yes.”

[P105]
*I’d heard of “Comrade Chairman,” but “Comrade Deputy Military Commissioner” was a new one.*

[P106]
Hong Jin giggled as he looked at me blinking.

[P107]
Good heavens. A middle-aged man was giggling.

[P108]
“Why that expression? Did something bad happen?”

[P109]
“…No. I’m just so happy.”

[P110]
“Happy? Ho ho ho, you’re adorable. Don’t you agree, Assistant Commissioner Li?”

[P111]
*He called me cute. Fuck, that bastard called me cute.*

[P112]
I was barely holding back my nausea when the man I had seen only briefly earlier greeted me in a blunt voice.

[P113]
“I am Li Feng, Assistant Military Commissioner of Shanxi Province. I oversee the training of the soldiers under the Shanxi Provincial Office.”

[P114]
“And he’s my direct subordinate. Isn’t that right, Assistant Commissioner Li?”

[P115]
Li Feng’s thick eyebrow twitched.

[P116]
We had known each other for less than five minutes, but I already knew one thing.

[P117]
Li Feng hated Hong Jin.

[P118]
That alone made him someone worth treating with courtesy. I performed a fist-and-palm salute.

[P119]
“My name is Jin Taekyung of the Jin Family of Taiyuan.”

[P120]
“I have heard your reputation. A great new star has risen over the Shanxi martial world.”

[P121]
“A new star? You flatter me.”

[P122]
Li Feng shook his head with a serious expression.

[P123]
“No. Rumors are often exaggerated, but after seeing Young Hero Jin today, I can tell they were all true.”

[P124]
Kind words deserved kind words in return.

[P125]
I brought up the soldiers I had seen on the way here.

[P126]
“I was surprised by how skilled the soldiers were. I wondered who had trained them, but I suppose it was only natural that it would be you.”

[P127]
I gave him a firm thumbs-up, and a smile flickered across Li Feng’s lips.

[P128]
It had been so long since I’d had a normal, pleasant conversation that I was almost moved.

[P129]
“If it isn’t discourteous, could you introduce the other guests as well?”

[P130]
“Of course. This is…”

[P131]
“Greetings! To the respected Seniors of Murim and those who toil day and night for the sake of the nation…”

[P132]
“……”

[P133]
What was this, an interview at a conglomerate?

[P134]
The young prodigies of the Five Gates of Shanxi, who had been waiting for an opportunity, rushed to give exaggerated introductions and shower everyone with flattery.

[P135]
That left only one person.

[P136]
“All right. Junior, where are you from, and who are you?”

[P137]
At Gong Ilhyuk’s question, delivered with all the smugness of someone high on his seniority, Cheongpung blinked.

[P138]
“Me?”

[P139]
“Who else would I mean?”

[P140]
“One, two, three, four… There are lots of people besides me.”

[P141]
The veins on Gong Ilhyuk’s forehead bulged.

[P142]
“Not that! You’re the only one who hasn’t introduced himself!”

[P143]
“Oh, I see. You called me a junior, so I didn’t think you meant me.”

[P144]
“Good heavens! In Murim, we’re all fellow practitioners! We’re all seniors and juniors to one another. How do you not know that?”

[P145]
If it were me, I would have responded with heavy sarcasm.

[P146]
But Cheongpung was Cheongpung.

[P147]
He was in a different class from ordinary people.

[P148]
“Wow, this is my first time being a junior! I look forward to working with you!”

[P149]
“…What kind of person is this?”

[P150]
Sometimes, a pure child was much harder to deal with than an adult who had been properly tainted by the world.

[P151]
Cheongpung spoke with a bright smile.

[P152]
“My name is Cheongpung, and I live in Shanxi.”

[P153]
Gong Ilhyuk had been left speechless, but he finally came to his senses and stammered out a question.

[P154]
“Ahem. Then you must also be one of the young prodigies of the Five Gates of Shanxi.”

[P155]
“Hm? No.”

[P156]
“You’re not?”

[P157]
“No. I came from Henan.”

[P158]
“You just said you were from Shanxi.”

[P159]
“I live in Shanxi, so I’m from Shanxi. Hehe.”

[P160]
“Then… whew.”

[P161]
A furrow appeared in Gong Ilhyuk’s forehead.

[P162]
He clearly wanted to throw a punch right then and there, but the occasion forced him to hold himself back.

[P163]
“All right, then. Which sect in Henan are you from? The Iron Blood Sect? The Five Tigers Sword Sect?”

[P164]
“Where are those?”

[P165]
“You’re from Henan, but you don’t know the Iron Blood Sect or the Five Tigers Sword Sect? Does that make any sense? Hm? Then are you from Shaolin?”

[P166]
“Oh, I stayed in Henan for about half a month before moving to Shanxi, so I don’t know much about it.”

[P167]
“You said you were from Henan?”

[P168]
“It’s true that I came from Henan, but before that I was in Shaanxi…”

[P169]
“You little bastard! Then just say the whole world is your hometown!”

[P170]
At last, Gong Ilhyuk exploded. He shouted as he grabbed Cheongpung by the collar—or tried to.

[P171]
Snag.

[P172]
His wrist was caught with absurd ease.

[P173]
Gong Ilhyuk let out a hollow laugh.

[P174]
“Well, look at you. You know at least one trick, huh?”

[P175]
“Ah, I just reacted on instinct. I’m sorry, Senior.”

[P176]
“On instinct? And you’re apologizing?”

[P177]
Seeing Cheongpung apologize with a miserable expression, Gong Ilhyuk gave a short laugh.

[P178]
“Never mind. You don’t have to let go. There’s no need to apologize, either.”

[P179]
“Really?”

[P180]
“Yes. But you’ll pay dearly for your reckless bravado.”

[P181]
“What? What does that mean?”

[P182]
“You’ll find out soon enough.”

[P183]
I stepped in at that exact moment.

[P184]
I threw myself in front of Cheongpung, and Gong Ilhyuk looked at me with dry eyes.

[P185]
“Move aside, Junior.”

[P186]
“Pardon me, Senior.”

[P187]
“Pardon you… Should I take this to mean the Jin Family of Taiyuan intends to oppose the actions of our sect?”

[P188]
I answered calmly.

[P189]
“Not at all. I only want to prevent this from becoming a bigger problem.”

[P190]
“A problem? What problem?”

[P191]
“His Highness will be arriving soon, won’t he? And there are plenty of eyes on us.”

[P192]
“Plenty of eyes. Deputy Military Commissioner, what do you think?”

[P193]
I could see Hong Jin smiling behind Gong Ilhyuk.

[P194]
His delicate voice followed.

[P195]
“Well, I don’t think it will be much of a problem.”

[P196]
Li Feng immediately objected.

[P197]
“This is the grand hall. We cannot tolerate even a minor disturbance.”

[P198]
“Assistant Commissioner Li, I find the word ‘tolerate’ unpleasant. Anyone listening might think you were my superior.”

[P199]
“Deputy Military Commissioner!”

[P200]
“Why, Assistant Military Commissioner?”

[P201]
The instant Hong Jin finished speaking, the other two members of the Three Hands of Zhongnan quietly stepped in front of Li Feng.

[P202]
As befitted members of the Zhongnan Sect, both were at least advanced First Rate masters.

[P203]
Li Feng bit down hard on his lip, then muttered to me,

[P204]
“I’m sorry.”

[P205]
Gong Ilhyuk smiled triumphantly.

[P206]
“Well? What are you going to do now?”

[P207]
What was I supposed to do?

[P208]
I shrugged once and stepped back. Gong Ilhyuk’s smile deepened.

[P209]
“A wise choice.”

[P210]
“I only wanted to prevent the problem from getting bigger. You understand, right?”

[P211]
“Of course. Everyone here will remember it clearly.”

[P212]
“I hope so.”

[P213]
Cheongpung stared blankly at me.

[P214]
“Benefactor, did I do something wrong?”

[P215]
Gong Ilhyuk was faster than I was with his response.

[P216]
“What? Wrong?”

[P217]
His gaze turned murderous as he glared at Cheongpung.

[P218]
“Are you insulting me and the Zhongnan Sect right now?”

[P219]
“That’s not it. I was just…”

[P220]
“Can’t you shut that mouth of yours?”

[P221]
A complicated, subtle expression appeared on Cheongpung’s face.

[P222]
Then he said the one thing more than enough to make Gong Ilhyuk lose his reason.

[P223]
“Wow, this is the first time anyone’s ever sworn at me. How fascinating.”

[P224]
“You goddamn bastard…!”

[P225]
Whoosh!

[P226]
A heavy sound split the air.

[P227]
Gong Ilhyuk’s fist shot toward Cheongpung’s ribs at blinding speed.

[P228]
Then—

[P229]
Crack. Crunch.

[P230]
“……!”

[P231]
“……!”

[P232]
Amid the silent shock, one man opened his mouth wide in pain.

[P233]
His fist had been crushed. Bone jutted through the torn flesh of his forearm, and blood covered Gong Ilhyuk as he asked in a trembling voice,

[P234]
“Wh-what is this? What kind of fist technique…?”

[P235]
If he hadn’t asked, I would have asked the same thing.

[P236]
I had expected this result, but not to this extent.

[P237]
With a single counter, Cheongpung had rendered Gong Ilhyuk, a Level 70-plus master, completely helpless.

[P238]
And then…

[P239]
“It wasn’t a fist technique.”

[P240]
At my mutter, Cheongpung answered with a face that looked ready to vomit.

[P241]
“Benefactor is right. It wasn’t a fist technique. It was a palm technique called the Taeeul Miri Palm. But Senior, you’re bleeding too much. The smell of blood is making my stomach churn. Urk!”

[P242]
What a lunatic.

[P243]
I gave a hollow laugh as Cheongpung flung Gong Ilhyuk aside and began dry heaving.

[P244]
That was when—

[P245]
“Ta-Taeeul Miri Palm!”

[P246]
Li Feng asked with his eyes wide.

[P247]
“Did you just say Taeeul Miri Palm? Are you certain?”

[P248]
“Urk, yes. My grandfather taught me.”

[P249]
“M-May I ask his name?”

[P250]
“Mae Jonghak, urk—urgh!”

[P251]
Splash!

[P252]
I was shocked that Cheongpung had vomited in the very place where the king was about to arrive, but Li Feng seemed unfazed.

[P253]
He trembled as though he had been struck by lightning, then squeezed out a single word.

[P254]
“Sword Saint…”
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 공일중    | **Gong Iljung**    |
| 공일혁    | **Gong Ilhyuk**    |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 종남파    | **Zhongnan Sect**                |
| 소림     | **Shaolin**                      |
| 산서오문   | **Five Gates of Shanxi**         |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 권법     | **fist technique**                               |                                                       |
| 장법     | **palm technique**                               |                                                       |
| 영약     | **elixir**                                       |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 큰형     | **eldest brother**                           |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 철혈문 | **Iron Blood Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 오호검문 | **Five Tigers Sword Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 태을미리장 | **Taeeul Miri Palm** | Palm technique taught to Cheongpung by Mae Jonghak. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 140,
  "passed": true,
  "metrics": {
    "source_characters": 7189,
    "translation_characters": 16074,
    "length_ratio": 2.236,
    "source_paragraphs": 233,
    "translation_paragraphs": 252
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
        "korean": "대협",
        "preferred": "Great Hero or Sir depending tone"
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
        "korean": "송이",
        "preferred": "Song-i"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "세가",
        "preferred": "great family"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "호호호",
        "romanization": "hohoho"
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
