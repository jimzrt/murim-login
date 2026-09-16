# Fidelity Gate — Chapter 118

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
  1|＃118화
  2|
  3|
  4|
  5|“너만 약 처먹으니까 좋았냐?”
  6|
  7|“뭐?”
  8|
  9|“혼자 약 처먹으니까 좋았냐고.”
 10|
 11|풍양은 헛웃음을 흘렸다.
 12|
 13|이제 고작 약관에 불과한 핏덩이 주제에 혀가 짧아도 너무 짧다. 태원진가의 막내 도련님으로 태어나 잠룡 소리를 듣고 있어 눈에 보이는 게 없는 건가?
 14|
 15|“그놈 참, 허허.”
 16|
 17|껍데기뿐인 웃음소리는 얼마 지나지 않아 잦아들고, 살기 어린 눈빛이 빈자리를 채웠다.
 18|
 19|“관을 봐야 눈물 흘리겠느냐?”
 20|
 21|진태경이 눈을 크게 떴다.
 22|
 23|“이야, 저 대사 실제로 들으니까 되게 이상하네. 다시 해 봐.”
 24|
 25|“말로 해선 안 되는 놈이군.”
 26|
 27|풍양은 느긋한 걸음걸이로 다가가며 생각했다. 어떻게 해야 저 어린놈의 주둥이에서 살려 달라는 말이 나올까?
 28|
 29|그가 평소 자주 사용하는 방법은 혀를 뽑고 사지를 잘근잘근 부러트리는 거다. 하지만 태원진가의 무공을 알려 줄 귀한 몸을 그리 함부로 대할 수가 있나.
 30|
 31|적당한 타협이 필요했다.
 32|
 33|‘다리 근맥을 끊어 놓으면 얌전해지겠지.’
 34|
 35|태원진가와는 이미 돌이킬 수 없는 강을 건넜다. 풍양은 이 싸움이 끝나면 사람의 발이 닿지 않는 심산유곡에서 무공을 보완한 다음 다시 무림에 나올 생각이었다.
 36|
 37|적풍단은 궤멸당했지만, 세력은 얼마든지 다시 모을 수 있다. 무림은 강자가 지배하는 곳이니까.
 38|
 39|“전부 네가 자초한 일이니 날 원망 말거라.”
 40|
 41|풍양이 곡도를 움켜쥔 그때였다.
 42|
 43|“아, 잠깐만.”
 44|
 45|손을 내저은 진태경이 뭔가를 입 안에 탁 털어 넣는다.
 46|
 47|너무나도 자연스러운 모습에 풍양은 멈칫할 수밖에 없었다.
 48|
 49|‘뭐 하는 거지?’
 50|
 51|의문도 잠시.
 52|
 53|한차례 몸을 부르르 떤 진태경의 전신에서 엄청난 열기가 피어오르기 시작했다.
 54|
 55|
 56|
 57|* * *
 58|
 59|
 60|
 61|어차피 내게 주어진 선택지는 하나밖에 없었다. 열화신단으로 최후의 도박을 벌이는 것.
 62|
 63|위험성이 크긴 하지만 풍양에게 무공 구결을 토해 내고 죽는 것보다는 백배 나은 선택이다.
 64|
 65|꿀꺽.
 66|
 67|과연 영단은 영단인지, 혀에 닿자마자 스르륵 녹아 목으로 넘어간다. 문제는 그다음부터였다.
 68|
 69|띠링.
 70|
 71|
 72|
 73|- [열화신단]을 복용했습니다.
 74|
 75|- [운기조식]으로 기운을 다스리십시오.
 76|
 77|
 78|
 79|뜨겁다. 열화신단이 품고 있던 30년의 공력이 사지백해로 들불처럼 퍼져 나갔다.
 80|
 81|
 82|
 83|- 일시적으로 [열양지기]의 속성을 부여받았습니다.
 84|
 85|- 일시적으로 [공력]이 45년으로 상승합니다.
 86|
 87|- 기운을 다스리지 못하면 죽음에 이를 수도 있습니다!
 88|
 89|- 퀘스트, [영단 흡수]가 생성되었습니다.
 90|
 91|
 92|
 93|끊임없이 울리는 시스템 알림을 확인할 여유 따위는 없었다. 당장 몸 안에서 날뛰는 열화신단의 기운을 제어하는 것만으로도 벅찼으니까.
 94|
 95|“후우, 후우우우.”
 96|
 97|인간 압력밥솥이 된 기분이다. 마치 정말 불이라도 난 것처럼 전신에서 연기가 모락모락 솟아올랐다.
 98|
 99|딛고 선 땅 위로 덮여 있던 눈이 녹고, 축축한 흙이 물처럼 흐물흐물해졌다.
100|
101|‘어느 정도 예상했지만 이건…….’
102|
103|정말이지 상상 이상이다. 비명도 지르지 못하고 몸을 부르르 떠는 내 귓가로 풍양의 목소리가 파고들었다.
104|
105|“무슨 짓을 한 거냐!”
106|
107|당황한 놈의 얼굴을 보자 오히려 살짝 열기가 가라앉는 기분이다.
108|
109|나는 억지로 입꼬리를 끌어 올리며 대답했다.
110|
111|“무슨 짓이긴, 갈 데까지 가 보자는 거지.”
112|
113|“놈!”
114|
115|대답에서 불길함을 느낀 걸까? 풍양의 곡도가 눈부신 속도로 날아들었다. 쭉 뻗어 나온 붉은 도기(刀氣)가 내 가슴을 노린다.
116|
117|쉭!
118|
119|딱 반걸음 차이로 죽음이 빗겨 나간다. 목표를 놓친 곡도가 다시 한번 어지러운 궤적을 그렸다.
120|
121|쉬쉬쉬쉭!
122|
123|그러나 이번에도 곡도는 헛되이 허공을 갈랐다. 어느새 뒤로 물러난 나를 바라보는 풍양의 얼굴이 일그러졌다.
124|
125|“너……!”
126|
127|“뭐, 인마.”
128|
129|애써 태연하게 대꾸했지만 사실 가장 놀란 건 나였다. 앞서 손을 섞었을 때는 이 정도로 손쉽게 피해 내지 못했다.
130|
131|풍양의 압도적인 기세와 도기에 밀려 피하기에 급급했던 그때와는 차원이 다르다.
132|
133|‘언제부터 몸이 이렇게 가벼웠지?’
134|
135|공격을 피해야겠다고 생각한 순간, 몸이 그 어느 때보다 빠르게 움직였다. 달라진 것은 그뿐만이 아니다.
136|
137|‘똑똑히 보인다.’
138|
139|풍양의 움직임 하나하나가 보이고, 읽힌다. 공격이 보이니 못 피할 것도 없다. 도기가 아니라 도강(刀罡)이라 해도 피할 수 있을 것 같은 기분이다.
140|
141|나는 마침내 그 이유를 깨달았다.
142|
143|‘공력 때문이야.’
144|
145|기존에 갖고 있던 15년의 공력과 열화신단의 30년 공력이 합쳐진 상태다. 비록 내가 완벽히 통제할 수는 없지만 그렇다고 해서 30년의 공력이 가진 힘이 없어지는 것이 아니다.
146|
147|부풀어 오른 풍선처럼, 열화신단의 기운은 내 전신을 가득 채우고 있었다.
148|
149|‘문제는 이 풍선이 언제 터질지 모른다는 거지만.’
150|
151|그러니 그 전에 풍양을 쓰러트려야 한다.
152|
153|나는 속에서 부글부글 끓어오르는 열기를 느끼며 철창을 고쳐 잡았다.
154|
155|“덤벼.”
156|
157|풍양이 입술을 깨물었다.
158|
159|“어린놈이 벌써부터 기고만장하군. 네놈 정도로는 어림도 없다.”
160|
161|“그런 것치곤 꽤 긴장한 것 같은데.”
162|
163|“맹수는 토끼를 잡는 일에도 최선을 다하는 법이지.”
164|
165|“근데 맹수는 토끼 잡을 때 잠력단 안 먹잖아.”
166|
167|“……!”
168|
169|풍양의 낯빛 위로 경악이 스쳤다. 입을 벌린 채 나를 응시하던 놈이 더듬더듬 물었다.
170|
171|“자, 잠력단이라고?”
172|
173|“그래, 잠력단.”
174|
175|“그 이름을 네가 어떻게?”
176|
177|“기업 비밀이다, 이 새끼야.”
178|
179|“혹시 네놈도?”
180|
181|“뭐, 비슷한 거 먹긴 했지.”
182|
183|열화신단이라고 말하면 알까 모르겠다.
184|
185|잠력단이랑 비교하면 안정성은 영 꽝이고, 효과가 어느 정도인지는 지금부터 알아볼 생각이다.
186|
187|“넌 뒈졌어.”
188|
189|마지막 한마디와 함께 땅을 박찼다.
190|
191|쐐애애액!
192|
193|
194|
195|* * *
196|
197|
198|
199|풍양은 심란했다.
200|
201|‘저놈이 어떻게 잠력단의 존재를 알고 있지?’
202|
203|잠력단의 존재는 무덤까지 안고 가야 할 비밀이다.
204|
205|언젠가 목숨을 구해 줄 숨겨 둔 한 수이기도 했지만, 세상에 알려진다면 피바람을 불러일으킬 기물(奇物)이기 때문이다.
206|
207|복용자가 가진 힘의 두 배, 세 배를 끌어 올릴 수 있는 효능만 봐도 천하의 무인들이 군침을 삼키고 달려들 텐데.
208|
209|그러나 그보다 더 큰 문제는 따로 있었다.
210|
211|‘사마외도(邪魔外道)의 유산이니까.’
212|
213|정마대전 이후 천하 무림은 정파 무림의 손아귀에 들어갔다.
214|
215|풍양이 사마외도의 기연을 이었다는 소문이라도 퍼진다면 태원진가가 아니라 천하 무림이 그를 쫓기 시작할 것이다.
216|
217|‘산서잠룡 진태경…… 반드시 죽여서 후환을 없애야 한다.’
218|
219|풍양은 이를 악물고 무공을 펼쳤다.
220|
221|단 몇 년간의 수련으로 어느덧 칠 성의 경지에 오른 적혈십이도(赤血十二刀)다. 나이로도, 무공으로도 턱없이 부족한 저 어린놈을 죽이기에는 차고 넘친다.
222|
223|“죽엇!”
224|
225|쉬잉-!
226|
227|적혈십이도는 패도적인 무공, 곡도에서 쭉 뻗어 나간 붉은 도기가 사방을 난도질했다. 그 흉험한 기세에 땅거죽이 갈라지고, 바람이 터져 나갔다.
228|
229|그러나 정작 베어야 할 목표는 이미 그곳에 없었다.
230|
231|딱 반걸음 차이로 공격을 피해 낸 진태경이 창을 찔렀다.
232|
233|쐐애애액!
234|
235|목젖을 노리고 찔러 들어오는 창날. 황급히 고개를 꺾어 공격을 피한 풍양은 가슴 한구석이 서늘해졌다.
236|
237|‘빠르다.’
238|
239|빠르고 정확하다. 절정 고수의 상징인 검기상인(劍氣傷人)의 경지에까지는 이르지 못했지만 움직임은 이미 그를 따라잡고 있었다.
240|
241|‘설마 이 녀석도 잠력단을? 아니다. 나와는 전혀 달라.’
242|
243|이미 잠력단을 몇 번 복용한 전력이 있는 풍양이다.
244|
245|전신이 시뻘겋게 달아오른 진태경의 모습으로 앞서 그가 삼킨 것이 잠력단이 아니라는 사실을 알 수 있었다.
246|
247|‘그럼 도대체 뭘…… 헛!’
248|
249|풍양은 생각을 이어 갈 수 없었다. 마침내 공세를 잡은 진태경이 본격적으로 진가창법을 펼쳐 내기 시작했기 때문이었다.
250|
251|쉬쉬쉬쉬쉭!
252|
253|소나기처럼 쏟아지는 수십 개의 창영(槍影). 보기만 해도 숨이 막히는 광경이다. 아니, 착각이 아니라 실제로도 그랬다.
254|
255|풍양의 이마에서 땀 한 방울이 굴러떨어졌다.
256|
257|‘이건…….’
258|
259|열양지기.
260|
261|그것도 절정 고수인 자신에게까지 영향을 줄 만큼 엄청난 열양지기다. 앞서 싸웠던 항산호 철무백도 열양지기의 소유자였지만 지금 진태경이 뿜어내는 것에 비할 바가 아니다.
262|
263|‘영단, 열양 계열의 영단을 먹었구나!’
264|
265|후우우웅!
266|
267|알아챈다고 달라지는 것은 없었다. 아찔한 열기와 날카로운 공격. 연달아 물러서며 창날을 피하는 데에 급급하던 풍양이 입술을 질끈 깨물었다.
268|
269|‘고작 이런 어린놈한테!’
270|
271|일평생을 치열하게 살아온 그다. 잠력단까지 복용한 지금, 이제야 이름을 알리기 시작한 어린놈을 상대로 물러서는 자신이 수치스러웠다.
272|
273|그 분노가 고스란히 곡도에 실렸다. 도신 위로 피어오른 도기가 그 어느 때보다 붉게 타올랐다.
274|
275|쉬이익!
276|
277|진가창법과 적혈십이도는 사용하는 병기와 투로는 다를지 몰라도 패도적인 무공이라는 공통점이 있다.
278|
279|눈 깜빡할 시간, 진무경의 철창과 풍양의 곡도가 십여 합의 치열한 격돌 끝에 떨어졌다.
280|
281|“음.”
282|
283|먼저 물러난 것은 진태경이었다. 찢어진 손아귀에서는 피가 흘렀고, 무겁고 견고하던 철창은 예리한 도기에 잘려 나가 채 반도 남지 않았다.
284|
285|“멍청한 놈.”
286|
287|풍양은 득의양양한 웃음을 지었다. 무인이 병장기를 잃었다는 것은 패배를 의미했다.
288|
289|오로지 권각으로 일가를 이룬 항산호 철무백도 자신에게 무릎을 꿇었는데, 아직 절정의 벽도 넘지 못한 진태경은 무기를 잃은 순간 이미 죽은 것이나 마찬가지다.
290|
291|“정면 승부로 날 꺾을 수 있을 거라 생각했더냐?”
292|
293|진태경이 손아귀에 묻은 피를 문질러 닦으며 대답했다.
294|
295|“아니, 그 대신 귀중한 정보를 알았지.”
296|
297|“……귀중한 정보?”
298|
299|“그래, 너의 공격 패턴을 알았다.”
300|
301|“패, 뭐?”
302|
303|“너의 공격 패턴은 강강강강강이다.”
304|
305|이건 무슨 개소린가.
306|
307|자신의 무공에 관한 이야기라는 건 알겠는데 패 뭐시기라는 말은 난생처음 들어 본다. 게다가 강강강강강이라니?
308|
309|풍양은 살기 어린 눈빛으로 진태경을 노려봤다.
310|
311|“헛소리를 한 대가로 사지 근맥을 잘라 주마.”
312|
313|진태경이 심드렁한 얼굴로 입을 열었다.
314|
315|“사지 자르고 뽑는 거 되게 좋아하네. 사지 성애자야?”
316|
317|“이 애새끼가…….”
318|
319|“이 늙은 새끼가…….”
320|
321|풍양은 깊게 심호흡했다. 그는 절정 고수였고 일평생을 냉철한 이성의 소유자로 살았다. 하지만 분노로 뚝뚝 끊기는 목소리만큼은 어쩔 수 없었다.
322|
323|“넌, 반드시, 내 손으로, 죽인다.”
324|
325|“난, 가끔, 사지를, 자른다, 가끔은, 이런 내가, 별로다.”
326|
327|그는 인내심이 뚝 끊어지는 것을 느꼈다. 단언컨대 근 십 년간 이 정도로 분노한 적은 처음이다.
328|
329|“크아아악!”
330|
331|비명인지 고함인지 모를 괴성을 내지른 풍양은 광인(狂人)처럼 돌진했다.
332|
333|그 어떤 초식도, 무공도 없이 있는 힘껏 진태경의 정수리 위로 곡도를 내리쳤다.
334|
335|“죽엇!”
336|
337|그때였다. 살기로 번들거리는 풍양의 핏빛 눈동자에 진태경의 담담한 표정이 비친 것은.
338|
339|순간 찬물을 뒤집어쓴 것처럼 정신이 번쩍 들었다.
340|
341|‘뭔가 잘못됐다.’
342|
343|풍양은 공력을 있는 힘껏 끌어올렸다.
344|
345|호신강기가 일어남과 동시에 텅 비어 있던 진태경의 손아귀에서 비수가 번쩍였다.
346|
347|푹!
```

## Assembled English

```markdown
[P1]
# Chapter 118

[P2]
“Was it fun being the only one popping pills?”

[P3]
“What?”

[P4]
“I asked if it was fun popping pills all by yourself.”

[P5]
Pung Yang let out a hollow laugh.

[P6]
*For a mere brat barely twenty, his speech was far too disrespectful. Had being born the youngest young master of the Jin Family of Taiyuan and being called the Sleeping Dragon made him think he could get away with anything?*

[P7]
“What a brat. Heh.”

[P8]
The hollow laughter soon faded, and killing intent filled his eyes.

[P9]
“Must you see the coffin before you shed tears?”

[P10]
Jin Taekyung’s eyes widened.

[P11]
“Wow, that line sounds really weird when you hear it in real life. Say it again.”

[P12]
“You’re beyond reasoning with.”

[P13]
As he approached at a leisurely pace, Pung Yang wondered how he could make that young brat beg for his life.

[P14]
His usual method was to pull out the tongue and slowly break all four limbs. But he couldn’t treat a valuable body that knew the Jin Family of Taiyuan’s martial arts so carelessly.

[P15]
A reasonable compromise was necessary.

[P16]
*If I sever the sinews and meridians in his legs, he’ll quiet down.*

[P17]
He had already crossed a river of no return with the Jin Family of Taiyuan. Once this fight was over, Pung Yang planned to retreat into some remote mountain valley untouched by human feet, refine his martial arts, and then return to the Murim.

[P18]
The Red Wind Band had been annihilated, but he could always gather another force. The Murim was ruled by the strong, after all.

[P19]
“You brought all of this upon yourself, so don’t blame me.”

[P20]
Pung Yang was just tightening his grip on his curved saber when—

[P21]
“Ah, wait a second.”

[P22]
Jin Taekyung held up a hand, then casually tossed something into his mouth.

[P23]
The action was so natural that Pung Yang couldn’t help stopping.

[P24]
*What is he doing?*

[P25]
His question was answered a moment later.

[P26]
After Jin Taekyung’s body shuddered once, tremendous heat began to rise from every inch of him.

[P27]
* * *

[P28]
I had only one option left.

[P29]
One final gamble with the Blazing Flame Divine Pill.

[P30]
It was dangerous, but still a hundred times better than dying after Pung Yang forced me to cough up the formulas for the Jin Family’s martial arts.

[P31]
Gulp.

[P32]
True to its status as a divine elixir, the pill melted the instant it touched my tongue and slid down my throat. The problem began after that.

[P33]
*Ding.*

[P34]
> **System**
> - You have taken the **Blazing Flame Divine Pill**.
> - **Circulate your qi** to control its energy.

[P35]
Hot.

[P36]
The thirty years of internal energy contained within the Blazing Flame Divine Pill spread through every part of my body like wildfire.

[P37]
> **System**
> - You have temporarily gained the **Scorching Yang Qi** attribute.
> - Your **internal energy** has temporarily increased to 45 years.
> - If you cannot control the energy, you may die!
> - Quest, **Divine Pill Absorption**, has been created.

[P38]
I had no time to check the System notifications chiming incessantly in my ears. I already had my hands full trying to control the Blazing Flame Divine Pill’s energy as it rampaged through my body.

[P39]
“Hoo. Hooooo.”

[P40]
I felt like a human pressure cooker. Smoke curled from my entire body as though I were actually on fire.

[P41]
The snow beneath my feet melted, and the damp earth softened until it ran like water.

[P42]
*I expected it to some extent, but this is…*

[P43]
It was far beyond anything I’d imagined. I couldn’t even scream. All I could do was tremble as Pung Yang’s voice cut into my ears.

[P44]
“What have you done?”

[P45]
Seeing the bewilderment on his face actually made the heat subside a little.

[P46]
I forced the corners of my mouth upward.

[P47]
“What else? I’m going all in.”

[P48]
“You brat!”

[P49]
Had he sensed something ominous in my answer? Pung Yang’s curved saber flew toward me at a blinding speed. A red strand of saber qi extended from the blade and aimed for my chest.

[P50]
*Swish!*

[P51]
Death missed me by exactly half a step. The curved saber missed its target and drew another dizzying arc.

[P52]
*Shh-shh-shh-shhk!*

[P53]
But once again, the blade only cut through empty air. Pung Yang’s face twisted as he stared at me, already backed away.

[P54]
“You…!”

[P55]
“What, asshole?”

[P56]
I answered as casually as I could, but no one was more surprised than me. When we’d crossed hands earlier, I hadn’t been able to dodge him this easily.

[P57]
This was on an entirely different level from before, when Pung Yang’s overwhelming aura and saber qi had forced me to do nothing but evade.

[P58]
*Since when has my body felt this light?*

[P59]
The instant I thought I needed to avoid an attack, my body moved faster than ever before. And that wasn’t the only thing that had changed.

[P60]
*I can see everything clearly.*

[P61]
I could see and read every one of Pung Yang’s movements. If I could see his attacks, there was no reason I couldn’t evade them. I felt like I could dodge even saber force, let alone saber qi.

[P62]
At last, I understood why.

[P63]
*It’s the internal energy.*

[P64]
My original fifteen years of internal energy had combined with the thirty years from the Blazing Flame Divine Pill. I couldn’t control it perfectly, but that didn’t mean the power of those thirty years had vanished.

[P65]
Like an overinflated balloon, the Blazing Flame Divine Pill’s energy filled my entire body.

[P66]
*The problem is that I have no idea when this balloon will burst.*

[P67]
So I had to take Pung Yang down before it did.

[P68]
Feeling the heat bubbling up inside me, I adjusted my grip on the iron spear.

[P69]
“Come at me.”

[P70]
Pung Yang bit his lip.

[P71]
“Young brat, you’re already getting cocky. Someone like you doesn’t stand a chance against me.”

[P72]
“You look pretty tense for someone saying that.”

[P73]
“A wild beast gives its all even when catching a rabbit.”

[P74]
“But a wild beast doesn’t take a Temporary Strength Pill to catch a rabbit.”

[P75]
“…!”

[P76]
Shock flashed across Pung Yang’s face. He stared at me with his mouth hanging open, then stammered.

[P77]
“T-Temporary Strength Pill?”

[P78]
“Yeah. Temporary Strength Pill.”

[P79]
“How do you know that name?”

[P80]
“Corporate secret, asshole.”

[P81]
“Did you take one too?”

[P82]
“Well, I did eat something similar.”

[P83]
I wondered whether he would recognize the name Blazing Flame Divine Pill.

[P84]
Compared to the Temporary Strength Pill, its stability was complete garbage. As for how powerful its effects were, I intended to find out right now.

[P85]
“You’re fucking dead.”

[P86]
With those final words, I kicked off the ground.

[P87]
*Shweeeeeek!*

[P88]
* * *

[P89]
Pung Yang was deeply troubled.

[P90]
*How does that brat know about the Temporary Strength Pill?*

[P91]
The existence of the Temporary Strength Pill was a secret he had to take to his grave.

[P92]
It was a hidden trump card that might one day save his life. But if word of it spread, this wondrous object would bring a bloodbath upon the world.

[P93]
Just the fact that it could draw out two or three times the power of the person who took it would be enough to make martial artists throughout the land salivate and come running.

[P94]
But there was an even greater problem.

[P95]
*It’s a legacy of demonic, heterodox arts.*

[P96]
After the Great Faction War, the Murim had fallen into the hands of the orthodox factions.

[P97]
If even a rumor spread that Pung Yang had inherited the legacy of demonic, heterodox arts, it wouldn’t be only the Jin Family of Taiyuan pursuing him. The entire Murim would come after him.

[P98]
*Jin Taekyung, the Sleeping Dragon of Shanxi… I must kill him and eliminate the trouble he’ll cause later.*

[P99]
Pung Yang gritted his teeth and unleashed his martial art.

[P100]
After only a few years of training, he had already attained seventy percent mastery of the Crimson Blood Twelve Sabers. It was more than enough to kill a brat hopelessly beneath him in both age and martial arts.

[P101]
“Die!”

[P102]
*Shiiing!*

[P103]
The Crimson Blood Twelve Sabers was a domineering martial art. Red saber qi shot from the curved saber and slashed wildly in every direction. The fierce momentum split open the surface of the earth and burst the air apart.

[P104]
Yet the target it was meant to cut was no longer there.

[P105]
Jin Taekyung dodged the attack by exactly half a step and thrust his spear.

[P106]
*Shweeeeeek!*

[P107]
The spearhead drove toward Pung Yang’s throat. He hastily twisted his head aside to evade it, and a chill ran through his chest.

[P108]
*Fast.*

[P109]
Fast and accurate. Jin Taekyung had yet to reach the stage of injuring others with Sword Energy, the hallmark of a Peak master, but his movements had already caught up to Pung Yang’s.

[P110]
*Could this brat have taken the Temporary Strength Pill too? No. It’s completely different from mine.*

[P111]
Pung Yang had taken the Temporary Strength Pill several times before.

[P112]
One look at Jin Taekyung’s body, flushed bright red with heat, was enough to tell him that the pill the brat had swallowed wasn’t a Temporary Strength Pill.

[P113]
*Then what did he—wait!*

[P114]
Pung Yang couldn’t finish the thought. Jin Taekyung had finally seized the initiative and begun unleashing the Jin Family’s Spear Technique in earnest.

[P115]
*Shh-shh-shh-shh-shhk!*

[P116]
Dozens of spear shadows poured down like a rain shower. The sight alone was suffocating.

[P117]
No, it wasn’t just an illusion. It really was suffocating.

[P118]
A bead of sweat rolled down Pung Yang’s forehead.

[P119]
*This is…*

[P120]
Scorching Yang Qi.

[P121]
And not just any Scorching Yang Qi. It was powerful enough to affect even Pung Yang, a Peak master. The Tiger of Mount Heng, Cheol Mubaek, had also possessed Scorching Yang Qi, but it couldn’t compare to what Jin Taekyung was emitting now.

[P122]
*He took a divine elixir—a Scorching Yang-type divine elixir!*

[P123]
*Whooooom!*

[P124]
Recognizing it changed nothing. The heat was dizzying, and the attacks were sharp. Pung Yang bit down hard on his lip as he retreated again and again, barely evading the spearhead.

[P125]
*Against a brat this young!*

[P126]
He had lived his entire life fiercely. Now, even after taking the Temporary Strength Pill, he felt humiliated to be driven back by a young brat who had only just begun making a name for himself.

[P127]
That anger flowed straight into his curved saber. The saber qi rising over the blade blazed redder than ever.

[P128]
*Hiss!*

[P129]
The Jin Family’s Spear Technique and the Crimson Blood Twelve Sabers differed in both weapon and form, but they had one thing in common: both were domineering martial arts.

[P130]
In the blink of an eye, Jin Mukyung’s iron spear and Pung Yang’s curved saber finally parted after more than ten fierce exchanges.

[P131]
“Hmm.”

[P132]
Jin Taekyung was the first to retreat. Blood flowed from his torn palm, and the heavy, sturdy iron spear had been cut by the sharp saber qi until less than half of it remained.

[P133]
“You fool.”

[P134]
Pung Yang smiled triumphantly. For a martial artist, losing one’s weapon meant defeat.

[P135]
Even the Tiger of Mount Heng, Cheol Mubaek, who had built his reputation with nothing but his fists and feet, had knelt before Pung Yang. Jin Taekyung hadn’t even crossed the wall into the Peak realm. The moment he lost his weapon, he was as good as dead.

[P136]
“Did you think you could defeat me head-on?”

[P137]
Jin Taekyung wiped the blood from his palm and answered.

[P138]
“No. But I did learn some valuable information.”

[P139]
“…Valuable information?”

[P140]
“Yeah. I figured out your attack pattern.”

[P141]
“Pat—what?”

[P142]
“Your attack pattern is strong, strong, strong, strong, strong.”

[P143]
*What kind of bullshit is this?*

[P144]
Pung Yang understood that the brat was talking about his martial arts, but he had never heard of this “pattern-whatever” before. And what did he mean by strong, strong, strong, strong, strong?

[P145]
Pung Yang glared at Jin Taekyung with murder in his eyes.

[P146]
“I’ll sever the sinews and meridians in all four of your limbs as payment for that nonsense.”

[P147]
Jin Taekyung opened his mouth with a bored expression.

[P148]
“You really like cutting off and pulling out people’s limbs. Do you have a limb fetish?”

[P149]
“You little bastard…”

[P150]
“You old bastard…”

[P151]
Pung Yang drew a deep breath. He was a Peak master who had spent his entire life possessing a cool, rational mind. But he couldn’t stop his voice from breaking into pieces with anger.

[P152]
“You. Will. Die. By. My. Hand.”

[P153]
“I. Sometimes. Cut off. Limbs. Sometimes. I don’t like this version of myself.”

[P154]
He felt his patience snap. He could swear that he had never been this furious in nearly ten years.

[P155]
“Graaaargh!”

[P156]
Pung Yang charged like a madman, unleashing a strange cry that could have been either a scream or a roar.

[P157]
Without using any form or martial art, he brought the curved saber down over the crown of Jin Taekyung’s head with all his strength.

[P158]
“Die!”

[P159]
That was when Jin Taekyung’s calm expression was reflected in Pung Yang’s bloodshot eyes gleaming with killing intent.

[P160]
In an instant, his mind snapped clear as though someone had dumped cold water over him.

[P161]
*Something’s wrong.*

[P162]
Pung Yang drew up his internal energy with all his might.

[P163]
As his Body-Protecting Qi rose, a dagger flashed in Jin Taekyung’s previously empty hand.

[P164]
*Shnk!*
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
# Chapter 118

[P2]
“Was it fun being the only one shoving pills down your throat?”

[P3]
“What?”

[P4]
“I asked if it was fun shoving pills down your throat all by yourself.”

[P5]
Pung Yang let out a hollow laugh.

[P6]
*For a mere brat barely twenty, his speech was far too disrespectful. Had being born the youngest young master of the Jin Family of Taiyuan and being called the Sleeping Dragon made him think he could get away with anything?*

[P7]
“What a brat. Heh.”

[P8]
The empty laughter soon died away, and murderous eyes took its place.

[P9]
“Must you see the coffin before you shed tears?”

[P10]
Jin Taekyung’s eyes widened.

[P11]
“Wow, hearing that line in real life makes it sound really weird. Try it again.”

[P12]
“You’re a brat who can’t be reasoned with.”

[P13]
As he approached at a leisurely pace, Pung Yang wondered how he could make that young brat beg for his life.

[P14]
His usual method was to pull out the tongue and slowly break all four limbs. But he couldn’t treat a valuable body that knew the Jin Family of Taiyuan’s martial arts so carelessly.

[P15]
A reasonable compromise was necessary.

[P16]
*If I sever the meridians in his legs, he’ll quiet down.*

[P17]
He had already crossed an irreversible river with the Jin Family of Taiyuan. Once this fight was over, Pung Yang planned to retreat into some remote mountain valley untouched by human feet, refine his martial arts, and then return to the Murim.

[P18]
The Red Wind Band had been annihilated, but he could gather a force again whenever he wanted. The Murim was a place ruled by the strong, after all.

[P19]
“Everything that happened was brought on by you, so don’t blame me.”

[P20]
Pung Yang was just tightening his grip on the curved saber when—

[P21]
“Ah, wait a second.”

[P22]
Jin Taekyung held up a hand, then casually tossed something into his mouth.

[P23]
The action was so natural that Pung Yang couldn’t help stopping.

[P24]
*What is he doing?*

[P25]
His question was answered a moment later.

[P26]
After Jin Taekyung’s body shuddered once, tremendous heat began to rise from every inch of him.

[P27]
* * *

[P28]
I had only one option left.

[P29]
To make one last gamble with the Blazing Flame Divine Pill.

[P30]
It was a dangerous choice, but it was a hundred times better than dying after being forced to spit out the Jin Family’s martial arts formulas for Pung Yang.

[P31]
Gulp.

[P32]
True to its name, the divine elixir melted the moment it touched my tongue and slid down my throat. The problem began after that.

[P33]
*Ding.*

[P34]
> **System**
> - You have taken the **Blazing Flame Divine Pill**.
> - **Circulate your qi** to control your energy.

[P35]
It was hot. The thirty years of internal energy contained within the Blazing Flame Divine Pill spread through every part of my body like wildfire.

[P36]
> **System**
> - You have temporarily gained the **Scorching Yang Qi** attribute.
> - Your **internal energy** has temporarily increased to 45 years.
> - If you cannot control your energy, you may die!
> - Quest, **Divine Pill Absorption**, has been created.

[P37]
I had no time to check the System notifications that continued ringing in my ears. Controlling the Blazing Flame Divine Pill’s energy rampaging through my body was already more than enough.

[P38]
“Hoo. Hooooo.”

[P39]
I felt like a human pressure cooker. It was as though a real fire had broken out inside me, and wisps of smoke rose from my entire body.

[P40]
The snow covering the ground beneath my feet melted, and the damp earth softened until it flowed like water.

[P41]
*I expected something this bad, but this is…*

[P42]
It was far beyond my imagination. I couldn’t even scream. I could only tremble as Pung Yang’s voice pierced my ears.

[P43]
“What have you done?”

[P44]
Seeing the bewilderment on his face actually made the heat subside a little.

[P45]
I forced the corners of my mouth upward and answered.

[P46]
“What else? I’m going all in.”

[P47]
“You brat!”

[P48]
Had he sensed something ominous in my answer? Pung Yang’s curved saber flew toward me at a blinding speed. A red strand of saber qi extended from the blade and aimed for my chest.

[P49]
*Swish!*

[P50]
Death passed me by at a distance of exactly half a step. The curved saber missed its target and drew another chaotic arc.

[P51]
*Shh-shh-shh-shhk!*

[P52]
But once again, the blade only cut through empty air. Pung Yang’s face twisted as he stared at me, already backed away.

[P53]
“You…!”

[P54]
“What, asshole?”

[P55]
I answered as casually as I could, but the person most surprised was me. When we had crossed hands earlier, I hadn’t been able to dodge so easily.

[P56]
This was on an entirely different level from before, when Pung Yang’s overwhelming aura and saber qi had forced me to do nothing but evade.

[P57]
*Since when has my body felt this light?*

[P58]
The instant I thought I needed to avoid an attack, my body moved faster than ever before. And that wasn’t the only thing that had changed.

[P59]
*I can see everything clearly.*

[P60]
I could see and read each of Pung Yang’s movements. If I could see the attacks, there was no reason I couldn’t evade them. I felt like I could dodge even saber force, not just saber qi.

[P61]
At last, I understood why.

[P62]
*It’s because of my internal energy.*

[P63]
My original fifteen years of internal energy had merged with the thirty years from the Blazing Flame Divine Pill. I couldn’t control it perfectly, but that didn’t mean the power of thirty years of internal energy had simply disappeared.

[P64]
Like an overinflated balloon, the Blazing Flame Divine Pill’s energy filled my entire body.

[P65]
*The problem is that I have no idea when this balloon will burst.*

[P66]
So I had to take down Pung Yang before that happened.

[P67]
Feeling the heat bubbling up inside me, I adjusted my grip on the iron spear.

[P68]
“Come at me.”

[P69]
Pung Yang bit his lip.

[P70]
“Young brat, you’re already getting cocky. Someone like you is nowhere near strong enough.”

[P71]
“You look pretty tense for someone saying that.”

[P72]
“A wild beast gives its all even when catching a rabbit.”

[P73]
“But a wild beast doesn’t take a Temporary Strength Pill to catch a rabbit.”

[P74]
“...!”

[P75]
Shock flashed across Pung Yang’s face. He stared at me with his mouth hanging open, then stammered.

[P76]
“Y-You mean the Temporary Strength Pill?”

[P77]
“Yeah. The Temporary Strength Pill.”

[P78]
“How do you know that name?”

[P79]
“Corporate secret, asshole.”

[P80]
“Did you take one too?”

[P81]
“Well, I did eat something similar.”

[P82]
I wondered whether he would recognize the name if I called it the Blazing Flame Divine Pill.

[P83]
Compared to the Temporary Strength Pill, its stability was complete garbage. I intended to find out exactly how powerful its effects were starting now.

[P84]
“You’re fucking dead.”

[P85]
With those final words, I kicked off the ground.

[P86]
*Shweeeeeek!*

[P87]
* * *

[P88]
Pung Yang was deeply troubled.

[P89]
*How does that brat know about the Temporary Strength Pill?*

[P90]
The existence of the Temporary Strength Pill was a secret he had to take to his grave.

[P91]
It was a hidden trump card that might save his life someday. But if its existence became known, it would be a wondrous object capable of bringing a bloodbath to the entire world.

[P92]
Just the fact that it could draw out two or three times the power of the person who took it would be enough to make martial artists throughout the land salivate and come running.

[P93]
But there was an even greater problem.

[P94]
*It’s a legacy of demonic, heterodox arts.*

[P95]
After the Great Faction War, the Murim had fallen into the hands of the orthodox factions.

[P96]
If even a rumor spread that Pung Yang had inherited the legacy of demonic, heterodox arts, it wouldn’t be only the Jin Family of Taiyuan pursuing him. The entire Murim would come after him.

[P97]
*Jin Taekyung, the Sleeping Dragon of Shanxi… I must kill him and eliminate the trouble he’ll cause later.*

[P98]
Pung Yang gritted his teeth and unleashed his martial arts.

[P99]
After only a few years of training, he had already mastered seventy percent of the Crimson Blood Twelve Sabers. That was more than enough to kill a brat hopelessly beneath him in both age and martial arts.

[P100]
“Die!”

[P101]
*Shiiing!*

[P102]
The Crimson Blood Twelve Sabers was a domineering martial art. Red saber qi shot from the curved saber and slashed wildly in every direction. The fierce momentum split open the surface of the earth and burst the air apart.

[P103]
Yet the target he needed to cut was no longer there.

[P104]
Jin Taekyung dodged the attack by exactly half a step and thrust his spear.

[P105]
*Shweeeeeek!*

[P106]
The spearhead drove toward Pung Yang’s throat. Pung Yang hastily twisted his head aside to evade it, and a chill settled in his chest.

[P107]
*Fast.*

[P108]
Fast and accurate. He had yet to reach the stage where Sword Energy could injure a person—the hallmark of a Peak master—but his movements had already caught up to Pung Yang’s.

[P109]
*Could this brat have taken the Temporary Strength Pill too? No. It’s completely different from mine.*

[P110]
Pung Yang had already taken the Temporary Strength Pill several times.

[P111]
From Jin Taekyung’s body, which had turned bright red with heat, Pung Yang could tell that what he had swallowed earlier was not the Temporary Strength Pill.

[P112]
*Then what did he… Wait!*

[P113]
Pung Yang couldn’t continue thinking. Jin Taekyung had finally seized the initiative and begun to unleash the Jin Family’s Spear Technique in earnest.

[P114]
*Shh-shh-shh-shh-shhk!*

[P115]
Dozens of spear shadows poured down like a rain shower. It was a suffocating sight.

[P116]
No, it wasn’t just an illusion. It really was suffocating.

[P117]
A bead of sweat rolled down Pung Yang’s forehead.

[P118]
*This is…*

[P119]
Scorching Yang Qi.

[P120]
And not just any Scorching Yang Qi—it was powerful enough to affect even Pung Yang, a Peak master himself. The Tiger of Mount Heng, Cheol Mubaek, had also possessed Scorching Yang Qi, but it couldn’t compare to what Jin Taekyung was emitting now.

[P121]
*He ate a divine elixir—a Scorching Yang-type divine elixir!*

[P122]
*Whooooom!*

[P123]
Recognizing it changed nothing. The heat was dizzying, and the attacks were sharp. Pung Yang bit down hard on his lip as he repeatedly retreated, barely managing to evade the spearhead.

[P124]
*Against a brat this young!*

[P125]
He had lived his entire life fiercely. Now, even after taking the Temporary Strength Pill, he felt humiliated to be driven back by a young brat who had only just begun making a name for himself.

[P126]
That anger flowed straight into his curved saber. The saber qi rising over the blade burned redder than ever.

[P127]
*Hiss!*

[P128]
The Jin Family’s Spear Technique and the Crimson Blood Twelve Sabers differed in their weapons and forms, but they shared one thing in common: both were domineering martial arts.

[P129]
In the blink of an eye, Jin Mukyung’s iron spear and Pung Yang’s curved saber finally parted after more than ten fierce exchanges.

[P130]
“Hmm.”

[P131]
Jin Taekyung was the first to retreat. Blood flowed from his torn palm, and the heavy, sturdy iron spear had been cut by the sharp saber qi until less than half of it remained.

[P132]
“You fool.”

[P133]
Pung Yang smiled triumphantly. A martial artist losing their weapon meant defeat.

[P134]
Even the Tiger of Mount Heng, Cheol Mubaek, who had built his reputation entirely with his fists and feet, had knelt before Pung Yang. Jin Taekyung hadn’t even crossed the wall into the Peak realm yet. The moment he lost his weapon, he was as good as dead.

[P135]
“Did you think you could defeat me in a head-on fight?”

[P136]
Jin Taekyung rubbed the blood from his palm and answered.

[P137]
“No. But I did learn some valuable information.”

[P138]
“...Valuable information?”

[P139]
“Yeah. I learned your attack pattern.”

[P140]
“Pat—what?”

[P141]
“Your attack pattern is strong, strong, strong, strong, strong.”

[P142]
*What kind of bullshit is this?*

[P143]
Pung Yang understood that the brat was talking about his martial arts, but he had never heard of this “pattern-whatever” before. And what did he mean by strong, strong, strong, strong, strong?

[P144]
Pung Yang glared at Jin Taekyung with murderous eyes.

[P145]
“I’ll sever the meridians in all four of your limbs as payment for talking nonsense.”

[P146]
Jin Taekyung opened his mouth with a bored expression.

[P147]
“You really like cutting off and pulling out people’s limbs. Are you a limb fetishist?”

[P148]
“You little brat…”

[P149]
“You old bastard…”

[P150]
Pung Yang drew a deep breath. He was a Peak master who had spent his entire life possessing a cool, rational mind. But he couldn’t stop his voice from breaking into pieces with anger.

[P151]
“You. Will. Die. By. My. Hand.”

[P152]
“I. Sometimes. Cut off limbs. Sometimes, I don’t like this version of myself.”

[P153]
He felt his patience snap. He could swear that he had never been this furious in nearly ten years.

[P154]
“Graaaargh!”

[P155]
Pung Yang charged like a madman, emitting a howl that could have been either a scream or a roar.

[P156]
Without using a single form or martial art, he brought the curved saber down over the crown of Jin Taekyung’s head with all his strength.

[P157]
“Die!”

[P158]
That was when Jin Taekyung’s calm expression was reflected in Pung Yang’s bloodshot eyes gleaming with killing intent.

[P159]
In an instant, his mind snapped clear as though someone had dumped cold water over him.

[P160]
*Something’s wrong.*

[P161]
Pung Yang drew up his internal energy with all his might.

[P162]
As his Body-Protecting Qi rose, a dagger flashed in Jin Taekyung’s previously empty hand.

[P163]
*Shnk!*
```


## Exact glossary matches

These English spellings are binding for the matched Korean keys.

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 철무백    | **Cheol Mubaek**   |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 창법     | **spear technique**                              |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 기연     | **fortuitous encounter**                         | Use sparingly                                         |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 정파     | **orthodox faction**                             |                                                       |
| 진가창법   | **Jin Family's Spear Technique**       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 대사      | **Master** for a senior Buddhist monk                           |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 적혈십이도 | **Crimson Blood Twelve Sabers** | Pung Yang's domineering saber art; he has reached approximately seventy percent mastery. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |

## Deterministic QA

```json
{
  "version": 1,
  "chapter": 118,
  "passed": true,
  "metrics": {
    "source_characters": 5399,
    "translation_characters": 12634,
    "length_ratio": 2.34,
    "source_paragraphs": 165,
    "translation_paragraphs": 164
  },
  "errors": [],
  "warnings": [
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "기연",
        "preferred": "fortuitous encounter"
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
        "korean": "진가창법",
        "preferred": "Jin Family's Spear Technique"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "대사",
        "preferred": "Master for a senior Buddhist monk"
      }
    },
    {
      "code": "terminology",
      "message": "matched preferred term is absent",
      "details": {
        "korean": "진태",
        "preferred": "Jintae"
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
