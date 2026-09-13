# Fidelity Gate — Chapter 370

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
  1|＃370화
  2|
  3|
  4|
  5|사천당문은 예로부터 폐쇄적이기로 유명한 가문이었다.
  6|
  7|어지간히 이름난 명사조차 쉽게 드나들 수 없고, 출가외인(出嫁外人)이 가문의 무공과 기밀을 누출할까 염려한 탓에 데릴사위를 들여 당씨 성을 잇게 했다.
  8|
  9|이러한 방식으로 수백 년을 존속한 사천당문의 문이 활짝 열린 것은, 불과 칠 주야 전의 일이었다.
 10|
 11|“거기, 기둥 똑바로 세워!”
 12|
 13|“셋 세면 당긴다. 자. 하나, 둘-!”
 14|
 15|단단한 체구의 인부들이 밧줄을 당기고, 돌과 목재를 실어나른다.
 16|
 17|너른 부지 위, 검붉은 핏자국이 남아 있는 주춧돌 위로 건물이 서서히 형태를 갖춰 나갔다.
 18|
 19|거기서 멀리 떨어진 어느 곳에서는 수십의 승려들이 모여 염불(念佛)을 외었다.
 20|
 21|“원아진생무별염 아미타불독상수 심심상계옥호광…….”
 22|
 23|파르라니 깎은 머리, 정기가 서린 눈빛을 한 승려의 정체는 아미파의 여승들이었다.
 24|
 25|그들의 앞에는 수많은 목관이 불길에 휩싸여 타오르고 있었다.
 26|
 27|“부디 극락왕생하시길. 그대들의 절개와 넋을 잊지 않겠습니다.”
 28|
 29|몇 번의 낮과 밤이 바뀌었지만, 불길은 아직도 꺼지지 않았다.
 30|
 31|삼문혈사(三門血史)에서 유명을 달리한 희생자들은 그만큼 많았고, 그중에서도 특히 사천당문이 입은 인명손실은 극심했다.
 32|
 33|“후우…….”
 34|
 35|“묘령사태, 피곤해 보이시는데 잠시라도 쉬시는 것이…….”
 36|
 37|“아닙니다. 명진 도장. 해야 할 일을 하는 것뿐이니 괘념치 않으셔도 됩니다. 계속하시지요.”
 38|
 39|파리한 안색의 중년 여승을 바라보던 도사가 무겁게 고개를 끄덕였다.
 40|
 41|잠시 후 검을 찬 무림인들이 수십여 개의 목관을 들고 줄지어 걸어왔다.
 42|
 43|그중에는 청성파의 도사도 있었고, 중소 문파의 제자들도 있었으며 땟국물이 줄줄 흐르는 거지도 있었다.
 44|
 45|그런 그들의 뒤로 헐레벌떡 뛰어가는 것은 한 무리의 의원들이었다.
 46|
 47|“갑자기 환자가 피를 토했다니. 안정된 것 아니었나?”
 48|
 49|“그걸 알면 내가 지금 여기 있겠소? 심각한 내상을 입은 건 분명한데 도무지 무슨 증상인지…….”
 50|
 51|“빨리 흩어져서 신의를 모셔와라!”
 52|
 53|아미의 여승과 청성의 도사, 개방의 거지들과 크고 작은 문파에서 파견한 무인들. 거기에 더해 목수, 석공과 의원을 비롯한 양민들까지.
 54|
 55|헤아릴 수 없이 많은 이가 사천당문의 경내를 누비며 각자의 역할을 충실히 하고 있었다.
 56|
 57|높이 솟은 전각. 활짝 열린 창 너머로 이 광경을 지켜보던 젊은 거지, 궁기방은 피곤한 듯한 목소리로 중얼거렸다.
 58|
 59|“살다 살다 이런 광경을 볼 줄은 몰랐군. 그것도 사천당문에서.”
 60|
 61|그러자 침상에 누워 있던 혁무진이 대꾸했다.
 62|
 63|“보지만 말고 가서 좀 도우십쇼. 후개라고 농땡이만 피우지 말고.”
 64|
 65|“농땡이?”
 66|
 67|눈을 부릅뜬 궁기방이 자신의 몸을 가리켰다.
 68|
 69|새하얀 붕대로 칭칭 감긴 상반신. 한쪽 다리에는 임시로 부목을 댔다. 삼괴를 상대하면서 얻은 영광의 상처였다.
 70|
 71|“지금 내 꼴을 보고도 그런 말이 나오나? 이게 농땡이야? 어?”
 72|
 73|“궁 소협만 다쳤습니까?”
 74|
 75|콧방귀를 뀐 혁무진이 보란 듯이 지렁이처럼 몸을 꿈틀거렸다.
 76|
 77|궁기방과는 달리 전신이 붕대로 감겨 있는 그의 모습은 목내이(木乃伊)를 연상케 했다.
 78|
 79|“이 정도는 다쳐야지 아, 이 녀석 고생 좀 했구나. 하는 겁니다. 아시겠어요?”
 80|
 81|“……!”
 82|
 83|궁기방은 몸을 부르르 떨었다. 분명히 크게 다치지 않은 건 자신의 무공이 더 높았다는 반증인데, 왠지 모르게 진 기분이다.
 84|
 85|“난 붕대를 다섯 번이나 갈았다!”
 86|
 87|“전 살아 있는 게 기적입니다. 그리고 그거야 몸이 하도 지저분하니까 그런 것 아닙니까. 참다못한 의원이 궁 소협 때 밀어 주다가 지쳐서 실신했다던데. 사실이에요?”
 88|
 89|“…….”
 90|
 91|“됐습니다. 더 말 섞어 봤자 입 냄새만 나지. 말이 나왔으니 말인데, 다음에는 이빨도 좀 닦아 달라고 하십쇼. 궁 소협이랑 대화할 때마다 저잣거리 똥개 엉덩이에 대고 말하는 기분이에요.”
 92|
 93|실로 악랄한 혓바닥이 아닌가.
 94|
 95|잠시 할 말을 잃었던 궁기방은 천장을 바라보며 한탄했다.
 96|
 97|“삼괴가 저놈을 죽였어야 했는데.”
 98|
 99|“어? 선 넘네?”
100|
101|“도대체 너 같은 놈이 어떻게 그 격전에서 살아남은 건지, 아직도 모르겠다.”
102|
103|“정 궁금하면 우리 조장님이랑 이 년만 붙어 다녀 보시든가.”
104|
105|“……그건 사양하지.”
106|
107|늘 티격태격하는 궁기방과 혁무진이 유일하게 일치하는 의견이 있다면, 그건 바로 진태경에 관한 문제였다.
108|
109|세상의 온갖 평지풍파(平地風波)를 합쳐 놓은 듯한 존재. 그 어떤 위기 속에서도 용케 살아남는 끈질긴 생명력과 집념.
110|
111|그리고 이제는 아득하게 느껴질 만큼의 무위를 갖춘 진태경을 보고 있노라면, 도무지 이게 같은 사람인가 싶을 정도였다.
112|
113|‘그런 사람이 하나 더 있긴 하지.’
114|
115|‘그래, 저놈.’
116|
117|같은 생각을 떠올린 두 사람의 고개가 동시에 한 방향을 향해 움직였다.
118|
119|“미미, 회오리치기!”
120|
121|취리릭!
122|
123|“잘했어, 미미! 이번에는 공중 날기!”
124|
125|취릭?
126|
127|“아, 이건 안 되는구나. 그럼 이번에는…….”
128|
129|혁무진과 궁기방은 생각했다. 뱀에게 공중을 날라고 시키는 저 괴상한 청년이, 정말 검성의 후인이자 기련삼괴 중 가장 강하다는 일괴를 단신으로 쓰러트린 화산신룡이 맞는지.
130|
131|“저기, 궁 소협.”
132|
133|“왜.”
134|
135|“원래 살짝 맛이 가야 초절정 고수가 될 수 있는 겁니까?”
136|
137|“……몰라. 이제는 나도 정말 모르겠다.”
138|
139|궁기방은 대답을 회피했다.
140|
141|그의 스승도 제법 괴팍한 축에 드는 성격이지만, 진태경이나 청풍만큼은 아니었다.
142|
143|검성과 화왕을 보면 제자들이 스승을 닮은 건지도 몰랐다.
144|
145|“그런데 저 뱀은 도대체 뭐예요?”
146|
147|“저렇게 큰 뿔이 달린 뱀은 이무기 빼면 하나뿐이야. 천년독각사.”
148|
149|“어렸을 때 본 영물백과(靈物百科)에서는 온통 검은 빛을 띤 엄청난 독물이라던데.”
150|
151|청풍이 외쳤다.
152|
153|“미미. 엎드려!”
154|
155|취릭!
156|
157|“저걸 보면 독물이 아니라 그냥 동물 같은데.”
158|
159|“제 말이요.”
160|
161|“그런데 청 소협은 왜 여기 있는 거야? 별로 다치지도 않았더만.”
162|
163|“아까 밖에서 큰 소리 나는 거 못 들었습니까? 그거 청 소협이 도와준답시고 나섰다가 전각 부순 거래요.”
164|
165|“……아.”
166|
167|동시에 할 말을 잃은 두 사람은 나란히 침상에 누워 천장을 바라봤다.
168|
169|구 할에 달하는 건물이 파손되는 와중에도 용케 형태를 유지한 전각은, 중요한 환자들을 모아 둔 임시 의방(醫方)으로 쓰이는 중이었다.
170|
171|어디선가 흘러들어 온 탕약 냄새를 맡던 혁무진이 문득 중얼거렸다.
172|
173|“꿈 같네요.”
174|
175|“그러게.”
176|
177|삼문혈사가 일어난 그 날로부터 어언 칠 주야.
178|
179|사천 무림이 결집하여 펼친 천라지망에 사천 곳곳을 피로 물들인 암천의 흑의인들은 대부분 죽거나 사로잡혔고 감쪽같이 사라졌던 삼괴마저 정체 모를 괴인에 의해 붙잡혔다. 그로써 짧은 전란은 막을 내렸다.
180|
181|하지만…….
182|
183|“이게 끝이 아닐 것 같은데. 궁 소협은 어떻게 생각합니까?”
184|
185|“그걸 말이라고. 여기서 끝나면 내 손바닥에 장을 지지겠다.”
186|
187|비단 두 사람뿐만이 아닌 모두가 느끼고 있는 위기였다.
188|
189|고작 두 달 남짓한 시간 동안 하남과 사천이 피로 물들었다.
190|
191|곧 삼문혈사에 관한 소식이 대륙 끄트머리까지 퍼진다면 천하인들은 깨닫게 될 것이다.
192|
193|어느새 암천이라는 먹구름이 코앞까지 다가왔음을.
194|
195|바야흐로 부정할 수 없는 난세(亂世)의 시작이었고, 영웅들은 그러한 난세 속에서 태어나는 법이었다.
196|
197|혁무진의 시선이 자연스럽게 닫혀 있는 문 너머를 향했다.
198|
199|“궁 소협이 생각하기에 조장님께서 언제쯤 깨어나실 것 같습니까?”
200|
201|“글쎄, 나라고 방도가 있나. 우선 문경의 말에 의하면 아무 문제도 없다 하니 기다리는 수밖에.”
202|
203|“말이 나왔으니 말인데, 문경이가 나이에 비해서 실력이 좋긴 하지만 조장을 맡기기에는 좀 그렇지 않습니까?”
204|
205|“신의도 바쁘시니까 그런 거겠지. 적천강 대협께서도 기력을 회복 중이시고, 당사독 대협 같은 중환자들도 워낙 많다 보니까 어쩔 수 없다.”
206|
207|“이해는 합니다. 이해는 하는데, 아무리 신의의 제자라고 하지만 문경이는 좀……. 그 어린 것이 알면 얼마나 알겠습니까?”
208|
209|우려 섞인 혁무진의 말에 청풍이 번쩍 고개를 쳐들었다.
210|
211|“어어, 하지 마세요. 죽어요.”
212|
213|“청 소협?”
214|
215|“방금 하셨던 말, 문 할. 아니 문경이 앞에서는 특히 하지 마세요.”
216|
217|“예? 갑자기 그게 무슨…….”
218|
219|“안 돼요. 정말 안 돼요.”
220|
221|“……?”
222|
223|혁무진과 궁기방이 어리둥절한 얼굴로 서로의 얼굴을 바라보는데 청풍이 갑자기 헙, 하고 숨을 삼켰다.
224|
225|“미미야! 어디 갔어, 미미야!”
226|
227|잠깐 눈을 뗀 사이 사라진 천년독각사를 청풍이 애타게 찾던 그 순간, 굳게 닫힌 문 너머에서 억눌린 외침이 터져 나왔다.
228|
229|“컥! 야, 이 뱀 새끼야!”
230|
231|세 사람의 시선이 허공에서 부딪쳤다.
232|
233|동시에 한 사람을 부르는 여러 개의 이름이 전각 밖까지 쩌렁쩌렁 울려 퍼졌다.
234|
235|“은인!”
236|
237|“조장님!”
238|
239|“진태경!”
240|
241|그 외침에 밖에서 각자의 일을 하고 있던 사람들 사이에서도 일대 소란이 일어났다.
242|
243|“방금 들었나?”
244|
245|“혹시 깨어나신 건가?”
246|
247|“이 소식을 장문인께 알려라! 어서!”
248|
249|
250|
251|* * *
252|
253|
254|
255|악몽을 꿨다.
256|
257|한 치 앞도 보이지 않는 칠흑 같은 어둠 속, 한 마리의 뱀이 천천히 목을 조 여오는 꿈을.
258|
259|숨이 막혔고, 눈앞이 새하얗게 물들었다.
260|
261|그리고 다음 순간, 나는 참았던 숨을 토해 내며 눈을 떴다.
262|
263|“커헉!”
264|
265|취릭.
266|
267|“……?”
268|
269|취릭? 이거 뭐여, 시벌.
270|
271|삼 초간의 사고 정지.
272|
273|마침내 악몽의 정체를 깨달은 나는 목에 칭칭 감겨 있는 뱀의 뿔을 잡아챘다.
274|
275|“야, 이 뱀 새끼야!”
276|
277|천년독각산지 미미쨩인지, 이름이 뭐였건 상관없다. 오늘부터 이 새끼 이름은 뱀술이다.
278|
279|“넌 오늘부터 이슬만 먹고 산다. 참이슬.”
280|
281|붕붕 휘둘러 힘차게 바닥에 내리찍으려던 그때, 굳게 닫혀 있던 문이 박살 나며 한 사람이 뛰쳐 들어왔다.
282|
283|“은인-!”
284|
285|청풍의 쩌렁쩌렁한 외침에 골이 울린다.
286|
287|녀석의 등 뒤로 지렁이처럼 꿈틀거리는 혁무진과 한 발로 콩콩 뛰어오는 궁기방이 보였다.
288|
289|“조장님!”
290|
291|“진태경!”
292|
293|“……너희는 꼴이 왜 그 모양이냐.”
294|
295|혁무진이 힘차게 몸을 튕기며 대답했다.
296|
297|“삼괴. 그 미친 노괴가 절 이렇게 만들었습니다.”
298|
299|궁기방이 친절하게 부연설명을 덧붙였다.
300|
301|“살아남은 것이 천운이다. 혁무진 저 미친놈이 흙에 돌을 섞어서 삼괴에게 던졌거든. 때마침 칠선자가 나서서 막아 주지 않았다면 오체분시 됐을 거다.”
302|
303|“……?”
304|
305|아니, 삼괴는 또 누구고 칠선자는 누구야. 김선자는 나 고등학생 때 학생주임 이름인데…….
306|
307|‘이런 미친놈들.’
308|
309|지하 뇌옥에서 살아남았다는 안도감도 잠시, 나는 두통을 느끼며 이마를 감쌌다.
310|
311|분명히 신의의 거처에 처박혀 있으랬는데, 그새를 못 참고 기어 나와 죽자고 싸운 모양이다.
312|
313|목숨을 건졌기에 망정이지, 죽었으면 어쩔 뻔했나.
314|
315|“너희들 죽고 싶어서 환장했냐? 또 무슨 사고를 친 거야?”
316|
317|“……?”
318|
319|“……?”
320|
321|“뭐, 왜?”
322|
323|이놈들 표정이 왜 이래?
324|
325|청풍을 제외한 우리 세 사람은 어리둥절한 얼굴로 시선을 교환했다.
326|
327|“무슨 문제 있냐?”
328|
329|“당연히 있지.”
330|
331|“조장님이 시키셨잖아요. 가서 아미파 구원하라고.”
332|
333|첫 번째 대답은 궁기방이고, 그다음은 혁무진이었다.
334|
335|둘다 헛소리라 나는 짐짓 눈살을 찌푸렸다.
336|
337|“무슨 소리야. 내가?”
338|
339|“예. 분명히 문경이한테 그렇게 들었는데. 혹시 머리 다치셨어요?”
340|
341|그럴 리가.
342|
343|눈을 뜨자마자 느낄 수 있었다. 전신에서 끓어오르는 강대한 기운.
344|
345|눈 앞에 펼쳐진 시야와 나를 둘러싼 대자연의 기운이 또렷하고 생생하게 느껴졌다.
346|
347|‘이것이 초절정…….’
348|
349|당장이라도 이 힘을 시험해 보고 싶다. 지금쯤 산더미처럼 쌓여 있을 시스템 메시지도.
350|
351|물론 그전에 이런 헛소리를 계속 듣는 대신 한 가지를 물어봐야 했다.
352|
353|“다들 무사하냐?”
354|
355|내가 말한 ‘다들’에 누가 포함되어 있는지는 녀석들도 알고 있을 것이다.
356|
357|환하게 웃은 청풍이 대답 대신 커다란 창문을 활짝 열어젖혔다.
358|
359|“은인께서 직접 확인하세요.”
360|
361|나는 홀린 것처럼 천천히 창가를 향해 걸어갔다.
362|
363|따스한 봄바람이 얼굴을 스쳤고, 이상할 만큼 조용한 공기가 창밖으로 고개를 내민 나를 반긴다.
364|
365|“아.”
366|
367|아래를 내려다본 나는 할 말을 잃었다.
368|
369|그곳에 사람들이 있었다.
370|
371|여승, 도사, 목수와 같은 장인으로 보이는 이도 있고 새하얀 의복을 걸친 의원도 있다. 헤아릴 수 없을 만큼 무수히 많은 시선에 담긴 감정은 하나였다.
372|
373|‘경외.’
374|
375|다음 순간, 그들은 약속이라도 한 것처럼 예를 취했다.
376|
377|누군가는 포권을 취하고, 누군가는 작게 고개를 숙였으며, 누군가는 깊이 엎드려 절했다.
378|
379|동시에 하나가 된 거대한 목소리가 흘러나왔다.
380|
381|“열화신룡(烈火神龍)을 뵙습니다!”
382|
383|한 줄기의 전율이 정수리부터 발끝까지 관통하며 훑어내린 그 순간.
384|
385|띠링.
386|
387|
388|
389|- 당신의 업적과 명성은 중원 전체에 울려 퍼질 것입니다.
390|
391|- 새로운 별호를 획득했습니다!
392|
393|
394|
395|귓가를 파고드는 시스템 알림과 함께, 나는 저 멀리 보이는 한 사람을 발견했다.
396|
397|- 잘했다.
398|
399|나는 적천강을 따라 웃었다.
```

## Assembled English

```markdown
[P1]
# Chapter 370

[P2]
The Sichuan Tang Clan had been famous for its insularity since ancient times.

[P3]
Even renowned figures could not come and go freely. Fearing that daughters who married out might leak the clan’s martial arts and secrets, the clan instead took in live-in sons-in-law and had them carry on the Tang surname.

[P4]
The gates of the Sichuan Tang Clan, which had endured for centuries in this fashion, had been thrown wide open only seven days ago.

[P5]
“Hey, you! Get that pillar straight!”

[P6]
“We pull on three. Ready. One, two—!”

[P7]
Stocky laborers hauled on ropes and carried stones and lumber from place to place.

[P8]
Buildings slowly took shape across the broad site, rising atop foundation stones still stained dark red with blood.

[P9]
Farther away, dozens of monastics gathered to chant Buddhist prayers.

[P10]
“May I live out my days with no other thought, following Amitabha alone, every thought forever fixed on the jade-white light between his brows…”

[P11]
With their closely shaven heads and clear, vigorous gazes, they were nuns of the Emei Sect.

[P12]
Countless wooden coffins burned before them, engulfed in flames.

[P13]
“May you be reborn in the Pure Land. We will never forget your integrity or your souls.”

[P14]
Several days and nights had passed, but the flames had yet to die down.

[P15]
That was how many victims the Three-Sect Bloodbath had claimed. The Sichuan Tang Clan in particular had suffered devastating losses.

[P16]
“Whew…”

[P17]
“You look tired, Satae Myo Ryeong. Perhaps you should rest, even if only for a little while…”

[P18]
“No, Daoist Myeongjin. I am merely doing what must be done, so please do not concern yourself. Let us continue.”

[P19]
The Daoist studied the pale-faced, middle-aged nun, then nodded solemnly.

[P20]
A short while later, martial artists with swords at their waists marched toward them in a line, carrying several dozen wooden coffins.

[P21]
Among them were Daoists from the Qingcheng Sect, disciples from various mid-sized and minor sects, and even a beggar with grime running down his face.

[P22]
A group of physicians hurried along behind them.

[P23]
“I heard a patient suddenly started vomiting blood. Weren’t they stable?”

[P24]
“If I knew that, would I be here right now? They clearly suffered severe internal injuries, but I can’t figure out what their symptoms mean…”

[P25]
“Hurry! Spread out and bring the Divine Physician!”

[P26]
Emei nuns, Qingcheng Daoists, beggars from the Beggars’ Sect, and martial artists dispatched from sects both great and small. Alongside them were commoners, including carpenters, stonemasons, and physicians.

[P27]
Countless people moved through the grounds of the Sichuan Tang Clan, each diligently carrying out their role.

[P28]
From a tall pavilion, a young beggar watched the scene through a wide-open window and muttered wearily.

[P29]
“I never thought I’d live to see something like this. And in the Sichuan Tang Clan, of all places.”

[P30]
Hyuk Mujin, lying on a bed nearby, answered him.

[P31]
“Don’t just stand there watching. Go help. Being the Future Beggar Chief doesn’t mean you get to loaf around.”

[P32]
“Loaf around?”

[P33]
Gung Gibang’s eyes widened as he pointed at himself.

[P34]
His upper body was swathed in snow-white bandages, and one leg had been fitted with a makeshift splint. They were glorious wounds earned while fighting Samgoe.

[P35]
“Look at me! You can see me like this and still say that? You call this loafing around? Huh?”

[P36]
“Are you the only one who got hurt, Young Hero Gung?”

[P37]
Hyuk Mujin snorted and made a show of wriggling like an earthworm.

[P38]
Unlike Gung Gibang, he was wrapped from head to toe in bandages, making him look like a mummy.

[P39]
“You have to get hurt this badly before people look at you and say, ‘Ah, that kid really went through hell.’ Understand?”

[P40]
“…”

[P41]
Gung Gibang trembled.

[P42]
The fact that he had escaped without more serious injuries was proof that his martial arts were superior, yet somehow he felt as though he had lost.

[P43]
“I changed my bandages five times!”

[P44]
“It’s a miracle I’m even alive. And wasn’t that only because you were so filthy? I heard the physician finally lost patience, tried to scrub the grime off you, and passed out from exhaustion. Is that true?”

[P45]
“…”

[P46]
“Forget it. Keep talking and I’ll just have to smell your breath. Since we’re on the subject, ask them to brush your teeth next time too. Every time I talk to you, it feels like I’m speaking straight into the ass of a stray dog in the marketplace.”

[P47]
What a vicious tongue.

[P48]
Struck speechless, Gung Gibang stared at the ceiling and lamented.

[P49]
“Samgoe should have killed that bastard.”

[P50]
“Hey. That’s crossing a line.”

[P51]
“I still don’t understand how someone like you survived that battle.”

[P52]
“If you’re really curious, try following our squad leader around for two years.”

[P53]
“…I’ll pass.”

[P54]
If there was one thing the constantly bickering Gung Gibang and Hyuk Mujin agreed on, it was Jin Taekyung.

[P55]
He seemed like every disaster under the sun rolled into one, with the tenacious vitality and dogged determination to somehow survive any crisis.

[P56]
And now his martial prowess had reached such distant heights that whenever they looked at him, they wondered whether he was truly the same man they had known.

[P57]
*There is one more person like that.*

[P58]
*Yeah. That guy.*

[P59]
Reaching the same thought, the two men turned their heads in the same direction.

[P60]
“Mimi, spin like a whirlwind!”

[P61]
Whrrr!

[P62]
“Good job, Mimi! This time, fly through the air!”

[P63]
Ssssk?

[P64]
“Ah, so this one doesn’t work. Then how about…”

[P65]
Hyuk Mujin and Gung Gibang wondered whether the bizarre young man ordering a snake to fly was truly the heir of the Sword Saint—and the Huashan Divine Dragon who had single-handedly defeated Ilgoe, the strongest of the Qilian Samgoe.

[P66]
“Say, Young Hero Gung.”

[P67]
“What?”

[P68]
“Do you have to be slightly unhinged to become a Supreme Peak master?”

[P69]
“…I don’t know. I really don’t anymore.”

[P70]
Gung Gibang dodged the question.

[P71]
His master was fairly eccentric himself, but not to the same degree as Jin Taekyung or Cheongpung.

[P72]
Judging by the Sword Saint and the Fire King, perhaps disciples really did take after their masters.

[P73]
“But what is that snake, exactly?”

[P74]
“Apart from an imugi,[^1] there’s only one snake with a horn that large. A thousand-year one-horned snake.”

[P75]
“An encyclopedia of spirit creatures I read as a child said it was an enormous, pitch-black venomous creature.”

[P76]
Cheongpung shouted.

[P77]
“Mimi! Lie down!”

[P78]
Ssssk!

[P79]
“Looking at that, it doesn’t seem venomous. It just seems like an animal.”

[P80]
“That’s exactly what I mean.”

[P81]
“But why is Young Hero Cheong here? He barely looks injured.”

[P82]
“Didn’t you hear that loud noise outside earlier? They say Young Hero Cheong went out to help and ended up destroying a pavilion.”

[P83]
“…Ah.”

[P84]
The two men fell silent together, then lay side by side on their beds and stared at the ceiling.

[P85]
Although nearly nine-tenths of the clan’s buildings had been damaged, this pavilion had somehow remained standing. It was now being used as a temporary treatment room for important patients.

[P86]
Hyuk Mujin caught the scent of a medicinal decoction drifting in from somewhere and suddenly muttered,

[P87]
“It feels like a dream.”

[P88]
“Yeah.”

[P89]
Seven days and nights had passed since the day of the Three-Sect Bloodbath.

[P90]
The Sichuan Murim had united and cast an inescapable net across the region. Most of Dark Heaven’s black-clad men, who had painted various parts of Sichuan red with blood, had been killed or captured. Even the Samgoe, who had vanished without a trace, had been caught by a mysterious figure.

[P91]
And with that, the brief war had come to an end.

[P92]
But…

[P93]
“I don’t think this is over. What do you think, Young Hero Gung?”

[P94]
“Do you really have to ask? If this ends here, I’ll eat my hat.”

[P95]
It was a crisis everyone felt—not just the two of them.

[P96]
In barely two months, Henan and Sichuan had been stained with blood.

[P97]
Once news of the Three-Sect Bloodbath spread to the farthest reaches of the continent, the people of the world would realize it.

[P98]
The dark cloud called Dark Heaven was already looming right under their noses.

[P99]
The beginning of an age of chaos that could no longer be denied.

[P100]
And heroes were born in such troubled times.

[P101]
Hyuk Mujin’s gaze naturally drifted toward the closed door.

[P102]
“When do you think our squad leader will wake up?”

[P103]
“Who knows? It’s not like I have any way of telling. Mungyeong says there’s nothing wrong with him, so all we can do is wait.”

[P104]
“Since we’re on the subject, Mungyeong may be skilled for his age, but isn’t he a little too young for us to entrust our squad leader to him?”

[P105]
“The Divine Physician is busy, I suppose. Great Hero Jeok Cheongang is still recovering his strength, and there are so many other critical patients, including Great Hero Tang Sadok. It can’t be helped.”

[P106]
“I understand. I do understand, but even if he is the Divine Physician’s Disciple, Mungyeong is a bit… How much could that child possibly know?”

[P107]
At Hyuk Mujin’s worried words, Cheongpung abruptly lifted his head.

[P108]
“Don’t say that. You’ll die.”

[P109]
“Young Hero Cheong?”

[P110]
“What you just said—don’t say it in front of Grandfa—no, especially not in front of Mungyeong.”

[P111]
“What? Why are you suddenly saying—”

[P112]
“No. Really, don’t.”

[P113]
“…”

[P114]
Hyuk Mujin and Gung Gibang exchanged bewildered looks. Then Cheongpung suddenly gasped.

[P115]
“Mimi! Where did you go, Mimi?”

[P116]
At that moment, just as Cheongpung began desperately searching for the thousand-year one-horned snake that had disappeared during the brief time he looked away, a muffled shout burst from beyond the firmly closed door.

[P117]
“Gack! Hey, you snake bastard!”

[P118]
The three men’s gazes collided in midair.

[P119]
At the same time, several different names for one person rang through the pavilion and echoed outside.

[P120]
“Benefactor!”

[P121]
“Squad Leader!”

[P122]
“Jin Taekyung!”

[P123]
The shouts caused a commotion among the people outside, who had been busy with their respective tasks.

[P124]
“Did you hear that?”

[P125]
“Could he have woken up?”

[P126]
“Report this to the Sect Leader! Quickly!”

[P127]
* * *

[P128]
I had a nightmare.

[P129]
A snake was slowly tightening around my neck in an abyss of pitch-black darkness where I couldn’t see an inch ahead.

[P130]
I couldn’t breathe, and my vision washed white.

[P131]
Then, in the next moment, I opened my eyes and exhaled the breath I had been holding.

[P132]
“Guh-ack!”

[P133]
Ssssk.

[P134]
“…?”

[P135]
*Ssssk? What the fuck is this?*

[P136]
Three seconds of complete mental shutdown.

[P137]
At last, I realized what my nightmare had been. I grabbed the horn of the snake coiled tightly around my neck.

[P138]
“Hey, you snake bastard!”

[P139]
I didn’t care whether its name was Thousand-Year One-Horned Snake, Mimi-chan, or whatever else.

[P140]
From today onward, this bastard’s name was Snake Wine.

[P141]
“You’re living on nothing but dew from now on. Cham Isul.[^2]”

[P142]
I swung it around, preparing to slam it forcefully onto the floor, when the firmly closed door exploded inward and someone charged through.

[P143]
“Benefactor!”

[P144]
Cheongpung’s thunderous shout made my skull ring.

[P145]
Behind him, I saw Hyuk Mujin wriggling like an earthworm and Gung Gibang hopping along on one leg.

[P146]
“Squad Leader!”

[P147]
“Jin Taekyung!”

[P148]
“…Why do you all look like that?”

[P149]
Hyuk Mujin answered while vigorously bouncing his body.

[P150]
“Samgoe. That insane old monster did this to me.”

[P151]
Gung Gibang helpfully elaborated.

[P152]
“It’s sheer luck he survived. That lunatic Hyuk Mujin mixed rocks into some dirt and threw it at Samgoe. If Chilseonja hadn’t stepped in and blocked him at just the right moment, Hyuk Mujin would have been torn limb from limb.”

[P153]
“…?”

[P154]
*Who the hell are Samgoe and Chilseonja? Kim Sunja was the name of my high-school dean of students…*

[P155]
*These fucking lunatics.*

[P156]
My relief at surviving the underground prison lasted only a moment. A headache came on, and I pressed a hand to my forehead.

[P157]
I had specifically told them to hole up at the Divine Physician’s residence, but apparently they couldn’t sit still for even that long and had crawled out to fight to the death.

[P158]
Thank God they had survived. What would I have done if they had died?

[P159]
“Were you idiots desperate to die? What kind of trouble did you cause this time?”

[P160]
“…?”

[P161]
“…?”

[P162]
“What? Why?”

[P163]
Why did they look like that?

[P164]
The three of us—everyone except Cheongpung—exchanged bewildered glances.

[P165]
“Is there a problem?”

[P166]
“Of course there is.”

[P167]
“You told us to go save the Emei Sect, Squad Leader.”

[P168]
The first answer came from Gung Gibang, the second from Hyuk Mujin.

[P169]
They were both talking nonsense, so I deliberately frowned.

[P170]
“What are you talking about? I did?”

[P171]
“Yes. That’s definitely what I heard from Mungyeong. Did you hit your head?”

[P172]
No way.

[P173]
I could feel it the moment I opened my eyes: a powerful qi boiling throughout my entire body.

[P174]
The world spread out before me and the qi of nature surrounding me both felt clear and vivid.

[P175]
*So this is the Supreme Peak realm…*

[P176]
I wanted to test this power right away—and check the mountain of System messages that must have piled up by now.

[P177]
But before either of those, I needed to stop listening to this nonsense and ask one thing.

[P178]
“Is everyone safe?”

[P179]
They all knew who I meant by *everyone*.

[P180]
Smiling brightly, Cheongpung threw open the enormous window instead of answering.

[P181]
“See for yourself, Benefactor.”

[P182]
As if possessed, I slowly walked toward the window.

[P183]
A warm spring breeze brushed my face. An oddly quiet atmosphere greeted me as I leaned out and looked beyond the window.

[P184]
“Ah.”

[P185]
I looked down and was rendered speechless.

[P186]
There were people gathered below.

[P187]
Nuns, Daoists, and people who appeared to be craftsmen, such as carpenters. Physicians wearing brilliant white garments.

[P188]
Countless gazes were fixed on me, all carrying the same emotion.

[P189]
*Awe.*

[P190]
The next moment, as though by some prior agreement, they all paid their respects.

[P191]
Some gave a fist-and-palm salute. Some bowed their heads slightly. Others prostrated themselves deeply.

[P192]
At the same time, one enormous voice rose as though from a single throat.

[P193]
“We pay our respects to the Blazing Fire Divine Dragon!”

[P194]
A shiver pierced me from the crown of my head to the tips of my toes.

[P195]
Ding.

[P196]
> **System**
>
> - Your achievements and Fame will resound throughout the Central Plains.
> - You have acquired a new epithet!

[P197]
Along with the System notification ringing in my ears, I spotted someone in the distance.

[P198]
“Well done.”

[P199]
I smiled back at Jeok Cheongang.

[P200]
[^1]: An *imugi* is a serpent from Korean legend said to become a dragon.

[P201]
[^2]: *Cham Isul* is a Korean soju brand whose name literally means “true dew.”
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 370

[P2]
The Sichuan Tang Clan had been famous for its closed-off ways since time immemorial.

[P3]
Even renowned figures could not easily come and go as they pleased. Fearing that daughters who married out might leak the clan’s martial arts and secrets, the clan instead took in live-in sons-in-law and had them carry on the Tang surname.

[P4]
The gates of the Sichuan Tang Clan, which had survived for hundreds of years in that fashion, had been thrown wide open only seven days ago.

[P5]
“Hey, you! Set that pillar straight!”

[P6]
“We’ll pull when I count to three. Ready. One, two—!”

[P7]
Stocky laborers hauled on ropes and carried stones and lumber from place to place.

[P8]
Across the broad grounds, buildings were slowly taking shape atop foundation stones still stained dark red with blood.

[P9]
Farther away, dozens of monks gathered and chanted Buddhist prayers.

[P10]
“May I be reborn without a single thought of separation. Amitabha alone as my companion. Deeply and profoundly bound, the radiance of the jeweled vessel…”

[P11]
With their heads shaved close and their eyes gleaming with vitality, the monks were nuns of the Emei Sect.

[P12]
Countless wooden coffins burned before them, engulfed in flames.

[P13]
“May you be reborn in the Pure Land. We will never forget your integrity and your souls.”

[P14]
Several days and nights had passed, but the flames had yet to die down.

[P15]
That was how many victims the Three-Sect Bloodbath had claimed. And among them, the Sichuan Tang Clan had suffered particularly devastating losses.

[P16]
“Whew…”

[P17]
“You look tired, Satae Myo Ryeong. You should rest, even if only for a little while…”

[P18]
“No, Daoist Myeongjin. I am merely doing what needs to be done, so please do not concern yourself. Let us continue.”

[P19]
The Daoist gazed at the pale-faced middle-aged nun, then nodded heavily.

[P20]
A short while later, martial artists with swords at their waists came marching in a line, carrying several dozen wooden coffins.

[P21]
Among them were Daoists from the Qingcheng Sect, disciples from various mid-sized and minor sects, and even a beggar with grime running down his face.

[P22]
A group of physicians hurried along behind them.

[P23]
“I heard a patient suddenly started vomiting blood. Wasn’t he stable?”

[P24]
“If I knew that, would I be here right now? He clearly suffered severe internal injuries, but I can’t figure out what his symptoms mean…”

[P25]
“Hurry! Spread out and bring the Divine Physician!”

[P26]
Emei nuns, Qingcheng Daoists, beggars from the Beggars’ Sect, and martial artists dispatched from sects both great and small. Alongside them were commoners, including carpenters, stonemasons, and physicians.

[P27]
Countless people moved through the grounds of the Sichuan Tang Clan, each faithfully carrying out their assigned role.

[P28]
From a tall pavilion, a young beggar watched the scene through a wide-open window and muttered in a weary voice.

[P29]
“I never thought I’d live to see something like this. And in the Sichuan Tang Clan, of all places.”

[P30]
Hyuk Mujin, lying on a bed nearby, answered him.

[P31]
“Don’t just watch. Go help. Just because you’re the Future Beggar Chief doesn’t mean you can loaf around.”

[P32]
“Loaf around?”

[P33]
Gung Gibang opened his eyes wide and pointed at himself.

[P34]
His upper body was tightly wrapped in snow-white bandages, and one leg had been temporarily fitted with a splint.

[P35]
They were glorious wounds earned while fighting Samgoe.

[P36]
“Look at me! You still have the nerve to say that? This is loafing around? Huh?”

[P37]
“Are you the only one who got hurt, Young Hero Gung?”

[P38]
Hyuk Mujin snorted and deliberately wriggled his body like an earthworm.

[P39]
Unlike Gung Gibang, he was wrapped in bandages from head to toe, making him resemble a mummy.

[P40]
“You have to be hurt this badly before people say, ‘Ah, that kid must have really been through hell.’ Do you understand?”

[P41]
“…”

[P42]
Gung Gibang’s body trembled.

[P43]
The fact that he had not been seriously injured was clearly proof that his martial arts were superior, yet for some reason, he felt as if he had lost.

[P44]
“I changed my bandages five times!”

[P45]
“Being alive is a miracle for me. And that’s only because your body was so filthy. I heard the physician who finally lost patience and tried to scrub you down passed out from exhaustion. Is that true?”

[P46]
“…”

[P47]
“Forget it. Talking to you will only leave a bad smell in my mouth. Since we’re on the subject, ask them to brush your teeth next time, too. Every time I talk to you, it feels like I’m speaking straight into the ass of a stray dog in the marketplace.”

[P48]
What a vicious tongue.

[P49]
Gung Gibang was speechless for a moment, then looked up at the ceiling and lamented.

[P50]
“Samgoe should have killed that bastard.”

[P51]
“Hey. That’s crossing a line.”

[P52]
“I still don’t understand how someone like you survived that battle.”

[P53]
“If you’re really curious, try following our squad leader around for two years.”

[P54]
“…”

[P55]
“I’ll pass.”

[P56]
If there was one thing the constantly bickering Gung Gibang and Hyuk Mujin agreed on, it was Jin Taekyung.

[P57]
A man who seemed to embody every disturbance in the world. A man with the tenacious vitality and dogged determination to somehow survive every crisis.

[P58]
And now Jin Taekyung possessed martial prowess so far beyond what they remembered that, whenever they looked at him, they wondered whether he was really the same person.

[P59]
*There is one more person like that.*

[P60]
*Yeah. That guy.*

[P61]
The two men arrived at the same thought, and their heads turned in the same direction.

[P62]
“Mimi, spin like a whirlwind!”

[P63]
Whrrr!

[P64]
“Good job, Mimi! This time, fly through the air!”

[P65]
Ssssk?

[P66]
“Ah, so this one doesn’t work. Then how about…”

[P67]
Hyuk Mujin and Gung Gibang wondered whether the bizarre young man ordering a snake to fly was truly the heir of the Sword Saint and the Huashan Divine Dragon who had single-handedly defeated Ilgoe, the strongest of the Qilian Samgoe.

[P68]
“Say, Young Hero Gung.”

[P69]
“What?”

[P70]
“Do you have to be slightly unhinged to become a Supreme Peak master?”

[P71]
“…”

[P72]
“I don’t know. I really don’t anymore.”

[P73]
Gung Gibang evaded the question.

[P74]
His master was fairly eccentric himself, but not to the same degree as Jin Taekyung or Cheongpung.

[P75]
*Maybe disciples really do take after their masters.*

[P76]
Or perhaps that was simply how the disciples of the Sword Saint and the Fire King turned out.

[P77]
“But what is that snake, exactly?”

[P78]
“There’s only one snake with horns that big, apart from an imugi.[^1] A thousand-year one-horned snake.”

[P79]
“An encyclopedia of spirit creatures I read as a child said it was an enormous, pitch-black venomous creature.”

[P80]
Cheongpung shouted.

[P81]
“Mimi! Lie down!”

[P82]
Ssssk!

[P83]
“Looking at that, it doesn’t seem venomous. It just seems like an animal.”

[P84]
“That’s exactly what I mean.”

[P85]
“Then why is Young Hero Cheong here? He doesn’t look very injured.”

[P86]
“Didn’t you hear that loud noise outside earlier? They say Young Hero Cheong went out to help and ended up destroying a pavilion.”

[P87]
“…”

[P88]
The two men fell silent at the same time. Then they lay side by side on their beds and stared at the ceiling.

[P89]
Although nearly nine-tenths of the buildings had been damaged, this pavilion had somehow remained intact. It was currently being used as a temporary treatment room for important patients.

[P90]
Hyuk Mujin caught the scent of a medicinal decoction drifting in from somewhere and suddenly muttered,

[P91]
“It feels like a dream.”

[P92]
“Yeah.”

[P93]
Seven days and nights had passed since the day of the Three-Sect Bloodbath.

[P94]
The Sichuan Murim had united and cast an inescapable net across the region. Most of Dark Heaven’s black-clad men, who had painted various parts of Sichuan red with blood, had been killed or captured. Even the Samgoe, who had vanished without a trace, had been caught by a mysterious figure.

[P95]
And with that, the brief war had come to an end.

[P96]
But…

[P97]
“I don’t think this is over. What do you think, Young Hero Gung?”

[P98]
“Do you really have to ask? If this ends here, I’ll fry my own palm.”

[P99]
It was a crisis everyone felt—not just the two of them.

[P100]
In barely two months, Henan and Sichuan had been stained with blood.

[P101]
Once news of the Three-Sect Bloodbath spread to the farthest reaches of the continent, the people of the world would realize it.

[P102]
The Dark Heaven storm cloud had already arrived right before their eyes.

[P103]
The beginning of an age of chaos that could no longer be denied.

[P104]
And heroes were born in such troubled times.

[P105]
Hyuk Mujin’s gaze naturally drifted toward the closed door.

[P106]
“When do you think our squad leader will wake up?”

[P107]
“Who knows? Do I look like I have any way of knowing? According to Mungyeong, there’s nothing wrong with him, so all we can do is wait.”

[P108]
“Since we’re on the subject, Mungyeong may be skilled for his age, but isn’t he a little too young for us to entrust our squad leader to him?”

[P109]
“The Divine Physician is busy, I suppose. Great Hero Jeok Cheongang is still recovering his strength, and there are so many other critical patients, including Great Hero Tang Sadok. It can’t be helped.”

[P110]
“I understand. I do understand, but even if he is the Divine Physician’s Disciple, Mungyeong is a bit… How much could that child possibly know?”

[P111]
At Hyuk Mujin’s worried words, Cheongpung abruptly lifted his head.

[P112]
“Don’t. You’ll die.”

[P113]
“Young Hero Cheong?”

[P114]
“What you just said—don’t say it in front of Grandfa—no, especially not in front of Mungyeong.”

[P115]
“What? Why are you suddenly saying—”

[P116]
“No. Really, don’t.”

[P117]
“…”

[P118]
Hyuk Mujin and Gung Gibang exchanged bewildered looks. Then Cheongpung suddenly sucked in a breath.

[P119]
“Mimi! Where did you go, Mimi?”

[P120]
At that moment, just as Cheongpung began desperately searching for the thousand-year one-horned snake that had disappeared during the brief time he looked away, a muffled shout burst from beyond the firmly closed door.

[P121]
“Gack! Hey, you snake bastard!”

[P122]
The three men’s gazes collided in midair.

[P123]
At the same time, several different names for one person rang through the pavilion and echoed outside.

[P124]
“Benefactor!”

[P125]
“Squad Leader!”

[P126]
“Jin Taekyung!”

[P127]
The shouts caused a commotion among the people outside, who had been busy with their respective tasks.

[P128]
“Did you hear that?”

[P129]
“Could he have woken up?”

[P130]
“Report this to the Sect Leader! Quickly!”

[P131]
* * *

[P132]
I had a nightmare.

[P133]
In an abyss of pitch-black darkness where I could not see even an inch ahead, a snake slowly tightening around my neck.

[P134]
I couldn’t breathe, and my vision washed white.

[P135]
Then, in the next moment, I opened my eyes and exhaled the breath I had been holding.

[P136]
“Guh-ack!”

[P137]
Ssssk.

[P138]
“…”

[P139]
*Ssssk? What the fuck is this?*

[P140]
Three seconds of complete mental shutdown.

[P141]
At last, I realized what the nightmare had been. I grabbed the horn of the snake tightly wrapped around my neck.

[P142]
“Hey, you snake bastard!”

[P143]
I didn’t care whether its name was Thousand-Year One-Horned Snake, Mimi-chan, or whatever else.

[P144]
From today onward, this bastard’s name was Snake Wine.

[P145]
“You’re living on nothing but dew from now on. Cham Isul.[^2]”

[P146]
I swung it around, preparing to slam it forcefully onto the floor, when the firmly closed door exploded inward and someone charged through.

[P147]
“Benefactor!”

[P148]
Cheongpung’s thunderous shout made my skull ring.

[P149]
Behind him, I saw Hyuk Mujin wriggling like an earthworm and Gung Gibang hopping along on one leg.

[P150]
“Squad Leader!”

[P151]
“Jin Taekyung!”

[P152]
“…”

[P153]
“Why do you all look like that?”

[P154]
Hyuk Mujin answered while vigorously bouncing his body.

[P155]
“Samgoe. That insane old monster did this to me.”

[P156]
Gung Gibang helpfully added an explanation.

[P157]
“It’s a miracle you’re alive. That crazy Hyuk Mujin mixed dirt with rocks and threw it at Samgoe. If Chilseonja hadn’t stepped in and blocked it at just the right moment, he would have been dismembered.”

[P158]
“What?”

[P159]
*Who the hell are Samgoe and Chilseonja? Kim Sunja was the name of my high-school dean of students…*

[P160]
*These fucking lunatics.*

[P161]
My relief at surviving the underground prison lasted only a moment before I felt a headache coming on and pressed a hand to my forehead.

[P162]
I had clearly told them to hole up at the Divine Physician’s residence, but apparently they had been unable to sit still and had crawled out to fight to the death.

[P163]
Thank God they had survived. What would I have done if they had died?

[P164]
“Were you idiots desperate to die? What kind of trouble did you cause this time?”

[P165]
“…”

[P166]
“…”

[P167]
“What? Why?”

[P168]
Why did they look like that?

[P169]
The three of us—everyone except Cheongpung—exchanged bewildered glances.

[P170]
“Is there a problem?”

[P171]
“Of course there is.”

[P172]
“You told us to go save the Emei Sect, Squad Leader.”

[P173]
The first answer came from Gung Gibang. The second came from Hyuk Mujin.

[P174]
They were both talking nonsense, so I deliberately frowned.

[P175]
“What are you talking about? I did?”

[P176]
“Yes. That’s definitely what I heard from Mungyeong. Did you hit your head?”

[P177]
No way.

[P178]
I could feel it the moment I opened my eyes: a powerful qi boiling throughout my entire body.

[P179]
The world spread out before me and the qi of nature surrounding me felt clear and vivid.

[P180]
*So this is the Supreme Peak realm…*

[P181]
I wanted to test this power immediately. And the System messages that must have piled up by now.

[P182]
But before I could keep listening to this nonsense, there was one thing I needed to ask.

[P183]
“Is everyone safe?”

[P184]
They all knew who I meant by *everyone*.

[P185]
Cheongpung threw open the enormous window instead of answering.

[P186]
“See for yourself, Benefactor.”

[P187]
As if possessed, I slowly walked toward the window.

[P188]
A warm spring breeze brushed my face. An oddly quiet atmosphere greeted me as I leaned out and looked beyond the window.

[P189]
“Ah.”

[P190]
I looked down and was rendered speechless.

[P191]
There were people gathered below.

[P192]
Nuns, Daoists, and people who appeared to be craftsmen, such as carpenters. Physicians wearing brilliant white garments.

[P193]
The emotion contained in the countless gazes turned toward me was singular.

[P194]
*Awe.*

[P195]
The next moment, they all paid their respects as if they had rehearsed it.

[P196]
Some gave a fist-and-palm salute. Some bowed their heads slightly. Others prostrated themselves deeply.

[P197]
At the same time, one enormous voice rose as though from a single throat.

[P198]
“We pay our respects to the Blazing Fire Divine Dragon!”

[P199]
A shiver pierced me from the crown of my head to the tips of my toes.

[P200]
Ding.

[P201]
> **System**
>
> - Your achievements and Fame will resound throughout the Central Plains.
> - You have acquired a new epithet!

[P202]
Along with the System notification ringing in my ears, I spotted someone in the distance.

[P203]
“Well done.”

[P204]
I smiled back at Jeok Cheongang.

[P205]
[^1]: An *imugi* is a serpent from Korean legend said to become a dragon.

[P206]
[^2]: *Cham Isul* is a Korean soju brand whose name literally means “true dew.”
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 370,
  "passed": true,
  "metrics": {
    "source_characters": 6321,
    "translation_characters": 14294,
    "length_ratio": 2.261,
    "source_paragraphs": 195,
    "translation_paragraphs": 201
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
        "korean": "개방",
        "preferred": "Beggars' Sect"
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

## Chapter 374 Expedition

- This branch backfills Chapters 370–373 against the Chapter 65 anchor. Chapters 66–369 have no accepted local English translation here.
- Treat `docs/EXPEDITION_SEED.md` as bounded orientation, not as a substitute for missing translations. Do not read parked Chapters 374–375 while drafting 370–373.
- When the current Korean source conflicts with bridge context, the current source wins. Preserve uncertainty instead of inventing skipped-range backstory.
- After Chapter 373 is committed, run `python tools/expedition.py resume-parked` so the existing 374–375 translations remain the accepted line.

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
