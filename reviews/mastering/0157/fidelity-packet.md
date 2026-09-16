# Fidelity Gate — Chapter 157

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
  1|＃157화
  2|
  3|
  4|
  5|예로부터 명산(名山)의 주인은 영물(靈物)이라고 했다. 중원 오악으로 불리는 화산도 예외는 아니었다.
  6|
  7|사람의 발이 닿기 전, 드높고 광활한 산림을 지배하던 것은 호랑이였다.
  8|
  9|왕의 위엄과 짐승의 흉성을 지닌 이 영물은 자신들의 영역이 침범당하자 분노했고, 이내 허락받지 않은 불청객들을 공격하기 시작했다.
 10|
 11|
 12|
 13|‘와아, 그래서요?’
 14|
 15|‘인명 피해가 극심해지자 화산파에서도 나서지 않을 수 없었지. 복호권(伏虎拳)은 그렇게 탄생했다.’
 16|
 17|
 18|
 19|호랑이를 굴복시키는 권법. 복호권.
 20|
 21|청풍은 오래전 복호권을 배울 당시 할아버지가 해 주었던 말을 똑똑히 기억하고 있었다.
 22|
 23|
 24|
 25|‘풍아, 복호권은 산중제왕을 굴복시킬 만큼 강맹한 무공이다. 이것 하나만 잘 익혀도 네 또래에 널 대적할 녀석은 없을 것이다. 알겠느냐?’
 26|
 27|‘네!’
 28|
 29|
 30|
 31|어린 시절의 청풍은 할아버지의 말을 철석같이 믿었다.
 32|
 33|그러나 십 년이 흐른 지금 이 순간.
 34|
 35|퍽!
 36|
 37|“어우, 아파라.”
 38|
 39|“……어라?”
 40|
 41|그는 처음으로 할아버지도 틀릴 수 있다는 사실을 깨달았다.
 42|
 43|
 44|
 45|* * *
 46|
 47|
 48|
 49|청풍과의 비무를 시작한 지 사흘째. 나는 마흔다섯 번째 비무에서 처음으로 말을 더듬는 녀석을 목격할 수 있었다.
 50|
 51|“으, 은인. 괜찮으세요?”
 52|
 53|“알아요. 복호권 맞죠?”
 54|
 55|눈으로 보고, 직접 맞으면서 겪어 보기까지 했다.
 56|
 57|명치에 복호권을 얻어맞고 뻗었던 것이 어제의 일이다.
 58|
 59|복호권을 시전 할 때의 청풍이 어떻게 움직이는지, 밟는 보법과 어깨의 위치, 이어지는 투로까지 눈에 담고 머릿속에 새겼다.
 60|
 61|하지만 그러고도 공격을 허용했으니 확실히 청풍은 나보다 한 수 위다.
 62|
 63|“방금 그거, 초식 이름이 뭡니까?”
 64|
 65|내 물음에 청풍이 얼떨떨한 얼굴로 대답했다.
 66|
 67|“일권복호(一拳伏虎)요.”
 68|
 69|한 주먹에 호랑이를 쓰러트린다? 확실히 그럴 만한 파괴력을 지닌 초식이다. 비무를 겪을 때마다 쭉쭉 상승하는 맷집이 아니었다면 어제처럼 무릎을 꿇었을 것이다.
 70|
 71|‘그래도 어제보단 많이 나아진 걸 위안 삼아야 하나?’
 72|
 73|올라간 것은 맷집뿐만이 아니다. 청풍의 무공을 직접 몸으로 겪으면서 점점 익숙해지고 있었다.
 74|
 75|“자, 다시 갑시다.”
 76|
 77|하지만 청풍은 그럴 생각이 없어 보였다.
 78|
 79|“어떻게 피하신 거예요?”
 80|
 81|“예?”
 82|
 83|“정확히 봉미혈(鳳尾穴) 부근을 노렸는데…….”
 84|
 85|봉미혈이라면 늑골 어림이다. 나름 피한다고 몸을 틀었다가 복부 한가운데를 정통으로 얻어맞은 거다.
 86|
 87|상대의 목적에서 벗어났으니 이것도 어떻게 보면 피하긴 한 셈인가? 나는 어깨를 으쓱했다.
 88|
 89|“한 대라도 안 맞아 보려고 몸부림쳐 본 거죠, 뭐. 결국은 얻어맞았지만.”
 90|
 91|“투로가 보였나요?”
 92|
 93|며칠 동안 두들겨 맞다 보니 어렴풋이 보이긴 한다. 어디서 어떻게 공격이 들어올지. 또 다음 초식이 어떻게 이어질지.
 94|
 95|‘아직 서툴러서 문제지.’
 96|
 97|나는 욱신거리는 복부를 문지르며 대답했다.
 98|
 99|“지금까지 맞은 짬이 있는데 그 정도는 읽어야죠. 일부러 맞을 때마다 눈 부릅뜨고 봤습니다.”
100|
101|얻어맞으면서도 눈을 감지 않는 것, 상대의 투로를 파악하는 것의 기본 아닌가?
102|
103|“어어, 이상하다. 복호권은 몇 번 안 썼는데.”
104|
105|“그래서 다른 것보다는 좀 더 걸리더라고요.”
106|
107|“다른 거요?”
108|
109|“네. 매화권 같은 건 나름 쉽던데? 비무에서 가장 많이 썼던 거라 그런지 대충 알겠더라고요.”
110|
111|청풍이 감탄성과 함께 박수를 쳤다.
112|
113|“와아, 보여 주실 수 있어요?”
114|
115|“뭐 어려운 건 아니니까.”
116|
117|나는 어설픈 자세로 짝퉁 매화권을 펼쳤다. 보법도, 동작도 영 엉성하지만 모두 청풍이 비무 때마다 펼치던 매화권의 초식들이다.
118|
119|‘이 정도쯤이야, 뭘.’
120|
121|무공을 익히다 보니 어느 순간부터 깨달았다.
122|
123|식(式)에는 무공에 대한 이해와 그에 걸맞은 공력 운용이 필요하지만, 형(形)을 따라 하는 건 쉽다는 사실을.
124|
125|‘여기서는 이렇게 움직였지, 아마?’
126|
127|일 초식부터 칠 초식까지. 간혹 버벅거리긴 했지만, 무리 없이 최대한 자연스럽게 펼쳐 보인 뒤 고개를 돌렸다.
128|
129|“일단 이 정도인데…… 저기 청 소협?”
130|
131|“아, 네. 은인.”
132|
133|“무슨 문제라도 있습니까? 표정이 왜 그래요?”
134|
135|“아뇨, 그게…….”
136|
137|어쩐지 복잡 미묘한 표정으로 나를 바라보던 청풍이 머뭇거리며 입을 열었다.
138|
139|“갑자기 할아버지가 하셨던 말씀이 생각나서요.”
140|
141|“검성 할배, 아니 조부님이요?”
142|
143|“네. 저를 도둑놈이라고 부르셨거든요.”
144|
145|“괜찮아요. 저도 어릴 때 엄마 지갑에서 몰래 천 원 빼 갔다가 뒤지게 맞았어요.”
146|
147|“그게 아니라…….”
148|
149|청풍이 한숨을 푹 내쉬었다.
150|
151|“무공을 가르쳐 주시면서 늘 그러셨어요. 저보고 무공 빼먹는 도둑놈이라고.”
152|
153|“아.”
154|
155|이거 칭찬 맞지? 청풍 같은 재능충에게 칭찬을 받다니.
156|
157|얼떨떨해하는 내게 청풍이 말했다.
158|
159|“은인은 무공의 천재가 분명해요.”
160|
161|“천재요? 제가?”
162|
163|“네.”
164|
165|천재는 무슨……이 아니고, 맞긴 맞다.
166|
167|따져 보면 고작 두세 달 만에 일류 무공인 진무보법과 창법을 대성했으니까.
168|
169|물론 전부 시스템 빨이지만.
170|
171|“그냥 편법이에요. 제가 몸 쓰는 건 잘하는 편이라. 눈도 좋은 편이고. 흐흐.”
172|
173|“할아버지께서 그러셨어요. 무공은 눈이 칠, 발이 삼이라고.”
174|
175|“그 말은 맞는 것 같은데, 아무튼 전 아니에요.”
176|
177|“잘 생각해 보세요. 분명히 전에도 비슷한 일이 있었을걸요?”
178|
179|그런가?
180|
181|문득 어린 시절이 떠올랐다. 원체 운동신경이 좋아서 무슨 스포츠건 잘하는 편이긴 했는데. 굳이 무공이라고 할 만한 건…….
182|
183|‘어, 하나 있네.’
184|
185|내 표정이 변하자 청풍이 그거 보란 듯이 고개를 끄덕였다.
186|
187|“그런 적 있죠?”
188|
189|“있긴 있네요. 태권도라고.”
190|
191|“태권도요?”
192|
193|“무술 비슷한 겁니다.”
194|
195|초딩 시절에 휴대용 게임기를 준다는 감언이설에 속아 등록한 태권도 도장.
196|
197|고등부 형들의 태권도 시범이 있었고, 정확히 두 번 만에 태극 1장부터 8장까지 따라 할 수 있게 됐다.
198|
199|물론 일주일도 지나지 않아 두 살 많은 중학생 형을 때리고 잘렸지만.
200|
201|‘설마 그게?’
202|
203|그러고 보니 F급 헌터 시절에도 뭐든 곧잘 따라 하긴 했었다.
204|
205|다만 허접한 신체 능력이 발목을 잡았을 뿐.
206|
207|나 같은 최하급 헌터가 중급 헌터의 움직임을 따라 하다가는 파괴력도 안 나올뿐더러 가랑이만 찢어지기 때문이었다.
208|
209|‘하지만 이제는 다르지.’
210|
211|넘치는 공력. 뛰어난 신체 능력. 그리고 무림에서 익힌 무공.
212|
213|이제 보니 무공의 천재까지는 아니어도, 내게 제법 재능이 있긴 한 모양이다.
214|
215|“청 소협은 매화권 익히기까지 얼마나 걸렸어요?”
216|
217|“한 달이요.”
218|
219|“한 달?”
220|
221|직접 해 본 바로는 매화권이 화산파의 무학이긴 하나 그 정도로 복잡한 무공은 아니다.
222|
223|그런데 저 녀석이 한 달 걸려서 익힌 걸 사흘 만에 얼추 따라 하게 됐다고?
224|
225|‘미쳤다.’
226|
227|입이 찢어질 정도로 환히 웃는 내게 청풍이 덧붙였다.
228|
229|“대성(大成)하는 데 한 달이나 걸렸다고 할아버지한테 호되게 혼이 났죠.”
230|
231|“…….”
232|
233|그럼 그렇지.
234|
235|어이없어하는 나를 보며 청풍이 중얼거렸다.
236|
237|“그래도…… 썩 좋은 기분은 아니네요. 누가 내 무공을 따라 한다는 거.”
238|
239|심상치 않은 기세가 피어올랐다.
240|
241|
242|
243|* * *
244|
245|
246|
247|혼절에서 깨어난 혁무진은 멍하니 연무장을 바라봤다.
248|
249|‘끝내주네.’
250|
251|연무장은 이미 반쯤 초토화된 상태였다.
252|
253|산서성에서 방귀깨나 뀐다는 석공들이 정성 들여 깔아 놓은 청석은 절반 이상이 박살 났고, 지금도 빠르게 망가지는 중이었다.
254|
255|캉! 카카카캉!
256|
257|계절이 무색하게도 연무장 중앙은 열기로 후끈 달아올랐다. 불꽃을 터트리며 격돌하는 창과 검.
258|
259|병장기를 쥔 주인들이 눈부신 속도로 움직이며 주고받는 합은 일류 고수인 혁무진의 눈으로도 따라가기 버거웠다.
260|
261|‘어떻게 저렇게 빠를 수 있지?’
262|
263|흰 무복을 입은 청풍과 검은 무복을 걸친 진태경.
264|
265|한눈에도 극도로 대비되는 그들이 자신과 비슷한 또래라는 사실이 그저 놀라울 따름이었다.
266|
267|‘청풍 저 인간은 괴물 수준이군.’
268|
269|적당한 체구에 선한 인상. 당장 태원 거리에 반나절만 있어도 또래의 비슷한 젊은이를 서너 명은 만날 수 있을 것 같다.
270|
271|그러나 저 평범한 청년에게는 아무도 쉽게 예상하지 못하는 신분이 감춰져 있다.
272|
273|‘검성 매종학의 모든 것을 물려받은 후인.’
274|
275|쐐애애애액! 쉭!
276|
277|높이 솟은 태양 아래 진태경의 창날이 번득인다.
278|
279|무겁고 간결한 초식, 그러나 힘과 속도가 더해지니 보는 것만으로도 아찔해지는 극쾌의 창술로 변모했다.
280|
281|‘만약 저 창이 나를 노린다면?’
282|
283|혁무진은 고개를 절레절레 저었다.
284|
285|부끄럽지만 일다경 이상 버틸 자신이 없다. 아니, 어쩌면 그 생각마저도 스스로의 자존심을 지키기 위한 위안일지 모른다.
286|
287|하지만 청풍은 달랐다.
288|
289|쉬익, 쉬쉬쉬쉭!
290|
291|사방을 점하고 달려들던 창날이 허무하게 허공을 갈랐다. 손쉽게 모든 공격을 피해 내는 청풍의 얼굴은 평온했다.
292|
293|이어 그의 손이 흐릿해진다 싶더니 한 줄기 빛이 공기를 갈랐다.
294|
295|쐐애애애액! 쾅!
296|
297|“흡!”
298|
299|굉음과 함께 진태경이 신음을 토해 냈다. 가까스로 검을 막아 낸 그를 향해 장대비 같은 검격이 쏟아졌다.
300|
301|그 광경을 지켜보던 혁무진은 자신도 모르게 입을 벌렸다. 지금 이 순간, 한 가지 생각이 그의 머릿속을 꽉 채웠다.
302|
303|‘유려하다.’
304|
305|그렇게밖에 표현할 수 없다.
306|
307|청풍의 움직임은 경지에 오른 화공의 붓놀림처럼 섬세하고 부드러웠고, 계절의 끝에서 너울너울 떨어지는 꽃잎을 닮았다.
308|
309|넋을 놓고 바라보던 혁무진이 문득 중얼거렸다.
310|
311|“매화검법…….”
312|
313|그는 지금까지 화산파의 무공을 본 적이 없다.
314|
315|그러나 한 가지는 확신할 수 있었다. 청풍의 몸놀림 하나하나에 화산파 무학의 정수(淨水)가 스며들어 있음을.
316|
317|‘괴물이군. 말 그대로 괴물이야.’
318|
319|그러나 괴물은 청풍 한 명만을 가리키는 단어가 아니었다.
320|
321|쉬쉬쉬쉬쉭!
322|
323|카가가강!
324|
325|검성의 제자가 펼치는 매화검법을 모조리 막아 내는 또 다른 한 사람.
326|
327|장대한 체구와 선 굵은 잘생긴 외모의 청년이 빠득, 이를 갈았다.
328|
329|“씨이벌, 화산파 무공 진짜 개같이 만들었네!”
330|
331|화산파가 들었다면 뒤집혔을 만한 걸쭉한 욕설을 내뱉은 진태경의 몸에서 거친 기세가 뿜어져 나왔다.
332|
333|청풍의 유려함을 순간적으로 억누를 만큼 패도적인 기세는 곧 반격으로 이어졌다.
334|
335|후우우웅! 쾅!
336|
337|강맹한 일격.
338|
339|굉음과 함께 창을 막아 낸 청풍의 신형이 훨훨 날았다. 단 한 수로 청풍의 공세를 떨쳐 낸 진태경이 인상을 찡그렸다.
340|
341|“으, 따가워.”
342|
343|스스슥. 말이 끝나기가 무섭게 그가 입고 있던 검은 무복이 길게 갈라졌다.
344|
345|살이 드러난 가슴팍에는 몇 줄기의 상흔과 핏물이 흥건하게 배어 나왔다.
346|
347|“이건 무슨 무공입니까?”
348|
349|“천응조(天鷹爪)요.”
350|
351|“없는 게 없네.”
352|
353|“알려 드릴까요?”
354|
355|“알려 줘도 됩니까?”
356|
357|“어, 지금 생각났는데 할아버지께서 외인한테는 알려 주지 말라고 하셨어요.”
358|
359|“또? 내 그럴 줄 알았지.”
360|
361|“화산파에 입문하실래요?”
362|
363|“안 해!”
364|
365|고함을 내지른 진태경이 지면을 박차고 달려들었다.
366|
367|아슬아슬하게 무공의 형태를 지키면서도 맹수와도 같은 본능적인 움직임. 혁무진은 몸을 부르르 떨었다.
368|
369|‘저 인간은 어째 갈수록 더 무서워지네.’
370|
371|사람에게는 저마다 기세라는 것이 있다.
372|
373|진태경의 기세는 끈질기고 치열하다. 보는 사람으로 하여금 두려워지게 하는 무언가가 있다.
374|
375|‘무공의 문제가 아니야.’
376|
377|현재의 진태경도 물론 충분히 뛰어난 고수지만 검성의 제자이자 당당한 절정 고수인 청풍만큼은 아니다.
378|
379|그러나 최근 몇 달간 그를 가까이서 지켜본 혁무진은 확신할 수 있었다.
380|
381|‘하늘이 무너져도 살아날 인간이지.’
382|
383|어떤 지옥에 던져 놔도 진태경은 살아 돌아올 것 같다는 확신.
384|
385|지금까지 세 명의 절정 고수가 그를 죽이려고 했지만 결국 쓰러진 것은 그들이었다. 무림에서는 살아남는 자가 강자이며, 진태경은 거기서 끝끝내 살아남았다.
386|
387|게다가…….
388|
389|‘조장의 성장 속도는 상상을 초월한다.’
390|
391|가장 가까이서 지켜봐 왔기에 알 수 있는 사실이었다.
392|
393|일문일살 조필을 처절한 혈투 끝에 쓰러트린 그때부터 청풍과 맞서 싸우고 있는 지금까지.
394|
395|진태경은 나날이 강해지고 있다.
396|
397|‘그건 지금 이 순간도 마찬가지.’
398|
399|바로 며칠 전만 하더라도 청풍이 쏟아 내는 화산파의 절기들 앞에 불과 백여 초를 버티지 못했다.
400|
401|그러나 지금은?
402|
403|혁무진이 직접 지켜본 것만 삼백여 초가 훌쩍 넘어갔다. 화산파의 본산 제자들만 익힐 수 있다는 천응조에 당해 놓고도 ‘앗, 따가워.’가 고작이다.
404|
405|‘괴물이지. 괴물.’
406|
407|비슷한 또래에 다들 절정, 초일류. 이건 해도 해도 너무한 것 아닌가. 어째 주위에 하나같이 괴물들만 득실거리는 것 같다.
408|
409|한숨을 푹 내쉬던 혁무진은 며칠 전 벽호공을 수련할 당시 진태경이 했던 말을 되새겼다.
410|
411|
412|
413|‘소중한 걸 잃기 싫다면 지금 목숨 걸고 해. 숨이 붙어 있을 때 죽도록 노력하는 게 죽는 것보다는 낫잖아?’
414|
415|
416|
417|그 말이 맞다. 그렇게 죽도록 노력해야 살아남아 강자가 된다. 무림이라는 파도에 휩쓸리지 않기 위해 선 촌각이 아쉽다.
418|
419|가만히 두 사람의 비무를 지켜보던 혁무진이 자리를 털고 일어났다.
420|
421|‘새끼발가락으로 끝낼 순 없지.’
422|
423|강해져야 한다. 진태경의 오른팔, 혹은 심장으로 인정받을 정도로. 그리고…….
424|
425|‘모든 사람에게 혁무진이라는 이름으로 기억될 정도로.’
426|
427|그는 검갑을 꽉 움켜쥐었다.
```

## Assembled English

```markdown
[P1]
# Chapter 157

[P2]
Since ancient times, it had been said that the masters of famous mountains were spirit creatures. Huashan, one of the Five Great Mountains of the Central Plains, was no exception.

[P3]
Before humans ever set foot there, tigers had ruled its lofty, sprawling forests.

[P4]
These spirit creatures possessed the majesty of kings and the ferocity of beasts. When their territory was invaded, they grew furious and soon began attacking the uninvited trespassers.

[P5]
“Wow! And then?”

[P6]
“When the loss of human life became severe, the Huashan Sect had no choice but to step in. That was how the Crouching Tiger Fist was born.”

[P7]
*A fist technique that subdues tigers. The Crouching Tiger Fist.*

[P8]
Cheongpung clearly remembered what his grandfather had told him when he learned the Crouching Tiger Fist long ago.

[P9]
“Pung, the Crouching Tiger Fist is a powerful martial art capable of subduing the king of the mountains. Master this one technique, and no one your age will be able to stand against you. Do you understand?”

[P10]
“Yes!”

[P11]
As a child, Cheongpung had believed his grandfather’s words without question.

[P12]
But now, ten years later—

[P13]
*Whack!*

[P14]
“Ow, that hurt.”

[P15]
“…Huh?”

[P16]
For the first time, he realized that even his grandfather could be wrong.

[P17]
* * *

[P18]
It was the third day since I’d begun sparring with Cheongpung. During our forty-fifth duel, I witnessed him stumble over his words for the first time.

[P19]
“B-Benefactor, are you all right?”

[P20]
“I know. That was the Crouching Tiger Fist, right?”

[P21]
I’d seen it with my own eyes and even experienced it firsthand by getting hit.

[P22]
It was yesterday that a Crouching Tiger Fist to the solar plexus had laid me out flat.

[P23]
I’d committed the way Cheongpung moved when he used the Crouching Tiger Fist to memory—the footwork, the position of his shoulders, even the sequence of forms that followed.

[P24]
And yet I had still allowed myself to be hit.

[P25]
There was no doubt about it. Cheongpung was one step ahead of me.

[P26]
“What was the name of that form just now?”

[P27]
Cheongpung answered with a dazed expression.

[P28]
“One Fist Subdues the Tiger.”

[P29]
A single fist that brought down a tiger? It certainly packed enough destructive power to justify the name. If my ability to take a hit hadn’t improved with every duel, I would have dropped to my knees just like yesterday.

[P30]
*Should I take comfort in doing much better than yesterday?*

[P31]
And it wasn’t only my ability to take a hit that had improved. After experiencing Cheongpung’s martial arts firsthand, I was gradually getting used to them.

[P32]
“All right, let’s go again.”

[P33]
But Cheongpung didn’t seem interested in continuing.

[P34]
“How did you dodge it?”

[P35]
“Huh?”

[P36]
“I was aiming precisely around your Fengwei acupoint…”

[P37]
The Fengwei acupoint was around the ribs. I’d twisted aside to dodge, only to take the blow square in the middle of my abdomen.

[P38]
Since I’d avoided his intended target, maybe that technically counted as dodging? I shrugged.

[P39]
“I just struggled to avoid getting hit even once. I got hit in the end, though.”

[P40]
“Could you see the sequence of forms?”

[P41]
After being beaten up for several days, I could make out the forms vaguely. Where and how an attack would come from. How the next form would follow.

[P42]
*The problem is that I’m still clumsy.*

[P43]
I rubbed my aching abdomen as I answered.

[P44]
“After taking this many hits, I should be able to read at least that much. Every time you hit me, I made sure to keep my eyes wide open and watch.”

[P45]
Wasn’t keeping your eyes open even while getting hit and figuring out your opponent’s sequence of forms the most basic thing?

[P46]
“Huh. That’s strange. I’ve only used the Crouching Tiger Fist a few times.”

[P47]
“That’s why it took me a little longer to figure out than the others.”

[P48]
“The others?”

[P49]
“Yeah. The Plum Blossom Fist was pretty easy. Maybe it’s because you used it the most during our duels, but I more or less figured it out.”

[P50]
Cheongpung clapped in admiration.

[P51]
“Wow! Can you show me?”

[P52]
“It’s nothing difficult.”

[P53]
I performed a poor imitation of the Plum Blossom Fist. My footwork and movements were both terribly awkward, but every form came from the Plum Blossom Fist Cheongpung had used in our duels.

[P54]
*This much is easy.*

[P55]
At some point after I began learning martial arts, I’d realized something.

[P56]
Executing a technique required an understanding of the martial art and the internal-energy control to match. But merely copying its shape was easy.

[P57]
*I moved like this here, didn’t I? Probably?*

[P58]
From the first form to the seventh. I occasionally stumbled, but I managed to perform them as naturally as possible without much difficulty. Then I turned my head.

[P59]
“That’s about it for now… Young Hero Cheongpung?”

[P60]
“Ah, yes, Benefactor.”

[P61]
“Is something wrong? Why do you look like that?”

[P62]
“No, it’s just…”

[P63]
Cheongpung stared at me with an oddly complicated expression before hesitantly opening his mouth.

[P64]
“I suddenly remembered something my grandfather once said.”

[P65]
“The Sword Saint old man—I mean, your grandfather?”

[P66]
“Yes. He used to call me a thief.”

[P67]
“It’s all right. When I was young, I secretly took a thousand won from my mother’s wallet and got beaten half to death.”

[P68]
“That’s not what I mean…”

[P69]
Cheongpung let out a deep sigh.

[P70]
“He always said it while teaching me martial arts. He called me a thief who stole martial arts.”

[P71]
“Oh.”

[P72]
That was a compliment, right? To think a talent freak like Cheongpung was praising me.

[P73]
As I stood there dumbfounded, Cheongpung said, “Benefactor, you’re definitely a martial-arts genius.”

[P74]
“A genius? Me?”

[P75]
“Yes.”

[P76]
*A genius, my ass…*

[P77]
No, wait. He was right.

[P78]
When I thought about it, I had mastered the Jin Family’s Manoeuvre Technique and spear technique—both First Rate martial arts—in barely two or three months.

[P79]
Of course, that was all thanks to the System.

[P80]
“It’s just a shortcut. I’m pretty good at using my body. My eyes are good, too. Heh heh.”

[P81]
“My grandfather used to say that martial arts are seventy percent eyes and thirty percent feet.”

[P82]
“I think he was right about that, but either way, I’m not a genius.”

[P83]
“Think about it carefully. I’m sure something similar happened before.”

[P84]
Was that so?

[P85]
I suddenly remembered my childhood. I’d always been good at sports thanks to my natural athletic ability, but as for anything that could be called martial arts…

[P86]
*Oh. There was one.*

[P87]
When my expression changed, Cheongpung nodded as if to say, *See?*

[P88]
“Something did happen, didn’t it?”

[P89]
“There was one. Taekwondo.”

[P90]
“Taekwondo?”

[P91]
“It’s something like a martial art.”

[P92]
Back in elementary school, I’d been lured into enrolling at a taekwondo academy with the promise of a portable game console.

[P93]
The older high school students had put on a taekwondo demonstration, and after watching it exactly twice, I could follow all eight Taegeuk forms.[^1]

[P94]
[^1]: The Taegeuk forms are a standardized sequence of eight color-belt patterns in taekwondo.

[P95]
Of course, less than a week later, I beat up a middle schooler two years older than me and got kicked out.

[P96]
*Could that have been it?*

[P97]
Come to think of it, even when I was an F-rank Hunter, I’d been pretty good at copying almost anything.

[P98]
My lousy physical abilities had simply held me back.

[P99]
If a bottom-tier Hunter like me tried to imitate the movements of a mid-rank Hunter, I wouldn’t be able to generate any destructive power. I’d just tear my groin apart.

[P100]
*But things are different now.*

[P101]
Overflowing internal energy. Excellent physical abilities. And martial arts learned in Murim.

[P102]
Now that I thought about it, I might not be a martial-arts genius, but I did seem to have a fair amount of talent.

[P103]
“How long did it take you to learn the Plum Blossom Fist, Young Hero Cheongpung?”

[P104]
“One month.”

[P105]
“One month?”

[P106]
From my own experience, the Plum Blossom Fist was a Huashan martial art, but it wasn’t complicated enough to take that long.

[P107]
And this guy had needed a month to learn it, while I’d managed a rough imitation in three days?

[P108]
*That’s insane.*

[P109]
As I grinned so broadly that the corners of my mouth nearly split, Cheongpung added, “It took me a whole month to achieve Great Attainment, so my grandfather scolded me terribly.”

[P110]
“…”

[P111]
Right. Of course.

[P112]
As I stared at him in disbelief, Cheongpung muttered, “Still… it doesn’t feel very good. Having someone copy my martial arts.”

[P113]
An ominous aura rose from him.

[P114]
* * *

[P115]
After regaining consciousness, Hyuk Mujin stared blankly at the training ground.

[P116]
*This is incredible.*

[P117]
The training ground had already been half reduced to rubble.

[P118]
More than half of the bluestone carefully laid by stonemasons famous throughout Shanxi Province had been smashed apart, and the destruction was continuing at a rapid pace.

[P119]
*Clang! Ka-ka-ka-clang!*

[P120]
Despite the season, the center of the training ground was scorching hot. Spear and sword clashed amid bursts of flame.

[P121]
The men wielding them moved at dazzling speed, exchanging blows so quickly that even Hyuk Mujin, a First Rate master, struggled to follow.

[P122]
*How can they be that fast?*

[P123]
Cheongpung wore white martial robes, while Jin Taekyung wore black. The stark contrast between them was obvious at a glance, yet it was astonishing that they were around the same age.

[P124]
*That Cheongpung fellow is a monster.*

[P125]
He had an average build and a gentle appearance. Spend half a day on the streets of Taiyuan, and one could probably find three or four young men his age who looked much like him.

[P126]
But that ordinary-looking young man concealed an identity no one could easily have guessed.

[P127]
*The heir to everything Sword Saint Mae Jonghak possessed.*

[P128]
*Whoosh! Swish!*

[P129]
Beneath the high sun, Jin Taekyung’s spearhead flashed.

[P130]
The forms were heavy and concise, but once power and speed were added, they transformed into an extremely fast spear technique that made Hyuk Mujin dizzy just watching it.

[P131]
*What if that spear were aimed at me?*

[P132]
Hyuk Mujin shook his head from side to side.

[P133]
It was embarrassing, but he wasn’t confident he could last even a quarter of an hour. No, perhaps even that thought was merely a consolation meant to preserve his pride.

[P134]
But Cheongpung was different.

[P135]
*Swish, swish-swish-swish!*

[P136]
The spearhead surged in from every direction, only to slice uselessly through empty air. Cheongpung’s face remained calm as he effortlessly dodged every attack.

[P137]
Then his hand blurred, and a streak of light split the air.

[P138]
*Whoosh! Boom!*

[P139]
“Hng!”

[P140]
Jin Taekyung let out a groan amid the thunderous impact. He had barely blocked the sword, but sword strikes poured toward him like a torrential downpour.

[P141]
Watching the scene, Hyuk Mujin opened his mouth without realizing it.

[P142]
At that moment, a single thought filled his mind.

[P143]
*Graceful.*

[P144]
That was the only way to describe it.

[P145]
Cheongpung’s movements were delicate and fluid, like the brushstrokes of a master painter. They resembled flower petals drifting and fluttering down at the end of the season.

[P146]
Hyuk Mujin watched in a daze before suddenly muttering, “Plum Blossom Sword Technique…”

[P147]
He had never seen Huashan’s martial arts before.

[P148]
But he could be certain of one thing. The very essence of Huashan martial arts had seeped into every one of Cheongpung’s movements.

[P149]
*He’s a monster. A monster in every sense of the word.*

[P150]
But “monster” was not a word that applied only to Cheongpung.

[P151]
*Swish-swish-swish-swish!*

[P152]
*Ka-ga-gang!*

[P153]
Another man was blocking every strike of the Plum Blossom Sword Technique unleashed by the Sword Saint’s disciple.

[P154]
The young man with a powerful build and striking, ruggedly handsome features ground his teeth.

[P155]
“Fuck, Huashan really made its martial arts a goddamn nightmare!”

[P156]
If Huashan had heard the thick profanity Jin Taekyung spat out, the entire sect would have turned upside down.

[P157]
A rough aura poured from his body.

[P158]
Its domineering force momentarily suppressed Cheongpung’s fluid grace before flowing straight into a counterattack.

[P159]
*Whoooosh! Boom!*

[P160]
A ferocious strike.

[P161]
Cheongpung went flying after blocking the spear amid the thunderous impact. Jin Taekyung had knocked aside Cheongpung’s offensive with a single move, but he immediately frowned.

[P162]
“Ow, that stings.”

[P163]
*Slice.*

[P164]
Before his words had even ended, the black martial robes he wore split open in a long tear.

[P165]
Several long wounds scored his exposed chest, blood welling freely from them.

[P166]
“What martial art was that?”

[P167]
“The Heavenly Eagle Claw.”

[P168]
“You really do have everything.”

[P169]
“Would you like me to teach you?”

[P170]
“You’re allowed to?”

[P171]
“Oh, I just remembered. My grandfather told me not to teach it to outsiders.”

[P172]
“Again? I knew it.”

[P173]
“Would you like to join Huashan?”

[P174]
“No!”

[P175]
Jin Taekyung shouted and kicked off the ground, charging forward.

[P176]
His movements were instinctive, like those of a wild beast, yet they barely retained the form of martial arts. Hyuk Mujin shuddered.

[P177]
*Why does that man get scarier the longer I watch him?*

[P178]
Everyone had their own distinctive aura.

[P179]
Jin Taekyung’s was tenacious and fierce. There was something about it that struck fear into anyone watching him.

[P180]
*It isn’t about his martial arts.*

[P181]
Jin Taekyung was certainly a highly skilled master, but he was not yet the equal of Cheongpung, the Sword Saint’s disciple and a true Peak master.

[P182]
Yet Hyuk Mujin had watched him from close by for the past several months, and he could say this with certainty.

[P183]
*Even if the sky fell, that man would survive.*

[P184]
No matter what kind of hell Jin Taekyung was thrown into, Hyuk Mujin felt certain he would return alive.

[P185]
Three Peak masters had tried to kill him so far, but in the end, they had been the ones to fall. In Murim, the one who survived was the strong one.

[P186]
And Jin Taekyung had survived to the bitter end.

[P187]
Besides…

[P188]
*Captain’s rate of growth is beyond imagination.*

[P189]
It was something Hyuk Mujin knew because he had watched him from closer than anyone else.

[P190]
From the moment Jin Taekyung defeated Jopil, One Question, One Kill, after a desperate battle to this very moment as he fought Cheongpung—

[P191]
Jin Taekyung was growing stronger every day.

[P192]
*And that’s still true right now.*

[P193]
Just a few days ago, he hadn’t been able to last even a hundred moves against the supreme techniques of Huashan that Cheongpung unleashed.

[P194]
But now?

[P195]
Hyuk Mujin had personally watched them exchange well over three hundred moves. Even after being struck by the Heavenly Eagle Claw, a martial art taught only to disciples of Huashan’s main sect, Jin Taekyung’s sole reaction had been, “Ow, that stings.”

[P196]
*He’s a monster. A monster.*

[P197]
Everyone around them was around the same age, and they were all Peak or advanced First Rate. Wasn’t that taking things too far? It seemed as though nothing but monsters surrounded him.

[P198]
Hyuk Mujin let out a deep sigh and recalled what Jin Taekyung had told him a few days earlier during their Wall Lizard Technique training.

[P199]
*If you don’t want to lose something precious, then risk your life and do it now. Working yourself to death while you’re still breathing is better than dying, isn’t it?*

[P200]
Those words were true.

[P201]
You had to work yourself to death to survive and become strong. Every second counted if you wanted to avoid being swept away by the waves of Murim.

[P202]
After silently watching the two men spar for a while, Hyuk Mujin rose to his feet.

[P203]
*I can’t finish this with just my little toe.*

[P204]
He had to become stronger. Strong enough to be recognized as Jin Taekyung’s right arm—or perhaps his heart.

[P205]
And…

[P206]
*Strong enough for everyone to remember the name Hyuk Mujin.*

[P207]
He gripped his sword case tightly.
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
# Chapter 157

[P2]
Since ancient times, people had said that the masters of famous mountains were spirit creatures. Huashan, one of the Central Plains’ Five Great Mountains, was no exception.

[P3]
Before human feet ever touched it, tigers had ruled over its lofty, sprawling forests.

[P4]
These spirit creatures possessed the majesty of kings and the ferocity of beasts. When their territory was invaded, they grew furious and soon began attacking the unwelcome trespassers who had entered without permission.

[P5]
“Wow, and then?”

[P6]
“When the loss of human life became severe, the Huashan Sect had no choice but to step in. That was how the Crouching Tiger Fist was born.”

[P7]
*A fist technique that subdues tigers. The Crouching Tiger Fist.*

[P8]
Cheongpung remembered clearly what his grandfather had told him when he learned the Crouching Tiger Fist long ago.

[P9]
“Pung, the Crouching Tiger Fist is a powerful martial art capable of subduing the king of the mountains. If you master this one technique, no one your age will be able to stand against you. Do you understand?”

[P10]
“Yes!”

[P11]
As a child, Cheongpung had believed his grandfather’s words without question.

[P12]
But now, ten years later—

[P13]
*Whack!*

[P14]
“Ow, that hurt.”

[P15]
“…Huh?”

[P16]
For the first time, he realized that even his grandfather could be wrong.

[P17]
* * *

[P18]
It was the third day since I had begun sparring with Cheongpung. During my forty-fifth duel, I witnessed him stumble over his words for the first time.

[P19]
“B-Benefactor, are you all right?”

[P20]
“I know. That was the Crouching Tiger Fist, right?”

[P21]
I had watched it with my own eyes, and I had even experienced it firsthand by getting hit.

[P22]
Getting knocked out after taking the Crouching Tiger Fist to the solar plexus had happened yesterday.

[P23]
I had committed the way Cheongpung moved when he used the Crouching Tiger Fist to memory—the footwork he used, the position of his shoulders, and even the sequence of forms that followed.

[P24]
And yet I had still allowed myself to be hit.

[P25]
There was no doubt about it. Cheongpung was one step ahead of me.

[P26]
“What was the name of that form just now?”

[P27]
At my question, Cheongpung answered with a dazed expression.

[P28]
“One Fist Subdues the Tiger.”

[P29]
A single fist that knocked down a tiger? It certainly possessed enough destructive power to justify the name. If I hadn’t been getting so much better at taking hits with every duel, I would have dropped to my knees just like yesterday.

[P30]
*Should I take comfort in the fact that I’m doing much better than yesterday?*

[P31]
My ability to take a hit wasn’t the only thing that had improved. By experiencing Cheongpung’s martial arts with my own body, I was gradually getting used to them.

[P32]
“All right, let’s go again.”

[P33]
But Cheongpung didn’t seem to have any intention of doing that.

[P34]
“How did you dodge it?”

[P35]
“Huh?”

[P36]
“I was aiming precisely around your Fengwei acupoint…”

[P37]
The Fengwei acupoint was located around the ribs. I had twisted my body in an attempt to dodge, only to take the blow squarely in the middle of my abdomen.

[P38]
Since I had avoided his intended target, could this technically count as dodging? I shrugged.

[P39]
“I just struggled to avoid getting hit even once. I got hit in the end, though.”

[P40]
“Did you see the sequence of forms?”

[P41]
After being beaten up for several days, I could make out the forms vaguely. Where and how an attack would come from. How the next form would follow.

[P42]
*The problem is that I’m still clumsy at it.*

[P43]
I rubbed my aching abdomen and answered.

[P44]
“After taking this many hits, I should be able to read at least that much. Every time you hit me, I kept my eyes wide open and watched.”

[P45]
Wasn’t keeping your eyes open even while getting hit and figuring out your opponent’s sequence of forms the most basic thing?

[P46]
“Hmm, that’s strange. I’ve only used the Crouching Tiger Fist a few times.”

[P47]
“That’s why it took me a little longer to figure out than the others.”

[P48]
“The others?”

[P49]
“Yes. The Plum Blossom Fist was pretty easy. Maybe because you used it the most during our duels, but I could more or less figure it out.”

[P50]
Cheongpung clapped with an exclamation of admiration.

[P51]
“Wow, can you show me?”

[P52]
“It’s nothing difficult.”

[P53]
I performed a poor imitation of the Plum Blossom Fist. My footwork and movements were both terribly awkward, but every form came from the Plum Blossom Fist Cheongpung had used in our duels.

[P54]
*This much is easy.*

[P55]
At some point after I began learning martial arts, I realized something.

[P56]
A technique required an understanding of martial arts and the internal-energy control to match it. But copying the form itself was easy.

[P57]
*I moved like this here, didn’t I? Probably?*

[P58]
From the first form to the seventh. I occasionally stumbled, but I managed to perform them as naturally as possible without much difficulty. Then I turned my head.

[P59]
“That’s about it for now… Young Hero Cheongpung?”

[P60]
“Ah, yes, Benefactor.”

[P61]
“Is something wrong? Why do you look like that?”

[P62]
“No, it’s just…”

[P63]
Cheongpung stared at me with an oddly complicated expression before hesitantly opening his mouth.

[P64]
“I suddenly remembered something my grandfather once said.”

[P65]
“The Sword Saint old man—I mean, your grandfather?”

[P66]
“Yes. He used to call me a thief.”

[P67]
“It’s all right. When I was young, I secretly took a thousand won from my mother’s wallet and got beaten half to death.”

[P68]
“That’s not what I mean…”

[P69]
Cheongpung let out a deep sigh.

[P70]
“He always said that while teaching me martial arts. He called me a thief who stole martial arts.”

[P71]
“Oh.”

[P72]
That was a compliment, right? To think a talent freak like Cheongpung was praising me.

[P73]
As I stood there dumbfounded, Cheongpung said,

[P74]
“Benefactor, you’re definitely a genius of martial arts.”

[P75]
“A genius? Me?”

[P76]
“Yes.”

[P77]
*A genius, my ass…*

[P78]
No, wait. He was right.

[P79]
When I thought about it, I had mastered the Jin Family’s Manoeuvre Technique and spear technique—both First Rate martial arts—in barely two or three months.

[P80]
Of course, the System had carried me through all of it.

[P81]
“It’s just a shortcut. I’m pretty good at using my body, that’s all. My eyes are good, too. Heh heh.”

[P82]
“My grandfather used to say that martial arts are seventy percent eyes and thirty percent feet.”

[P83]
“I think he was right about that, but either way, I’m not a genius.”

[P84]
“Think about it carefully. I’m sure something similar happened before.”

[P85]
Was that true?

[P86]
I suddenly remembered my childhood. I had always been good at sports because of my natural athletic ability, but martial arts specifically…

[P87]
*Oh. There was one.*

[P88]
When my expression changed, Cheongpung nodded as though to say he had been right.

[P89]
“See? Something like that happened, didn’t it?”

[P90]
“There was one. Taekwondo.”

[P91]
“Taekwondo?”

[P92]
“It’s something like a martial art.”

[P93]
Back in elementary school, I had been tricked into enrolling at a taekwondo academy by the promise of receiving a portable game console.

[P94]
The older high school students had put on a taekwondo demonstration, and after watching it exactly twice, I could follow all eight Taegeuk forms.[^1]

[P95]
[^1]: Taegeuk forms are a standardized sequence of eight color-belt patterns in taekwondo.

[P96]
Of course, I beat up a middle-school student two years older than me and got kicked out less than a week later.

[P97]
*Could that have been it?*

[P98]
Come to think of it, even back when I had been an F-rank Hunter, I had been pretty good at copying almost anything.

[P99]
My poor physical abilities had simply held me back.

[P100]
If someone at the bottom of the Hunter ranks tried to imitate the movements of a mid-rank Hunter, he wouldn’t be able to generate any destructive power. He would only end up tearing his groin apart.

[P101]
*But things are different now.*

[P102]
Overflowing internal energy. Excellent physical abilities. And martial arts learned in Murim.

[P103]
Now that I thought about it, I might not be a genius of martial arts, but I did seem to have a fair amount of talent.

[P104]
“How long did it take you to learn the Plum Blossom Fist, Young Hero Cheongpung?”

[P105]
“One month.”

[P106]
“One month?”

[P107]
From my own experience, the Plum Blossom Fist was a Huashan martial art, but it wasn’t complicated enough to take that long.

[P108]
And this guy had taken a month to learn it, while I had managed to roughly copy it after three days?

[P109]
*That’s insane.*

[P110]
As I grinned so broadly that the corners of my mouth nearly split, Cheongpung added,

[P111]
“It took me a whole month to achieve Great Attainment, so my grandfather scolded me terribly.”

[P112]
“…”

[P113]
Right. Of course.

[P114]
As I stared at him in disbelief, Cheongpung muttered,

[P115]
“Still… it doesn’t feel very good. Having someone copy my martial arts.”

[P116]
A dangerous aura rose from him.

[P117]
* * *

[P118]
After regaining consciousness, Hyuk Mujin stared blankly at the training ground.

[P119]
*This is incredible.*

[P120]
The training ground had already been half reduced to rubble.

[P121]
More than half of the bluestone carefully laid by stonemasons famous throughout Shanxi Province had been smashed apart, and the destruction was continuing at a rapid pace.

[P122]
*Clang! Ka-ka-ka-clang!*

[P123]
Despite the season, the center of the training ground was scorching hot. Spear and sword clashed amid bursts of flame.

[P124]
The owners of the weapons moved at dazzling speed, exchanging blows so quickly that even Hyuk Mujin, a First Rate master, struggled to follow them.

[P125]
*How can they be that fast?*

[P126]
Cheongpung wore white martial robes, while Jin Taekyung wore black. The two young men were starkly different at a glance, yet the fact that they were around the same age was simply astonishing.

[P127]
*That Cheongpung fellow is a monster.*

[P128]
He had an ordinary build and a gentle appearance. If he spent half a day walking around Taiyuan, he would probably encounter three or four young men his age who looked much like him.

[P129]
But that ordinary-looking young man concealed an identity no one could easily have guessed.

[P130]
*The heir who inherited everything from the Sword Saint Mae Jonghak.*

[P131]
*Whoosh! Whoosh!*

[P132]
Beneath the high-riding sun, Jin Taekyung’s spearhead flashed.

[P133]
His forms were heavy and concise, but with power and speed added to them, they transformed into an extremely fast spear technique that made Hyuk Mujin dizzy just watching it.

[P134]
*What if that spear were aimed at me?*

[P135]
Hyuk Mujin shook his head from side to side.

[P136]
It was embarrassing, but he had no confidence that he could last even a full quarter hour. No, perhaps even that thought was nothing more than consolation meant to preserve his pride.

[P137]
But Cheongpung was different.

[P138]
*Swish, swish-swish-swish!*

[P139]
The spearhead came at him from every direction, only to slice uselessly through empty air. Cheongpung’s face remained calm as he effortlessly dodged every attack.

[P140]
Then his hand blurred.

[P141]
A streak of light split the air.

[P142]
*Whoosh! Boom!*

[P143]
“Hng!”

[P144]
Jin Taekyung let out a groan amid the thunderous impact. He had barely blocked the sword, but sword strikes poured toward him like a torrential downpour.

[P145]
Hyuk Mujin watched the scene with his mouth falling open.

[P146]
At that moment, one thought filled his mind.

[P147]
*Graceful.*

[P148]
That was the only way to describe it.

[P149]
Cheongpung’s movements were delicate and fluid, like the brushstrokes of a master painter. They resembled flower petals drifting and fluttering down at the end of the season.

[P150]
Hyuk Mujin watched in a daze before suddenly muttering,

[P151]
“Plum Blossom Sword Technique…”

[P152]
He had never seen Huashan martial arts before.

[P153]
But he could be certain of one thing. The very essence of Huashan martial arts had seeped into every one of Cheongpung’s movements.

[P154]
*He’s a monster. He really is a monster.*

[P155]
But “monster” was not a word that applied only to Cheongpung.

[P156]
*Swish-swish-swish-swish!*

[P157]
*Ka-ga-gang!*

[P158]
Another man was blocking every strike of the Plum Blossom Sword Technique unleashed by the Sword Saint’s disciple.

[P159]
The young man with a powerful build and striking, ruggedly handsome features ground his teeth.

[P160]
“Fuck, Huashan made its martial arts a fucking nightmare!”

[P161]
If Huashan had heard the thick profanity Jin Taekyung spat out, the entire sect would have turned upside down.

[P162]
A rough aura poured from his body.

[P163]
The domineering force of it momentarily suppressed Cheongpung’s graceful movements, and then flowed straight into a counterattack.

[P164]
*Whoooosh! Boom!*

[P165]
A powerful strike.

[P166]
Cheongpung’s body flew through the air after blocking the spear amid the thunderous impact. Jin Taekyung had knocked aside Cheongpung’s offensive with a single move, but he immediately frowned.

[P167]
“Ow, that stings.”

[P168]
*Slice.*

[P169]
Before his words had even ended, the black martial robes he wore split open in a long tear.

[P170]
Several long wounds scored his exposed chest, blood welling freely from them.

[P171]
“What martial art was that?”

[P172]
“The Heavenly Eagle Claw.”

[P173]
“You really have everything.”

[P174]
“Would you like me to teach you?”

[P175]
“You’re allowed to teach me?”

[P176]
“Oh, I just remembered. My grandfather told me not to teach it to outsiders.”

[P177]
“Again? I knew you’d say that.”

[P178]
“Would you like to join Huashan?”

[P179]
“No!”

[P180]
Jin Taekyung shouted and kicked off the ground, charging forward.

[P181]
His movements were instinctive, like those of a wild beast, yet they barely retained the form of martial arts. Hyuk Mujin shuddered.

[P182]
*Why does that man get scarier the longer I watch him?*

[P183]
Every person possessed something called an aura.

[P184]
Jin Taekyung’s aura was tenacious and fierce. There was something about it that made anyone watching him feel afraid.

[P185]
*It isn’t about his martial arts.*

[P186]
Jin Taekyung was certainly a highly skilled master, but he was not yet the equal of Cheongpung, the Sword Saint’s disciple and a true Peak master.

[P187]
Yet Hyuk Mujin had watched him from close by for the past several months, and he could say this with certainty.

[P188]
*Even if the sky fell, that man would survive.*

[P189]
Hyuk Mujin was certain Jin Taekyung would somehow return alive no matter what kind of hell he was thrown into.

[P190]
Three Peak masters had tried to kill him so far, but in the end, they had been the ones to fall. In Murim, the one who survived was the strong one.

[P191]
And Jin Taekyung had survived to the bitter end.

[P192]
Besides…

[P193]
*Captain’s growth is beyond imagination.*

[P194]
It was something Hyuk Mujin knew because he had watched him from closer than anyone else.

[P195]
From the moment Jin Taekyung had defeated Jopil, One Question, One Kill, after a desperate battle to the present, when he was fighting Cheongpung.

[P196]
Jin Taekyung was growing stronger every day.

[P197]
*And that’s true even now.*

[P198]
Just a few days ago, he hadn’t been able to last even a hundred moves against the supreme techniques of Huashan that Cheongpung unleashed.

[P199]
But now?

[P200]
Hyuk Mujin alone had watched the exchange go well beyond three hundred moves. Even after being struck by the Heavenly Eagle Claw, a martial art that could be learned only by disciples of Huashan’s main sect, all Jin Taekyung said was, “Ow, that stings.”

[P201]
*He’s a monster. A monster.*

[P202]
Everyone around them was around the same age, and they were all Peak or advanced First Rate. Wasn’t that taking things too far? It seemed as though nothing but monsters surrounded him.

[P203]
With a deep sigh, Hyuk Mujin remembered what Jin Taekyung had said a few days earlier while training the Wall Lizard Technique.

[P204]
*If you don’t want to lose something precious, then risk your life and do it now. Working yourself to death while you’re still breathing is better than dying, isn’t it?*

[P205]
Those words were true.

[P206]
You had to work yourself to death to survive and become strong. Every moment was precious if you wanted to avoid being swept away by the waves of Murim.

[P207]
Hyuk Mujin watched the two men spar for a while longer, then got to his feet.

[P208]
*I can’t finish this with just my little toe.*

[P209]
He had to become stronger. Strong enough to be acknowledged as Jin Taekyung’s right arm—or perhaps his heart.

[P210]
And…

[P211]
*Strong enough for everyone to remember the name Hyuk Mujin.*

[P212]
He gripped his sword case tightly.
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 조필     | **Jopil**          |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 화산파    | **Huashan**                      |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 검법     | **sword technique**                              |                                                       |
| 권법     | **fist technique**                               |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 소협      | **Young Hero**                                                  |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 진무보법 | **Jin Family's Manoeuvre Technique** | Named Jin Family footwork technique mastered by Taekyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 매화검법 | **Plum Blossom Sword Technique** | Huashan sword technique Cheongpung performed at age ten. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 천응 | **Heavenly Eagle** | Huge bird regarded as a spirit creature, said to have a wingspan exceeding one jang. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 복호권 | **Crouching Tiger Fist** | Huashan martial art Cheongpung uses during the spar. |
| 일권복호 | **One Fist Subdues the Tiger** | Named form of the Crouching Tiger Fist. |
| 매화권 | **Plum Blossom Fist** | Huashan fist technique Cheongpung uses in sparring. |
| 천응조 | **Heavenly Eagle Claw** | Huashan claw technique used by Cheongpung. |
| 봉미혈 | **Fengwei acupoint** | Acupoint around the ribs targeted by Cheongpung. |
| 태권도 | **Taekwondo** | Martial art Taekyung practiced as a child. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 157,
  "passed": true,
  "metrics": {
    "source_characters": 6457,
    "translation_characters": 15360,
    "length_ratio": 2.379,
    "source_paragraphs": 203,
    "translation_paragraphs": 207
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "경지",
        "preferred": "realm / realm stage"
      }
    },
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
        "korean": "진태",
        "preferred": "Jintae"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진무보법",
        "preferred": "Jin Family's Manoeuvre Technique"
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
        "korean": "세가",
        "preferred": "great family"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "태극",
        "romanization": "taegeuk"
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
