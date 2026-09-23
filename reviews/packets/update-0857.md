<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0857.txt",
      "sha256": "f39fde7cac3898e2ae199899674462f01b078b4c090c581583d0aaffdecf2f76",
      "bytes": 14156
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "006f2d893e1da8eeafb14ed19134a9ce17f672690652ba5ca5ba64257be8295e",
      "bytes": 1938
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c71f13dfc442c6e46aa85633ed364d93f329588811e408d32dcd5604f9a1a746",
      "bytes": 228458
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1972e9c28a96ec91c09ee5afb99a879a341e4f1912644a26578bf0007aba4994",
      "bytes": 759
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "f67fbc17afa01817e9893aa3e5cf6bb302942c2f578c0230ade1b8e31c449264",
      "bytes": 1355
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "36a15c8046df4178f860326eaee2af9a9a7ca2045b0503ae9f81c5e6ff5b7994",
      "bytes": 253598
    }
  ],
  "estimated_tokens": 9539
}
-->

# Durable State Update — Chapter 857

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 857. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 857. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 857,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 857,
    "continuity_sources": [857],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "The Divine Physician secured the Blood Soul Gu found in the deceased City Lord of Sichuan Province; it weakens hosts, causes madness, and eventually kills them.",
    "Jin suspects Dark Heaven’s covert killing of the City Lord is part of a scheme targeting the Great Nation, possibly its imperial family.",
    "Prince Shangshan Zhu Bao is traveling toward the imperial capital with Hong Jin and fifty Embroidered Uniform Guard members.",
    "The late Emperor entrusted Hong Jin with Zhu Bao’s care; Hong Jin fears the current Emperor intends harm, while Zhu Bao trusts his elder brother.",
    "Jin’s party reached Jiangsu after eleven days of arduous travel and is exhausted; Jin insists the group stay together.",
    "The Embroidered Uniform Guard’s procession stopped over an unidentified corpse ahead; Hong Jin heard a familiar voice nearby and hopes Jin’s party has caught up.",
    "Jin says he is currently well but may hit a wall again; the Divine Physician is traveling with the party to treat him."
  ],
  "continuity_sources": [
    855,
    856
  ],
  "open_questions": [
    "Why did Dark Heaven secretly kill the City Lord of Sichuan Province, and is it targeting the Emperor or imperial family?",
    "What does the Emperor intend for Prince Shangshan, and what prompted the imperial decree against Hong Jin?",
    "Who is the unidentified corpse ahead of the procession, and has Jin’s party caught up with Prince Shangshan?",
    "What explains the attackers’ unnatural ferocity during the caravan assault?"
  ],
  "safe_through": 856,
  "temporary_decisions": [
    "Render 혈혼고 as “Blood Soul Gu.”",
    "Render 대국 as “Great Nation.”",
    "Render 금의위 as “Embroidered Uniform Guard.”",
    "Render 강소 as “Jiangsu.”",
    "Distinguish 홍건적 as “Red Turban Bandits” from 홍건군 as “Red Turban Army.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 혁무진    | **Hyuk Mujin**     |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 선배     | **Senior**                                   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 공수납백인 | **Empty-Hand Seizes the Blade** | Technique for catching an opponent's weapon between bare fingers. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 검기상인 | **the level of injuring others with Sword Energy** | Realm description used for Moon Beauty Saber. |
| 초일류 | **Supreme First Rate** | Realm attained by each Baekcheon Unit member. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 856
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 856
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

## Korean source

```text
＃857화



“뭐야, 다 어디 갔어. 저기요, 아저씨. 혹시 여기 근처에 있던 사람들 못 봤어요?”

잔뜩 떡 진 머리와 얼굴 가득한 땟국물.

자리에서 일어나 횡설수설하는 청년의 모습에, ‘아저씨’라 불린 사내가 문득 입을 열었다.

“어떻게 된 거지? 아무리 봐도 저건 시체가 아닌 것 같은데.”

“죄, 죄송합니다. 너무 죽은 듯이 잠들어 있는 바람에 그만 착각했던 것 같…….”

“그만. 환궁(還宮)한 뒤에 다시 이야기하지.”

앞서 척후 내용을 보고 했던 금의위 무사의 얼굴이 딱딱하게 굳었다.

무사는 삼 년 가까이 모신 자신의 상관이 어떤 인물인지 잘 알고 있었다.

그가 이번 사안을 얼마나 중요하게 생각하는지도.

좌천이라면 다행이고, 자칫하면 삭탈관직(削奪官職)까지도 각오해야 할 상황.

‘빌어먹을.’

입술을 질끈 깨문 무사는 끓어오르는 감정을 애써 억눌렀다.

내심 억울한 마음이 없지는 않았지만, 실수는 실수.

이미 바닥에 엎질러진 물을 주워 담을 수는 없겠지만, 닦아 내는 것쯤은 할 수 있다.

아니, 반드시 닦아 내야 한다.

머지않아 자신에게 떨어질 처벌의 강도를 조금이나마 줄이기 위해서라도.

“……제가 처리하겠습니다.”

가라앉은 목소리로 입을 연 무사가 아직 잠이 덜 깬 청년을 향해 걸음을 내디뎠다.

어차피 상대는 어디서 굴러들어 왔는지도 모를 거지 같은 놈. 만약 저항해도 단칼에 베어 버리면 그만이었다.

적어도 무사의 생각은 그랬다.

“무슨 짓이냐.”

저벅.

갑작스러운 사내의 부름에 무사의 발걸음이 우뚝 멈췄다.

담담하지만 서늘한 눈빛으로 자신을 내려다보는 상관의 모습에, 그가 더듬더듬 대답했다.

“그것이, 이대로 놔둘 순 없으니 그냥 제가 직접…….”

“처리하겠다?”

“그, 그렇습니다.”

“어떻게?”

“예?”

“어떻게 처리할 생각이냐 물었다.”

“그야…… 상황이 상황인 만큼 무력을 사용해서라도 위험 요소를 제거하는 것이 맞지 않겠습니까.”

그러자 잠시 침묵하던 사내가 입을 열었다.

“네 연차가 올해로 몇이냐.”

“정 천호(千戶)님을 모신 지는 삼 년이 되어 갑니다. 그리고…….”

눈치를 보며 머뭇거리던 무사가 덧붙였다.

“제 아버님의 말씀에 따라, 언제나 정 천호님의 지시에 최선을 다했다고 생각합니다.”

이어진 무사의 목소리에는 약간의 불안함과 그보다 많은 섭섭함이 묻어나 있었다.

수하가 된 지 삼 년이 되어 감에도 눈길조차 제대로 주지 않는 상관의 태도도 그랬지만, 지체 높은 가문의 자제인 자신을 너무 무시하는 듯한 처사 때문이기도 했다.

‘금의위에 들어오기 위해 우리 집안에서 쓴 재물이 얼마인데!’

금은보화와 권력의 입김이 닿지 않는 곳은 어디에도 없다. 심지어 황제 직속의 금의위조차도 마찬가지였다.

비록 철저한 심사를 거치는 탓에 만금을 들여서 얻은 자리라고 해도 고작 말단에 불과했지만, 그마저도 들어오지 못해 안달하는 이들이 한둘인가.

그런 만큼, 무사는 결코 이대로 물러날 생각 따위는 없었다.

굳이 아버지를 언급한 것도 일종의 시위에 가까웠다.

저 까다롭고 엄격한 상관에게, 자신의 뒷배를 다시 한번 상기시키고자 하는 의도가 진하게 묻어 있는 시위.

그렇기에 뒤이어 들려온 사내의 한 마디는, 무사가 귀를 의심케 하기에 충분했다.

“삼 년이라, 그만하면 이제 충분하겠군.”

“예?”

“지금 당장 패(牌)를 반납하고 네가 있어야 할 곳으로 떠나라. 앞서 저지른 실책에 대한 처분은 이것으로 끝마치겠다.”

“……!”

“왜, 아직 할 말이 남았나?”

눈을 부릅뜬 채, 믿지 못할 현실을 마주한 무사가 버럭 외쳤다.

“이 무슨! 이런 말도 안 되는 일이 어디 있습니까! 제가 누구인지 잊으셨……!”

“똑똑히 기억하고 있다. 그렇지 않았다면 삼 년씩이나 수하로 두지는 않았겠지.”

무사의 외침을 가로막은 사내가 담담하게 덧붙였다.

“그리고 사람들이 기억하는 것은 네가 아니라, 네 뒤에 있는 가문의 후광뿐이다. 두 번 다시 같은 실수를 반복하기 싫다면 그 사실을 몸과 마음에 새기도록.”

“지금 말 다 했소?”

“아직 끝나지 않았지만, 굳이 말해 줄 필요는 없을 것 같군. 상대도 제대로 파악하지 못하는 자에게는 더더욱.”

“그게 무슨 헛소……!”

무사가 버럭 고함을 내지르려던 그 순간이었다. 그의 귓가에 한 줄기 목소리가 닿은 것은.

“저기요. 말씀 중에 죄송한데 우선 물 좀 얻어먹을 수 있을까요. 제가 아까부터 너무 목이 말라서.”

“……!”

멀리서 들려오는 목소리가 아니다.

바로 등 뒤. 숨결에 섞인 단내까지 느껴질 정도로 가까웠다.

‘도대체 어떻게!’

충격과 함께 전신의 솜털이 곤두선다. 대경한 무사는 번개처럼 돌아서며 허리춤의 검을 뽑았다.

스릉, 쉭!

가문 대대로 내려오는 보검(寶劍)이 오색 창연한 빛을 뿌리며 등 뒤의 상대를 정확히 반으로 갈랐다.

아니, 갈랐다고 생각했다.

보검이 정수리를 파고들려는 그 순간, 땟국물이 줄줄 흐르는 두 손이 섬광처럼 움직이기 전까지는.

쩌엉!

합장(合掌)과 함께 울려 퍼지는 굉음. 동시에 무사의 입술 사이로 외마디 탄식이 흘러나왔다.

“공수납백인(空手納白刃)……?”

최소 한 수, 혹은 두 수 이상의 고수가 하수를 상대로나 보일 법한 기예(技藝).

가문의 아낌없는 지원으로 초일류의 경지까지 오른 무사는 이 상황의 의미를 즉각 깨달았고, 단지 거지로만 생각했던 상대를 바라보며 경악했다.

“저, 절정 고수!”

그리고 그 경악 어린 외침에, 의문의 절정 고수가 대답했다.

“뭐래, 시벌. 가뜩이나 검기도 못 쓰는 새끼라고 맨날 구박받는데.”

“네, 네놈은 누구냐! 정체를 밝혀라!”

“좆 까. 물이나 내놔. 칼 말고.”

후웅, 퍽!

그야말로 순식간이었다.

양 손바닥으로 붙잡고 있던 검을 옆으로 흘림과 동시에, 단단한 무르팍을 무사의 면상에 꽂아 넣은 그는 썩은 통나무처럼 허물어진 무사의 품에서 호리병을 찾아 단번에 들이켰다.

벌컥, 벌컥.

“크으으. 이제 좀 살겠네.”

마치 며칠간 물 한 방울 입에 대지 못한 것 같은 모습.

사내, 정 천호(天戶)는 호리병을 비우다 못해 탈탈 터는 청년을 물끄러미 바다보다가 불쑥 입을 열었다.

“처음 봤을 때부터 짐작은 했지만, 솜씨가 제법이군.”

잠시만 기다리면 술이라도 나올 거라 생각하는지, 이미 바닥을 드러낸 호리병 입구를 노려보던 청년이 되물었다.

“그 말, 진심이오?”

“물론이다. 비록 검기상인(劒氣傷人)의 경지에는 아직 오르지 못한 것 같지만, 조금 전의 움직임은 극히 효율적이고 훌륭했어.”

“고맙소. 나보다 훨씬 고수한테 그런 말을 듣다니 눈물이 날 것 같구려. 반말은 좀 거슬리지만.”

“오해한 모양이군. 그대를 비웃은 것이 아니다.”

“알고 있소. 오해한 게 아니고 그냥 진짜 눈물이 날 것 같아서 한 말인데.”

“……?”

“내가 시부랄, 그렇게 개고생을 해 가면서 욕이란 욕은 다 처먹고. 뭐 빠지게 수련해도 맨날 검기 왜 못 쓰냐고, 그거 못 하는데 사람 구실을 어떻게 하냐고 구박만 받고. 하다 하다 이제는 길바닥에 버리고 가질 않나……. 큼. 크흐흑!”

정 천호는 자신도 모르게 입을 다물었다.

기다렸다는 듯이 쏟아진 하소연에 이어 이제는 눈물까지 줄줄 흘리는 청년의 모습에, 그를 비롯한 모두가 같은 의문을 떠올리고 있었다.

‘뭐지, 저 새끼는?’

겉모습은 영락없는 거지새끼인데, 알고 보니 미친 새끼였던 상황.

한 가지 문제가 있다면 희한하게도 저 미친 새끼가 제법 고수라는 사실이다. 그것도 초일류 주제에 흡사 절정 고수 같은 움직임을 보이는.

하지만 지금은 작전을 이행하고 있는 상황.

정 천호의 뒤에 늘어선 금의위 무사들은, 서로를 향해 당혹스러운 눈빛을 주고받았다.

‘이런 경우에는 대체 어떻게 해야 합니까?’

‘몰라. 홍 교위(校尉)님은 아실 것 같은데.’

‘나도 모른다.’

‘아니, 홍 교위님이 모르시면 어떻게 합니까. 저희를 이끄시는 조장이신데.’

‘조장이 무슨 천지신명이라도 된다더냐? 그래도 나보다 선배님이신 갈 교위님은 아실 거다. 훨씬 선배시니까.’

‘아냐. 나도 몰라…….’

‘예?’

방향을 잃고 흔들리는 시선과 바짝바짝 말라 가는 입술.

그토록 이름 높은 금의위가 언제 이런 상황을 겪어 봤을까.

이제는 급기야 길바닥에 주저앉아 엉엉 소리를 내며 통곡까지 하는 저 미친 새끼를 어떻게 해야 할지, 모두가 갈피를 잡지 못했다.

아니, 정확히는 한 사람을 제외한 모두가.

다그닥. 다그닥.

천천히 말을 몰아 앞으로 나아간 정 천호가 특유의 담담한 눈빛으로 청년을 내려다보았다.

“다 울었나?”

청년이 울음기 어린 목소리로 대답했다.

“아직 조금 남았소.”

“상관없다. 갈 길이 지체되고 있으니 이만 옆으로 비켜서라.”

“음.”

잠시 코를 훌쩍거린 청년이 말을 이었다.

“그건 좀 곤란할 것 같은데.”

“어째서?”

“길을 비키는 건 어렵지 않지만, 그랬다간 내가 모시는 분이 크게 노하실 거요.”

“이미 버림받은 몸이라고 했던 것 같은데.”

“그분과 함께하다 보면 잠깐 버려질 때도 종종 있소. 여하튼 무슨 이유에서 내가 이곳에 있는지는 몰라도 금방 돌아오시겠지.”

툭. 툭.

엉덩이에 묻은 먼지를 털며 자리에서 일어난 청년이 말을 이었다.

“이래 봬도 내가 오른팔이거든. 뭐, 새끼발가락일 수도 있지만.”

“그렇군.”

가볍게 고개를 끄덕인 정 천호가 물었다.

“호패(號牌)는 있나?”

“호패가 뭐요. 국 끓여 먹는 건가?”

“강호의 무뢰한이라는 뜻이군. 천자께서 바로 세우신 지엄한 국법을 헛소리 취급하는.”

“비슷하오만. 갑자기 그런 건 왜 물어본 거요?”

“단지 확인 절차다. 헛된 판단으로 호패까지 소지한 대국의 백성을 해할 수는 없으니까.”

“흠. 꼭 관부(官府)에 속한 사람처럼 말씀하시는구려.”

“비슷하지만, 조금은 차이가 있지.”

“영 애매모호한 대답인데, 이해를 돕기 위해 한 가지 예를 들자면?”

“알 것 없다.”

“오.”

담담하지만 서늘한 대답에, 어깨를 으쓱해 보인 청년이 손에 들고 있던 무언가를 떨어트렸다.

툭.

미세한 소음과 함께, 구리로 만든 동패가 빛을 반사하며 번쩍인다. 흙먼지가 묻은 표면에는 세 글자가 음각(陰刻)되어 있었다.

금의위(錦衣衛).

“어이쿠. 실수로 떨어트렸네. 기념으로 가져가려고 했는데.”

과장된 어투와 목소리. 하지만 정 천호를 응시하는 청년의 눈동자는 깊게 가라앉아 있었다.

“호리병만 찾으려고 했는데, 웬 이상한 게 딸려 나오더라고.”

“강호의 무뢰한답게 손버릇이 좋지 않군.”

“이번 경우는 정당방위라고 합시다. 내가 모시는 분이었으면 겨우 이 정도로 끝나지도 않았겠지만.”

그러자 정 천호는 대답 대신 손을 들어 올렸다.

어느새 무기를 뽑아 든 금의위들이 강철의 파도가 되어 청년을 에워쌌다.

“네놈을 죽이기 전에, 한 가지만 묻겠다.”

“시간 괜찮으면 최대한 많이 물어봐도 괜찮소. 그래도 조금은 오래 살고 싶어서.”

청년을 바라보는 정 천호의 눈동자에 이채가 스쳤다.

이 뜻밖의 상황은 이미 끝난 것이나 다름없다.

신호가 떨어지면 청년은 찰나 지간에 죽음을 맞이할 테고, 그들은 아무 일도 없었던 것처럼 가던 길을 계속 이동할 것이다.

그러나…….

‘물러설 생각 따위는 추호도 없군.’

죽음을 두려워하지만, 결코 물러서지 않는 모습.

그는 청년의 모습에서 무인의 기개(氣槪)를 읽었다.

“네 이름이 무엇이냐.”

“혁무진.”

청년, 혁무진을 향해 고개를 끄덕인 정 천호가 입을 열었다.

“배후는?”

이 모든 상황은 절대 우연이 아니다.

이름을 알 수 없는 누군가는 처음부터 그들을 기다렸고, 반드시 지나갈 수밖에 없는 길목마다 사람을 배치해 둔 것이 틀림없다.

정 천호는 반드시 그 배후의 정체를 알아내야 했고, 그가 원했던 대답은 예상치도 못한 곳에서 들려왔다.

“배후라고 불릴 만큼 거창하진 않은데, 막상 들어 보니까 느낌은 썩 괜찮네. 약간 성좌가 된 기분 같기도 하고.”

기척도, 소리도 없었다.

하지만 어느새 나타난 한 청년의 그림자가, 나무 위에서 그들을 향해 드리워졌다.

“드디어 만났네. 그동안 잘 지냈어?”

“나를…… 아나?”

정천호의 굳은 물음에, 청년이 웃으며 대답했다.

“내가 널 어떻게 아냐, 이 시벌놈아.”
```

## Final English reading copy

```markdown
# Chapter 857

“What? Where’d everyone go? Hey, mister. Have you seen anyone around here?”

His hair was matted into a greasy mess, and grime streaked his face.

At the sight of the young man getting to his feet and babbling, the man he’d called “mister” suddenly spoke.

“What happened? No matter how I look at him, he doesn’t seem to be dead.”

“I-I’m sorry. He was sleeping so still, like he was dead, so I think I mistook him for—”

“That’s enough. We’ll talk about it again after we return to the palace.”

The Embroidered Uniform Guard martial artist who had reported the scouts’ findings earlier went rigid.

He knew very well what kind of man his superior was. He’d served under him for nearly three years.

He also knew how important this matter was to him.

If he was lucky, he’d be demoted. If things went badly, he could lose his position entirely.

*Damn it.*

The martial artist clenched his lips and struggled to suppress the anger welling inside him.

He couldn’t deny that he felt wronged, but a mistake was still a mistake.

He couldn’t gather water that had already spilled across the ground, but he could at least wipe it up.

No—he had to wipe it up.

If only to lessen the punishment that would soon fall on him.

“……I’ll take care of it.”

The martial artist spoke in a subdued voice and stepped toward the young man, who still looked half asleep.

The other guy was some miserable piece of trash who could’ve rolled in from anywhere. If he resisted, the martial artist could simply cut him down in one stroke.

At least, that was what he thought.

“What are you doing?”

Clop.

At the man’s sudden call, the martial artist stopped dead.

Under his superior’s calm but icy gaze, he stammered out a reply.

“I—it can’t be left like this, so I thought I’d handle it myself…”

“Handle it?”

“Y-Yes.”

“How?”

“Pardon?”

“I asked how you intend to handle it.”

“Well… given the situation, wouldn’t it be right to use force if necessary and remove the threat?”

The man was silent for a moment before speaking.

“How many years have you served?”

“I’ve been serving you, Commander Jeong, for almost three years. And…”

The martial artist hesitated, watching his superior’s expression, then added,

“Following my father’s advice, I believe I’ve always done my best to carry out your orders.”

A little unease—and a lot more resentment—colored his voice.

His superior had barely paid him any attention, even after nearly three years as his subordinate. And the way he was treated made it seem as if the man had no respect at all for someone born into a prestigious family.

*How much wealth did my family spend to get me into the Embroidered Uniform Guard?*

There was nowhere beyond the reach of gold, silver, or the influence of power. Not even the Embroidered Uniform Guard, directly under the Emperor, was an exception.

Even if a fortune had only bought him a low-ranking position after a rigorous screening, how many people would have killed to get even that far?

For that reason, the martial artist had no intention of backing down.

He’d mentioned his father as a sort of warning.

A clear attempt to remind his difficult, strict superior that he had powerful connections.

That was why the man’s next words were enough to make him question his own ears.

“Three years. That’s long enough.”

“Pardon?”

“Hand over your badge right now and go where you belong. This will conclude your punishment for the mistake you made earlier.”

“……!”

“What? Do you still have something to say?”

Eyes wide, the martial artist faced a reality he couldn’t believe and shouted,

“What is this! How can you do something so outrageous? Have you forgotten who I am—”

“I remember perfectly. Otherwise, I wouldn’t have kept you as a subordinate for three years.”

The man cut him off, then continued in the same calm voice.

“And the people remember not you, but the prestige of the family behind you. If you don’t want to make the same mistake again, engrave that fact into your heart and mind.”

“Have you said your piece?”

“I haven’t finished, but I don’t think there’s any need to explain the rest. Especially not to someone who can’t even tell what he’s dealing with.”

“What the hell are you—”

The martial artist was about to bellow when a voice reached his ear.

“Excuse me. Sorry to interrupt, but could I get some water first? I’ve been really thirsty for a while.”

“……!”

The voice hadn’t come from far away.

It was right behind him. Close enough that he could smell the sweetness of the man’s breath.

*How did he—?!*

Shock sent the hairs all over his body standing on end. The martial artist spun around like lightning and drew the sword at his waist.

Shing—whoosh!

The treasured sword, passed down through his family for generations, shone in a dazzling array of colors as it cleaved the figure behind him clean in half.

Or so he thought.

Until two hands dripping with grime moved like a flash, just as the sword was about to bite into the crown of his head.

Clang!

A deafening crash rang out as the man brought his palms together. At the same time, a single gasp slipped from the martial artist’s lips.

“Empty-Hand Seizes the Blade…?”

A technique a master would only use against someone at least a step or two beneath them.

Having reached the Supreme First Rate realm with generous support from his family, the martial artist immediately understood what had happened. He stared in shock at the man he’d taken for a mere beggar.

“A Peak master!”

At that horrified cry, the mysterious Peak master answered,

“What are you talking about, asshole? I get shit from everyone all the time for not being able to use Sword Energy.”

“Y-You! Who are you? State your identity!”

“Fuck off. Give me water. Not a sword.”

Whoosh—thud!

It happened in the blink of an eye.

As he redirected the sword he’d caught between his palms, the man drove his hard knee into the martial artist’s face. Then, from the martial artist’s body as it crumpled like a rotten log, he found a small flask and drained it in one go.

Gulp, gulp.

“Ahhh. That’s better.”

He looked like he hadn’t had a drop of water in days.

Commander Jeong watched the young man empty the flask, then shake out the last few drops. He spoke without warning.

“I had my suspicions from the moment I first saw you, but you’re pretty skilled.”

The young man stared at the mouth of the flask, now completely empty, as if expecting wine to come out if he just waited a little longer. Then he asked,

“Do you mean that?”

“Of course. You don’t seem to have reached the level of injuring others with Sword Energy, but the movement you just showed was extremely efficient and impressive.”

“Thanks. Hearing that from someone way more skilled than me almost brings a tear to my eye. Though I could do without you talking down to me.”

“You misunderstand. I wasn’t mocking you.”

“I know. I’m not saying you were. I really do feel like I’m about to cry.”

“……?”

“I’ve been through so much fucking shit. I’ve had every kind of abuse thrown at me. I train my ass off, and all I ever hear is, ‘Why can’t you use Sword Energy?’ and, ‘How can you call yourself a proper person if you can’t even do that?’ And now they’ve gone and left me on the side of the road, too… Ahem. Hic!”

Commander Jeong found himself at a loss for words.

The young man’s complaints had poured out as if he’d been waiting for the chance, and now tears were streaming down his face. He and everyone else there found themselves wondering the same thing.

*What the hell is that guy?*

He looked exactly like a beggar, but turned out to be a lunatic.

There was just one problem: that lunatic was actually pretty damn skilled. A Supreme First Rate martial artist, yet he moved like a Peak master.

But they were in the middle of carrying out an operation.

The Embroidered Uniform Guard martial artists lined up behind Commander Jeong exchanged bewildered looks.

*What are we supposed to do in a situation like this?*

*I don’t know. Captain Hong might know.*

*I don’t know, either.*

*How can you not know, Captain Hong? You’re our Captain.*

*Does a Captain have to be some kind of god? Still, Senior Officer Gal should know. He’s been around much longer than I have.*

*No. I don’t know, either…*

Their gazes wandered, and their mouths grew dry.

When had the famed Embroidered Uniform Guard ever dealt with a situation like this?

At this point, the lunatic had sat down right there on the road and was bawling his eyes out. No one could figure out what to do with him.

Well—not everyone.

Clip-clop. Clip-clop.

Commander Jeong slowly rode forward and looked down at the young man with his usual calm expression.

“Are you done crying?”

The young man answered in a tear-choked voice.

“Not quite.”

“That’s fine. We’re holding up the journey, so move aside.”

“Mm.”

The young man sniffled, then continued.

“That might be a little difficult.”

“Why?”

“Moving out of the way is easy enough, but the person I serve would get furious if I did.”

“I thought you said you’d been abandoned.”

“Sometimes I get left behind when I’m with that person. Anyway, I don’t know why I ended up here, but they’ll be back soon.”

Brush, brush.

The young man stood and dusted off his backside.

“Believe it or not, I’m his right-hand man. Though I might just be his little toe.”

“I see.”

Commander Jeong gave a slight nod and asked,

“Do you have an identity tag?”

“An identity tag? Is that something you boil in soup?”

“So you’re a rogue of the martial world. You treat the strict laws established by the Son of Heaven as nonsense.”

“Something like that. Why are you asking all of a sudden?”

“Just a formality. I can’t harm a citizen of the Great Nation who carries an identity tag based on a rash assumption.”

“Hm. You talk like you belong to the authorities.”

“Something like that, but there’s a slight difference.”

“That’s awfully vague. Maybe an example would help me understand?”

“You don’t need to know.”

“Oh.”

At that calm but icy answer, the young man shrugged and dropped something he’d been holding.

Tap.

A faint sound, and a copper badge flashed as it caught the light. Three characters were engraved on its dirt-streaked surface.

Embroidered Uniform Guard.

“Whoops. Dropped it by accident. I was going to take it as a souvenir.”

His tone and voice were exaggerated. But his eyes, fixed on Commander Jeong, had gone cold.

“I was only looking for the flask, but some weird thing came along with it.”

“You’ve got sticky fingers for a rogue of the martial world.”

“Let’s just call this self-defense. If it’d been the person I serve, you wouldn’t have gotten off this easily.”

Instead of answering, Commander Jeong raised a hand.

The Embroidered Uniform Guard had drawn their weapons. They surrounded the young man like a rising wave of steel.

“Before I kill you, I’ll ask you one thing.”

“If you have time, ask as many as you like. I’d like to live a little longer, if possible.”

Something glinted in Commander Jeong’s eyes as he looked at the young man.

This unexpected situation was as good as over.

When the signal came, the young man would be dead in an instant, and they would continue on their way as if nothing had happened.

And yet…

*He has no intention of backing down.*

He was afraid of death, but he would never retreat.

Commander Jeong saw the bearing of a martial artist in the young man.

“What is your name?”

“Hyuk Mujin.”

Commander Jeong nodded to the young man—Hyuk Mujin—and asked,

“Who’s behind this?”

None of this was a coincidence.

Someone whose identity they didn’t know had been waiting for them from the start. They had surely placed people at every chokepoint the procession had to pass through.

Commander Jeong had to find out who was behind it. But the answer he wanted came from somewhere he never would have expected.

“Calling me the mastermind sounds a little grand, but now that I hear it, I kind of like it. Makes me feel like a Constellation, almost.”

There was no presence. No sound.

Yet the shadow of a young man had appeared among them, stretching down from a tree above.

“We finally meet. How’ve you been?”

“Do you… know me?”

At Commander Jeong’s stiff question, the young man laughed.

“How the fuck would I know you, you son of a bitch?”
```
