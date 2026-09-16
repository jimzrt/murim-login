# Fidelity Gate — Chapter 98

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
  1|＃98화
  2|
  3|
  4|
  5|홍우진은 후회했다.
  6|
  7|‘내 생각이 짧았구나.’
  8|
  9|침입은 성공적이었다. 고양이 덕후인 표적의 여동생에게 접근, 애처로우면서도 반짝이는 눈망울로 마음을 사로잡았으니까. 다만 문제는…….
 10|
 11|“우리 여름이는 뭘 먹고 이렇게 귀여워요? 응? 응응?”
 12|
 13|미야옹.
 14|
 15|“여름아, 왜 자꾸 문밖으로 나가려고 해. 여기서 언니랑 놀자.”
 16|
 17|야옹.
 18|
 19|“꺅, 너무 귀여워!”
 20|
 21|하악! 하아아악!
 22|
 23|“헉, 여름이 화났어? 미안해. 언니가 너무 만졌지? 알았어, 가만히 있을 테니까 침대 위에서 놀고 있어. 응?”
 24|
 25|이 망할 여동생이라는 녀석이 도무지 밖으로 내보내 줄 생각을 안 한다는 거다. 덕분에 하루 반나절 이상을 진하연의 방에 갇혀 지내는 신세가 됐다.
 26|
 27|‘차라리 개로 할걸.’
 28|
 29|개였다면 지금처럼 쉽게 들어올 수는 없었겠지만 들어온 이후에 반 감금되어 있지는 않았을 것이다. 적어도 산책 정도는 시켜 줬을 테니까.
 30|
 31|‘이대로는 죽도 밥도 안 된다.’
 32|
 33|위기감에 휩싸인 홍우진은 탈출을 시도했다.
 34|
 35|‘네가 이기나, 내가 이기나 보자!’
 36|
 37|그렇게 독한 마음으로 시작했는데…….
 38|
 39|벅, 벅벅벅벅.
 40|
 41|“…….”
 42|
 43|야옹. 야오오오옹.
 44|
 45|“…….”
 46|
 47|첫 번째 시도는 실패다. 괜히 방문도 박박 긁어 보고, 큰 소리로도 울어도 봤지만 진하연은 책상에 앉아 단 한 번도 반응하지 않았다.
 48|
 49|이어폰도 끼지 않은 채 그저 매서운 눈빛과 손놀림으로 문제집을 풀어 가고 있을 뿐.
 50|
 51|‘전국 상위 0.01%라더니.’
 52|
 53|1차 조사 자료에서 봤다. 중학교 때부터 전교 1, 2등은 예사고 각종 경시 대회에서 입상한 경력이 수두룩했으니 잊기도 힘든 내역이다.
 54|
 55|홍우진은 오늘에서야 그 이유를 알았다. 책상 앞에 앉은 그녀는 정말이지, 어마 무시한 집중력의 소유자였다.
 56|
 57|‘이런 애가 마법사 하면 딱인데……가 아니고.’
 58|
 59|그는 그 후로도 어떻게든 공부를 방해하려고 애썼다. 쉴 새 없이 발을 건드리고 애교를 부려 댔다.
 60|
 61|하지만 진하연의 대응은 간단했다.
 62|
 63|“언니 지금 공부 중이야. 방해하면 안 돼.”
 64|
 65|의자에 발을 올려 책상다리로 앉아 버리고 나니 이 조그마한 몸으로는 결코 닿을 수 없게 되었다. 아기 고양이의 한계였다.
 66|
 67|‘이번 작전은 실패다.’
 68|
 69|공부 방해 작전이 실패로 돌아갔으니 별수 없이 최후의 카드를 꺼내야 한다. 인간의 존엄성에 큰 손상을 입겠지만 지금은 이것저것 가릴 때가 아니었다.
 70|
 71|‘이것도 무시하나 보자.’
 72|
 73|쉬이이이이.
 74|
 75|새하얀 이불보가 노랗게 물든다. 본래 큰일과 작은 일은 한 번에 해결해야 하는 법. 두 가지 일을 동시에 끝마친 홍우진은 굳게 결심했다.
 76|
 77|‘그래, 기왕 이렇게 된 거 확실하게 처리하자. 프로답게.’
 78|
 79|데굴데굴.
 80|
 81|패밀리어 마법을 시작한 지 5년. 이렇게까지 망가진 적은 이번이 처음이었다. 그는 끊임없이 자기 세뇌를 걸었다.
 82|
 83|‘나는 프로다, 나는 프로다, 나는 프로다…….’
 84|
 85|잠시 후, 뭔가 이상한 냄새를 맡은 진하연이 고개를 돌렸을 때는 모든 게 끝난 후였다.
 86|
 87|미야옹.
 88|
 89|대소변으로 물든 이불, 마찬가지로 오물로 범벅이 된 아기 고양이 한 마리.
 90|
 91|“꺅, 여름아!”
 92|
 93|깜짝 놀란 진하연이 신속하게 움직였다. 더러워진 이불을 걷고, 조심스럽게 고양이의 뒷덜미를 잡아 들어 올렸다.
 94|
 95|“화장실 두고 여기서 싸면 어떡해. 우리 여름이 씻어야겠다.”
 96|
 97|‘그래, 문으로 가라! 문!’
 98|
 99|고대하던 순간이다. 비록 오물로 범벅이 된 채 스무 살도 안 된 여자애의 손에 대롱대롱 매달려 있지만 홍우진은 희열에 가득 찼다.
100|
101|달칵.
102|
103|열린다, 문이!
104|
105|어제 이후로 보지 못했던 거실이 보인다!
106|
107|미야옹! 미야오옹!
108|
109|“이상하네. 얘가 왜 이렇게 좋아하는 것 같지?”
110|
111|진하연이 갸우뚱하던 그때였다.
112|
113|비밀번호를 입력하는 익숙한 기계음과 함께 현관문이 열렸다.
114|
115|“다녀왔습니…… 뭐냐, 그건?”
116|
117|“어디 다녀왔…… 그건 뭐야?”
118|
119|남매는 서로를 황당한 시선으로 바라봤다. 정확히 말하면 각자의 손에 들린 생물체를.
120|
121|야옹.
122|
123|미야옹.
124|
125|황당한 시선을 교환하는 것은 이쪽도 마찬가지였다.
126|
127|‘저게 홍우진?’
128|
129|‘저놈은 상동 길드의 아마추어?’
130|
131|그리고 이어지는 생각.
132|
133|‘쟤는 왜 온몸에 똥칠을 하고 있어?’
134|
135|‘아, 시바.’
136|
137|홍우진이 갖고 있던 마지막 인간의 존엄성이 와르르 무너지는 순간이었다.
138|
139|
140|
141|* * *
142|
143|
144|
145|“이불에다가 똥칠을 해 놨다고?”
146|
147|“어. 잠깐 공부하는 사이에 실수했나 봐.”
148|
149|실수는 개뿔, 다분히 의도적이다.
150|
151|하연이가 방에만 두고 물고 빠니까 어떻게든 나오려고 머리 굴린 거지, 뭐.
152|
153|미야옹…….
154|
155|고양이, 아니 이제 두 마리니까 이름을 불러 줘야겠구나.
156|
157|어쨌건 여름이의 힘없는 울음소리에 하연이가 걱정스러운 얼굴로 물었다.
158|
159|“애가 아까부터 힘이 없어.”
160|
161|“음, 그럴 수 있지.”
162|
163|모르긴 몰라도 자괴감이 장난 아닐 거다.
164|
165|몸에 똥칠한 채로 업계 동업자와 감시 표적을 동시에 맞닥트렸으니까.
166|
167|“너무 걱정하지 마. 원래 고양이들은 몸에 물 닿는 거 싫어하잖아.”
168|
169|“그래서 그런 건가? 아냐, 아까 씻길 땐 반항도 안 하고 얌전하던데.”
170|
171|“아, 그래?”
172|
173|“기분 탓인지는 모르겠는데…… 애가 좀 넋이 나간 느낌이야. 자기도 사고 친 걸 알아서 미안해하는 건가?”
174|
175|우리 여름이, 현자 타임이 제대로 왔구나.
176|
177|나는 웃음을 삼키며 말했다.
178|
179|“그거야 모르지. 아무튼 너 이불 어쩌냐? 시트도 새로 갈아야 되겠네.”
180|
181|“괜찮아. 사람이 한 것도 아니고 동물인데, 뭘.”
182|
183|별생각 없이 던진 돌에 개구리가 맞아 죽는다더니.
184|
185|지금이 딱 그 상황이다. 하연이의 한마디는 비수로 변해 누군가의 가슴에 꽂혔다.
186|
187|움찔.
188|
189|울음소리도 못 내고 작은 몸을 부르르 떠는 아기 고양이 한 마리. 반면 다른 한쪽은 신이 났다.
190|
191|그릉, 그르릉.
192|
193|기분 좋은 소리를 내며 내 다리에 연신 얼굴을 비벼 대는 검은 고양이를 하연이가 귀여워 죽겠다는 얼굴로 바라봤다.
194|
195|“얘는 어디서 데려왔어?”
196|
197|“아파트 단지 입구에서.”
198|
199|“길고양이야?”
200|
201|“그렇겠지. 혼자 있었으니까.”
202|
203|“뭐? 그럼 엄마가 있을지도 모르잖아. 그래서 새끼 고양이는 하루 정도는 지켜보고 데려와야 해.”
204|
205|“어떤 아저씨한테 들었는데, 어제부터 혼자 울고 있었다는데?”
206|
207|“아, 그럼 엄마 없네.”
208|
209|움찔!
210|
211|골골거리던 애교가 딱 멎는다. 자신도 모르는 사이에 2킬을 달성한 하연이가 해맑게 웃었다.
212|
213|“우쭈쭈. 너도 엄마가 없구나. 괜찮아, 오늘부터 언니가 엄마 해 줄게.”
214|
215|“…….”
216|
217|내 동생이지만 웃는 얼굴로 엿 먹이는 재주가 제법인데.
218|
219|검은 고양이는 직업 정신과 패드립 사이에서 갈등하는 듯했지만 이내 현실을 받아들였다.
220|
221|야옹.
222|
223|어머니의 원수에게 애교를 부리는 모습이 처량하기까지 하다. 저런 게 바로 직장인의 애환이지.
224|
225|지켜보고 있자니 문득 엄마에게 생각이 미쳤다.
226|
227|“엄마는?”
228|
229|“몰라, 중요한 약속 있다고 나가셨어.”
230|
231|“약속?”
232|
233|“응, 요즘 자주 나가셔.”
234|
235|무슨 일이지?
236|
237|근래 들어 엄마의 외출이 잦아졌다. 일을 관둔 후 어느 정도 여유가 생기니 스스로의 삶을 찾으시는 걸까?
238|
239|‘그러고 보니 분위기가 이상하긴 했지.’
240|
241|뭔가 할 말이 있는 듯한 얼굴로 앉아 계신다거나, 갑자기 말을 걸면 화들짝 놀란다거나. 확실히 엄마의 주변에 어떤 변화가 일어나고 있는 것은 분명해 보인다.
242|
243|‘때가 되면 말씀해 주시겠지.’
244|
245|내가 세상에서 가장 사랑하고 믿는 분이 바로 우리 엄마다. 언제나 그렇듯이 믿고 기다리는 수밖에.
246|
247|물론 적절한 시기에 함께 대화를 나누고 이야기를 들어 드리는 것도 자식의 도리다.
248|
249|“무슨 생각을 그렇게 해?”
250|
251|“별것 아냐. 그나저나 너는 어디 안 나가냐?”
252|
253|“뭐야, 꼭 어디 나가기를 바라는 말투네.”
254|
255|“꼭 그런 건 아니고.”
256|
257|“흠, 수상해. 여자 친구 데려오려는 건 아니지?”
258|
259|“…….”
260|
261|제발 데려올 여자 친구라도 있었으면 좋겠다.
262|
263|생각이 고스란히 드러나는 내 표정에 하연이가 주춤했다.
264|
265|“아, 미안.”
266|
267|“……사과하지 마. 두 배로 비참해져.”
268|
269|“진짜 미안해.”
270|
271|“너 일부러 이러는 거지?”
272|
273|“생각해 보니까 도서관에 책 반납해야 할 게 있네.”
274|
275|방 안으로 뛰어가더니 가방을 들쳐 메고 나오는 속도가 광속이다. 쾅 소리와 함께 현관문이 닫히자 집 안이 조용해졌다.
276|
277|‘솔로의 마음을 후벼 놓다니.’
278|
279|가슴 한구석이 휑해졌지만 내가 원하던 무대가 드디어 만들어졌다.
280|
281|가급적이면 가족이 없을 때 해결해야 될 문제니까.
282|
283|미야옹.
284|
285|야옹.
286|
287|각기 검고 흰 두 마리의 고양이가 슬금슬금 다가와 주위를 맴돌기 시작했다. 초롱초롱한 눈망울, 쫑긋 선 귀.
288|
289|나에 대한 정보를 건지고 싶어 안달이 난 패밀리어들을 뒤로하고 베란다로 나갔다.
290|
291|가장 먼저 보이는 건 수백 대의 차량이 늘어선 주차장이다.
292|
293|‘주차장은 클리어.’
294|
295|귀가하기 전, 패밀리어를 품에 안고 아파트 단지를 한 바퀴 돌아 보았다. 남들 눈에는 날씨 좋은 날 산책하는 한량으로 보였겠지만 목적은 차량 확인이었다.
296|
297|결과는 이상 무.
298|
299|‘그럼 역시 집밖에 없지.’
300|
301|이로써 감시자들이 최근 거래된 아파트를 아지트로 삼았음이 확인됐다. 나는 부동산에서 얻은 정보를 다시 한번 떠올렸다.
302|
303|‘5동 901호. 4동 302호. 3동 202호.’
304|
305|공교롭게도 세 곳 전부 우리 아파트를 중심으로 감싸는 형태로 자리해 있다. 창문으로도 동 입구를 내려다볼 수 있어 감시에 용이한 위치.
306|
307|감시자들이 어느 곳에 있어도 이상하지 않다.
308|
309|‘문제는 저 중 어디에 숨었냐는 건데…….’
310|
311|발각을 우려해 마법 장비가 아닌 패밀리어를 붙일 정도로 조심성을 갖춘 놈들이다.
312|
313|섣부르게 다가갔다가는 놓친다. 확실한 검거를 위해서는 그만큼 큼지막한 미끼를 던지는 수밖에 없다.
314|
315|‘슬슬 시작해 볼까.’
316|
317|촥, 촤르륵.
318|
319|우선 집 안의 모든 커튼을 쳤다. 한낮임에도 불구하고 어둑해진 거실 중앙에서 주머니를 뒤적였다.
320|
321|‘인벤토리 오픈. 마나 탐지 장비.’
322|
323|동시에 손바닥의 절반만 한 쇳덩이가 손에 잡혔다.
324|
325|이름 그대로 마나를 탐지할 수 있는 장비, 스토어에서 2천만 원이나 주고 산 물건이다.
326|
327|‘다음 단계, 수색.’
328|
329|탐지 장비를 들고 집 안을 꼼꼼히 훑었다. 내부에 아무런 마나가 감지되지 않는 걸 확인하고 스마트폰을 꺼내어 누군가에게 통화를 걸었다.
330|
331|뚜, 뚜. 달칵.
332|
333|통화 연결음과 함께 상대방이 전화를 받았다.
334|
335|- 여보세요?
336|
337|내가 대답했다.
338|
339|“접니다, 진태경.”
340|
341|그런 내 모습을 두 마리의 패밀리어가 숨도 쉬지 않고 지켜보고 있었다.
342|
343|
344|
345|* * *
346|
347|
348|
349|김준수는 눈을 뜸과 동시에 외쳤다.
350|
351|“왔어요, 왔어!”
352|
353|옹기종기 모여 앉아 소견서를 쓰고 있던 보안팀원들이 화들짝 놀랐다.
354|
355|“뭐?”
356|
357|“누가 와? 우리 팀장?”
358|
359|“아니면 설마…….”
360|
361|말꼬리를 흐린 팀원을 향해 김준수가 고개를 끄덕였다.
362|
363|“표적이요. 이 자식 이거 구린내 장난 아닙니다.”
364|
365|“진짜로?”
366|
367|“네. 집 비자마자 커튼 칠 때부터 뭔가 쎄 했는데, 탐지 장비까지 사용해서 집 안 점검하더라고요.”
368|
369|평범한 C급 헌터, 그것도 휴가 중인 놈이 할 만한 일이 아니다. 방 안의 모두가 침을 꿀꺽 삼켰다.
370|
371|“그, 그래서?”
372|
373|“폰 꺼내더니 전화부터 걸던데요.”
374|
375|“전화? 누구한테?”
376|
377|“그걸 모르겠어요.”
378|
379|김준수가 미간을 찡그렸다.
380|
381|“통화가 3분도 안 될 만큼 짧았던 것도 있지만, 호칭에 굉장히 주의한다는 게 느껴질 정도?”
382|
383|“그 정도면 충분해. 일단 윗선에 보고해서 저놈 통화 기록 털어 보면 되니까.”
384|
385|“그래, 더 나온 건 없고?”
386|
387|“왜 없겠습니까. 그놈이 뭐라고 한 줄 아세요?”
388|
389|크흠. 한차례 목을 가다듬은 그의 입에서 낮은 목소리가 흘러나왔다.
390|
391|“계획은 차질 없이 진행 중입니다. 네, 네. 상동 길드 쪽에서는 아직 눈치 못 챘습니다. 물건은 잘 갖고 있습니다.”
392|
393|듣고 있던 팀원들이 무릎을 탁 쳤다.
394|
395|“이거네!”
396|
397|“드디어 하나 건졌다.”
398|
399|“와, 방금 살짝 소름 돋았어. 이거 무슨 비밀 요원이야?”
400|
401|그때, 가만히 듣고 있던 김권동이 불쑥 입을 열었다.
402|
403|“진수야, 방금 그 자식이 무슨 물건 갖고 있다고 하지 않았냐?”
404|
405|“좋은 지적입니다.”
406|
407|김진수가 의미심장하게 웃었다.
408|
409|“그놈, USB를 갖고 있어요.”
```

## Assembled English

```markdown
[P1]
# Chapter 98

[P2]
Hong Woojin regretted it.

[P3]
*I didn’t think this through.*

[P4]
The intrusion itself had gone perfectly. He had approached the target’s cat-loving younger sister and won her heart with a pair of pitiful yet sparkling eyes.

[P5]
The problem was…

[P6]
“What does our Yeoreum eat to be this cute? Hmm? Hmm-hmm?”

[P7]
*Meow.*

[P8]
“Yeoreum, why do you keep trying to get out the door? Stay here and play with Sis.”

[P9]
*Meow.*

[P10]
“Eek, you’re so cute!”

[P11]
*Hiss! Hissssss!*

[P12]
“Oh no, is Yeoreum mad? I’m sorry. Did Sis pet you too much? Okay, I’ll stay still, so play on the bed, all right?”

[P13]
This damn younger sister had absolutely no intention of letting him out. Thanks to her, he had spent more than a day and a half trapped in Jin Hayeon’s room.

[P14]
*I should’ve gone with a dog.*

[P15]
If he had been a dog, getting inside wouldn’t have been this easy. But once he was in, he wouldn’t have been practically held captive, either. At the very least, they would have taken him out for walks.

[P16]
*This is getting me nowhere.*

[P17]
Swept up by a sense of crisis, Hong Woojin attempted to escape.

[P18]
*Let’s see who wins—you or me!*

[P19]
He had begun with that fierce resolve, but then…

[P20]
Scritch, scritch-scritch-scritch.

[P21]
“…”

[P22]
*Meow. Myaaaaaow.*

[P23]
“…”

[P24]
His first attempt failed. He scratched desperately at the door and even yowled as loudly as he could, but Jin Hayeon didn’t react even once.

[P25]
She wasn’t even wearing earphones. She simply continued working through her workbook with a fierce look in her eyes and swift movements of her hands.

[P26]
*So this is what it means to be in the top 0.01 percent nationwide.*

[P27]
He had seen it in the initial investigation report. Ever since middle school, she had routinely ranked first or second in her entire school and had earned countless awards in academic competitions. It was hard to forget a record like that.

[P28]
Only today did Hong Woojin understand why.

[P29]
Sitting at her desk, she displayed a truly terrifying level of concentration.

[P30]
*Someone like this would make the perfect mage… No, that’s not the point.*

[P31]
He continued trying everything he could to disrupt her studies. He pawed at her feet without pause and kept acting cute.

[P32]
But Jin Hayeon’s response was simple.

[P33]
“Big sis is studying right now. Don’t bother me.”

[P34]
She pulled her feet up onto the chair and sat cross-legged, putting them completely out of reach of his tiny body.

[P35]
That was the limit of being a kitten.

[P36]
*This operation has failed.*

[P37]
Since his plan to disrupt her studies had gone up in smoke, he had no choice but to play his final card. It would deal a serious blow to his human dignity, but this was no time to be picky.

[P38]
*Let’s see if you ignore this, too.*

[P39]
Sssssssss.

[P40]
The pristine white duvet turned yellow.

[P41]
When nature called, it was best to take care of both kinds of business at once. Having finished both simultaneously, Hong Woojin made a solemn decision.

[P42]
*Fine. Since things have come to this, I might as well do it properly. Like a professional.*

[P43]
He rolled over and over.

[P44]
It had been five years since he started using Familiar magic. This was the first time he had ever sunk this low.

[P45]
He kept brainwashing himself.

[P46]
*I’m a professional. I’m a professional. I’m a professional…*

[P47]
A little while later, Jin Hayeon noticed a strange smell and turned around.

[P48]
By then, it was all over.

[P49]
*Meow.*

[P50]
A duvet stained with urine and feces, and a kitten likewise covered in filth.

[P51]
“Eek, Yeoreum!”

[P52]
Startled, Jin Hayeon moved quickly. She pulled off the dirty duvet, then carefully grabbed the kitten by the scruff and lifted it up.

[P53]
“What are you doing going to the bathroom here when your litter box is right there? We need to wash our Yeoreum.”

[P54]
*Yes, go to the door! The door!*

[P55]
This was the moment he had been waiting for.

[P56]
Even though he was covered in filth and dangling from the hand of a girl who wasn’t even twenty, Hong Woojin was filled with joy.

[P57]
Click.

[P58]
The door was opening!

[P59]
The living room he hadn’t seen since yesterday came into view!

[P60]
*Meow! Myaaaow!*

[P61]
“That’s strange. Why does it seem so happy?”

[P62]
Jin Hayeon tilted her head.

[P63]
That was when the front door opened with the familiar electronic tones of someone entering the passcode.

[P64]
“I’m ho—… What is that?”

[P65]
“Where have you been—… What’s that?”

[P66]
The siblings stared at each other in bewilderment.

[P67]
More precisely, they stared at the creatures in each other’s hands.

[P68]
*Meow.*

[P69]
*Myaow.*

[P70]
The two cats exchanged equally bewildered looks.

[P71]
*That’s Hong Woojin?*

[P72]
*That guy is the Sangdong Guild’s amateur?*

[P73]
And then came the next thought.

[P74]
*Why is he covered in shit from head to toe?*

[P75]
*Ah, fuck.*

[P76]
It was the moment the last shred of Hong Woojin’s human dignity came crashing down.

[P77]
* * *

[P78]
“He got poop all over the duvet?”

[P79]
“Yeah. I guess he had an accident while I was studying for a bit.”

[P80]
*An accident, my ass.*

[P81]
Hayeon had kept him in her room, petting and cuddling him nonstop, so he’d put his brain to work trying to escape. That was all.

[P82]
*Myaow…*

[P83]
The cat—no, there were two of them now, so I supposed I should call them by their names.

[P84]
Anyway, Yeoreum let out a feeble cry, and Hayeon asked worriedly, “He’s been listless for a while.”

[P85]
“Hmm. That can happen.”

[P86]
I couldn’t say for sure, but his self-loathing had to be off the charts.

[P87]
He had run into both a fellow professional and his surveillance target while covered in shit.

[P88]
“Don’t worry too much. Cats hate getting wet, you know.”

[P89]
“Is that why? No, he didn’t even resist when I washed him earlier. He was completely docile.”

[P90]
“Oh, really?”

[P91]
“I don’t know if it’s just my imagination, but he seems kind of out of it. Maybe he knows he made a mess and feels sorry?”

[P92]
*Our Yeoreum had a serious case of post-nut clarity.*

[P93]
I swallowed my laughter and said, “Who knows? Anyway, what are you going to do about the duvet? You’ll have to change the sheets, too.”

[P94]
“It’s fine. It was an animal, not a person. What’s the big deal?”

[P95]
They said a thoughtlessly thrown stone could kill a frog.

[P96]
This was exactly that kind of situation. Hayeon’s offhand remark turned into a dagger and plunged into someone’s heart.

[P97]
Flinch.

[P98]
The kitten trembled violently in silence, unable to even cry out.

[P99]
Meanwhile, the other one was having the time of its life.

[P100]
*Purr. Prrrr.*

[P101]
The black cat made happy noises as it rubbed its face against my leg over and over, and Hayeon gazed at it with utter adoration.

[P102]
“Where did you bring him from?”

[P103]
“The entrance to the apartment complex.”

[P104]
“Is he a stray?”

[P105]
“I guess so. He was alone.”

[P106]
“What? Then his mother might be nearby. You’re supposed to watch a kitten for about a day before bringing it home.”

[P107]
“Some man told me he’d been crying alone since yesterday.”

[P108]
“Oh, then he doesn’t have a mother.”

[P109]
Flinch!

[P110]
Its purring and attempts to act cute stopped dead. Without realizing it, Hayeon had scored two kills, and she smiled brightly.

[P111]
“There, there. You don’t have a mother, either. It’s okay. From today on, Sis will be your mommy.”

[P112]
“…”

[P113]
For my little sister, she certainly had a talent for screwing people over with a smile.

[P114]
The black cat seemed torn between professional duty and the cheap shot at his mom, but soon accepted reality.

[P115]
*Meow.*

[P116]
The sight of it acting cute for its mother’s enemy was downright pitiful.

[P117]
*That’s the hardship of being a working stiff.*

[P118]
Watching them, I suddenly thought of Mom.

[P119]
“Where’s Mom?”

[P120]
“I don’t know. She went out for an important appointment.”

[P121]
“An appointment?”

[P122]
“Yeah. She’s been going out a lot lately.”

[P123]
*What’s going on?*

[P124]
Mom had been leaving the house frequently these days. Now that she had some free time after quitting her job, was she finally finding a life of her own?

[P125]
*Come to think of it, she had been acting strange.*

[P126]
Sometimes she would sit there looking as though she had something to say. Other times, she would jump whenever I suddenly spoke to her.

[P127]
Something had definitely changed around Mom.

[P128]
*She’ll tell me when the time is right.*

[P129]
My mother was the person I loved and trusted most in this world. As always, all I could do was trust her and wait.

[P130]
Of course, listening to her and talking things over at the right time was also a child’s duty.

[P131]
“What are you thinking about so hard?”

[P132]
“It’s nothing. By the way, aren’t you going out?”

[P133]
“What? You sound like you want me to leave.”

[P134]
“Not exactly.”

[P135]
“Hmm. Suspicious. You’re not planning to bring a girlfriend over, are you?”

[P136]
“…”

[P137]
*I wish I had a girlfriend to bring over.*

[P138]
My expression must have revealed my thoughts, because Hayeon hesitated.

[P139]
“Ah, I’m sorry.”

[P140]
“Don’t apologize. It makes me twice as pathetic.”

[P141]
“I’m really sorry.”

[P142]
“You’re doing this on purpose, aren’t you?”

[P143]
“Come to think of it, I have some books to return to the library.”

[P144]
She sprinted into her room, threw on her backpack, and came back out at the speed of light.

[P145]
The front door slammed shut, and the house fell silent.

[P146]
*She really went and gouged out a single man’s heart.*

[P147]
A corner of my chest felt hollow, but the stage I had been waiting for had finally been set.

[P148]
This was a problem I needed to deal with while my family was out of the house, if possible.

[P149]
*Myaow.*

[P150]
*Meow.*

[P151]
The two cats, one black and one white, crept toward me and began circling.

[P152]
Bright eyes. Perked-up ears.

[P153]
I left the Familiars, who were dying to learn more about me, behind and stepped onto the balcony.

[P154]
The first thing I saw was the parking lot, where hundreds of cars were lined up.

[P155]
*The parking lot is clear.*

[P156]
Before returning home, I had carried the Familiar in my arms and taken a lap around the apartment complex. To everyone else, I probably looked like an idler out for a walk on a pleasant day.

[P157]
My real purpose had been to check the vehicles.

[P158]
The result was nothing suspicious.

[P159]
*Then it has to be one of those apartments.*

[P160]
That confirmed the watchers had made one of the recently sold or leased apartments their base. I recalled the information I had obtained from the real-estate office once more.

[P161]
*Building 5, Unit 901. Building 4, Unit 302. Building 3, Unit 202.*

[P162]
Coincidentally, all three were positioned around our apartment, forming a ring. Their windows also overlooked the building entrances, making them ideal for surveillance.

[P163]
The watchers could have been in any one of them.

[P164]
*The question is which one they’re hiding in…*

[P165]
They were cautious enough to use a Familiar instead of magical Equipment to avoid being discovered.

[P166]
If I approached recklessly, I would lose them. To make a definite capture, I had no choice but to throw out equally substantial bait.

[P167]
*Time to get started.*

[P168]
Swish. Rustle.

[P169]
First, I drew every curtain in the house. Though it was the middle of the day, the living room grew dim. Standing in its center, I reached into my pocket.

[P170]
*Inventory open. Mana-detection Equipment.*

[P171]
At the same time, my hand closed around a lump of metal half the size of my palm.

[P172]
As its name suggested, it was Equipment that could detect mana. I had paid twenty million won for it at the Store.

[P173]
*Next step: search.*

[P174]
I carefully swept through the house with the detection Equipment. After confirming that no mana was being detected inside, I took out my smartphone and called someone.

[P175]
Beep. Beep. Click.

[P176]
The call connected, and the other person answered.

[P177]
—Hello?

[P178]
I replied, “It’s me, Jin Taekyung.”

[P179]
The two Familiars watched me without even seeming to breathe.

[P180]
* * *

[P181]
The moment Kim Junsu opened his eyes, he shouted.

[P182]
“He’s here! He’s here!”

[P183]
The Security Team members, who had been huddled together writing their assessments, jumped in surprise.

[P184]
“What?”

[P185]
“Who’s here? Our Team Leader?”

[P186]
“Or could it be…”

[P187]
Kim Junsu nodded at the team member who had trailed off.

[P188]
“The target. This bastard reeks of something rotten.”

[P189]
“Seriously?”

[P190]
“Yes. I got a bad feeling when he drew all the curtains as soon as the house was empty, and then he even used detection Equipment to inspect the inside.”

[P191]
That wasn’t something an ordinary C-rank Hunter would do, especially while on vacation.

[P192]
Everyone in the room swallowed hard.

[P193]
“Th-then what?”

[P194]
“He pulled out his phone and made a call.”

[P195]
“A call? To whom?”

[P196]
“I don’t know.”

[P197]
Kim Junsu furrowed his brow.

[P198]
“The call was so short that it didn’t even last three minutes. But more than that, I could tell he was being extremely careful about how he addressed the other person.”

[P199]
“That’s enough. We’ll report it up the chain and have them pull that bastard’s call records.”

[P200]
“Right. Was there anything else?”

[P201]
“Of course there was. Do you know what he said?”

[P202]
Ahem. After clearing his throat, he lowered his voice.

[P203]
“‘The plan is proceeding without a hitch. Yes, yes. The Sangdong Guild hasn’t noticed anything yet. I have the item with me.’”

[P204]
The team members listening slapped their knees.

[P205]
“This is it!”

[P206]
“We finally got something!”

[P207]
“Wow, I just got chills. What is he, some kind of secret agent?”

[P208]
At that moment, Kim Gwondong, who had been listening quietly, suddenly spoke.

[P209]
“Junsu, didn’t that bastard say he had some kind of item?”

[P210]
“Good observation.”

[P211]
Kim Junsu smiled meaningfully.

[P212]
“That guy has a USB.”
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
# Chapter 98

[P2]
Hong Woojin regretted it.

[P3]
*I didn't think this through.*

[P4]
The intrusion itself had gone perfectly. He had approached the target’s cat-loving younger sister and won her heart with a pair of pitiful yet sparkling eyes.

[P5]
The problem was…

[P6]
“What does our Yeoreum eat to be this cute? Hmm? Hmm-hmm?”

[P7]
*Meow.*

[P8]
“Yeoreum, why do you keep trying to get out the door? Stay here and play with your big sis.”

[P9]
*Meow.*

[P10]
“Eek, you’re so cute!”

[P11]
*Hiss! Hissssss!*

[P12]
“Oh no, is Yeoreum mad? I’m sorry. Did Sis touch you too much? Okay, I’ll stay still, so play on the bed, all right?”

[P13]
This damn younger sister had absolutely no intention of letting him outside. Thanks to her, he had spent more than a day and a half trapped in Jin Hayeon’s room.

[P14]
*I should’ve gone with a dog.*

[P15]
If he had been a dog, getting inside wouldn’t have been this easy. But once he was in, he wouldn’t have been practically held captive, either. At the very least, they would have taken him out for walks.

[P16]
*This gets me nowhere.*

[P17]
Swept up by a sense of crisis, Hong Woojin attempted to escape.

[P18]
*Let’s see who wins—you or me!*

[P19]
He had begun with that fierce resolve, but then…

[P20]
Scritch, scritch-scritch-scritch.

[P21]
“…”

[P22]
*Meow. Myaaaaaow.*

[P23]
“…”

[P24]
His first attempt was a failure. He scratched desperately at the door and even tried crying as loudly as he could, but Jin Hayeon didn’t react even once.

[P25]
Without even putting on earphones, she simply continued solving problems with a fierce look in her eyes and swift movements of her hands.

[P26]
*So this is what it means to be in the top 0.01 percent nationwide.*

[P27]
He had seen it in the initial investigation report. Ever since middle school, she had routinely ranked first or second in her entire school and had earned countless awards in various academic competitions. It was hard to forget a record like that.

[P28]
Only today did Hong Woojin understand why.

[P29]
Sitting in front of her desk, she possessed truly terrifying powers of concentration.

[P30]
*Someone like this would make the perfect mage… No, that’s not the point.*

[P31]
He continued trying to disrupt her studies somehow. He pawed at her feet without pause and kept acting cute.

[P32]
But Jin Hayeon’s response was simple.

[P33]
“Big sis is studying right now. Don’t bother me.”

[P34]
She pulled her feet up onto the chair and sat cross-legged, putting them completely out of reach of his tiny body.

[P35]
That was the limit of being a kitten.

[P36]
*This operation has failed.*

[P37]
Since his plan to disrupt her studies had gone up in smoke, he had no choice but to bring out his final card. It would deal a serious blow to his human dignity, but this was no time to be picky.

[P38]
*Let’s see if you ignore this, too.*

[P39]
Sssssssss.

[P40]
The pristine white duvet turned yellow.

[P41]
When nature called, it was best to take care of both kinds of business at once. Having finished both simultaneously, Hong Woojin made a solemn decision.

[P42]
*Fine. Since things have come to this, I might as well take care of it properly. Like a professional.*

[P43]
He rolled over and over.

[P44]
It had been five years since he started using Familiar magic. This was the first time he had ever fallen this far.

[P45]
He kept hypnotizing himself.

[P46]
*I’m a professional. I’m a professional. I’m a professional…*

[P47]
A little while later, Jin Hayeon noticed a strange smell and turned around.

[P48]
By then, everything was over.

[P49]
*Meow.*

[P50]
A duvet stained with urine and feces, and a kitten covered in filth.

[P51]
“Eek, Yeoreum!”

[P52]
Jin Hayeon was startled and moved quickly. She pulled off the dirty duvet, then carefully grabbed the kitten by the scruff of its neck and lifted it up.

[P53]
“What are you doing going to the bathroom here when your litter box is right there? We need to wash our Yeoreum.”

[P54]
*Yes, go to the door! The door!*

[P55]
This was the moment he had been waiting for.

[P56]
Even though he was covered in filth and dangling from the hand of a girl who wasn’t even twenty, Hong Woojin was filled with joy.

[P57]
Click.

[P58]
The door was opening!

[P59]
The living room he hadn’t seen since yesterday came into view!

[P60]
*Meow! Myaaaow!*

[P61]
“That’s strange. Why does it look so happy?”

[P62]
Jin Hayeon tilted her head.

[P63]
That was when the front door opened with the familiar electronic tones of someone entering the passcode.

[P64]
“I’m ho—… What is that?”

[P65]
“Where have you been—… What’s that?”

[P66]
The siblings stared at each other in bewilderment.

[P67]
More precisely, they stared at the creatures in each other’s hands.

[P68]
*Meow.*

[P69]
*Myaow.*

[P70]
The two cats exchanged equally bewildered looks.

[P71]
*That’s Hong Woojin?*

[P72]
*That guy is the Sangdong Guild’s amateur?*

[P73]
And then came the next thought.

[P74]
*Why is he covered in shit from head to toe?*

[P75]
*Ah, fuck.*

[P76]
It was the moment the last shred of Hong Woojin’s human dignity collapsed.

[P77]
* * *

[P78]
“You smeared poop all over the duvet?”

[P79]
“Yeah. I guess he had an accident while I was studying for a bit.”

[P80]
*An accident, my ass.*

[P81]
Since Hayeon had kept him in her room, petting and cuddling him nonstop, he had wracked his brain for a way to get out.

[P82]
*Myaow…*

[P83]
A cat.

[P84]
No, there were two of them now, so I supposed I should call them by their names.

[P85]
Whatever the case, Hayeon asked worriedly at the sound of Yeoreum’s feeble cry.

[P86]
“He’s been looking weak for a while.”

[P87]
“Hmm. That can happen.”

[P88]
I couldn’t say for sure, but his self-loathing had to be something else.

[P89]
He had run into both a fellow professional and his surveillance target while covered in shit.

[P90]
“Don’t worry too much. Cats normally hate getting water on their bodies.”

[P91]
“Is that why? No, he didn’t even resist when I washed him earlier. He was completely docile.”

[P92]
“Oh, really?”

[P93]
“I don’t know if it’s just my imagination, but he seems kind of out of it. Maybe he knows he made a mess and feels sorry?”

[P94]
*Our Yeoreum had a serious case of post-nut clarity.*

[P95]
I swallowed my laughter and said, “Who knows? Anyway, what are you going to do about the duvet? You’ll have to change the sheets, too.”

[P96]
“It’s fine. It was an animal, not a person. What’s the big deal?”

[P97]
They say a frog can die from a stone thrown without a second thought.

[P98]
That was exactly what had happened here. Hayeon’s offhand remark turned into a blade and lodged itself in someone’s chest.

[P99]
The kitten trembled violently in silence, unable to even cry out.

[P100]
Meanwhile, the other one was having a wonderful time.

[P101]
*Purr. Prrrr.*

[P102]
Hayeon gazed at the black cat with a face full of adoration as it repeatedly rubbed its face against my leg, making happy noises.

[P103]
“Where did you bring him from?”

[P104]
“The entrance to the apartment complex.”

[P105]
“Is he a stray?”

[P106]
“I guess so. He was alone.”

[P107]
“What? Then he might have a mother. You’re supposed to watch a kitten for about a day before bringing it home.”

[P108]
“Some man told me he’d been crying alone since yesterday.”

[P109]
“Oh, then he doesn’t have a mother.”

[P110]
The black cat flinched.

[P111]
Its purring and attempts to act cute stopped dead. Without realizing it, Hayeon had scored two kills, and she smiled brightly.

[P112]
“There, there. You don’t have a mother, either. It’s okay. From today onward, Sis will be your mommy.”

[P113]
“…”

[P114]
For my little sister, she certainly had a talent for screwing people over with a smile.

[P115]
The black cat seemed torn between professional duty and the cheap shot at his mom, but soon accepted reality.

[P116]
*Meow.*

[P117]
The sight of it acting cute for its mother’s enemy was downright pitiful.

[P118]
*That’s the hardship of being a working stiff.*

[P119]
Watching them, I suddenly thought of Mom.

[P120]
“Where’s Mom?”

[P121]
“I don’t know. She went out because she had an important appointment.”

[P122]
“An appointment?”

[P123]
“Yeah. She’s been going out a lot lately.”

[P124]
*What’s going on?*

[P125]
Mom had been leaving the house frequently these days. Now that she had some free time after quitting her job, was she finally looking for a life of her own?

[P126]
*Come to think of it, she had been acting strange.*

[P127]
Sometimes she would sit there with an expression that looked as though she had something to say. Other times, she would jump whenever I suddenly spoke to her.

[P128]
Something had definitely changed around Mom.

[P129]
*She’ll tell me when the time is right.*

[P130]
The person I loved and trusted most in this world was my mother. Just as always, all I could do was trust her and wait.

[P131]
Of course, listening to her and talking things over at the right time was also a child’s duty.

[P132]
“What are you thinking about so hard?”

[P133]
“It’s nothing. By the way, aren’t you going out?”

[P134]
“What, you sound like you want me to leave.”

[P135]
“Not exactly.”

[P136]
“Hmm. Suspicious. You’re not planning to bring a girlfriend over, are you?”

[P137]
“…”

[P138]
*I wish I had a girlfriend to bring over.*

[P139]
My expression must have revealed my thoughts, because Hayeon hesitated.

[P140]
“Ah, I’m sorry.”

[P141]
“Don’t apologize. It makes me twice as pathetic.”

[P142]
“I’m really sorry.”

[P143]
“You’re doing this on purpose, aren’t you?”

[P144]
“Come to think of it, I have some books to return to the library.”

[P145]
She sprinted into her room, threw on her backpack, and came back out at the speed of light.

[P146]
The front door slammed shut, and the house fell silent.

[P147]
*She really went and gouged out a single man’s heart.*

[P148]
A corner of my chest felt hollow, but the stage I had been waiting for had finally been set.

[P149]
This was a problem I needed to deal with while my family was out of the house, if possible.

[P150]
*Myaow.*

[P151]
*Meow.*

[P152]
Two cats, one black and one white, began creeping toward me and circling around.

[P153]
Bright eyes. Perked-up ears.

[P154]
I left the Familiars, who were dying to learn more about me, behind and stepped onto the balcony.

[P155]
The first thing I saw was the parking lot, where hundreds of cars were lined up.

[P156]
*The parking lot is clear.*

[P157]
Before returning home, I had carried the Familiar in my arms and taken a lap around the apartment complex. To everyone else, I probably looked like an idler out for a walk on a pleasant day.

[P158]
My real purpose had been to check the vehicles.

[P159]
The result was nothing suspicious.

[P160]
*Then it has to be one of those houses.*

[P161]
That confirmed the watchers had made one of the recently traded apartments their base. I recalled the information I had obtained from the real-estate office once more.

[P162]
*Building 5, Unit 901. Building 4, Unit 302. Building 3, Unit 202.*

[P163]
Coincidentally, all three were positioned around our apartment, forming a sort of ring. They were ideal for surveillance, since their windows offered a view of the entrances to the buildings.

[P164]
It wouldn’t be strange for the watchers to be in any one of them.

[P165]
*The question is which one they’re hiding in…*

[P166]
They were cautious enough to use a Familiar instead of magical Equipment to avoid being discovered.

[P167]
If I approached recklessly, I would lose them. To make a definite capture, I had no choice but to throw out equally substantial bait.

[P168]
*I think it’s time to begin.*

[P169]
Swish. Rustle.

[P170]
First, I drew all the curtains in the house. Even though it was the middle of the day, the living room had grown dim. I reached into my pocket.

[P171]
*Inventory open. Mana-detection Equipment.*

[P172]
At the same time, my hand closed around a lump of metal about half the size of my palm.

[P173]
As its name suggested, it was Equipment that could detect mana. I had paid twenty million won for it at the Store.

[P174]
*Next step: search.*

[P175]
I carefully swept through the house with the detection Equipment. After confirming that no mana was being detected inside, I took out my smartphone and called someone.

[P176]
Beep. Beep. Click.

[P177]
The other person answered as the call connected.

[P178]
—Hello?

[P179]
I replied.

[P180]
“It’s me, Jin Taekyung.”

[P181]
The two Familiars watched me without even seeming to breathe.

[P182]
* * *

[P183]
The moment Kim Junsu opened his eyes, he shouted.

[P184]
“He’s here! He’s here!”

[P185]
The Security Team members, who had been sitting close together and writing their assessments, jumped in surprise.

[P186]
“What?”

[P187]
“Who’s here? Our Team Leader?”

[P188]
“Or could it be…”

[P189]
Kim Junsu nodded at the team member who had let his voice trail off.

[P190]
“The target. This guy reeks to high heaven.”

[P191]
“Seriously?”

[P192]
“Yes. I got a bad feeling when he drew all the curtains as soon as the house was empty, and then he even used detection Equipment to inspect the inside.”

[P193]
That wasn’t something an ordinary C-rank Hunter, especially one on vacation, would do.

[P194]
Everyone in the room swallowed hard.

[P195]
“Th-then?”

[P196]
“He pulled out his phone and made a call.”

[P197]
“A call? To whom?”

[P198]
“I don’t know.”

[P199]
Kim Junsu furrowed his brow.

[P200]
“The call was so short that it didn’t even last three minutes. But more than that, I could tell he was being extremely careful about how he addressed the other person.”

[P201]
“That’s enough. We’ll report it up the chain and pull that bastard’s call records.”

[P202]
“Right. And there was nothing else?”

[P203]
“How could there be nothing else? Do you know what he said?”

[P204]
He cleared his throat once. Then a low voice came from his mouth.

[P205]
“‘The plan is proceeding without a hitch. Yes, yes. The Sangdong Guild hasn’t noticed anything yet. I have the item with me.’”

[P206]
The team members listening slapped their knees.

[P207]
“This is it!”

[P208]
“We finally got something!”

[P209]
“Wow, I just got chills. What is he, some kind of secret agent?”

[P210]
At that moment, Kim Gwondong, who had been listening quietly, suddenly spoke.

[P211]
“Junsu, didn’t that bastard say he had an item?”

[P212]
“Good observation.”

[P213]
Kim Junsu smiled meaningfully.

[P214]
“That guy has a USB.”
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 진태경    | **Jin Taekyung**   |
| 진하연    | **Jin Hayeon**    |
| 홍우진    | **Hong Woojin**   |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 귀가      | **your family**                                                 |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 98,
  "passed": true,
  "metrics": {
    "source_characters": 5898,
    "translation_characters": 12931,
    "length_ratio": 2.192,
    "source_paragraphs": 200,
    "translation_paragraphs": 212
  },
  "errors": [],
  "warnings": [
    {
      "code": "numbers",
      "message": "Arabic numerals from the source are absent",
      "details": {
        "values": [
          "1"
        ]
      }
    },
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
        "korean": "진태",
        "preferred": "Jintae"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "기감",
        "preferred": "Qi Sense"
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
        "korean": "전하",
        "preferred": "His Highness"
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
