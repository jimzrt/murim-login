# Fidelity Gate — Chapter 21

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
  1|＃21화
  2|
  3|
  4|
  5|띠링.
  6|
  7|
  8|
  9|- [진가심법]을 수련했습니다.
 10|
 11|- 반복 수련의 결과로 근맥과 근골이 1씩 상승합니다.
 12|
 13|
 14|
 15|“후우.”
 16|
 17|심호흡과 함께 눈을 떴다. 어스름한 새벽, 촛불로 밝힌 방 안은 호박빛으로 출렁이고 있었다.
 18|
 19|‘이번에도 실패.’
 20|
 21|고요 속에서 주먹이 불끈 쥐어진다.
 22|
 23|몇 번째 시도였을까. 스무 번? 서른 번? 중요한 건 결과다. 이번에도 굳은 공력을 끌어내는 것에 실패했다.
 24|
 25|‘그나마 나아지고 있다는 걸 위안 삼아야 하나?’
 26|
 27|공력을 다루는 것에 점점 익숙해지고 있다. 내가 F급 헌터가 아니라 C급. 아니 최소 D급만 되었어도 훨씬 빨리 적응했겠지만, 현실은 냉혹한 법이다.
 28|
 29|‘근골, 근맥이 꾸준히 향상되는 덕분인 것도 있겠지.’
 30|
 31|공력은 인체의 혈을 타고 흐른다. 심법을 수련하면 할수록, 근골과 근맥이 향상되면 될수록 혈이 넓어지고 튼튼해진다. 처음과 비교하면 보다 더 많은 공력을, 훨씬 빠른 속도로 순환시킬 수 있었다.
 32|
 33|‘스킬 포인트 덕분이지.’
 34|
 35|레벨 업 한 번에 10씩 주어지는 스킬 포인트는 그 역할을 톡톡히 하고 있었다. 근골과 근맥을 향상시키는 데에는 그만한 양분이 없다.
 36|
 37|‘스킬창 오픈.’
 38|
 39|
 40|
 41|스킬창
 42|
 43|
 44|
 45|[LV.17 진태경]
 46|
 47|심법 : 진가심법 (사 성)
 48|
 49|무공 : 진가창법 (오 성) / 진가보법 (오 성)
 50|
 51|근골 : 105
 52|
 53|잔여 포인트 :  0
 54|
 55|
 56|
 57|
 58|
 59|‘가능성이 보인다.’
 60|
 61|난공불락의 요새가 점점 작고 허술해지고 있다. 계속해서 두드리다 보면 곧 문을 열 수 있을 것 같은 느낌이다.
 62|
 63|다행히 내가 재능은 없어도 끈기는 있는 놈이지.
 64|
 65|‘계속 시도한다. 될 때까지.’
 66|
 67|다시 가부좌를 틀고 운기조식을 시작하려던 찰나였다.
 68|
 69|앞서 수차례의 운기조식 덕분에 잔뜩 곤두선 감각들 사이로, 심상치 않은 소리가 들려왔다.
 70|
 71|‘이건…….’
 72|
 73|웅웅웅. 언뜻 들으면 벌 떼 우는 소리처럼 들리는 그것은 사람들의 웅성거림이었다.
 74|
 75|‘무슨 일이지?’
 76|
 77|귓가로 공력을 흘려보냈다. 거리가 멀어서 그런지 완전히 알아듣기에는 턱없이 부족했다. 하지만 그것으로도 충분했다.
 78|
 79|웅얼거리는 목소리들 사이에서 한 단어를 들었으니까.
 80|
 81|‘전투!’
 82|
 83|항산검문이다. 드디어 전투가 벌어진 것이다.
 84|
 85|나는 황급히 가부좌를 풀고 일어섰다. 그리고 반쯤 열린 창문 너머로 뛰어내렸다.
 86|
 87|고양이처럼 착지한 내 시야에, 차례차례 불이 밝혀지는 전각들이 들어왔다.
 88|
 89|‘결국…….’
 90|
 91|시작됐구나.
 92|
 93|
 94|
 95|* * *
 96|
 97|
 98|
 99|스물다섯. 가지런히 눕힌 시신의 숫자였다.
100|
101|모든 생기를 잃은 채 고목처럼 누워 있는 그들을 확인했을 때, 할 말을 잃고 말았다.
102|
103|“이건.”
104|
105|나는 헌터다. 무수한 전투를 겪었고 죽음을 지켜봤다.
106|
107|중독되고, 베이고, 으스러지고, 터지고…….
108|
109|상대하는 몬스터에 따라 죽음의 종류도 천차만별이다. 하지만 그들에게는 한 가지 공통점이 있었다.
110|
111|바로 ‘성인’이라는 것.
112|
113|그건 각성의 기본 조건이었다. 어떤 기준인지, 왜인지는 아무도 몰랐다. 게이트의 존재만큼이나 자연스럽게 자리 잡은 법칙이었다.
114|
115|그래서 내가 목격한 그 숱한 죽음들 중에는 어린아이의 죽음이 포함되어 있지 않았다.
116|
117|‘이건 게임이다. 고작 게임이라고.’
118|
119|마음속으로 계속해서 중얼거렸다. 그러나 단순히 그렇게 치부하기에는 눈앞의 광경이 너무나도 참혹했다.
120|
121|
122|
123|혈血
124|
125|
126|
127|이마에 아로새겨진 글자. 말라붙은 핏물 위로 횃불이 비친다. 열 명이 넘는 어린아이들이 그렇게 싸늘하게 식어 있었다.
128|
129|기껏해야 중학생. 혹은 그 밑으로 보이는 아이들까지 하나도 빠짐없이. 그렇게 죽어 있었다.
130|
131|“우웁!”
132|
133|떨리는 손으로 횃불을 들고 있던 무사 하나가 허리를 숙이는 것을 시작으로 곳곳에서 토악질 소리가 울려 퍼졌다.
134|
135|그때 무사가 떨어트린 횃불을 집어 드는 손이 있었다.
136|
137|“소미. 분명 그런 이름이었지. 내가 가주 대행이 되던 날, 응현 지부장이 자신의 보물이라며 침이 마르게 자랑했었다.”
138|
139|진위경이다. 그는 꺼질 듯한 눈동자로 횃불을 들어 아이들의 얼굴을 비췄다. 한 사람. 한 사람. 얼굴이 드러날 때마다 어김없이 각자의 이름이 흘러나왔다.
140|
141|마지막 아이의 이름을 부른 진위경이 나를 바라봤다.
142|
143|“이 아이들이 누군지 아느냐?”
144|
145|“……모릅니다.”
146|
147|“응현(應現), 산음(山陰), 삭주(朔州) 지부에 파견된 본가의 식솔들이다.”
148|
149|그곳이 어디인지 나는 모른다. 하지만 이 아이들의 부모들이 어떤 최후를 맞았을지는 짐작할 수 있었다.
150|
151|더불어 항산검문의 의도에 구역질이 났다.
152|
153|‘미친 사이코패스 새끼들.’
154|
155|봐라, 우리는 이런 어린아이까지도 참혹하게 죽일 수 있다. 곧 너희도 이처럼 될 것이다.
156|
157|얼굴도 모르는 항산검문주의 목소리가 들리는 듯했다.
158|
159|“모든 게 내 탓이다. 무공을 모르는 아이들까지 이리 참혹하게…….”
160|
161|진위경이 떨리는 목소리로 자책하던 그때였다.
162|
163|“그것이 전쟁의 본질이오. 소가주.”
164|
165|대장로가 은빛 수염을 매만지며 나타났다. 시신들을 바라보는 그의 눈동자는 담담하게 가라앉아 있었다.
166|
167|“승리와 패배. 둘 중 어디에도 죽음은 빠지지 않는 법. 항산검문주. 혈랑검 이천백이라고 했나? 그는 낭인 출신답게 전쟁을 잘 알고 있소. 이 아이들만 봐도 알 수 있지.”
168|
169|그 대수롭지 않다는 말투에 나는 소름이 돋았다.
170|
171|‘어떻게 돼먹은 인공지능이야.’
172|
173|이 NPC는 어딘가 결여되어 있다. 그래서 더욱 위험하게 느껴진다.
174|
175|나는 입을 다물었고, 진위경은 일그러진 얼굴로 입을 열었다.
176|
177|“……말을 삼가시지요. 본가의 식솔들입니다.”
178|
179|“아니, 저 아이들은 전사자요. 앞으로도 무수한 이들이 죽어 나가겠지. 어쩌면 지금 이 순간에도.”
180|
181|“대장로. 말을 삼가라 했습니다.”
182|
183|진위경이 으르렁거렸다. 사람들의 눈만 없었다면 진작 일을 냈을 기세였다. 하지만 대장로는 여전히 담담했다.
184|
185|“예상하지 못했느냐?”
186|
187|갑작스러운 하대였다. 하지만 나도, 진위경도 인식하지 못할 정도로 자연스러웠다.
188|
189|“산음, 응현, 삭주. 모두 항산검문의 손이 닿는 곳이었다. 전날 각 지부에 전서구를 보내면서 이런 일이 벌어질 수 있음을 전혀 염두에 두지 않았단 말이냐?”
190|
191|“그건…….”
192|
193|“너는 알고 있었다. 그들에게 화가 미치리라는 사실을 말이다. 전서구를 보냈던 건 단순한 양심의 가책이었을 뿐이지.”
194|
195|“그만. 그만하십시오.”
196|
197|“훌륭한 판단이었다. 만약 지부를 구원하고자 했다면 쉬지 않고 칠 주야를 달려야 했을 것이고, 극도로 지친 상태에서 적과 싸워야 했을 테니까. 그렇지 않으냐?”
198|
199|진위경은 하얗게 질린 얼굴로 대장로를 바라봤다. 꽉 쥔 주먹 사이로 선혈이 흘렀다.
200|
201|“난, 나는…….”
202|
203|“모든 것에는 희생이 따르는 법. 대국을 직시해라. 너는 태원진가의 수백 식솔을 책임질 소가주다.”
204|
205|진위경의 몸이 부르르 떨렸다. 분노와 슬픔이 빠져나간 표정에는 왠지 모를 허탈함이 가득했다.
206|
207|“희생…….”
208|
209|“전쟁은 이제 막 시작되었을 뿐이오. 안 그렇소? 소가주.”
210|
211|포권을 취해 보이는 대장로의 모습에, 나는 입술을 질끈 깨물었다.
212|
213|‘종잡을 수 없는 노인네.’
214|
215|대장로는 분명 위험한 인물이다. 가문에서의 위치, 도무지 짐작할 수 없는 속내, 어린아이들을 시체를 보고도 눈썹 하나 깜짝하지 않는 사이코패스적인 면모까지.
216|
217|하지만…….
218|
219|‘그의 말이 맞아.’
220|
221|내 시선에서 진위경은 좋은 소가주다. 인간미도 넘치고 머리도 영특하다.
222|
223|하지만 시신들을 보는 순간, 누구보다 크게 흔들렸다. 대장로의 싸늘한 일침이 아니었다면 평정심을 되찾기까지 상당한 시간이 걸렸을 것이다.
224|
225|‘도움을 줬다. 다른 누구도 아닌, 바로 그 대장로가…….’
226|
227|평화로울 때는 적대 관계지만 전쟁 시에는 뭉친다는 건가?
228|
229|‘그럼 다행인데.’
230|
231|의심과 안도가 섞인 눈초리로 대장로를 바라보던 그때였다.
232|
233|“삼공자도 있었군.”
234|
235|노회한 잿빛 눈동자에 가슴이 덜컥 내려앉았다. 처음으로 대장로가 내게 말을 걸어온 것이다.
236|
237|“대장로를 뵙습니다.”
238|
239|애써 당황을 숨기는 나를 대장로가 묘한 미소를 띠고 바라봤다.
240|
241|“요새 가문 내에 재미있는 소문이 들리던데, 그게 아마…… 산서잠룡이라던가?”
242|
243|저 웃기지도 않는 별명을 대장로에게서 들을 줄이야.
244|
245|“일설에 의하면 염라편과 친분이 있다고도 하더군. 그와 힘을 합쳐 천력부를 쓰러트렸다던데.”
246|
247|“쿨럭. 쿨럭.”
248|
249|“어디 아픈가?”
250|
251|“아, 아닙니다. 그냥 몸이 으슬으슬해서요.”
252|
253|“저런. 곧 큰 공을 세울 사람이 그래서야 쓰나.”
254|
255|어색하게 웃던 내 얼굴이 천천히 굳어졌다.
256|
257|“그게 무슨 말씀이신지.”
258|
259|“천력부라는 걸출한 마두를 제거하는 데 일조한 실력자라면 귀중한 전력이지. 설마 그 소문이 거짓은 아닐 테고.”
260|
261|“…….”
262|
263|“해서, 본가의 직계로서 앞장서서 싸우는 건 당연한 의무라고 생각되는데. 소가주의 생각은 어떠시오?”
264|
265|빙긋. 대장로의 웃음을 물끄러미 바라보던 진위경이 내게 물었다.
266|
267|“네 생각은 어떠하냐?”
268|
269|외통수. 한 단어를 떠올린 순간, 익숙한 알림이 울렸다.
270|
271|띠링.
272|
273|
274|
275|* * *
276|
277|
278|
279|퀘스트
280|
281|
282|
283|[임무 수행]
284|
285|당신은 백호당 정찰조장으로 임명되었습니다.
286|
287|지금부터 휘하에 배속된 부하들을 이끌고 임무를 수행, 공적을 쌓으십시오!
288|
289|
290|
291|등급 : 반복 퀘스트
292|
293|제한 : 진태경
294|
295|임무 : 공적치 100 달성 (0 / 100)
296|
297|보상 : 성공 정도에 따라 변화합니다.
298|
299|실패 : 실패 정도에 따라 변화합니다.
300|
301|
302|
303|
304|
305|퀘스트창을 껐다. 이미 몇 번이나 봤을뿐더러, 잠시 자리를 비웠던 백호당 소속 무사가 지금 막 돌아왔기 때문이었다.
306|
307|“조장들에게 기본으로 지급되는 물품들입니다.”
308|
309|검, 그리고 백호가 조잡하게 수놓아진 흑색 무복과 나무 냄새가 물씬 나는 반들반들한 목패(木牌).
310|
311|그게 전부였다.
312|
313|“새로 휘하에 배속된 이들은 정찰조 숙소에서 대기 중입니다. 위치는…….”
314|
315|다행히 내가 아는 곳이었다. 몇 번 오가면서 봤던 전각이 바로 정찰조에 배정된 숙소였다.
316|
317|백호당을 빠져나온 후 우선 인적이 없는 골목으로 숨었다.
318|
319|‘인벤토리 오픈.’
320|
321|모든 복장을 갖추는 데는 10초면 충분했다. 옷을 갈아입고, 검은 인벤토리 깊숙이 처박은 다음 [예리한 창]을 꺼냈다.
322|
323|지금까지야 으리으리한 개인 전각에서 삼공자의 신분을 톡톡히 누렸지만 지금부터는 다르다.
324|
325|‘공동 생활이랬지.’
326|
327|먹는 것도, 자는 것도 함께다. 필요할 때마다 허공에서 2m짜리 철창이 튀어나오는 마술을 보여 줄 수는 없는 법이다.
328|
329|조장이라고 음각된 목패를 허리춤에 차자 태원진가의 평범한 무사1이 된 것 같았다.
330|
331|‘그냥 무사는 아니지. 정찰조장이니까.’
332|
333|백호당 정찰조장. 생각지도 못한 직책을 받게 됐다.
334|
335|물론 여기에는 나름 치열한 의견 대립이 있었다. 대장로는 나를 장로원 계열의 전투 부대에 넣고 싶어 했고, 진위경은 극렬하게 반대했다.
336|
337|‘결국 타협을 봤지.’
338|
339|임무 자체는 어렵지 않은 정찰조장. 하지만 장로원 일파인 백호당주의 휘하로. 결국 어어, 하는 사이에 이런 직책을 받게 됐다.
340|
341|‘이런 식으로 전쟁에 끼게 될 줄은 몰랐는데.’
342|
343|배 째라 식으로 나갈 수도 있었지만 참았다. 염라편을 언급할 때마다 번뜩이는 대장로의 눈빛이 첫 번째 이유였고, 두 번째 이유는…… 어린아이들 때문이다.
344|
345|‘게임이다. 전부 그래픽이고 허상일 뿐이야.’
346|
347|수없이 되뇌어도 그 시신들이, 이마에 칼로 새겨진 글자가 눈앞에 어른거렸다. 맞다. 이 결정에는 감성적인 부분도 있었다.
348|
349|이대로라면 좋지 않다.
350|
351|‘몰입하지 말자. 현실과 게임을 혼동해서는 안 돼.’
352|
353|언젠가부터 부쩍 그런 일들이 많아졌다. 처음에는 재미 삼아 NPC들을 사람처럼 대했던 것이, 요즘 들어서는 정말 사람이라고 생각하고 관계를 맺고 있었다.
354|
355|그럴 때마다 깜짝깜짝 놀라곤 한다. 이것도 게임을 오래 하다 보니 생긴 부작용일지도 모르지.
356|
357|“여긴가?”
358|
359|어느새 정찰조의 숙소에 도착한 나는 입을 벌렸다.
360|
361|갈라진 목재와 쾌쾌한 냄새. 세상에, 처마 밑에는 벌집까지 있다. 저렇게 큰 건 또 처음 본다.
362|
363|‘역시 가족 같은 기업…….’
364|
365|복지 수준 봐라. 아니, 어쩌면 날 싫어하는 백호당주의 심술일 수도 있겠다. 대놓고 갈구는 건 아직 못 하겠고, 엿 좀 먹어 보라 이건가.
366|
367|‘그래, 일단 해 보자.’
368|
369|크게 심호흡한 나는 문을 열고 한 발을 내딛었다.
370|
371|끼이이익. 오래된 바닥이 울부짖는 소리가 유난히 불길했다.
```

## Assembled English

```markdown
[P1]
# Chapter 21

[P2]
Ding.

[P3]
> **System**
>
> - Practiced the **Jin Family’s Cultivation Technique**.
>
> - As a result of repeated practice, **Sinews** and **Bones** each increase by 1.

[P4]
“Whew.”

[P5]
I opened my eyes with a deep exhale. In the dim light before dawn, the candlelit room swam in amber hues.

[P6]
*Failed again.*

[P7]
My fist clenched in the silence.

[P8]
How many attempts had it been? Twenty? Thirty? The result was what mattered. Once again, I had failed to draw out the solidified internal energy.

[P9]
*Should I take comfort in the fact that I’m getting better?*

[P10]
I was gradually getting used to handling internal energy. If I had been a C-rank Hunter instead of an F-rank—or at least a D-rank—I would have adapted much faster. But reality was cold and unforgiving.

[P11]
*My Sinews and Bones improving steadily must be helping, too.*

[P12]
Internal energy flowed through the body’s meridians. The more I practiced a cultivation technique, and the more my Sinews and Bones improved, the wider and sturdier those pathways became. Compared to when I had started, I could circulate more internal energy at a much faster speed.

[P13]
*It’s all thanks to the Skill Points.*

[P14]
The ten Skill Points awarded with every level-up were doing their job well. Nothing could nourish my Sinews and Bones better.

[P15]
*Open Skill Window.*

[P16]
> **Skill Window**
>
> **Lv. 17 Jin Taekyung**
>
> **Cultivation Technique:** Jin Family’s Cultivation Technique (Fourth Stage)
>
> **Martial Arts:** Jin Family’s Spear Technique (Fifth Stage) / Jin Family’s Manoeuvre Technique (Fifth Stage)
>
> **Bones:** 105
>
> **Remaining Points:** 0

[P17]
*I can see the possibility.*

[P18]
The impregnable fortress was starting to look smaller and flimsier. If I kept pounding away at it, I felt like I would soon be able to open the gate.

[P19]
Fortunately, I might lack talent, but I had persistence.

[P20]
*I’ll keep trying. Until it works.*

[P21]
I was just about to sit cross-legged and begin circulating my qi again when my senses, sharpened by the many earlier rounds of circulating my qi, picked up an unusual sound.

[P22]
*This is…*

[P23]
A low, droning hum. At first, it sounded like a swarm of bees, but it was actually the murmur of many people.

[P24]
*What’s going on?*

[P25]
I let internal energy flow to my ears. Perhaps because of the distance, I couldn’t make out everything clearly. But I heard enough.

[P26]
One word stood out among the indistinct voices.

[P27]
*Battle!*

[P28]
The Mount Heng Sword Sect.

[P29]
The battle had finally begun.

[P30]
I hurriedly uncrossed my legs and stood. Then I leaped through the half-open window.

[P31]
I landed like a cat. Before me, the pavilions lit up one after another.

[P32]
*In the end…*

[P33]
It had begun.

[P34]
* * *

[P35]
Twenty-five.

[P36]
That was the number of corpses laid out in orderly rows.

[P37]
When I saw them lying like dead trees, every trace of vitality gone, I was left speechless.

[P38]
“This is…”

[P39]
I was a Hunter. I had fought countless battles and witnessed countless deaths.

[P40]
Poisoned, cut apart, crushed, blown apart…

[P41]
The kinds of death varied wildly depending on the monster involved. But all those deaths had one thing in common.

[P42]
They were all adults.

[P43]
That was one of the basic conditions for awakening. No one knew what the standard was or why it existed. It was a law as naturally established as the existence of Gates.

[P44]
That was why none of the countless deaths I had witnessed had involved a child.

[P45]
*This is a game. It’s just a game.*

[P46]
I kept repeating the words to myself. But the sight before me was too horrific to dismiss so simply.

[P47]
**BLOOD**

[P48]
The character had been carved into their foreheads. Torchlight glinted off the dried blood.

[P49]
More than ten children had gone cold like that.

[P50]
They were middle-school age at most. Some looked even younger. Every single one of them was dead.

[P51]
“Urgh!”

[P52]
One of the martial artists holding a torch in a trembling hand doubled over. Soon, the sound of retching rang out from all around us.

[P53]
Then a hand reached down and picked up the torch he had dropped.

[P54]
“Somi. That was definitely her name. The day I became acting Family Head, the Branch Leader of Eung-hyeon bragged about her until his mouth ran dry, calling her his treasure.”

[P55]
It was Jin Wikyung. His eyes looked as though their light might go out at any moment as he raised the torch to illuminate the children’s faces.

[P56]
One by one.

[P57]
As each face was revealed, he unfailingly spoke its name.

[P58]
After naming the last child, Jin Wikyung looked at me.

[P59]
“Do you know who these children are?”

[P60]
“…No.”

[P61]
“They were members of our family sent to the branches in Eung-hyeon, Saneum, and Sakju.”

[P62]
I didn’t know where those places were. But I could guess what kind of end the children’s parents had met.

[P63]
And the Mount Heng Sword Sect’s intentions made me sick.

[P64]
*Those crazy fucking psychopaths.*

[P65]
*Look. We can slaughter even children this young. Soon, you’ll end up the same way.*

[P66]
I could almost hear the voice of the Mount Heng Sword Sect’s Sect Leader, whose face I had never seen.

[P67]
“This is all my fault. To slaughter even children who don’t know martial arts so cruelly…”

[P68]
Jin Wikyung was blaming himself in a trembling voice when—

[P69]
“That is the essence of war, Lesser Family Head.”

[P70]
The Head Elder appeared, stroking his silver beard. His gaze was calm as he looked over the corpses.

[P71]
“Victory and defeat—neither comes without death. The Mount Heng Sword Sect’s Leader—Blood Wolf Sword Lee Cheonbaek, was it? As one would expect of a former wandering martial artist, he understands war well. These children alone make that clear.”

[P72]
The casual way he said it sent a chill through me.

[P73]
*What the hell is wrong with this AI?*

[P74]
Something was missing from this NPC. That made him feel even more dangerous.

[P75]
I kept my mouth shut. Jin Wikyung spoke, his expression twisted.

[P76]
“…Please choose your words carefully. They are members of our family.”

[P77]
“No. Those children are casualties of war. Countless more will die from now on. Perhaps even at this very moment.”

[P78]
“Head Elder. I told you to watch your words.”

[P79]
Jin Wikyung growled. If no one else had been watching, he looked ready to start something right then and there.

[P80]
But the Head Elder remained calm.

[P81]
“Did you not anticipate this?”

[P82]
He had abruptly dropped into the speech of a superior addressing an inferior, yet the shift was so natural that neither Jin Wikyung nor I even registered it.

[P83]
“Saneum, Eung-hyeon, Sakju. All of them were places within the Mount Heng Sword Sect’s reach. When you sent messenger pigeons to the branches the day before, did you truly not consider that something like this might happen?”

[P84]
“That…”

[P85]
“You knew harm would come to them. Sending those pigeons was nothing more than a way to ease your conscience.”

[P86]
“Enough. Please, enough.”

[P87]
“It was an excellent decision. If you had wanted to save the branches, you would have had to run for seven days and nights without rest, then fight the enemy in a state of extreme exhaustion. Isn’t that right?”

[P88]
Jin Wikyung stared at the Head Elder, his face deathly pale. Fresh blood ran between his tightly clenched fingers.

[P89]
“I—I…”

[P90]
“Everything comes with a sacrifice. Look at the bigger picture. You are the Lesser Family Head responsible for the hundreds of family members of the Jin Family of Taiyuan.”

[P91]
Jin Wikyung’s body trembled. The anger and sorrow had drained from his face, leaving it filled with a strange emptiness.

[P92]
“Sacrifice…”

[P93]
“The war has only just begun. Isn’t that so, Lesser Family Head?”

[P94]
The Head Elder gave a fist-and-palm salute. I bit down hard on my lip.

[P95]
*What an impossible old man to figure out.*

[P96]
The Head Elder was clearly dangerous. His position within the family, his utterly unreadable motives, even his psychopathic side—he hadn’t so much as twitched an eyebrow at the sight of those children’s corpses.

[P97]
But…

[P98]
*He was right.*

[P99]
From my perspective, Jin Wikyung was a good Lesser Family Head. He was deeply humane and sharp-minded.

[P100]
But the moment he saw the corpses, he had been shaken more deeply than anyone. Without the Head Elder’s cold rebuke, it would have taken him a long time to regain his composure.

[P101]
*He helped him. The Head Elder, of all people…*

[P102]
*Were they enemies in peacetime but closed ranks during war?*

[P103]
*If so, that’s a relief.*

[P104]
I was looking at the Head Elder with a mixture of suspicion and relief when he spoke.

[P105]
“So the Third Young Master is here as well.”

[P106]
My heart dropped at the sight of those shrewd gray eyes. It was the first time the Head Elder had spoken to me.

[P107]
“Greetings, Head Elder.”

[P108]
The Head Elder looked at me with a strange smile as I did my best to hide my surprise.

[P109]
“I’ve been hearing an interesting rumor within the family lately. Something about… the Sleeping Dragon of Shanxi?”

[P110]
I never expected to hear that ridiculous nickname from the Head Elder.

[P111]
“I’ve also heard that you are acquainted with Yama Whip. They say you joined forces with him to defeat the Heavenly Axe.”

[P112]
“Cough. Cough.”

[P113]
“Are you ill?”

[P114]
“N-no. I’m just feeling a little chilly.”

[P115]
“Oh dear. That won’t do for someone who is about to distinguish himself.”

[P116]
My awkward smile slowly froze.

[P117]
“What do you mean?”

[P118]
“Someone capable of helping eliminate an exceptional demon like the Heavenly Axe is a valuable asset in battle. Surely that rumor isn’t false.”

[P119]
“…”

[P120]
“Therefore, as a direct-line member of our family, I believe it is only natural that you lead from the front. What do you think, Lesser Family Head?”

[P121]
The Head Elder smiled faintly. Jin Wikyung, who had been gazing at that smile, asked me,

[P122]
“What do you think?”

[P123]
*Checkmate.*

[P124]
The moment the word came to mind, a familiar notification rang out.

[P125]
Ding.

[P126]
* * *

[P127]
> **System**
>
> **Quest**
>
> **Carry Out Missions**
>
> You have been appointed reconnaissance squad leader of White Tiger Hall.
>
> From now on, lead the subordinates assigned under you, carry out missions, and build merit!
>
> **Grade:** Repeating Quest  
> **Restriction:** Jin Taekyung  
> **Mission:** Achieve 100 Merit (0 / 100)  
> **Reward:** Changes according to the degree of success.  
> **Failure:** Changes according to the degree of failure.

[P128]
I closed the Quest Window. I had already seen it several times, and besides, the White Tiger Hall martial artist who had briefly stepped away had just returned.

[P129]
“These are the supplies issued to squad leaders.”

[P130]
A sword.

[P131]
A black martial uniform with a crudely embroidered white tiger.

[P132]
And a smooth wooden plaque that smelled strongly of fresh wood.

[P133]
That was everything.

[P134]
“The newly assigned members are waiting at the reconnaissance squad’s quarters. The location is…”

[P135]
Fortunately, I knew the place. The pavilion I had passed several times was the quarters assigned to the reconnaissance squad.

[P136]
After leaving White Tiger Hall, I first ducked into a deserted alley.

[P137]
*Open Inventory.*

[P138]
Ten seconds was enough to put on the full uniform. I changed clothes, shoved the sword deep into my Inventory, then pulled out the *Sharp Spear*.

[P139]
Until now, I had thoroughly enjoyed the privileges of being the Third Young Master in a lavish private pavilion.

[P140]
But things were different from here on out.

[P141]
*It’s communal living, right?*

[P142]
We would eat together and sleep together. I couldn’t exactly perform a magic trick where a two-meter iron spear popped out of thin air whenever I needed it.

[P143]
Once I hung the wooden plaque engraved with *Squad Leader* at my waist, I felt like I’d become Ordinary Martial Artist #1 of the Jin Family of Taiyuan.

[P144]
*Not just an ordinary martial artist. I’m a reconnaissance squad leader.*

[P145]
White Tiger Hall reconnaissance squad leader.

[P146]
I had never expected to receive a position like this.

[P147]
Of course, there had been some fierce disagreement over it. The Head Elder wanted to place me in a combat unit under the Elder Council faction, while Jin Wikyung had vehemently opposed him.

[P148]
*In the end, they compromised.*

[P149]
I received the relatively undemanding position of reconnaissance squad leader, but under the command of the White Tiger Hall Leader, who belonged to the Elder Council faction.

[P150]
Before I could get a word in, the position was mine.

[P151]
*I never imagined this was how I’d get dragged into the war.*

[P152]
I could have dug in my heels and told them to do their worst, but I held back. The first reason was the Head Elder’s eyes, which flashed every time Yama Whip was mentioned.

[P153]
The second reason was…

[P154]
The children.

[P155]
*It’s a game. It’s all graphics. Nothing but an illusion.*

[P156]
No matter how many times I repeated that to myself, the corpses and the character carved into their foreheads with a knife kept flickering before my eyes.

[P157]
Part of this decision had been emotional.

[P158]
At this rate, things weren’t looking good.

[P159]
*Don’t get sucked in. I can’t confuse reality with the game.*

[P160]
Things like this had been happening more and more often lately. At first, I had treated the NPCs like people for fun. But these days, I was actually thinking of them as real people and forming relationships with them.

[P161]
It startled me every time.

[P162]
Maybe this was a side effect of playing the game for too long.

[P163]
“Is this it?”

[P164]
Before I knew it, I had arrived at the reconnaissance squad’s quarters. My mouth fell open.

[P165]
Cracked wood and a musty smell.

[P166]
Good lord, there was even a beehive under the eaves. I had never seen one that big before.

[P167]
*Just like a company that treats its employees like family…*

[P168]
Look at those benefits.

[P169]
Or maybe it was a mean-spirited prank by the White Tiger Hall Leader, who disliked me. Perhaps he couldn’t openly give me grief yet, so this was his way of telling me to eat shit.

[P170]
*All right. Let’s give it a shot.*

[P171]
I took a deep breath, opened the door, and stepped inside.

[P172]
Creeeak.

[P173]
The old floor wailed beneath my foot, and the sound felt especially ominous.
```


## Accepted baseline for regression comparison

This is the accepted English copy before mastering. Use it as a regression
anchor: report a finding when the assembled copy loses an established term,
source-specific image, formatting convention, continuity fact, or other detail
that the baseline preserved, unless the Korean source clearly requires the
change.

```markdown
[P1]
# Chapter 21

[P2]
Ding.

[P3]
> **System**
>
> - Practiced the **Jin Family’s Cultivation Technique**.
>
> - As a result of repeated practice, **Sinews** and **Bones** each increase by 1.

[P4]
“Whew.”

[P5]
I opened my eyes, exhaling deeply. Before dawn, the candlelit room glowed amber in the darkness.

[P6]
*Failed again.*

[P7]
I clenched my fist.

[P8]
How many times had I tried? Twenty? Thirty? The result was what mattered. Once again, I had failed to draw out the condensed internal energy.

[P9]
*Should I take comfort in the fact that I’m getting better?*

[P10]
I was gradually getting used to handling internal energy. If I had been a C-rank Hunter instead of an F-rank—or at least a D-rank—I would have adapted much faster. But reality was cold and unforgiving.

[P11]
*My Sinews and Bones improving steadily must be helping, too.*

[P12]
Internal energy flowed through the body’s meridians. The more I practiced a cultivation technique, and the more my Sinews and Bones improved, the wider and sturdier those pathways became. Compared to when I had started, I could circulate more internal energy at a much faster speed.

[P13]
*It’s all thanks to the Skill Points.*

[P14]
The ten Skill Points awarded with every level-up were doing their job well. Nothing could nourish my Sinews and Bones better.

[P15]
*Open Skill Window.*

[P16]
> **Skill Window**
>
> **Lv. 17 Jin Taekyung**
>
> **Cultivation Technique:** Jin Family’s Cultivation Technique (Fourth Stage)
>
> **Martial Arts:** Jin Family’s Spear Technique (Fifth Stage) / Jin Family’s Manoeuvre Technique (Fifth Stage)
>
> **Sinews and Bones:** 105
>
> **Remaining Points:** 0

[P17]
*I can see the possibility.*

[P18]
The impregnable fortress was cracking and crumbling. If I kept pounding away at it, I felt as if I could open the gate soon.

[P19]
Fortunately, I might lack talent, but I had persistence.

[P20]
*I’ll keep trying. Until it works.*

[P21]
I was just about to sit cross-legged and begin circulating my qi again when it happened.

[P22]
My senses, sharpened by the earlier rounds of circulating my qi, picked up an unusual sound.

[P23]
*This is…*

[P24]
A low, droning hum. At first, it sounded like a swarm of bees, but it was actually the murmur of many people.

[P25]
*What’s going on?*

[P26]
I let internal energy flow to my ears. Perhaps because of the distance, I couldn’t make out everything clearly. But I heard enough.

[P27]
One word stood out among the indistinct voices.

[P28]
*Battle!*

[P29]
The Mount Heng Sword Sect. The battle had finally begun.

[P30]
I hurriedly uncrossed my legs and stood. Then I leaped through the half-open window.

[P31]
I landed like a cat. Before me, the pavilions lit up one by one.

[P32]
*In the end…*

[P33]
It had begun.

[P34]
* * *

[P35]
Twenty-five.

[P36]
That was the number of corpses laid out in orderly rows.

[P37]
When I saw them lying like dead trees, every trace of vitality gone, I was left speechless.

[P38]
“This is…”

[P39]
I was a Hunter. I had fought countless battles and witnessed death countless times.

[P40]
Poisoned, cut apart, crushed, blown apart…

[P41]
The kinds of death varied wildly depending on the monster involved. But all those deaths had one thing in common.

[P42]
They were all adults.

[P43]
That was one of the basic conditions for awakening. No one knew what the standard was or why it existed. It was a law as naturally established as the existence of Gates.

[P44]
That was why none of the countless deaths I had witnessed had involved a child.

[P45]
*This is a game. It’s just a game.*

[P46]
I kept repeating the words to myself. But the sight before me was too horrific to dismiss so simply.

[P47]
**BLOOD**

[P48]
The character had been carved into their foreheads. Torchlight reflected off the dried blood.

[P49]
More than ten children had gone cold like that.

[P50]
They were middle-school age at most. Some looked even younger. Every single one of them was dead.

[P51]
“Urgh!”

[P52]
One of the martial artists, holding a torch in a shaking hand, doubled over, and soon the sound of retching rang out from all around us.

[P53]
Then a hand reached down and picked up the torch he had dropped.

[P54]
“Somi. That was definitely her name. On the day I became acting Family Head, the Branch Leader of Eung-hyeon bragged about her endlessly, calling her his treasure.”

[P55]
It was Jin Wikyung. With eyes that seemed ready to go out, he lifted the torch and illuminated the children’s faces.

[P56]
One by one.

[P57]
As each face was revealed, he unfailingly spoke its name.

[P58]
After naming the last child, Jin Wikyung looked at me.

[P59]
“Do you know who these children are?”

[P60]
“…No.”

[P61]
“They were members of our family sent to the branches in Eung-hyeon, Saneum, and Sakju.”

[P62]
I didn’t know where those places were. But I could guess what end the children’s parents had met.

[P63]
And I was sickened by the Mount Heng Sword Sect’s intentions.

[P64]
*Those lunatics. Those fucking psychopaths.*

[P65]
*Look. We can slaughter even children this young. Soon, you’ll end up the same way.*

[P66]
I could almost hear the voice of the Mount Heng Sword Sect’s Sect Leader, whose face I had never seen.

[P67]
“This is all my fault. To slaughter even children who don’t know martial arts so cruelly…”

[P68]
Jin Wikyung was blaming himself in a trembling voice when—

[P69]
“That is the essence of war, Lesser Family Head.”

[P70]
The Head Elder appeared, stroking his silver beard. His gaze was calm as he looked over the corpses.

[P71]
“Victory and defeat—neither comes without death. The Mount Heng Sword Sect’s Leader—Blood Wolf Sword Lee Cheonbaek, was it? As one would expect of a former wandering martial artist, he understands war well. These children alone make that clear.”

[P72]
The casual way he said it sent a chill through me.

[P73]
*What the hell is wrong with this AI?*

[P74]
This NPC was missing something. That made him feel even more dangerous.

[P75]
I kept my mouth shut, while Jin Wikyung spoke with a twisted expression.

[P76]
“…Please choose your words carefully. They are members of our family.”

[P77]
“No. Those children are casualties of war. Countless more will die from now on. Perhaps even at this very moment.”

[P78]
“Head Elder. I told you to watch your words.”

[P79]
Jin Wikyung growled. Had we been alone, he would have been ready to start something right then and there.

[P80]
But the Head Elder remained calm.

[P81]
“Did you not anticipate this?”

[P82]
He had suddenly switched to informal speech, yet it was so natural that neither Jin Wikyung nor I even registered it.

[P83]
“Saneum, Eung-hyeon, Sakju. All of them were places within the Mount Heng Sword Sect’s reach. When you sent messenger pigeons to the branches the day before, did you truly not consider that something like this might happen?”

[P84]
“That…”

[P85]
“You knew harm would come to them. Sending those pigeons was nothing more than a way to ease your conscience.”

[P86]
“Enough. Please, enough.”

[P87]
“It was an excellent decision. If you had wanted to save the branches, you would have had to run for seven days and nights without rest, then fight the enemy in a state of extreme exhaustion. Isn’t that right?”

[P88]
Jin Wikyung stared at the Head Elder with a pale face. Fresh blood flowed between his tightly clenched fingers.

[P89]
“I—I…”

[P90]
“Everything comes with a sacrifice. Look at the bigger picture. You are the Lesser Family Head responsible for the hundreds of family members of the Jin Family of Taiyuan.”

[P91]
Jin Wikyung’s body trembled. The anger and sorrow had drained from his face, leaving it filled with a strange emptiness.

[P92]
“Sacrifice…”

[P93]
“The war has only just begun. Isn’t that so, Lesser Family Head?”

[P94]
The Head Elder made a respectful fist-and-palm salute. I bit down hard on my lip.

[P95]
*What an impossible old man to figure out.*

[P96]
The Head Elder was clearly dangerous. His position in the family, his utterly unreadable motives, and even his psychopathic side—he didn’t so much as twitch an eyebrow while looking at the corpses of children.

[P97]
But…

[P98]
*He was right.*

[P99]
From my perspective, Jin Wikyung was a good Lesser Family Head. He was deeply humane and sharp-minded.

[P100]
But the moment he saw the corpses, he had been shaken more than anyone. Without the Head Elder’s cold rebuke, it would have taken him a long time to regain his composure.

[P101]
*He helped. The Head Elder, of all people…*

[P102]
*Were they enemies in peacetime but united during war?*

[P103]
*Then that’s fortunate.*

[P104]
I was looking at the Head Elder with a mixture of suspicion and relief when he spoke.

[P105]
“So the Third Young Master is here as well.”

[P106]
My heart dropped at the sight of those shrewd gray eyes. It was the first time the Head Elder had spoken to me.

[P107]
“Greetings, Head Elder.”

[P108]
The Head Elder looked at me with a strange smile as I did my best to hide my surprise.

[P109]
“I’ve been hearing an interesting rumor within the family lately. Something about… the Sleeping Dragon of Shanxi?”

[P110]
I never expected to hear that ridiculous nickname from the Head Elder.

[P111]
“I’ve also heard that you are acquainted with Yama Whip. They say you joined forces with him to defeat the Heavenly Axe.”

[P112]
“Cough. Cough.”

[P113]
“Are you ill?”

[P114]
“N-no. I’m just feeling a little chilly.”

[P115]
“Oh dear. That won’t do for someone who is about to accomplish great things.”

[P116]
My awkward smile slowly froze.

[P117]
“What do you mean?”

[P118]
“Someone capable of helping eliminate an exceptional demon like the Heavenly Axe is a valuable asset in battle. Surely that rumor isn’t false.”

[P119]
“…”

[P120]
“Therefore, as a direct-line member of our family, I believe it is only natural that you take the lead in battle. What do you think, Lesser Family Head?”

[P121]
The Head Elder smiled faintly. Jin Wikyung, who had been gazing at that smile, asked me,

[P122]
“What do you think?”

[P123]
I was cornered.

[P124]
The moment the word came to mind, a familiar notification rang out.

[P125]
Ding.

[P126]
* * *

[P127]
> **System**
>
> **Quest**
>
> **Mission**
>
> You have been appointed reconnaissance squad leader of White Tiger Hall.
>
> From now on, lead the subordinates assigned under you on missions and build merit!
>
> **Grade:** Repeating Quest  
> **Restriction:** Jin Taekyung  
> **Mission:** Achieve 100 Merit (0 / 100)  
> **Reward:** Changes according to the degree of success.  
> **Failure:** Changes according to the degree of failure.

[P128]
I closed the Quest Window. I had already seen it several times, and besides, the White Tiger Hall martial artist who had been away for a while had just returned.

[P129]
“These are the supplies issued to squad leaders.”

[P130]
A sword.

[P131]
A black martial uniform with a crude white tiger embroidered on it.

[P132]
And a smooth wooden plaque that smelled strongly of fresh wood.

[P133]
That was everything.

[P134]
“The newly assigned members are waiting at the reconnaissance squad’s quarters. The location is…”

[P135]
Fortunately, I knew the place. The pavilion I had passed several times was the quarters assigned to the reconnaissance squad.

[P136]
After leaving White Tiger Hall, I first ducked into an empty alley.

[P137]
*Open Inventory.*

[P138]
Ten seconds was enough to put on the full uniform. I changed clothes, shoved the sword deep into my Inventory, then pulled out the *Sharp Spear*.

[P139]
Until now, I had thoroughly enjoyed the privileges of being the Third Young Master in a lavish private pavilion.

[P140]
But things were different from here on out.

[P141]
*It’s communal living, right?*

[P142]
We would eat together and sleep together. I couldn’t have a two-meter iron spear pop out of thin air whenever I needed one.

[P143]
Once I hung the wooden plaque engraved with *Squad Leader* at my waist, I felt like I’d become Ordinary Martial Artist #1 of the Jin Family of Taiyuan.

[P144]
*Not just an ordinary martial artist. I’m a reconnaissance squad leader.*

[P145]
White Tiger Hall reconnaissance squad leader.

[P146]
I had never expected to receive a position like this.

[P147]
Of course, there had been some fierce disagreement over it. The Head Elder wanted to place me in a combat unit under the Elder Council faction, while Jin Wikyung had vehemently opposed him.

[P148]
*In the end, we reached a compromise.*

[P149]
The mission itself was easy enough, but I would be serving under the command of White Tiger Hall’s Leader, who belonged to the Elder Council faction.

[P150]
Before I knew it, I had received this position.

[P151]
*I never imagined this was how I’d get dragged into the war.*

[P152]
I could have just told them to do whatever the hell they wanted, but I held back. The first reason was the Head Elder’s eyes, which flashed every time Yama Whip was mentioned.

[P153]
The second reason was…

[P154]
The children.

[P155]
*It’s a game. It’s all graphics and nothing more than an illusion.*

[P156]
No matter how many times I repeated that to myself, the corpses and the character carved into their foreheads kept flickering before my eyes.

[P157]
Part of this decision had been emotional.

[P158]
This wasn’t good.

[P159]
*Don’t get immersed. I can’t confuse reality with the game.*

[P160]
Things like this had been happening more and more often lately. At first, I had treated the NPCs like people for fun. But these days, I was actually thinking of them as real people and forming relationships with them.

[P161]
Every time it happened, I was startled.

[P162]
Maybe this was a side effect of playing the game for too long.

[P163]
“Is this it?”

[P164]
Before I knew it, I had arrived at the reconnaissance squad’s quarters, and my mouth fell open.

[P165]
Cracked wood and a musty smell.

[P166]
Good lord, there was even a beehive under the eaves. I had never seen one that big before.

[P167]
*Just like a company that treats you like family…*

[P168]
Look at those benefits.

[P169]
Or maybe it was a mean-spirited prank by the White Tiger Hall Leader, who disliked me. Perhaps he couldn’t openly give me grief yet, so this was his way of telling me to eat shit.

[P170]
*All right. Let’s give it a shot.*

[P171]
I took a deep breath, opened the door, and stepped inside.

[P172]
Creeeak.

[P173]
The old floor let out a wailing sound that felt especially ominous.
```


## Deterministic QA

```json
{
  "version": 1,
  "chapter": 21,
  "passed": true,
  "metrics": {
    "source_characters": 5942,
    "translation_characters": 13575,
    "length_ratio": 2.285,
    "source_paragraphs": 169,
    "translation_paragraphs": 173
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "기세",
        "preferred": "aura / momentum"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "운기조식",
        "preferred": "circulate one's qi"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진가심법",
        "preferred": "Jin Family's Cultivation Technique"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진가보법",
        "preferred": "Jin Family's Manoeuvre Technique"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진가창법",
        "preferred": "Jin Family's Spear Technique"
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
        "korean": "지능",
        "preferred": "Intelligence"
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
