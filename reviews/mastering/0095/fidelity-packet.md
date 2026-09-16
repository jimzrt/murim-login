# Fidelity Gate — Chapter 95

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
  1|＃95화
  2|
  3|
  4|
  5|‘후후후. 성공이다.’
  6|
  7|홍우진은 득의양양하게 웃었다. 그는 표적 대상의 일거수일투족을 감시하며 모든 정보를 읽어 내는 베테랑이다.
  8|
  9|진태경의 여동생이 동물, 그중에서도 특히 고양이에 환장한다는 정보는 특히 유용했다.
 10|
 11|“야옹아, 대답해 봐. 집 들어오니까 좋지?”
 12|
 13|침투는 자연스러웠고, 성공적이었다. 새끼 고양이의 몸 안에 들어간 홍우진이 기쁨의 포효를 내질렀다.
 14|
 15|미야오옹.
 16|
 17|“꺄, 귀여워! 오빠, 방금 들었어? 들었어?”
 18|
 19|“응. 들었다.”
 20|
 21|“이런 귀여운 생물체를 두고 어떻게 그렇게 무심할 수가 있어? 사람이야?”
 22|
 23|“그럼 내가 짐승이냐?”
 24|
 25|문제는 진태경, 저놈이다.
 26|
 27|아무리 감정이 메마른 사람이라고 해도 귀여운 동물, 특히 조그마한 새끼 앞에서는 마음이 말랑말랑해지기 마련인데…….
 28|
 29|“옆으로 좀 비켜 봐. TV 화면 가리고 있잖아.”
 30|
 31|이놈은 그딴 거 없다. 사하라 사막보다 건조한 감수성에 여동생, 진하연이 구시렁거렸다.
 32|
 33|“어휴, 사람이 삭막해도 정도가 있지. 안 그래, 여름아?”
 34|
 35|“여름이?”
 36|
 37|“응. 여름에 태어났으니까 한여름. 이름 예쁘지?”
 38|
 39|“한여름은 무슨. 덩치 보니까 3개월은 되어 보이는데 늦봄에 태어났으니까 늦봄이라고 하든가.”
 40|
 41|“……그게 말이야, 방구야? 아무튼 얘 이름은 오늘부터 여름이야. 그치, 여름아?”
 42|
 43|야오옹.
 44|
 45|홍우진 입장에서는 진하연이 일등 공신이다. 덕분에 일이 술술 풀리고 있었다.
 46|
 47|“꺄악! 대답했어! 여름이 방금 언니한테 대답한 거 맞죠? 그렇죠?”
 48|
 49|미야옹.
 50|
 51|“으헉, 내 심장!”
 52|
 53|후후, 다루기 쉬운 녀석 같으니라고. 몇 번 울어 주기만 해도 아주 자지러진다.
 54|
 55|‘이래서 여고생들이란…… 아니지, 내 패밀리어 선택이 탁월했던 거지.’
 56|
 57|홍우진이 흐뭇하게 웃고 있던 그때.
 58|
 59|멀뚱히 TV만 보고 있던 진태경이 한마디를 툭 던졌다.
 60|
 61|“걔 수컷 아냐?”
 62|
 63|“응? 그거야…….”
 64|
 65|“아직 모르지?”
 66|
 67|“그러고 보니 확인을 안 했어.”
 68|
 69|“까 봐. 확인해 보자.”
 70|
 71|어라?
 72|
 73|일이 요상하게 돌아간다. 비록 몸은 고양이지만 홍우진은 혈기왕성한 청년. 진태경의 커다란 손이 다가오자 문득 수치심이 몰려왔다.
 74|
 75|‘더러운 사내놈이 내 거기를 본다고?’
 76|
 77|정확히 말하자면 홍우진의 몸은 아니다. 종(種)이 다른 만큼 신체 구조도 다르다.
 78|
 79|그러나 패밀리어 마법은 시전자와 패밀리어가 모든 것을 공유한다. 그렇다 보니 기분이 더러워지는 건 어쩔 수 없었다.
 80|
 81|‘절대 안 돼!’
 82|
 83|홍우진은 황급히 진하연의 품속으로 파고들었다.
 84|
 85|야오오옹.
 86|
 87|“어머, 얘가 싫어하는 거 같은데?”
 88|
 89|“원래 세상이 그래. 하고 싶은 거만 하면서 사는 사람이 어디 있어?”
 90|
 91|“여름이는 고양이잖아.”
 92|
 93|“고양이도 마찬가지야. 뜨신 사료에 간식으로 통조림 하나라도 얻어먹으려면 이 정도는 감수해야지.”
 94|
 95|저런 미친놈. 고양이 성별 한번 확인해 보겠다고 말도 안 되는 소리를 지껄이네. 홍우진은 이를 갈며 유일한 희망인 진하연에게 매달렸다.
 96|
 97|그녀의 팔에 온몸을 비비며 애처로운 눈빛을 발사하자 진하연의 눈동자가 스르륵 풀린다.
 98|
 99|“어떡해. 귀여워서 미칠 것 같아.”
100|
101|“그래, 귀여우니까 한번 까 보자.”
102|
103|“다음에 해. 애가 무서워하잖아.”
104|
105|“기분 탓이야.”
106|
107|“여름이가 오빠 싫어하는 것 같다니까.”
108|
109|타이밍에 맞춰 신음 한번 흘려 주는 게 포인트다.
110|
111|끼양. 끼으응.
112|
113|“봐 봐. 맞지?”
114|
115|“……그럼 어쩔 수 없지.”
116|
117|“괜히 애 억지로 만지고 그랬단 봐라. 새끼 고양이들은 예민해서 신경 써 줘야 한단 말이야.”
118|
119|됐다. 당장 위기는 넘겼다. 진태경 이 녀석, 세상 혼자 사는 또라이 같아도 가족에게는 약한 놈이었다.
120|
121|이미 상동 길드 측에서 건네준 사전 정보를 모두 숙지한 홍우진은 자신이 한 수 앞을 내다보고 있다고 생각했다.
122|
123|‘이래서 정보가 중요하지. 넌 나한테 이미 걸려들었어.’
124|
125|그러나 홍우진이 차마 몰랐던 사실이 있었다.
126|
127|“동생아.”
128|
129|“응?”
130|
131|“용돈 더 안 필요하니?”
132|
133|“……지금 나를 돈으로 매수해서 우리 여름이를 막, 농락하겠다 이거야?”
134|
135|“어. 10만 원.”
136|
137|“콜. 그 대신 너무 싫어하지 않게 살살 해야 돼?”
138|
139|“내 방 책상에 지갑 있으니까 가져가.”
140|
141|“꺅!”
142|
143|미야옹?
144|
145|총알처럼 사라지는 진하연의 뒷모습에 홍우진은 어이없는 마음을 담아 울음을 토해 냈다.
146|
147|귀여워서 미칠 것 같다며? 우리 여름이라며?
148|
149|‘저런 되바라진 것을 봤나.’
150|
151|언제는 간이고 쓸개고 다 빼 줄 것처럼 굴더니 고작 10만 원에 우리 여름이를 버려?
152|
153|그러나 자본주의 사회의 현실에 한탄하고 있을 틈 따위는 더 이상 주어지지 않았다.
154|
155|“자, 이제 나랑 놀자.”
156|
157|덥석.
158|
159|번개 같은 속도로 사지를 결박한 진태경의 징글맞은 웃음.
160|
161|홍우진은 절박한 심정으로 비명을 내질렀다.
162|
163|‘놔! 놔, 이 새끼야!’
164|
165|하악! 하아아악!
166|
167|털을 바짝 세운 하악질 소리에 진태경의 지갑을 뒤지던 유일한 희망이 반응했다.
168|
169|“오빠!”
170|
171|“어, 10만 원 더 빼 가라.”
172|
173|“고마워!”
174|
175|야, 야!
176|
177|유일한 희망이 자본주의의 노예로 타락했다!
178|
179|충격이 채 가시기도 전에 진태경의 뜨거운 숨결이 훅 밀려왔다.
180|
181|“우리 여름이, 고추 좀 볼까?”
182|
183|절체절명의 순간.
184|
185|‘링크(Link) 해제!’
186|
187|미야오오옹!
188|
189|구슬픈 울음소리와 함께 새끼 고양이의 몸에서 힘이 쭉 빠져나갔다.
190|
191|그리고 어두컴컴한 어딘가에서 눈을 뜬 홍우진이 숨을 토해 냈다.
192|
193|“푸하악!”
194|
195|헌터 일을 시작하고 크고 작은 백여 건의 의뢰를 처리했지만 지금처럼 생명의 위협을 느낀 적은 처음이다.
196|
197|소름이 오소소 돋은 팔뚝을 내려다본 그가 헛구역질을 시작했다.
198|
199|“우욱.”
200|
201|속이 울렁거리고 머리가 지끈지끈했다.
202|
203|갑작스러운 링크 해제의 부작용이다. 미리 준비해 놓은 포션을 냉수처럼 들이켜고 나서야 홍우진은 한숨 돌릴 수 있었다.
204|
205|“진태경, 이 개새끼 진짜…….”
206|
207|처음으로 의뢰를 받은 게 후회되는 순간이었다.
208|
209|
210|
211|* * *
212|
213|
214|
215|[Lv.2 고양이]
216|
217|
218|
219|“갔네, 갔어.”
220|
221|나는 혀를 쯧쯧 차며 새끼 고양이를 놔주었다. 3개월이나 됐을까. 손바닥 두 개를 합친 것보다 작은 녀석이 어리둥절한 얼굴로 뒷걸음질 쳤다.
222|
223|미야옹.
224|
225|내 방을 나오던 하연이가 그 광경을 발견했다.
226|
227|“우리 여름이한테 못된 짓 한 거 아니지?”
228|
229|“그 여름이를 20만 원에 팔아넘긴 게 너고?”
230|
231|“……흠. 흠.”
232|
233|“됐다. 어휴, 주워 와도 꼭 저런 걸 주워 와서.”
234|
235|“뭐래, 얘가 얼마나 귀여운데.”
236|
237|“그게 아니라…… 아니다. 말을 말자.”
238|
239|일일이 설명하기에는 길고 복잡한 얘기다. 설명해 줄 생각도 없고.
240|
241|어떤 음흉한 놈이 고양이 몸 안에 들어가 우리를 관찰하고 있다고 말해 봐라. 얼마나 불안해할지 안 봐도 뻔한데. 지금 벌어지고 있는 일들을 가족들이 알아서는 안 된다.
242|
243|‘어차피 나도 허락한 일이고.’
244|
245|패밀리어를 집에 들인 이유는 하연이가 부탁해서, 엄마가 허락해서가 아니다.
246|
247|‘내가 원해서지.’
248|
249|누구의 의뢰인지는 몰라도 놈들은 당장 쫓아낸다 해도 계속해서 시도할 것이다.
250|
251|패밀리어의 형태가 지난번처럼 벌레든, 오늘처럼 고양이든 그건 상관없다.
252|
253|내가 패밀리어의 정체를 이미 알고 있으며, 언제든지 쳐 낼 수 있다는 사실이 중요하다.
254|
255|‘분명 이 근방이야.’
256|
257|집으로부터 최대 500m. 그 안에 패밀리어를 조종하는 마법사가 있다. 그놈을 털면 분명히 연결 고리가 나올 거다.
258|
259|‘일단 아구창에 주먹 한 대 꽂고 물어봐야지.’
260|
261|어차피 불법으로 민간인 사찰을 한 놈이니 때려도 신고 못 할 게 뻔하다. 제대로 손봐 줄 생각에 벌써 주먹이 근질거렸다.
262|
263|‘감히 누구 집에서 깔짝대?’
264|
265|오랜만의 휴가까지 방해받고 심지어 이 자식들 덕분에 쓴 돈도 3억이 훌쩍 넘어간다. 여러모로 손해 보는 장사가 아닐 수 없다.
266|
267|잔뜩 구겨진 얼굴로 TV를 보고 있는데, 하연이가 슬금슬금 눈치를 살피며 입을 열었다.
268|
269|“오빠, 화났어?”
270|
271|“아니. 화날 게 뭐가 있어.”
272|
273|“내가 미안해.”
274|
275|“……왜 이러냐? 무서워지려고 하네.”
276|
277|농담이 아니라 진짜다. 패밀리어를 처음 발견했을 때보다 더 놀랐다. 얘가 이런 말도 할 줄 알았나?
278|
279|나는 진지하게 물었다.
280|
281|“어디 아파?”
282|
283|“아니 뭐, 그냥.”
284|
285|“그럼 배고파?”
286|
287|“그게 아니고…….”
288|
289|뭔가 말하려던 하연이가 멈칫한 순간, 어디선가 꼬르륵 소리가 들려왔다.
290|
291|나는 아니고. 엄마는 잠깐 볼일 보러 나가셨고.
292|
293|“너 배고프지.”
294|
295|“음, 살짝?”
296|
297|“그래, 배고파서 헛소리까지 나오는구나. 내 지갑 어디 있는지 알지? 너 먹고 싶은 거 다 시켜.”
298|
299|“진짜?”
300|
301|“응. 10만 원 한도 내에서.”
302|
303|“와, 돈 벌더니 통 커졌네. 우리 오빠.”
304|
305|살다 살다 우리 오빠 소리도 들어 보는구나. 하연이가 중학생일 때 이후로 처음 듣는 말이라 소름이 돋았다.
306|
307|“너 패밀리어지, 이 새끼야!”
308|
309|“무슨 헛소리야. 암튼 그럼 10만 원 선에서 막 시킨다?”
310|
311|“어, 아니네. 그래. 다 시켜.”
312|
313|“남은 돈은?”
314|
315|“……너 나한테 돈 맡겨 놨니?”
316|
317|“다다익선.”
318|
319|당당한 하연이의 모습에 기가 찼지만 한편으로는 기뻤다.
320|
321|지금까지 용돈 달라는 소리 한번 없던 녀석이다. 입고 다니는 옷이나 평소 상태만 봐도 길거리에서 종종 마주치는 또래 애들에 비하면 한참 수수했다.
322|
323|‘애늙은이 같은 녀석.’
324|
325|생각해 보면 하연이는 어릴 때부터 그랬다. 쉽게 울지도 않았고 솔직하게 감정을 표현하는 일도 적었다. 지금 같은 성격이 된 것은 오히려 고등학교에 입학한 이후다.
326|
327|가끔은 어리광을 피워도 될 텐데…… 너무 일찍 철이 들었다.
328|
329|‘어쩌면 나보다도 훨씬.’
330|
331|그래서 그런가? 녀석의 행동과 말이 하나도 얄밉지 않다. 오히려 기특하고 기뻤다.
332|
333|“그래, 다 가져라, 다 가져.”
334|
335|“진짜?”
336|
337|“어.”
338|
339|내 말에 하연이가 방긋 웃었다.
340|
341|“다행이다. 괜히 미안할 뻔했네.”
342|
343|“미안할 게 뭐가 있어.”
344|
345|“아까 오빠 지갑에서 30만 원 빼 갔거든.”
346|
347|“……어?”
348|
349|“그런데 오빠가 10만 원 선에서 먹고 남은 거 다 가지라고 하니까 마음이 편해지네.”
350|
351|“잠깐만, 내가 20만 원 가져가라고 하지 않았냐?”
352|
353|“우발적 사고였어.”
354|
355|“……우발적 범죄 아니냐?
356|
357|아까 했던 말 취소.
358|
359|콧노래를 부르며 방으로 들어가는 뒷모습이 얄밉기 짝이 없다.
360|
361|
362|
363|* * *
364|
365|
366|
367|상동 길드 보안팀장은 눈살을 찌푸렸다.
368|
369|“고양이 패밀리어?”
370|
371|“네, 확실합니다.”
372|
373|단호한 목소리로 대답한 사람은 보안팀 소속이자 길드 유일의 패밀리어 마법사다. 헌터 등급은 C급에 불과하지만 희귀한 정신계 마법사라 보안팀의 핵심 멤버이기도 했다.
374|
375|“표적의 여동생이 고양이 덕후랍니다. 빈틈을 잘 노렸어요.”
376|
377|“분위기 파악 안 되냐? 지금 내 앞에서 그 새끼 칭찬이 나와?”
378|
379|“죄, 죄송합니다.”
380|
381|“1팀장님이 그러더라. 홍우진이가 전화해서 우리 때문에 바로 들킬 뻔했다고 지랄했대.”
382|
383|“…….”
384|
385|“뭐 따지고 보면 그 새끼도 우리 편이긴 하지. 근데 프리랜서한테 밀리면 되겠냐? 길드장님이 각별하게 신경 쓰고 계신 거 몰라?”
386|
387|이번 일에 투입된 인원은 그를 포함해 총 여섯. 그중 하나는 패밀리어 마법사고 나머지 넷은 추적과 은신에 특화된 근접 헌터들, 마지막으로 팀장 본인은 B급 헌터였다.
388|
389|“너희가 뭘 착각하나 본데…… 우리 C급 헌터 하나 털어 보자고 온 거 아니다.”
390|
391|보안팀장은 험악한 얼굴로 팀원들을 응시했다.
392|
393|이번 건은 길드장이 직접 지시한 일이다. 무조건 지시한 것 그 이상의 성과를 내야만 했다.
394|
395|“잘하자. 이거 길드장님 직통이야. 너희 여기서 끝날 거야? 보너스도 받고 승진도 해야지.”
396|
397|팀원들은 말없이 고개를 숙였다.
398|
399|보너스와 승진이 가장 간절한 사람이 바로 보안팀장이다. 은퇴 시기가 슬슬 다가오는 중년 가장의 히스테리는 이제 와선 하루 이틀 일이 아니었다.
400|
401|“그리고 너.”
402|
403|보안팀장이 패밀리어 마법사를 지목했다.
404|
405|“너도 고양이 해.”
406|
407|“고양이요? 그건 이미 저쪽에서 했는데.”
408|
409|“그럼? 괜히 컨트롤도 안 되는 초소형 패밀리어로 발연기 하다가 지난번처럼 뒤질래?”
410|
411|“…….”
412|
413|“시키는 대로 해. 여자애가 고양이 덕후라며?”
414|
415|까면 까야지, 별수 있나. 한바탕 성질을 부린 보안팀장이 나간 뒤 패밀리어 마법사는 곧장 스마트폰을 켜서 검색을 시작했다.
416|
417|틱. 틱. 틱.
418|
419|[일산 고양이 분양]
420|
421|“……이것도 영수증 처리해 주려나?”
```

## Assembled English

```markdown
[P1]
# Chapter 95

[P2]
*Heh heh heh. Success.*

[P3]
Hong Woojin smiled smugly. He was a veteran at monitoring his targets’ every move and extracting every bit of information from them.

[P4]
The information that Jin Taekyung’s younger sister was crazy about animals—cats in particular—had proved especially useful.

[P5]
“Meow-meow, answer me. You like being inside the house, don’t you?”

[P6]
The infiltration had been natural and successful. Inside the kitten’s body, Hong Woojin let out a roar of joy.

[P7]
“Miaowww.”

[P8]
“Ahh, so cute! Oppa, did you hear that just now? You heard it, right?”

[P9]
“Yeah. I heard it.”

[P10]
“How can you be so indifferent to such a cute little creature? Are you even human?”

[P11]
“Then what am I, a beast?”

[P12]
The problem was Jin Taekyung.

[P13]
Even the most emotionally dried-up person tended to soften in front of a cute animal, especially a tiny one, but…

[P14]
“Move over a little. You’re blocking the TV.”

[P15]
This guy had none of that. His sensitivity was drier than the Sahara Desert, and his younger sister, Jin Hayeon, grumbled.

[P16]
“Good grief, there’s a limit to how bleak a person can be. Right, Yeoreum?”

[P17]
“Yeoreum?”

[P18]
“Yeah. Born in summer, so Midsummer. Pretty, right?”

[P19]
“Midsummer, my ass. Judging by the size, the kitten looks about three months old. That means it was born in late spring, so call it Late Spring or something.”

[P20]
“…Was that a comment or a fart? Anyway, this kitten’s name is Yeoreum from today onward. Right, Yeoreum?”

[P21]
“Mrowww.”

[P22]
As far as Hong Woojin was concerned, Jin Hayeon deserved most of the credit. Thanks to her, everything was going smoothly.

[P23]
“Ahh! She answered! Yeoreum, you just answered your big sister, didn’t you? Didn’t you?”

[P24]
“Miaow.”

[P25]
“Eek, my heart!”

[P26]
*Heh. What an easy one to handle.* A few meows were all it took to make her lose her mind.

[P27]
*This is why high-school girls are… No, wait. It’s because my choice of Familiar was excellent.*

[P28]
Hong Woojin was grinning contentedly when—

[P29]
Jin Taekyung, who had been staring blankly at the TV, casually tossed out a remark.

[P30]
“Isn’t that one male?”

[P31]
“Huh? Well, that…”

[P32]
“We don’t know yet, do we?”

[P33]
“Come to think of it, I haven’t checked.”

[P34]
“Let’s take a look. We can find out.”

[P35]
Huh?

[P36]
Things were taking a strange turn. His body might currently belong to a cat, but Hong Woojin was still a vigorous young man. As Jin Taekyung’s large hand approached, a wave of shame suddenly washed over him.

[P37]
*That filthy bastard is going to look at my junk?*

[P38]
Strictly speaking, it wasn’t Hong Woojin’s body. They were different species, so naturally their anatomy was different as well.

[P39]
However, Familiar magic made the caster and Familiar share everything. He couldn’t help feeling disgusted.

[P40]
*Absolutely not!*

[P41]
Hong Woojin hurriedly burrowed into Jin Hayeon’s arms.

[P42]
“Mrowww.”

[P43]
“Oh my, I don’t think she likes that.”

[P44]
“That’s how the world works. Who gets to live doing only what they want?”

[P45]
“But Yeoreum’s a cat.”

[P46]
“Cats are the same. If you want warm feed and even a can of treats, you have to put up with this much.”

[P47]
What a lunatic. He was spouting utter nonsense just because he wanted to check a cat’s sex. Grinding his teeth, Hong Woojin clung to his only hope, Jin Hayeon.

[P48]
He rubbed his entire body against her arm and gave her a pitiful look. Her eyes slowly softened.

[P49]
“What am I going to do? Yeoreum’s so cute I could die.”

[P50]
“Yeah, it’s cute. So let’s take a look.”

[P51]
“Do it next time. You’re scaring her.”

[P52]
“That’s just your imagination.”

[P53]
“I’m telling you, Yeoreum doesn’t like you, Oppa.”

[P54]
The trick was to let out a whimper at exactly the right moment.

[P55]
“Mnyaa. Mngh.”

[P56]
“See? I’m right, aren’t I?”

[P57]
“…Then I guess it can’t be helped.”

[P58]
“Don’t you dare manhandle the kitten. Kittens are sensitive, so you have to be careful with them.”

[P59]
Good. He had gotten past the immediate crisis. Jin Taekyung seemed like a lunatic who lived in his own world, but he was weak when it came to his family.

[P60]
Having fully absorbed all the background information Sangdong Guild had given him, Hong Woojin thought he was one step ahead.

[P61]
*This is why information matters. You’ve already fallen right into my trap.*

[P62]
But there was one fact Hong Woojin had never imagined.

[P63]
“Hey, Sis.”

[P64]
“Yeah?”

[P65]
“Do you need more spending money?”

[P66]
“…Are you trying to bribe me so you can have your way with our Yeoreum?”

[P67]
“Yeah. A hundred thousand won.”

[P68]
“Deal. But be gentle so she doesn’t hate you too much, okay?”

[P69]
“My wallet’s on the desk in my room. Go get it.”

[P70]
“Eek!”

[P71]
“Miaow?”

[P72]
Jin Hayeon disappeared like a bullet. Hong Woojin let out a cry filled with disbelief.

[P73]
*You said she was so cute you could die! You called her our Yeoreum!*

[P74]
*What a shameless little brat.*

[P75]
One minute she had acted ready to give Yeoreum her liver and gallbladder, and now she was abandoning “our Yeoreum” for a mere hundred thousand won?

[P76]
But he was given no time to lament the realities of capitalist society.

[P77]
“Come on. Let’s play.”

[P78]
Grab.

[P79]
Jin Taekyung restrained all four of his limbs with lightning speed, a revolting smile on his face.

[P80]
Hong Woojin screamed desperately.

[P81]
*Let go! Let go, you son of a bitch!*

[P82]
“Hiss! Hissss!”

[P83]
The kitten’s fur stood on end as he hissed, catching the attention of his only hope as she rummaged through Jin Taekyung’s wallet.

[P84]
“Oppa!”

[P85]
“Yeah, take another hundred thousand won.”

[P86]
“Thanks!”

[P87]
*Hey! Hey!*

[P88]
His only hope had fallen and become a slave to capitalism!

[P89]
Before the shock had even worn off, Jin Taekyung’s hot breath swept over him.

[P90]
“Our Yeoreum, shall we take a look at your little peepee?”

[P91]
At that desperate, life-or-death moment—

[P92]
*Sever Link!*

[P93]
“Miaowww!”

[P94]
With a sorrowful cry, all the strength drained out of the kitten’s body.

[P95]
Then Hong Woojin opened his eyes somewhere dark and let out a breath.

[P96]
“Puhack!”

[P97]
Since starting work as a Hunter, he had handled more than a hundred assignments, large and small, but this was the first time he had ever felt his life was in danger.

[P98]
He looked down at his forearms, which were covered in goose bumps, and began to gag.

[P99]
“Urgh.”

[P100]
His stomach churned, and his head throbbed.

[P101]
It was a side effect of the sudden Link severance. Only after he gulped down the potion he had prepared in advance like cold water could Hong Woojin finally catch his breath.

[P102]
“Jin Taekyung, that fucking bastard…”

[P103]
It was the moment he first regretted ever accepting the assignment.

[P104]
* * *

[P105]
> **System**
>
> **Lv. 2 Cat**

[P106]
“There he goes.”

[P107]
Clicking my tongue, I released the kitten. Was it even three months old? The little thing, smaller than my two palms put together, backed away with a bewildered look.

[P108]
“Miaow.”

[P109]
Hayeon was leaving my room when she spotted what had happened.

[P110]
“You didn’t do anything mean to our Yeoreum, did you?”

[P111]
“And you’re the one who sold Yeoreum for 200,000 won?”

[P112]
“…Ahem. Ahem.”

[P113]
“Whatever. Good grief. Of all the things you could’ve picked up, you had to bring home that.”

[P114]
“What are you talking about? Look how cute she is.”

[P115]
“That’s not what I meant… Never mind. Forget it.”

[P116]
The whole story was too long and complicated to explain piece by piece. Besides, I had no intention of telling her.

[P117]
Imagine telling her that some sinister bastard had entered the body of a cat and was watching us. It was obvious how anxious she would become. My family couldn’t find out about what was happening.

[P118]
*Besides, I was the one who had allowed it.*

[P119]
The reason I had let a Familiar into the house wasn’t because Hayeon had asked or because Mom had given her permission.

[P120]
*It was because I wanted it.*

[P121]
I didn’t know who had hired them, but even if I drove them off now, they would keep trying.

[P122]
It didn’t matter whether the Familiar took the form of an insect like last time or a cat like today.

[P123]
What mattered was that I already knew what the Familiar was and could swat it away whenever I wanted.

[P124]
*They’re definitely somewhere around here.*

[P125]
Within 500 meters of the house. Somewhere inside that radius was a mage controlling the Familiar. If I shook him down, I was sure I’d find the connection.

[P126]
*First I’ll punch him in the mouth. Then I’ll ask questions.*

[P127]
He had illegally surveilled a civilian, so there was no way he could report me even if I beat him. Just thinking about teaching him a proper lesson made my fists itch.

[P128]
*How dare they snoop around my house?*

[P129]
They had interrupted my first vacation in a long time, and thanks to these bastards, I had already spent well over 300 million won. In every respect, this was a losing proposition.

[P130]
I was watching TV with my face twisted into a scowl when Hayeon cautiously studied my expression and spoke.

[P131]
“Oppa, are you mad?”

[P132]
“No. What would I be mad about?”

[P133]
“I’m sorry.”

[P134]
“…What’s gotten into you? You’re starting to scare me.”

[P135]
I wasn’t joking. I was more startled than when I had first discovered the Familiar. Since when could she say something like that?

[P136]
I asked seriously.

[P137]
“Are you sick?”

[P138]
“No, it’s just…”

[P139]
“Then are you hungry?”

[P140]
“That’s not it…”

[P141]
Just as Hayeon hesitated, about to say something, a stomach growled from somewhere.

[P142]
It wasn’t mine. Mom had stepped out to run an errand.

[P143]
“You’re hungry.”

[P144]
“Mm, a little?”

[P145]
“Right. You’re so hungry you’re starting to spout nonsense. You know where my wallet is, right? Order anything you want to eat.”

[P146]
“Really?”

[P147]
“Yeah. Up to a hundred thousand won.”

[P148]
“Wow, now that you’re making money, you’ve gotten generous. Our Oppa.”

[P149]
I never thought I’d live to hear her call me “our Oppa.” It was the first time I’d heard it since Hayeon had been in middle school, and it gave me goose bumps.

[P150]
“You’re the Familiar, you little bastard!”

[P151]
“What are you talking about? Anyway, I can order whatever I want as long as it’s under a hundred thousand won?”

[P152]
“Yeah. No, wait. Fine. Order everything you want.”

[P153]
“What about the money left over?”

[P154]
“…Did you leave your money with me?”

[P155]
“The more, the better.”

[P156]
Her shamelessness left me dumbfounded, but at the same time, I was happy.

[P157]
She had never once asked me for spending money. Judging by the clothes she wore and how she usually looked, she was far more modest than the kids her age I occasionally saw on the street.

[P158]
*What an old soul.*

[P159]
Come to think of it, Hayeon had been like that since she was little. She rarely cried, and she didn’t often express her feelings honestly. Her current personality had only developed after she entered high school.

[P160]
*She ought to be allowed to act spoiled once in a while… She grew up too soon.*

[P161]
*Maybe even far sooner than I did.*

[P162]
Was that why? None of her actions or words annoyed me in the slightest. If anything, I found her admirable, and I was happy.

[P163]
“Fine. Take it all. Take everything.”

[P164]
“Really?”

[P165]
“Yeah.”

[P166]
Hayeon beamed at my words.

[P167]
“That’s a relief. I almost felt bad for nothing.”

[P168]
“What’s there to feel bad about?”

[P169]
“I took three hundred thousand won from your wallet earlier.”

[P170]
“…Huh?”

[P171]
“But when you said I could have whatever was left after eating within the 100,000-won limit, I felt better.”

[P172]
“Hold on. Didn’t I tell you to take two hundred thousand won?”

[P173]
“It was an impulsive accident.”

[P174]
“…Don’t you mean an impulsive crime?”

[P175]
I take back what I said earlier.

[P176]
The sight of her back as she hummed her way into her room couldn’t have been more irritating.

[P177]
* * *

[P178]
The head of Sangdong Guild’s Security Team frowned.

[P179]
“A Cat Familiar?”

[P180]
“Yes, I’m certain.”

[P181]
The person who answered in a firm voice was a member of the Security Team and the Guild’s only Familiar mage. He was only a C-rank Hunter, but as a rare mental mage, he was also a core member of the Security Team.

[P182]
“The target’s younger sister is a cat fanatic. Hong Woojin took advantage of that opening perfectly.”

[P183]
“Can’t you read the room? You’re praising that bastard to my face?”

[P184]
“I-I’m sorry.”

[P185]
“Team 1 Leader said Hong Woojin called and went ballistic, saying he nearly got exposed because of us.”

[P186]
“…”

[P187]
“Come to think of it, that bastard is technically on our side, too. But can we afford to be outdone by a freelancer? Don’t you know the Guild Master is taking a special interest in this?”

[P188]
Six people had been assigned to the operation, including the Security Team Leader. One was the Familiar mage. Four were close-combat Hunters specializing in tracking and stealth. The last was the Security Team Leader himself, a B-rank Hunter.

[P189]
“You seem to be misunderstanding something… We didn’t come here just to dig up dirt on one C-rank Hunter.”

[P190]
The Security Team Leader glared menacingly at his team.

[P191]
The Guild Master had personally ordered this operation. They had to produce results that went beyond the direct order, no matter what.

[P192]
“Let’s do this properly. This came straight from the Guild Master. Are you going to end here? You should get bonuses and promotions too.”

[P193]
The team members silently lowered their heads.

[P194]
The person most desperate for a bonus and promotion was the Security Team Leader himself. The hysteria of a middle-aged family man whose retirement was slowly approaching was nothing new by this point.

[P195]
“And you.”

[P196]
The Security Team Leader pointed at the Familiar mage.

[P197]
“You do the cat, too.”

[P198]
“The cat? They already did that over there.”

[P199]
“What, then? Are you going to put on another pathetic act with a tiny Familiar you can’t even control and die like last time?”

[P200]
“…”

[P201]
“Do as you’re told. The girl’s a cat fanatic, isn’t she?”

[P202]
If he was told to use a cat, then he had to use a cat. What choice did he have?

[P203]
After the Security Team Leader stormed out, the Familiar mage immediately turned on his smartphone and began searching.

[P204]
Tap. Tap. Tap.

[P205]
> **Cats for Adoption in Ilsan**

[P206]
“…Will they let me expense this?”
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
# Chapter 95

[P2]
*Heh heh heh. Success.*

[P3]
Hong Woojin smiled smugly. He was a veteran at monitoring his targets’ every move and extracting every bit of information from them.

[P4]
The information that Jin Taekyung’s younger sister was crazy about animals—cats in particular—had been especially useful.

[P5]
“Meow-meow, answer me. You like being inside the house, don’t you?”

[P6]
The infiltration had been natural and successful. Inside the kitten’s body, Hong Woojin let out a roar of joy.

[P7]
“Miaowww.”

[P8]
“Ahh, so cute! Oppa, did you hear that just now? You heard it, right?”

[P9]
“Yeah. I heard it.”

[P10]
“How can you be so indifferent to such a cute little creature? Are you even human?”

[P11]
“Then what am I, a beast?”

[P12]
The problem was Jin Taekyung.

[P13]
Even the most emotionally dried-up person tended to soften in front of a cute animal, especially a tiny one, but…

[P14]
“Move over a little. You’re blocking the TV.”

[P15]
This guy had none of that. His sensitivity was drier than the Sahara Desert, and his younger sister, Jin Hayeon, grumbled.

[P16]
“Good grief, there’s a limit to how bleak a person can be. Right, Yeoreum?”

[P17]
“Yeoreum?”

[P18]
“Yeah. Born in summer, so Midsummer. Pretty, right?”

[P19]
“What do you mean, Midsummer? Judging by the size, the kitten looks about three months old. That would mean it was born in late spring, so call it Late Spring or something.”

[P20]
“…Is that supposed to be a joke or what? Anyway, this kitten’s name is Yeoreum from today onward. Right, Yeoreum?”

[P21]
“Mrowww.”

[P22]
From Hong Woojin’s perspective, Jin Hayeon was his greatest asset. Thanks to her, everything was going smoothly.

[P23]
“Ahh! Yeoreum answered! You just answered your big sister, didn’t you? Didn’t you?”

[P24]
“Miaow.”

[P25]
“Eek, my heart!”

[P26]
*Heh. What an easy one to handle.* All it took was a few meows, and she practically melted.

[P27]
*This is why high-school girls are… No, wait. It’s because my choice of Familiar was excellent.*

[P28]
Hong Woojin was grinning contentedly when—

[P29]
Jin Taekyung, who had been staring blankly at the TV, casually tossed out a remark.

[P30]
“Isn’t that one male?”

[P31]
“Huh? Well, that…”

[P32]
“We don’t know yet, do we?”

[P33]
“Come to think of it, I haven’t checked.”

[P34]
“Let’s take a look. We can find out.”

[P35]
Huh?

[P36]
Things were taking a strange turn. His body might have been a cat’s, but Hong Woojin was a vigorous young man. When Jin Taekyung’s large hand approached, a sense of shame suddenly washed over him.

[P37]
*That filthy bastard is going to look at my junk?*

[P38]
Strictly speaking, it wasn’t Hong Woojin’s body. Since the species were different, the physical structures were different, too.

[P39]
However, Familiar magic made the caster and the Familiar share everything. There was no helping the disgust he felt.

[P40]
*Absolutely not!*

[P41]
Hong Woojin hurriedly burrowed into Jin Hayeon’s arms.

[P42]
“Mrowww.”

[P43]
“Oh my, I don’t think the kitten likes that.”

[P44]
“That’s how the world works. Who gets to live doing only what they want?”

[P45]
“But Yeoreum’s a cat.”

[P46]
“Cats are the same. If you want warm feed and even a can of treats, you have to put up with this much.”

[P47]
What a lunatic. He was spouting ridiculous nonsense just because he wanted to check a cat’s sex. Grinding his teeth, Hong Woojin clung to his only hope, Jin Hayeon.

[P48]
He rubbed his entire body against her arm and gave her a pitiful look. Her eyes slowly softened.

[P49]
“What am I going to do? Yeoreum’s so cute I could die.”

[P50]
“Yeah, very cute. So let’s take a look.”

[P51]
“Do it next time. You’re scaring the kitten.”

[P52]
“That’s just your imagination.”

[P53]
“I told you, Yeoreum doesn’t like you, Oppa.”

[P54]
The key was to let out a groan at exactly the right moment.

[P55]
“Mnyaa. Mngh.”

[P56]
“See? I’m right, aren’t I?”

[P57]
“…Then I can’t help it.”

[P58]
“Don’t you dare force the kitten to let you handle it. Kittens are sensitive, so you have to be careful with them.”

[P59]
Good. He had gotten past the immediate crisis. Jin Taekyung seemed like a lunatic who lived in his own world, but he was weak when it came to his family.

[P60]
Having fully absorbed all the background information Sangdong Guild had given him, Hong Woojin thought he was one step ahead.

[P61]
*This is why information matters. You’ve already fallen right into my trap.*

[P62]
But there was one fact Hong Woojin had never imagined.

[P63]
“Hey, Sis.”

[P64]
“Yeah?”

[P65]
“Do you need more spending money?”

[P66]
“…Are you trying to bribe me so you can mess with our Yeoreum?”

[P67]
“Yeah. A hundred thousand won.”

[P68]
“Deal. But you have to be gentle so she doesn’t hate you too much, okay?”

[P69]
“My wallet’s on the desk in my room. Go get it.”

[P70]
“Eek!”

[P71]
“Miaow?”

[P72]
Jin Hayeon disappeared like a bullet. Hong Woojin let out a cry filled with disbelief.

[P73]
*You said she was so cute you could die. You called her our Yeoreum!*

[P74]
*What a shameless little brat.*

[P75]
One minute she had acted ready to give Yeoreum anything, and now she was abandoning “our Yeoreum” for a mere hundred thousand won?

[P76]
But he was given no time to lament the realities of a capitalist society.

[P77]
“Come on. Let’s play.”

[P78]
He grabbed him.

[P79]
Jin Taekyung restrained all four of his limbs with lightning speed and smiled horribly.

[P80]
Hong Woojin screamed desperately.

[P81]
*Let go! Let go, you son of a bitch!*

[P82]
“Hiss! Hissss!”

[P83]
The kitten’s fur stood on end as Hong Woojin hissed, catching the attention of his only hope as she rummaged through Jin Taekyung’s wallet.

[P84]
“Oppa!”

[P85]
“Yeah, take another hundred thousand won.”

[P86]
“Thanks!”

[P87]
*Hey! Hey!*

[P88]
His only hope had become a slave to capitalism!

[P89]
Before the shock had even worn off, Jin Taekyung’s hot breath swept over him.

[P90]
“Our Yeoreum, shall we take a look at your little peepee?”

[P91]
At that desperate, life-or-death moment—

[P92]
*Sever Link!*

[P93]
“Miaowww!”

[P94]
With a sorrowful cry, all the strength drained out of the kitten’s body.

[P95]
Then Hong Woojin opened his eyes somewhere dark and let out a breath.

[P96]
“Puhack!”

[P97]
Since starting work as a Hunter, he had handled more than a hundred large and small assignments, but this was the first time he had ever felt his life was in danger.

[P98]
He looked down at his forearms, which were covered in goose bumps, and began to gag.

[P99]
“Urgh.”

[P100]
His stomach churned, and his head throbbed.

[P101]
It was a side effect of the sudden Link severance. Only after he gulped down the potion he had prepared in advance like cold water could Hong Woojin finally catch his breath.

[P102]
“Jin Taekyung, you fucking bastard…”

[P103]
It was the moment he first regretted ever accepting the assignment.

[P104]
* * *

[P105]
> **System**
>
> **Lv. 2 Cat**

[P106]
“There he goes.”

[P107]
Clicking my tongue, I let the kitten go. Was it three months old? The little thing, smaller than my two joined palms, backed away with a bewildered expression.

[P108]
“Miaow.”

[P109]
Hayeon was leaving my room when she spotted what had happened.

[P110]
“You didn’t do anything mean to our Yeoreum, did you?”

[P111]
“And you’re the one who sold Yeoreum for 200,000 won?”

[P112]
“…Ahem. Ahem.”

[P113]
“Whatever. Good grief. Whenever you pick something up, it has to be something like that.”

[P114]
“What are you talking about? Look how cute Yeoreum is.”

[P115]
“That’s not what I meant… Never mind. Forget it.”

[P116]
It was a long and complicated story to explain one detail at a time. Besides, I had no intention of explaining it.

[P117]
If I told her that some sinister bastard had entered the body of a cat and was watching us, it was obvious how anxious she would become. My family couldn’t find out about what was happening.

[P118]
*Besides, I was the one who had allowed it.*

[P119]
The reason I had let a Familiar into the house wasn’t because Hayeon had asked or because Mom had given her permission.

[P120]
*It was because I wanted it.*

[P121]
I didn’t know who had hired them, but even if I drove them off now, they would keep trying.

[P122]
It didn’t matter whether the Familiar took the form of an insect like last time or a cat like today.

[P123]
What mattered was that I already knew what the Familiar was and could swat it away whenever I wanted.

[P124]
*They’re definitely somewhere around here.*

[P125]
Within 500 meters of the house. Somewhere inside that radius was a mage controlling the Familiar. If I roughed him up, I was sure I’d find the connection.

[P126]
*First, I’ll punch him in the mouth, then ask some questions.*

[P127]
He had illegally surveilled a civilian, so there was no way he could report me even if I beat him. Just thinking about teaching him a proper lesson made my fists itch.

[P128]
*How dare they snoop around someone’s house?*

[P129]
They had interrupted my first vacation in a long time, and thanks to these bastards, I had already spent well over 300 million won. In every respect, this was a losing proposition.

[P130]
I was watching TV with my face twisted into a scowl when Hayeon cautiously watched my reaction and spoke.

[P131]
“Oppa, are you mad?”

[P132]
“No. What is there to be mad about?”

[P133]
“I’m sorry.”

[P134]
“…What’s gotten into you? You’re starting to scare me.”

[P135]
I wasn’t joking. I was more startled than when I had first discovered the Familiar. Since when could she say something like that?

[P136]
I asked seriously.

[P137]
“Are you sick?”

[P138]
“No, it’s just…”

[P139]
“Then are you hungry?”

[P140]
“That’s not it…”

[P141]
Just as Hayeon hesitated, apparently about to say something, a stomach growled from somewhere.

[P142]
It wasn’t mine. Mom had stepped out to run an errand.

[P143]
“You’re hungry.”

[P144]
“Mm, a little?”

[P145]
“Right. You’re so hungry you’re starting to spout nonsense. You know where my wallet is, right? Order anything you want to eat.”

[P146]
“Really?”

[P147]
“Yeah. Up to 100,000 won.”

[P148]
“Wow, now that you’re making money, you’ve gotten generous, Oppa.”

[P149]
In all my life, I never thought I’d hear her call me “our Oppa.” It was the first time I’d heard it since Hayeon had been in middle school, and it gave me goose bumps.

[P150]
“You’re the Familiar, you little bastard!”

[P151]
“What are you talking about? Anyway, can I order whatever I want as long as it’s under 100,000 won?”

[P152]
“Yeah. No, wait. Fine. Order everything you want.”

[P153]
“What about the money left over?”

[P154]
“…Did you leave your money with me?”

[P155]
“More is better.”

[P156]
I was dumbfounded by Hayeon’s shamelessness, but at the same time, I was happy.

[P157]
She had never once asked me for spending money. Even judging by the clothes she wore and her usual appearance, she was far more modest than the kids her age I occasionally saw on the street.

[P158]
*What an old soul.*

[P159]
Come to think of it, Hayeon had been like that since she was little. She rarely cried, and she didn’t often express her feelings honestly. Her current personality had only developed after she entered high school.

[P160]
*She ought to be allowed to act spoiled once in a while… She grew up too soon.*

[P161]
*Maybe even much sooner than I did.*

[P162]
Maybe that was why. None of her actions or words annoyed me in the slightest. If anything, I found her admirable, and I was happy.

[P163]
“Fine. Take it all. Take everything.”

[P164]
“Really?”

[P165]
“Yeah.”

[P166]
Hayeon beamed at my words.

[P167]
“That’s a relief. I almost felt bad for nothing.”

[P168]
“What’s there to feel bad about?”

[P169]
“I took 300,000 won from your wallet earlier.”

[P170]
“…Huh?”

[P171]
“But when you said I could have whatever was left after eating within the 100,000-won limit, I felt better.”

[P172]
“Hold on. Didn’t I tell you to take 200,000 won?”

[P173]
“It was an accident.”

[P174]
“…Don’t you mean a crime of opportunity?”

[P175]
I take back what I said earlier.

[P176]
The sight of her back as she hummed her way into her room couldn’t have been more irritating.

[P177]
* * *

[P178]
The head of Sangdong Guild’s Security Team frowned.

[P179]
“A Cat Familiar?”

[P180]
“Yes, I’m certain.”

[P181]
The person who answered in a firm voice was a member of the Security Team and the Guild’s only Familiar mage. He was only a C-rank Hunter, but he was also a core member of the Security Team because mental mages were rare.

[P182]
“The target’s younger sister is a cat fanatic. Hong Woojin took advantage of that opening perfectly.”

[P183]
“Can’t you read the room? You’re praising that bastard in front of me?”

[P184]
“I-I’m sorry.”

[P185]
“Team 1 Leader said Hong Woojin called and went ballistic, saying he nearly got exposed because of us.”

[P186]
“…”

[P187]
“Come to think of it, that bastard is technically on our side, too. But can we afford to be outdone by a freelancer? Don’t you know the Guild Master is taking a special interest in this?”

[P188]
Six people had been assigned to this operation, including the Security Team Leader. One was the Familiar mage, four were close-combat Hunters specializing in tracking and stealth, and the Team Leader himself was a B-rank Hunter.

[P189]
“I think you’re under a misconception… We didn’t come here just to dig up dirt on one C-rank Hunter.”

[P190]
The Security Team Leader glared at his team with a menacing expression.

[P191]
The Guild Master had personally ordered this operation. They had to produce results that went beyond the direct order, no matter what.

[P192]
“Let’s do this properly. This came straight from the Guild Master. Are you going to let your careers end here? You want bonuses and promotions, don’t you?”

[P193]
The team members silently lowered their heads.

[P194]
The person most desperate for a bonus and promotion was the Security Team Leader himself. The hysteria of a middle-aged family man whose retirement was slowly approaching was nothing new by this point.

[P195]
“And you.”

[P196]
The Security Team Leader pointed at the Familiar mage.

[P197]
“You do the cat, too.”

[P198]
“The cat? They already did that over there.”

[P199]
“What, then? Are you going to put on another pathetic performance with a tiny Familiar you can’t even control and die like last time?”

[P200]
“…”

[P201]
“Do as you’re told. The girl’s a cat fanatic, isn’t she?”

[P202]
If they wanted a cat, he had to use a cat. What else could he do?

[P203]
After the Security Team Leader stormed out, the Familiar mage immediately turned on his smartphone and began searching.

[P204]
Tap. Tap. Tap.

[P205]
> **Ilsan Cat Adoption**

[P206]
“…Do you think this will count as a business expense?”
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 진태경    | **Jin Taekyung**   |
| 진하연    | **Jin Hayeon**    |
| 홍우진    | **Hong Woojin**   |
| 상태               | **Status**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 95,
  "passed": true,
  "metrics": {
    "source_characters": 5989,
    "translation_characters": 13455,
    "length_ratio": 2.247,
    "source_paragraphs": 205,
    "translation_paragraphs": 206
  },
  "errors": [],
  "warnings": [
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
        "korean": "등급",
        "preferred": "Grade"
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
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "사하라",
        "romanization": "sahara"
      }
    },
    {
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "상동",
        "romanization": "sangdong"
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
