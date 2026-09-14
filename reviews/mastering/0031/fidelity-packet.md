# Fidelity Gate — Chapter 31

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
  1|＃31화
  2|
  3|
  4|
  5|“어쭈. 이 자식은 팔자도 좋네.”
  6|
  7|슬며시 눈을 뜨자 익숙한 얼굴이 보인다.
  8|
  9|“소풍 왔냐? 게이트에서 잠을 자?”
 10|
 11|깜빡 졸았던 모양이다. 나는 뻔뻔한 얼굴로 대꾸했다.
 12|
 13|“안 잤어요. 자긴 누가 잤다고 그래.”
 14|
 15|“입가에 침 자국이나 닦고 구라를 쳐라.”
 16|
 17|“씁.”
 18|
 19|“어이고, 이걸 확.”
 20|
 21|주먹을 흔들어 보였지만 입가에는 웃음이 맺혀 있다. 나는 뻐근한 목을 주물렀다.
 22|
 23|“어우, 피곤해.”
 24|
 25|“어제 여자라도 만났냐. 왜 레이드 뛰면서까지 병든 닭처럼 꾸벅꾸벅 졸아?”
 26|
 27|“제가 여자 만날 시간이 어디 있어요. 사정 뻔히 아시면서.”
 28|
 29|“그렇긴 하지.”
 30|
 31|첫 전투 때부터 지금까지, 5년이나 동고동락한 처지다. 내가 그를 잘 아는 것처럼 그도 나를 잘 알았다.
 32|
 33|“그럼 왜 그러는데?”
 34|
 35|“왜 그러겠습니까. 돈 때문이지.”
 36|
 37|“돈? 설마 너 투잡 뛰냐?”
 38|
 39|한껏 낮아진 목소리다. 나는 그의 등 너머로 휴식을 취하고 있는 팀원들을 바라보며 고개를 끄덕였다.
 40|
 41|“와, 이 자식 이거. 짬밥 좀 먹었다고 뒷주머니를 차네. 그것도 부팀장이라는 놈이.”
 42|
 43|“요즘 레이드도 줄었고, 급해서 그래요. 급해서. 형님도 다 해 봤으면서 그러시네.”
 44|
 45|프로 라이센스를 가진 헌터는 투잡이 법적으로 금지되어 있다. D급만 되어도 이렇게 살지는 않을 텐데, 우리 같은 F급들은 별수 없다. 그런 사정을 알기 때문에 길드에서 알아도 모른 척 넘어가는 거지.
 46|
 47|“그렇긴 한데…… 조심해라. 관리청에 민원이라도 들어오면 골치 아파져.”
 48|
 49|“믿을 만한 곳이에요. 페이도 당일 현찰로 받아서 문제없고. 제가 괜히 하겠습니까.”
 50|
 51|“그래?”
 52|
 53|표정을 보아하니 구미가 당기는 모양이다.
 54|
 55|“형님도 돈 필요하세요?”
 56|
 57|“애가 셋이다. 마당에 유전이라도 터져야 해.”
 58|
 59|그는 슬픈 눈으로 말을 쏟아 냈다. 이미 수십 번 들었던 레퍼토리다. 육아의 괴로움과 분유값 상승, 장사치들의 파렴치함에 대해 울분을 토해 낸 뒤 내 어깨를 두드렸다.
 60|
 61|“넌 결혼하지 마라.”
 62|
 63|“안 해요.”
 64|
 65|정확히는 못 하는 거지만.
 66|
 67|여자도 없고, 돈도 없다. 5년 내로 안전 구역의 집을 한 채 사는 게 인생의 목표인 나로서는 내심 그가 부러웠다.
 68|
 69|사랑하는 배우자와 아이들. 행복한 가정. 그런 걸 언제쯤 가질 수 있을지 모르겠다.
 70|
 71|“결혼은 늪이야.”
 72|
 73|말은 저렇게 해도 소문난 애처가에 좋은 아빠다. 가끔 가족사진을 꺼내 보면서 흐뭇하게 웃는 것을 나는 알고 있었다.
 74|
 75|“인생이 빨려 들어가. 정신 차려 보면 가슴까지 파묻혀서 간신히 숨만 쉬고 있다니까.”
 76|
 77|“…….”
 78|
 79|잘못 알고 있었을 수도 있겠다.
 80|
 81|“그러니까 너무 일만 하지 말고 쉬면서 해, 쉬면서. 연애, 취미 생활 이런 거 좋잖아.”
 82|
 83|“글쎄요. 아직은 돈이 급해서.”
 84|
 85|머리를 긁적이며 대답했다. 그가 안쓰러운 눈으로 바라본다.
 86|
 87|“아까 보니까 식은땀까지 흘려 가면서 자던데. 그러다가 과로로 훅 간다.”
 88|
 89|“제가요?”
 90|
 91|그러고 보니 등허리가 식은땀으로 축축하다. 뭔가 안 좋은 꿈을 꾼 모양인데…….
 92|
 93|‘기억이 안 나네.’
 94|
 95|보나 마나 개꿈이겠지, 뭐.
 96|
 97|
 98|
 99|* * *
100|
101|
102|
103|게이트(Gate).
104|
105|지금이야 나 같은 헌터들의 밥줄 역할을 하고 있지만 그 실체는 마계 군단의 침공 루트다.
106|
107|마왕 아스모데우스가 쓰러지면서 그의 강대한 군대도 패퇴했지만 수십 년이 지난 지금도 게이트만은 남아 있었다.
108|
109|“수비 대형!”
110|
111|그의 지휘에 따라 거대한 타워 실드를 짊어진 헌터 셋이 전방을 막았다. 길이 좁은 동굴에서는 이 정도만으로 대부분의 공격을 해소할 수 있다.
112|
113|캉. 카캉!
114|
115|“끼이이익!”
116|
117|이십여 마리의 고블린이 독침과 도끼, 창을 투척했지만 크고 아름다운 타워 실드에 모두 튕겨 나갔다.
118|
119|“궁수!”
120|
121|전방에서는 탱커가 모든 공격을 막아 내고, 후방에서는 궁수가 화살을 쏟아 낸다. 전진 압박을 가하며 절반가량을 쓰러트리자 고블린들이 당황한 울음을 토해 냈다.
122|
123|“까아아악!”
124|
125|“끼익!”
126|
127|때에 맞춰 그가 명령했다.
128|
129|“공격 대형!”
130|
131|탱커들이 타워 실드를 떨어트리는 동시에 뛰쳐나간다. 하지만 그보다 내가 더 빨랐다.
132|
133|“핫!”
134|
135|철창을 크게 휘두르자 초록색 피가 터지며 선두가 흐트러진다. 그 사이로 뛰어들며 닥치는 대로 찌르고 베자 대열이 우르르 무너져 내렸다.
136|
137|“돌격!”
138|
139|이어 딜러와 탱커들이 가세하자 고블린 무리는 순식간에 시체가 되어 누웠다.
140|
141|“오늘 되게 쉬운데?”
142|
143|“솔직히 부팀장이 반은 했지. 아주 날아다니던데, 언제 저렇게 실력이 좋아졌…… 쉿. 팀장님 열받았다.”
144|
145|잡담을 나누던 사람들은 그가 나타난 순간 입을 다물었다.
146|
147|“야, 진태경!”
148|
149|깜짝이야.
150|
151|멍하니 생각에 빠져 있던 나는 화들짝 놀라 반문했다.
152|
153|“왜요?”
154|
155|“너 인마, 누가 단독 행동 하래? 네가 탱커야? 공격 순서 다 잊었어? 그러고도 네가 부팀장이야?”
156|
157|“그게 아니라요…….”
158|
159|“이따위로 할 거면 팀 옮겨. 다른 팀원들까지 위험해지니까.”
160|
161|그의 험악한 얼굴을 보다가 한숨을 내쉬었다.
162|
163|“죄송합니다. 제가 왜 그랬는지 모르겠어요. 그냥, 갑자기 별것 아닌 것 같더라고요. 잠깐 미쳤나 봐요.”
164|
165|기분이 묘했다. 고블린 무리를 보는 순간, 혼자서 저놈들을 쓸어버릴 수 있다는 생각이 들었다. 아니, 그건 확신이었다.
166|
167|“너…….”
168|
169|그가 말을 삼켰다. 서로 등을 맡기고 싸워 온 지 어언 5년, 지금 같은 돌발 행동은 이번이 처음이었다.
170|
171|“다음부턴 이러지 마라. 힘든 일 있으면 말하고.”
172|
173|어깨를 두드리고 떠나는 그의 뒷모습을 바라봤다. 왠지 모르게 가슴 한구석이 욱신거렸다.
174|
175|‘병원이라도 가 봐야 하나.’
176|
177|하지만 통증 따위는 이내 신경도 쓰지 않게 되었다.
178|
179|
180|
181|* * *
182|
183|
184|
185|“마정석 나왔습니다!”
186|
187|“나왔어요!”
188|
189|“또!”
190|
191|“떴다. 떴다. 떴다!”
192|
193|“엄마! 하연아!”
194|
195|아, 마지막 외침은 내가 한 거다. 그도 잔뜩 달아오른 얼굴로 중얼거린다.
196|
197|“야, 이게 다 뭐냐…….”
198|
199|바닥에는 크고 작은 스무 개의 마정석이 가지런히 놓여 있었다.
200|
201|마정석. 겉보기에는 붉은 돌멩이지만 게이트의 꽃이라 불리는 물건이다. 몬스터가 지닌 이 마력 덩어리는 고차원 에너지인 동시에 몬스터의 부산물 중 가장 값진 거다.
202|
203|“이 정도면 개당 백만 원은 넘겠는데.”
204|
205|E급 헌터로 이 바닥에서 10년을 버틴 팀장의 말이다. 그 황홀한 광경에 사람들의 눈동자가 스르르 풀어졌다.
206|
207|“원래 이런 건가요?”
208|
209|신입의 질문에 모두가 맹렬히 고개를 흔들었다.
210|
211|“절대 아니지.”
212|
213|F급 게이트에서는 평균이 한두 개고 아무리 운이 좋아도 다섯 개를 못 채운다. 나는 돈 계산에 바빴다.
214|
215|‘마정석만 최소 이천 잡고, 부산물에 장비까지 하면 오백. 거기에 각종 수당까지 더하면…….’
216|
217|시발. 이게 다 얼마야. 헌터를 시작한 이래 최고의 대박이다.
218|
219|심지어 아직 레이드가 끝난 것도 아니다.
220|
221|“우리가 지금 얼마쯤 왔지?”
222|
223|“거의 다 왔죠. 오른쪽 길로 꺾으면 바로 보스 존이에요.”
224|
225|보스 존. 그 단어에 모두의 눈이 번쩍였다.
226|
227|당연한 말이지만, 보스 존에는 보스가 있다. 보스 몬스터는 해당 게이트에서 가장 강력한 몬스터. 그리고 가장 비싼 부산물과 장비, 마정석을 갖고 있는 몬스터다.
228|
229|‘보스 몬스터까지 잡으면?’
230|
231|말 그대로 잭팟이다. F급 헌터로 살아가면서 다시없을 절호의 기회인 것이다. 모두가 그런 생각으로 환하게 웃고 있던 그때였다.
232|
233|“잠깐. 생각 좀 해 보고.”
234|
235|아니, 이 인간이 지금 뭐라는 거야?
236|
237|“그게 무슨 말이에요?”
238|
239|“그렇잖아. 마주치는 몬스터는 일반 고블린뿐인데. 마정석이 이렇게 많이? 아무래도 이상해.”
240|
241|그가 한숨을 내쉬었다. 아직도 흥분이 채 가라앉지 않아 붉은 얼굴에는 갈등이 떠올라 있었다.
242|
243|“너희 기분 알아. 아는데…… 이미 엄청나게 챙겼다. 이 정도에서 만족하고 돌아가자.”
244|
245|만족? 지금 여기서, 여기까지 와서 돌아가자고?
246|
247|나는 다른 팀원들을 바라봤다. 그중에는 2, 3년간 손발을 맞춘 이들도 있고, 신입도 있다. 하지만 다들 나와 같은 얼굴을 하고 있었다.
248|
249|“저는 반대…….”
250|
251|그 순간 숨이 턱 막혔다. 빌어먹을. 또 가슴 통증이다.
252|
253|어떻게든 말을 이으려고 했지만 목소리가 나오지 않았다. 이제는 이명까지 들리기 시작한다.
254|
255|‘이게 무슨.’
256|
257|통증도, 이명도 점점 심해지고 있었다. 나는 무릎을 꿇고 숨을 헐떡였다.
258|
259|‘누가 나 좀. 나 좀 도와줘.’
260|
261|누군가의 바짓가랑이를 붙잡고 매달렸다. 바로 그다. 지난 5년간 형제처럼, 아버지처럼 나를 돌봐 준 그였다.
262|
263|‘형. 제발 저 좀 살려 줘요.’
264|
265|그가 덤덤한 시선으로 날 내려다봤다.
266|
267|“내가? 모두를 두고 도망친 너를?”
268|
269|뭐?
270|
271|“나도 살고 싶었어.”
272|
273|나는 통증도 잊고 멍하니 그를 바라봤다. 옷과 피부가 녹아내리고 뼈가 드러났다. 나를 제외한 모두가 해골이 되어 널브러졌다.
274|
275|‘아. 그랬었지.’
276|
277|모두 죽었다. 2년 전 그날. 내가 가자고 주장했던 그 보스 존에서 모두가 죽었다.
278|
279|‘나 혼자 살아남았어.’
280|
281|나는 기억에 파묻혀 허우적거렸다. 보스 존에 내려앉은 불길한 어둠. 불쾌한 냄새와 축축한 바닥을 떠올렸고 놈의 거대한 날개를 기억했다.
282|
283|허공에서 갈기갈기 찢겨 나가는 시신. 공포에 질린 비명과 도망치는 사람들.
284|
285|
286|
287|‘이런 개새끼가!’
288|
289|
290|
291|하지만 내 모든 걸 쏟아부은 스킬로도 놈을 죽일 수 없었다. 죽음을 기다리고 있던 나를 그가 일으켜 세웠다.
292|
293|
294|
295|‘태경아!’
296|
297|‘형, 미안해요. 전부 제 잘못이에요.’
298|
299|
300|
301|나만 아니었으면. 내가 욕심을 부리지 않았다면 모두가 살 수 있었을 텐데. 가족에게 돌아갈 수 있었을 텐데.
302|
303|어린애처럼 엉엉 우는 내게 그는 애써 미소를 지어 보였다.
304|
305|
306|
307|‘그게 왜 네 책임이야? 자식이 이제는 팀장 흉내까지 내고 있어.’
308|
309|
310|
311|거대한 동체가 동굴을 부유했다. 종유석이 쏟아지고 마지막 팀원이 단말마를 내질렀다. 어둠 속, 놈의 붉은 눈동자가 우리를 향했다.
312|
313|
314|
315|‘저 건방진 새끼. 태경아. 먼저 가라.’
316|
317|‘형. 천수 형!’
318|
319|
320|
321|가슴이 아팠다. 눈앞이 아득해질 정도의 고통이 밀려들어 왔다. 용암을 삼킨 것처럼, 내 안의 모든 것들이 타들어 가는 것 같았다. 간간이 들리던 이명은 괴물의 포효로 바뀌었다.
322|
323|캬우우우!
324|
325|
326|
327|* * *
328|
329|
330|
331|“형-!”
332|
333|비명과 함께 눈을 떴다. 하지만 그곳은 게이트가 아니었고 몬스터도, 팀원들도 없었다. 햇빛이 쏟아지는 창가에서 한 사람이 일어났다.
334|
335|“주군에 관한 꿈을 꾸신 겁니까? 전해 드리면 좋아하시겠군요.”
336|
337|차가움이 뚝뚝 묻어 나오는 얼굴. 진위경의 오른팔인 위팽이다. 그를 보자 아직 게임 속이라는 것이 실감이 났다.
338|
339|“괜찮으십니까?”
340|
341|“아뇨. 악몽이었어요.”
342|
343|“그럼 그 부분은 빼고 전하겠습니다.”
344|
345|“마음대로.”
346|
347|땀으로 온몸이 흠뻑 젖어 있었다. 온몸에 칭칭 감긴 붕대 틈새로 피딱지가 돋은 살이 보인다.
348|
349|“제가 얼마나 누워 있었죠?”
350|
351|“닷새 동안 혼절해 계셨습니다. 상태가 워낙 위중해서 하루를 못 넘길 거라는 게 약왕당주의 결론이었고요.”
352|
353|“그래요?”
354|
355|“예. 그 얘기를 들은 주군께서 길길이 날뛰셨죠. 제가 안 말렸으면 약왕당주를 때려죽였을 겁니다.”
356|
357|“아.”
358|
359|며칠 전 회의 때 백호당주의 항문에 대침을 꽂아 넣겠다고 하던 늙은이가 생각났다. 아주 죽으라고 염불을 외웠구나.
360|
361|“다른 일들은 없었나요?”
362|
363|“많은 일이 있었죠. 그중에서도 좋은 소식과 더 좋은 소식이 있는데…… 어느 것부터 들으시겠습니까?”
364|
365|“좋은 소식부터.”
366|
367|“우선 정찰조와 삭주 지부의 생존자들은 무사히 복귀했습니다. 그중 두 명은 제법 큰 부상을 입긴 했지만 목숨에는 지장이 없을 겁니다.”
368|
369|생존자. 그 세 글자에 가슴이 덜컥 내려앉는다.
370|
371|‘칠 호.’
372|
373|목과 미간에 비수가 박힌 채 마지막 숨을 토하던 그 얼굴이 떠올랐다. 기껏해야 스물이나 되었을까. 목숨을 잃기에는 너무 어린 나이였다.
374|
375|“죽은 이를 생각하십니까?”
376|
377|“시신은, 시신은 수습했나요?”
378|
379|“잘 수습하여 장사 지냈습니다. 천애 고아인지라 유족이 없더군요.”
380|
381|“…….”
382|
383|“한 말씀 드려도 되겠습니까?”
384|
385|위팽은 대답을 기다리지 않았다. 그가 나를 향해 한발 다가오며 입을 열었다.
386|
387|“삼공자, 수하의 죽음을 개죽음으로 만들지 마십시오.”
388|
389|“그게 무슨…….”
390|
391|“무인은 보호받는 존재가 아니라 적과 싸워 스스로를 증명하는 자들입니다. 비록 손쓸 수 없을 만큼 강한 적을 만나 죽었지만, 사망(死亡)이 아닌 전사(戰事)라는 말입니다.”
392|
393|전장에서 죽었으니 영예로운 죽음이라는 말은 희대의 개소리다. 영예로운 죽음은 없다. 지금도 2년 전 죽은 동료들의 비명과 숨이 끊긴 칠 호의 부릅뜬 눈이 생생하다.
394|
395|“죽었다는 사실은 변하지 않아요.”
396|
397|“결코 변하지 않는 사실에 집착하는 사람도 있더군요. 누구라고는 말하지 않겠습니다.”
398|
399|“…….”
400|
401|“후회됩니까?”
402|
403|“당연히.”
404|
405|“그럼 그의 몫까지 사십시오.”
406|
407|위팽이 이제껏 들어 본 적 없는 부드러운 목소리로 말을 이었다.
408|
409|“죽은 이들을 잊으라는 말이 아닙니다. 가슴에 묻고, 머리에 새기라는 뜻입니다. 그 후회를 발판 삼아 그들이 꿈꿨던 곳까지 비상하는 것이 공자가 가야 할 길입니다.”
410|
411|내가 가야 할 길이라…….
412|
413|듣는 것만으로도 가슴 한구석이 울렁거리는 그 한마디를 곰곰이 생각하다가 풀썩 웃어 버렸다.
414|
415|“젠장. 가다가 다리 부러지겠네.”
416|
417|“일평생이 걸리겠죠.”
418|
419|“일평생을 바치면 도착할 수 있을까요?”
420|
421|“모릅니다. 저도 제 길이 어디까지인지 모르는데 공자의 길을 어찌 알겠습니까.”
422|
423|“위 대협이 가는 길 끝에는 뭐가 있는데요?”
424|
425|“천하제일인(天下第一人).”
426|
427|농담? 아니다. 지금의 위팽은 그 어느 때보다 진지하고, 단호했다.
428|
429|“어렵네요.”
430|
431|“꿈이니까요.”
432|
433|맞다. 꿈이란 늘 이루기 어렵다. 떠나보낸 이들의 꿈까지 짊어진다면 더더욱.
434|
435|“위 대협. 한 가지만 물어봐도 될까요?”
436|
437|“얼마든지요.”
438|
439|“그 녀석, 이름이 뭐였습니까?”
440|
441|“그의 이름은…….”
442|
443|위팽의 입술이 열린 순간, 겨울 찬바람이 창문을 흔들었다.
444|
445|휘이잉. 서늘한 바람 소리 너머로 칠 호의 이름이 들려온다.
446|
447|“멋진 이름이네요.”
448|
449|“본인이 직접 지었다고 들었습니다. 그만큼 꿈도 컸죠.”
450|
451|“뭔데요?”
452|
453|“고금제일인(古今第一人).”
454|
455|“…….”
456|
457|“고생 좀 하실 겁니다.”
458|
459|“그러게요. 어이가 없네.”
460|
461|실소가 터져 나온다. 그제야 무거웠던 마음이 홀가분해진 것이 느껴졌다. 모두 위팽 덕분이다.
462|
463|“이제야 좀 원래대로 돌아왔군요.”
464|
465|“고맙습니다.”
466|
467|“별말씀을.”
468|
469|고개를 까딱인 위팽이 입을 열었다.
470|
471|“이제 더 좋은 소식이 남았군요.”
472|
473|아, 그랬지. 좋은 소식과 더 좋은 소식.
474|
475|나는 한껏 기대하며 이어질 말을 기다렸다.
```

## Assembled English

```markdown
[P1]
# Chapter 31

[P2]
“Well, look at you. This bastard’s got it made.”

[P3]
I slowly opened my eyes to a familiar face.

[P4]
“Did you come here for a picnic? Sleeping in a Gate?”

[P5]
I must have dozed off. I answered with a shameless look.

[P6]
“I wasn’t sleeping. Who says I was?”

[P7]
“Wipe the drool off your mouth before you start lying.”

[P8]
“Slurp.”

[P9]
“Oh, you little—”

[P10]
He shook a fist at me, but a smile tugged at the corners of his mouth. I rubbed my stiff neck.

[P11]
“Ugh, I’m tired.”

[P12]
“Did you meet a woman yesterday? Why are you nodding off like a sick chicken even in the middle of a raid?”

[P13]
“When would I have time to meet a woman? You know my situation.”

[P14]
“True enough.”

[P15]
We’d been through thick and thin together for five years, ever since our first battle. He knew me as well as I knew him.

[P16]
“Then what’s wrong?”

[P17]
“What do you think? Money.”

[P18]
“Money? Don’t tell me you’re moonlighting.”

[P19]
His voice dropped low. I looked past his shoulder at the team members resting nearby and nodded.

[P20]
“Well, well. This bastard gets a little experience under his belt and starts lining his own pockets. And he’s the vice team leader, no less.”

[P21]
“Raids have been scarce lately, and I’m strapped. Really strapped. You’ve done it yourself, hyung, so don’t give me that.”

[P22]
Hunters with professional licenses were legally barred from second jobs. Even a D-rank probably wouldn’t have to live like this, but F-ranks like us had no choice. That was why the Guild looked the other way even when they knew.

[P23]
“True, but… be careful. If someone files a complaint with the Management Agency, you’ll have a real headache on your hands.”

[P24]
“It’s a trustworthy place. They pay cash the same day, so there’s no problem. You think I’d do it if it weren’t safe?”

[P25]
“Really?”

[P26]
Judging by his face, he was tempted.

[P27]
“Do you need money too, hyung?”

[P28]
“I’ve got three kids. I’d need an oil well to blow in the yard.”

[P29]
He poured it out with sad eyes. I’d already heard this routine dozens of times. After venting about the misery of raising kids, the rising price of formula, and the shamelessness of merchants, he patted my shoulder.

[P30]
“Don’t get married.”

[P31]
“I won’t.”

[P32]
More precisely, I couldn’t.

[P33]
I had no woman and no money. My life’s goal was to buy a house in a safe zone within five years, so deep down I envied him.

[P34]
A spouse I loved, and children. A happy family. I had no idea when I’d ever have something like that.

[P35]
“Marriage is a swamp.”

[P36]
For all that talk, he had a reputation as a devoted husband and a good father. I knew how he sometimes took out his family photos and smiled fondly at them.

[P37]
“It sucks your whole life in. By the time you come to your senses, you’re buried up to your chest and can barely breathe.”

[P38]
“…”

[P39]
Maybe I’d been wrong about him.

[P40]
“So don’t just work. Take breaks. Dating, hobbies—stuff like that’s good for you.”

[P41]
“I don’t know. I still need the money.”

[P42]
I scratched my head as I answered. He looked at me with pity.

[P43]
“I saw you sleeping earlier. You were even breaking out in a cold sweat. Keep that up and you’ll drop dead from overwork.”

[P44]
“Was I?”

[P45]
Now that he mentioned it, my back was damp with cold sweat. I must have had a bad dream…

[P46]
*Can’t remember.*

[P47]
Probably just some stupid dream anyway.

[P48]
* * *

[P49]
A Gate.

[P50]
These days it was how Hunters like me made a living, but its true nature was an invasion route for the Demon Realm’s army.

[P51]
When Demon King Asmodeus fell, his mighty army was routed with him. Yet even decades later, the Gates remained.

[P52]
“Defensive formation!”

[P53]
At his command, three Hunters bearing huge tower shields blocked the front. In a narrow cave, that alone was enough to soak most attacks.

[P54]
*Clang! Clang-clang!*

[P55]
“Giiiiik!”

[P56]
About twenty goblins hurled poison needles, axes, and spears, but every one of them bounced off those big, beautiful tower shields.

[P57]
“Archers!”

[P58]
The tanks blocked every attack from the front while the archers rained arrows from the rear. We pressed forward and took down about half the goblins, drawing panicked shrieks from the rest.

[P59]
“Gyaaaah!”

[P60]
“Kieek!”

[P61]
He gave the next order at just the right moment.

[P62]
“Attack formation!”

[P63]
The tanks dropped their tower shields and burst forward at the same time. I was faster.

[P64]
“Hah!”

[P65]
I swung my iron spear in a wide arc. Green blood burst through the air, and the front rank broke apart. I plunged into the gap, stabbing and slashing at anything within reach, and their entire formation collapsed.

[P66]
“Charge!”

[P67]
The damage dealers and tanks joined in, and the goblin pack became a heap of corpses in the blink of an eye.

[P68]
“Pretty easy today, huh?”

[P69]
“Honestly, the vice team leader did half the work. He was flying around out there. When did he get that good…? Shh. The Team Leader’s pissed.”

[P70]
The people chatting shut their mouths the moment he appeared.

[P71]
“Hey, Jin Taekyung!”

[P72]
That made me jump.

[P73]
I’d been staring blankly, lost in thought, and I startled as I answered.

[P74]
“What?”

[P75]
“Who told you to go off on your own? Are you a tank? Did you forget the attack order? And you still call yourself the vice team leader?”

[P76]
“That’s not—”

[P77]
“If you’re going to act like this, transfer teams. You’re putting everyone else in danger too.”

[P78]
I looked at his grim face and sighed.

[P79]
“I’m sorry. I don’t know why I did that. They just… suddenly didn’t seem like a big deal. I must have lost it for a second.”

[P80]
It was a strange feeling. The moment I saw the pack of goblins, I’d thought I could wipe them out by myself.

[P81]
No, it hadn’t been a thought.

[P82]
It had been certainty.

[P83]
“You…”

[P84]
He swallowed the rest of his words. We’d had each other’s backs for five years now, and this was the first time I’d ever pulled something like this.

[P85]
“Don’t do it again. If you’re having a hard time, tell me.”

[P86]
I watched him walk away after patting my shoulder. For some reason, a spot in my chest throbbed.

[P87]
*Should I see a doctor?*

[P88]
But before long I wasn’t even thinking about the pain.

[P89]
* * *

[P90]
“Magic Gem!”

[P91]
“Got one!”

[P92]
“Another!”

[P93]
“It dropped! It dropped! It dropped!”

[P94]
“Mom! Hayeon!”

[P95]
Ah, that last shout was mine. His face was flushed too as he muttered.

[P96]
“Hey, what is all this…?”

[P97]
Twenty Magic Gems, large and small, lay neatly on the floor.

[P98]
Magic Gems. They looked like red pebbles, but they were called the flower of the Gate. These lumps of mana that monsters carried were high-dimensional energy, and the most valuable byproduct a monster had.

[P99]
“At this rate, each one’s got to be worth over a million won.”

[P100]
That came from the Team Leader, an E-rank Hunter who’d lasted ten years in this business. People’s eyes went slack at the intoxicating sight.

[P101]
“Is it normally like this?”

[P102]
At the new recruit’s question, everyone shook their heads vigorously.

[P103]
“Absolutely not.”

[P104]
In an F-rank Gate the average was one or two, and even with incredible luck you wouldn’t hit five.

[P105]
I was busy doing the math.

[P106]
*At least twenty million from the Magic Gems alone, another five million from the byproducts and Equipment. Add all the various allowances and…*

[P107]
*Fuck. How much is this?*

[P108]
It was the biggest jackpot I’d hit since becoming a Hunter.

[P109]
And the raid wasn’t even over yet.

[P110]
“How far have we come?”

[P111]
“Almost there. Turn right and the boss zone’s just ahead.”

[P112]
The words *boss zone* made everyone’s eyes light up.

[P113]
It went without saying, but a boss zone had a boss. A boss monster was the strongest monster in that Gate—and the one with the most expensive byproducts, Equipment, and Magic Gems.

[P114]
*What if we take down the boss monster too?*

[P115]
A literal jackpot. A once-in-a-lifetime chance for an F-rank Hunter.

[P116]
Everyone was smiling brightly at the thought when he spoke.

[P117]
“Wait. Let me think.”

[P118]
What the hell was he talking about?

[P119]
“What do you mean?”

[P120]
“Think about it. Every monster we’ve run into has been an ordinary goblin. This many Magic Gems? Something’s off.”

[P121]
He sighed. Excitement still hadn’t left his flushed face, but there was conflict on it too.

[P122]
“I know how you feel. I do… but we’ve already grabbed a fortune. Let’s be satisfied with this much and go back.”

[P123]
Satisfied?

[P124]
Here? After coming this far, turn back?

[P125]
I looked at the other team members. Some had been in sync for two or three years; some were new. But they all had the same look I did.

[P126]
“I’m against—”

[P127]
My breath caught.

[P128]
*Damn it. The chest pain again.*

[P129]
I tried to keep talking, but no voice came out. Now my ears were ringing too.

[P130]
*What is this?*

[P131]
The pain and the ringing got worse and worse. I dropped to my knees, gasping.

[P132]
*Someone. Please, help me.*

[P133]
I grabbed someone’s pant leg and clung to it.

[P134]
It was him. The man who’d looked after me like a brother, like a father, for the past five years.

[P135]
*Hyung. Please save me.*

[P136]
He looked down at me with an indifferent gaze.

[P137]
“Me? Save you, after you ran away and left everyone behind?”

[P138]
What?

[P139]
“I wanted to live too.”

[P140]
I forgot the pain and stared at him. Clothes and skin melted away, and bone showed through. Everyone except me had become skeletons, sprawled across the ground.

[P141]
*Ah. That’s right.*

[P142]
They were all dead.

[P143]
That day two years ago. In the boss zone I had insisted we enter, they had all died.

[P144]
*I was the only one who survived.*

[P145]
I floundered, buried in the memories. I remembered the ominous darkness that had settled over the boss zone, the foul smell, the damp floor, and that thing’s enormous wings.

[P146]
Bodies ripped to shreds in midair. Screams of terror. People running.

[P147]
*You fucking bastard!*

[P148]
But even the Skill I’d poured everything into hadn’t been enough to kill it. As I waited for death, he pulled me to my feet.

[P149]
*Taekyung!*

[P150]
*Hyung, I’m sorry. It was all my fault.*

[P151]
If it hadn’t been for me. If I hadn’t gotten greedy, everyone could have lived. They could have gone home to their families.

[P152]
I wailed like a child, and he forced a smile.

[P153]
*How is that your fault? Look at this kid, now you’re even playing Team Leader.*

[P154]
The massive body drifted through the cave. Stalactites rained down, and the last member of the team let out a death cry. In the darkness, its red eyes turned toward us.

[P155]
*That arrogant bastard. Taekyung, you go first.*

[P156]
*Hyung. Cheonsu hyung!*

[P157]
My chest hurt. Pain rolled in hard enough to blank my vision. It felt like I had swallowed lava, like everything inside me was burning away. The ringing in my ears turned into a monster’s roar.

[P158]
*Kyaaaaau!*

[P159]
* * *

[P160]
“Hyung—!”

[P161]
I woke with the scream.

[P162]
But it wasn’t a Gate. There were no monsters, and no team members.

[P163]
Someone stood up at the window, where sunlight poured in.

[P164]
“Did you dream about my lord? He’ll be pleased if I tell him.”

[P165]
Coldness dripped from his face.

[P166]
Wipeng, Jin Wikyung’s right-hand man.

[P167]
Seeing him drove home that I was still inside the game.

[P168]
“Are you all right?”

[P169]
“No. It was a nightmare.”

[P170]
“Then I’ll leave that part out when I tell him.”

[P171]
“Suit yourself.”

[P172]
My whole body was soaked in sweat. Through the gaps in the bandages wound tight around me, I could see flesh raised with blood scabs.

[P173]
“How long was I out?”

[P174]
“You were unconscious for five days. Your condition was so critical that the Medicine King Hall Leader concluded you wouldn’t last the day.”

[P175]
“Really?”

[P176]
“Yes. When my lord heard that, he went berserk. If I hadn’t stopped him, he would have beaten the Medicine King Hall Leader to death.”

[P177]
“Ah.”

[P178]
I remembered the old man from the meeting a few days ago, the one who had threatened to shove a giant needle into the White Tiger Hall Leader’s anus.

[P179]
*So he really had been chanting for me to die.*

[P180]
“Did anything else happen?”

[P181]
“A great deal happened. Among it, there’s good news and even better news. Which would you like to hear first?”

[P182]
“The good news.”

[P183]
“First, the reconnaissance squad and the survivors of the Sakju Branch returned safely. Two of them suffered fairly serious injuries, but their lives are not in danger.”

[P184]
*Survivors.*

[P185]
The word made my heart sink.

[P186]
*Number Seven.*

[P187]
I remembered his face as he gasped out his last breath, a dagger in his throat and another between his brows. Twenty at most. Far too young to lose his life.

[P188]
“Are you thinking of the dead?”

[P189]
“The body—did they recover the body?”

[P190]
“We recovered it properly and held a funeral for him. He was an orphan with no one in the world, so there were no surviving relatives.”

[P191]
“…”

[P192]
“May I say something?”

[P193]
Wipeng didn’t wait for an answer. He took a step toward me and went on.

[P194]
“Third Young Master, do not turn your subordinate’s death into a dog’s death.”

[P195]
“What does that…”

[P196]
“Martial artists are not beings meant to be protected. They are people who fight their enemies and prove themselves. He died facing an enemy too strong to do anything about, but that was not mere death—it was death in battle.”

[P197]
The idea that dying on a battlefield made it an honorable death was the biggest load of bullshit ever.

[P198]
There was no such thing as an honorable death. Even now, I could vividly hear the screams of my comrades who had died two years ago. I could still see Number Seven’s wide-open eyes as he breathed his last.

[P199]
“The fact that he died hasn’t changed.”

[P200]
“There are people who cling to facts that will never change. I won’t say who.”

[P201]
“…”

[P202]
“Do you regret it?”

[P203]
“Of course.”

[P204]
“Then live his share as well.”

[P205]
Wipeng continued in a gentler voice than I had ever heard from him.

[P206]
“I’m not telling you to forget the dead. Bury them in your heart and carve them into your mind. Use that regret as a foothold and soar to the place they dreamed of reaching. That is the path you must take, Young Master.”

[P207]
*The path I must take…*

[P208]
Just hearing those words made something in my chest lurch. I turned them over for a while, then let out a sudden laugh.

[P209]
“Damn. I’ll break my legs before I get there.”

[P210]
“It will take a lifetime.”

[P211]
“If I devote my whole life to it, can I make it there?”

[P212]
“I don’t know. I don’t even know how far my own path goes, so how could I know yours?”

[P213]
“What’s at the end of your path, Great Hero Wipeng?”

[P214]
“Number One Under Heaven.”

[P215]
A joke?

[P216]
No. Wipeng was more serious and resolute than ever.

[P217]
“That’s a hard one.”

[P218]
“Because it’s a dream.”

[P219]
He was right. Dreams were always hard to reach.

[P220]
Even more so if you were carrying the dreams of those you had lost.

[P221]
“Great Hero Wipeng. May I ask you one thing?”

[P222]
“Anything.”

[P223]
“That guy. What was his name?”

[P224]
“His name was…”

[P225]
The moment Wipeng opened his lips, a cold winter wind shook the window.

[P226]
*Whoooosh.*

[P227]
Beyond the chilly sound of the wind, I heard Number Seven’s name.

[P228]
“That’s a cool name.”

[P229]
“I heard he chose it himself. His dream was just as big.”

[P230]
“What was it?”

[P231]
“Number One of All Time.”

[P232]
“…”

[P233]
“You’re going to have a hard time.”

[P234]
“Yeah. This is ridiculous.”

[P235]
A laugh slipped out. Only then did I feel the weight lift from my heart.

[P236]
It was all thanks to Wipeng.

[P237]
“You’re finally back to your old self.”

[P238]
“Thank you.”

[P239]
“Don’t mention it.”

[P240]
Wipeng gave a slight nod and spoke.

[P241]
“Now, there’s still the even better news.”

[P242]
Ah. Right.

[P243]
Good news and even better news.

[P244]
Brimming with anticipation, I waited for him to continue.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 31

[P2]
“Well, look at this. This bastard’s got it made.”

[P3]
I slowly opened my eyes to a familiar face.

[P4]
“Did you come here for a picnic? Sleeping in a Gate?”

[P5]
I must have dozed off. I answered, shameless.

[P6]
“I wasn’t sleeping. Who says I was?”

[P7]
“Wipe the drool off your mouth before you start lying.”

[P8]
“Tsk.”

[P9]
“Oh, you little—”

[P10]
He shook a fist at me, but a smile sat at the corners of his mouth. I rubbed my stiff neck.

[P11]
“Ugh, I’m tired.”

[P12]
“Did you meet a woman yesterday? Why are you nodding off like a sick chicken even in the middle of a raid?”

[P13]
“When would I have time to meet a woman? You know my situation.”

[P14]
“True enough.”

[P15]
We’d been through thick and thin for five years, from our first battle until now. He knew me as well as I knew him.

[P16]
“Then what’s wrong?”

[P17]
“What do you think? Money.”

[P18]
“Money? Don’t tell me you’re moonlighting.”

[P19]
His voice dropped low. I looked past his shoulder at the team members resting nearby and nodded.

[P20]
“Well, well. This bastard gets a little time under his belt and now he’s stuffing his back pocket. And he’s the vice team leader, no less.”

[P21]
“Raids have been scarce lately, and I’m strapped. Really strapped. You’ve done it yourself, hyung, so don’t give me that.”

[P22]
Hunters with professional licenses were legally barred from second jobs. Even a D-rank probably wouldn’t have to live like this, but F-ranks like us had no choice. That was why the Guild looked the other way even when they knew.

[P23]
“True, but… be careful. If someone files a complaint with the Management Agency, it’ll become a real headache.”

[P24]
“It’s a trustworthy place. They pay cash the same day, so there’s no problem. You think I’d do this for nothing?”

[P25]
“Really?”

[P26]
Judging by his face, he was tempted.

[P27]
“Do you need money too, hyung?”

[P28]
“I’ve got three kids. I’d need an oil well to blow in the yard.”

[P29]
He poured it out with a miserable look. I’d already heard this routine dozens of times. After venting about the misery of raising kids, the rising price of formula, and the shamelessness of merchants, he patted my shoulder.

[P30]
“Don’t get married.”

[P31]
“I won’t.”

[P32]
More precisely, I couldn’t.

[P33]
I had no woman and no money. My life’s goal was to buy a house in a safe zone within five years, so deep down I envied him.

[P34]
A spouse I loved, and kids. A happy family. I had no idea when I’d ever get something like that.

[P35]
“Marriage is a swamp.”

[P36]
For all that talk, he had a reputation as a devoted husband and a good father. I knew how he sometimes took out his family photos and smiled fondly at them.

[P37]
“Your whole life gets sucked in. You come to your senses and you’re buried up to your chest, barely breathing.”

[P38]
“…”

[P39]
Maybe I’d had the wrong idea about him.

[P40]
“So don’t just work. Take breaks. Dating, hobbies—stuff like that’s good for you.”

[P41]
“I don’t know. I still need the money.”

[P42]
I scratched my head as I answered. He looked at me with pity.

[P43]
“I saw you sleeping earlier, sweating cold the whole time. Keep that up and you’ll drop dead from overwork.”

[P44]
“Was I?”

[P45]
Now that he mentioned it, my back was damp with cold sweat. Must have been a bad dream…

[P46]
*Can’t remember.*

[P47]
Probably just some stupid dream anyway.

[P48]
* * *

[P49]
A Gate.

[P50]
These days it was how Hunters like me made a living, but its true nature was an invasion route for the Demon Realm’s army.

[P51]
When Demon King Asmodeus fell, his mighty army was routed with him. Decades later, the Gates were still there.

[P52]
“Defensive formation!”

[P53]
At his command, three Hunters bearing huge tower shields blocked the front. In a narrow cave, that alone was enough to soak most attacks.

[P54]
*Clang! Clang-clang!*

[P55]
“Giiiiik!”

[P56]
About twenty goblins hurled poison needles, axes, and spears, but every one of them bounced off those big, beautiful tower shields.

[P57]
“Archers!”

[P58]
Up front, the tanks blocked every attack. From the rear, the archers poured arrows. We pushed forward and dropped about half of them, and the goblins let out panicked cries.

[P59]
“Gyaaaah!”

[P60]
“Kieek!”

[P61]
He timed the next order perfectly.

[P62]
“Attack formation!”

[P63]
The tanks dropped their tower shields and burst forward at the same time. I was faster.

[P64]
“Hah!”

[P65]
I swung the iron spear in a wide arc. Green blood burst, and the front rank broke. I dove into the gap, stabbing and cutting at everything I could reach, and the line came crashing down.

[P66]
“Charge!”

[P67]
The damage dealers and tanks piled in, and in an instant the goblin pack was a pile of corpses.

[P68]
“Pretty easy today, huh?”

[P69]
“Honestly, the vice team leader did half of it. He was flying around. When did he get that good…? Shh. The Team Leader’s pissed.”

[P70]
The people chatting shut their mouths the moment he appeared.

[P71]
“Hey, Jin Taekyung!”

[P72]
That made me jump.

[P73]
I’d been staring off, lost in thought, and I startled as I answered.

[P74]
“What?”

[P75]
“Who told you to go solo? Are you a tank? Forget the attack order? And you still call yourself vice team leader?”

[P76]
“That’s not—”

[P77]
“If you’re going to act like this, transfer teams. You’re putting the rest of them in danger too.”

[P78]
I looked at his grim face and sighed.

[P79]
“I’m sorry. I don’t know why I did that. They just… suddenly didn’t seem like a big deal. I must have lost it for a second.”

[P80]
The feeling was strange. The moment I saw the goblin pack, I’d thought I could wipe them out by myself.

[P81]
No. That hadn’t been a thought.

[P82]
It had been certainty.

[P83]
“You…”

[P84]
He swallowed the rest. We’d had each other’s backs for five years now, and this was the first time I’d ever pulled something like this.

[P85]
“Don’t do it again. If you’re having a hard time, tell me.”

[P86]
I watched him walk away after patting my shoulder. For some reason, a spot in my chest throbbed.

[P87]
*Should I see a doctor?*

[P88]
But before long I wasn’t even thinking about the pain.

[P89]
* * *

[P90]
“Magic Gems!”

[P91]
“Got some!”

[P92]
“Another!”

[P93]
“Jackpot! Jackpot! Jackpot!”

[P94]
“Mom! Hayeon!”

[P95]
Ah, that last shout was mine. His face was flushed too as he muttered.

[P96]
“Hey, what is all this…?”

[P97]
Twenty Magic Gems, large and small, lay neatly on the floor.

[P98]
Magic Gems. They looked like red pebbles, but they were called the flower of the Gate. These lumps of mana that monsters carried were high-dimensional energy, and the most valuable byproduct a monster had.

[P99]
“At this rate, each one’s got to be worth over a million won.”

[P100]
That from the Team Leader, an E-rank Hunter who’d lasted ten years in this business. People’s eyes went slack at the intoxicating sight.

[P101]
“Is it normally like this?”

[P102]
At the new recruit’s question, everyone shook their heads hard.

[P103]
“Absolutely not.”

[P104]
In an F-rank Gate the average was one or two, and even with incredible luck you wouldn’t hit five.

[P105]
I was busy doing the math.

[P106]
*Twenty million from the Magic Gems alone, another five million for the byproducts and Equipment. Add all the various allowances and…*

[P107]
*Fuck. How much is this?*

[P108]
The biggest jackpot I’d hit since becoming a Hunter.

[P109]
And the raid wasn’t even over yet.

[P110]
“How far have we come?”

[P111]
“Almost there. Turn right and it’s the boss zone.”

[P112]
The words *boss zone* made everyone’s eyes light up.

[P113]
It went without saying, but a boss zone had a boss. A boss monster was the strongest monster in that Gate—and the one with the most expensive byproducts, Equipment, and Magic Gems.

[P114]
*If we take down the boss monster too?*

[P115]
A literal jackpot. A once-in-a-lifetime chance for an F-rank Hunter.

[P116]
Everyone was smiling bright at the thought when he spoke.

[P117]
“Wait. Let me think.”

[P118]
What the hell was he talking about?

[P119]
“What do you mean?”

[P120]
“Think about it. Every monster we’ve run into has been an ordinary goblin. This many Magic Gems? Something’s off.”

[P121]
He sighed. Excitement still hadn’t left his flushed face, but there was conflict on it too.

[P122]
“I know how you feel. I do… but we’ve already grabbed a fortune. Let’s be satisfied with this much and go back.”

[P123]
Satisfied?

[P124]
Here? After coming this far, turn back?

[P125]
I looked at the other team members. Some had been in sync for two or three years; some were new. They all had the same look I did.

[P126]
“I’m against—”

[P127]
My breath caught.

[P128]
*Damn it. The chest pain again.*

[P129]
I tried to keep talking, but no voice came out. Now there was ringing in my ears too.

[P130]
*What is this?*

[P131]
The pain and the ringing got worse and worse. I dropped to my knees, gasping.

[P132]
*Someone. Please, help me.*

[P133]
I grabbed someone’s pant leg and hung on.

[P134]
It was him. The man who’d looked after me like a brother, like a father, for the past five years.

[P135]
*Hyung. Please save me.*

[P136]
He looked down at me, indifferent.

[P137]
“Me? You, who ran and left everyone behind?”

[P138]
What?

[P139]
“I wanted to live too.”

[P140]
I forgot the pain and stared at him. Clothes and skin melted away, and bone showed through. Everyone except me had become skeletons, sprawled across the ground.

[P141]
*Ah. That’s right.*

[P142]
They were all dead.

[P143]
That day two years ago. In the boss zone I had insisted we enter, they had all died.

[P144]
*I was the only one who survived.*

[P145]
I floundered, buried in the memories. I remembered the ominous darkness that had settled over the boss zone, the foul smell, the damp floor, and that thing’s enormous wings.

[P146]
Bodies ripped to shreds in midair. Screams of terror. People running.

[P147]
*You fucking bastard!*

[P148]
But even the Skill I had poured everything into hadn’t been enough to kill it. As I waited to die, he pulled me to my feet.

[P149]
*Taekyung!*

[P150]
*Hyung, I’m sorry. It was all my fault.*

[P151]
If it hadn’t been for me. If I hadn’t gotten greedy, everyone could have lived. They could have gone home to their families.

[P152]
I wailed like a child, and he forced a smile.

[P153]
*How is that your fault? Look at this kid, now you’re even playing Team Leader.*

[P154]
The massive body drifted through the cave. Stalactites rained down, and the last member of the team let out a death cry. In the darkness, its red eyes turned toward us.

[P155]
*That arrogant bastard. Taekyung, you go first.*

[P156]
*Hyung. Cheonsu hyung!*

[P157]
My chest hurt. Pain rolled in hard enough to blank my vision. It felt like I had swallowed lava, like everything inside me was burning away. The ringing in my ears turned into a monster’s roar.

[P158]
*Kyaaaaau!*

[P159]
* * *

[P160]
“Hyung—!”

[P161]
I woke with the scream.

[P162]
But it wasn’t a Gate. There were no monsters, and no team members.

[P163]
Someone stood up at the window, where sunlight poured in.

[P164]
“Did you dream about my lord? He’ll be pleased if I tell him.”

[P165]
Coldness dripped from his face.

[P166]
Wipeng, Jin Wikyung’s right-hand man.

[P167]
Seeing him made it real that I was still inside the game.

[P168]
“Are you all right?”

[P169]
“No. It was a nightmare.”

[P170]
“Then I’ll leave that part out of the report.”

[P171]
“Suit yourself.”

[P172]
I was soaked in sweat. Through the gaps in the bandages wound tight around my whole body, I could see flesh raised with blood scabs.

[P173]
“How long was I out?”

[P174]
“You were unconscious for five days. Your condition was so critical that the Medicine King Hall Leader concluded you wouldn’t last the day.”

[P175]
“Really?”

[P176]
“Yes. When my lord heard that, he went berserk. If I hadn’t stopped him, he would have beaten the Medicine King Hall Leader to death.”

[P177]
“Ah.”

[P178]
I remembered the old man from the meeting a few days ago, the one who had threatened to shove a giant needle into the White Tiger Hall Leader’s anus.

[P179]
*So he really had been chanting for me to die.*

[P180]
“Did anything else happen?”

[P181]
“A great deal happened. Among it, there’s good news and even better news. Which would you like to hear first?”

[P182]
“The good news.”

[P183]
“First, the reconnaissance squad and the survivors of the Sakju Branch returned safely. Two of them suffered fairly serious injuries, but their lives are not in danger.”

[P184]
*Survivors.*

[P185]
The word made my heart drop.

[P186]
*Number Seven.*

[P187]
I remembered his face as he gasped out his last breath, a dagger in his throat and another between his brows. Twenty at most. Far too young to lose his life.

[P188]
“Are you thinking of the dead?”

[P189]
“The body—did they recover the body?”

[P190]
“We recovered it properly and buried him. He was an orphan with no one in the world, so there were no surviving relatives.”

[P191]
“…”

[P192]
“May I say something?”

[P193]
Wipeng didn’t wait for an answer. He took a step toward me and went on.

[P194]
“Third Young Master, do not turn your subordinate’s death into a dog’s death.”

[P195]
“What does that…”

[P196]
“Martial artists are not beings meant to be protected. They are people who fight their enemies and prove themselves. He died facing an enemy too strong to do anything about, but that was not mere death—it was death in battle.”

[P197]
The idea that dying on a battlefield made it an honorable death was the biggest load of bullshit ever.

[P198]
There was no such thing as an honorable death. Even now, the screams of my comrades who died two years ago and Number Seven’s wide-open eyes as his breath left him were still vivid.

[P199]
“The fact that he died hasn’t changed.”

[P200]
“There are people who cling to facts that will never change. I won’t say who.”

[P201]
“…”

[P202]
“Do you regret it?”

[P203]
“Of course.”

[P204]
“Then live his share as well.”

[P205]
Wipeng continued in a gentler voice than I had ever heard from him.

[P206]
“I’m not telling you to forget the dead. Bury them in your heart and carve them into your mind. Use that regret as a foothold and soar to the place they dreamed of reaching. That is the path you must take, Young Master.”

[P207]
*The path I must take…*

[P208]
Just hearing those words made something in my chest lurch. I turned them over for a while, then let out a sudden laugh.

[P209]
“Damn. I’ll break a leg before I get there.”

[P210]
“It will take a lifetime.”

[P211]
“If I give it my whole life, can I make it there?”

[P212]
“I don’t know. I don’t even know how far my own path goes, so how could I know yours?”

[P213]
“What’s at the end of the road Great Hero Wipeng is walking?”

[P214]
“Number One Under Heaven.”

[P215]
A joke?

[P216]
No. Wipeng was more serious and resolute than ever.

[P217]
“That’s a hard one.”

[P218]
“Because it’s a dream.”

[P219]
He was right. Dreams were always hard to reach.

[P220]
Even more so if you were carrying the dreams of those you had lost.

[P221]
“Great Hero Wipeng. May I ask you one thing?”

[P222]
“Anything.”

[P223]
“That guy. What was his name?”

[P224]
“His name was…”

[P225]
The moment Wipeng opened his lips, a cold winter wind shook the window.

[P226]
*Whoooosh.*

[P227]
Beyond the chill of the wind, I heard Number Seven’s name.

[P228]
“That’s a cool name.”

[P229]
“I heard he chose it himself. His dream was just as big.”

[P230]
“What was it?”

[P231]
“Number One of All Time.”

[P232]
“…”

[P233]
“You’re going to have a hard time.”

[P234]
“Yeah. That’s unbelievable.”

[P235]
A laugh slipped out. Only then did I feel the weight in my heart lift.

[P236]
It was all thanks to Wipeng.

[P237]
“You’re finally back to your old self.”

[P238]
“Thank you.”

[P239]
“Don’t mention it.”

[P240]
Wipeng tipped his head and spoke.

[P241]
“Now, there’s still the even better news.”

[P242]
Ah. Right.

[P243]
Good news and even better news.

[P244]
I waited, as expectant as I could get, for what he would say next.
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 31,
  "passed": true,
  "metrics": {
    "source_characters": 7116,
    "translation_characters": 14804,
    "length_ratio": 2.08,
    "source_paragraphs": 223,
    "translation_paragraphs": 244
  },
  "errors": [],
  "warnings": [
    {
      "code": "numbers",
      "message": "Arabic numerals from the source are absent",
      "details": {
        "values": [
          "2"
        ]
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
      "code": "novel_name",
      "message": "source term was romanized without a ledger entry; use the established English or footnote the first use",
      "details": {
        "korean": "천수",
        "romanization": "cheonsu"
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
