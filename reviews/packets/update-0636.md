<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0636.txt",
      "sha256": "825cd0c7f9c1a47279145b345c51ef39d106a0753e1d09902f6db2b1c7b090ae",
      "bytes": 13159
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a90ff257b7757fa3d769d27286dd2cf7e13ad8b408138286cbb892555693aff8",
      "bytes": 1526
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "7e5808f7b11b616f1792ff0096317d4ac49802e47fa719fc9dc90293060f982f",
      "bytes": 195314
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "1b910ef6246b1f9cedb640c59baf9d5faab8ce2e39e2eaa3f5c761d7610ae21f",
      "bytes": 808
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "75e860c7cf8253c7536529709b1fe469767be49284f1bf8c03dc1f2b70bb7f76",
      "bytes": 517
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b40dc19cf624fa2502ed330f3f65ce67166c71a9a36e006cbe3c2a9a126c033c",
      "bytes": 553
    },
    {
      "path": "characters/Hanga.md",
      "sha256": "f81bf4e44be793bcdc6bde4e5526e150a236fa428ae43e647d60483b6a1f02bc",
      "bytes": 568
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "33613f75c439b4fcf992902e1cb3009dba85e0c321e02701eb4c60af756b986a",
      "bytes": 871
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e83f041fbf3984a67f63db5be92e1bbd01ccf61c452f8bb2fdc96250003c79fc",
      "bytes": 202182
    }
  ],
  "estimated_tokens": 10001
}
-->

# Durable State Update — Chapter 636

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 636. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 636. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 636,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 636,
    "continuity_sources": [636],
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
    "Ailao Mountain's Wraith is a colossal Black Tiger identified by the System.",
    "The Wraith emits Fear comparable to the Water God Dragon and can overwhelm ordinary spiritual creatures such as White Tiger.",
    "The Wraith evaded attacks from the Beast Miao King and Jin Taekyung, survived a Force-wreathed spear strike, and escaped Jin's Qi Sense.",
    "The Wraith outran Jin Taekyung, the Beast Miao King, and White Tiger during the pursuit.",
    "The pursuit revealed poisoned ravines and the corpses of Nanman warriors.",
    "The Wraith disappeared into a deep valley near the center of Ailao Mountain.",
    "The Beast Miao King entered the valley in anger, and Jin Taekyung followed after White Tiger warned that it was dangerous.",
    "The Southern Heaven Demon Empress's involvement remains suspected but unproven."
  ],
  "continuity_sources": [
    635
  ],
  "open_questions": [
    "What is the true nature of Ailao Mountain's Wraith?",
    "Did the Southern Heaven Demon Empress or Dark Heaven cause or control the Wraith?",
    "Where are the remaining Nanman warriors and the beasts they commanded?",
    "What awaits Jin Taekyung and the Beast Miao King inside the deep valley?"
  ],
  "safe_through": 635,
  "temporary_decisions": [
    "Use Black Tiger for 흑호.",
    "Use Ailao Mountain's Wraith for 애뇌산의 망령.",
    "Use Transcendent for 초일류.",
    "Retain mountain lord for 산군 with an explanatory footnote on first use."
  ],
  "version": 1
}
```

## Exact glossary matches

| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 신법     | **movement technique**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 사천     | **Sichuan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 항아 | **Hanga** | Local village boy who lives near Jang Taebo. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 천년독각사 | **Thousand-Year Poison Horned Snake** | Extremely venomous horned snake used to make Hong Dao's thirty-year-old liquor. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 피독주 | **poison-warding pearl** | Poison-neutralizing artifact carried by the black-clad attackers. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 오독문 | **Five Poisons Sect** | Formerly dominant Nanman faction destroyed by the Fire Gate Clan. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 흑호 | **Black Tiger** | A colossal black tiger that appears at the Ailao Mountain massacre site. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 야수묘왕 | 흑호 | hostile pursuer to unknown supernatural beast | you | blunt and furious | Directly challenges the Black Tiger over the massacre. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 634
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle; he lost a beloved son in the Great Faction War, bears a burn scar from Jeok Cheongang after calling him a crazy old man, opposes the Nanman Beast Palace joining the Murim Alliance, and helps Yohi keep Heugung under control.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 635
- **Aliases:** None
- **Role:** The Beast Miao King is the ruler of the Nanman Beast Palace and oversees its warriors and beasts.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace and is responsible for the forces stationed at Ailao Mountain.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 635
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hanga.md

# Hanga (항아)

- **Safe through:** Chapter 438
- **Aliases:** None
- **Role:** Local village girl, Jang-pal’s daughter, who lives near Jang Taebo and regularly visits him.
- **Personality:** Curious, energetic, observant, and already attentive to the value of information and food.
- **Voice:** Childlike, direct, and inquisitive, with an occasional surprisingly worldly remark.
- **Relationships:** Calls Jang Taebo Grandpa; Jang Taebo is his elderly neighbor and only conversational companion.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 635
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

## Korean source

```text
＃636화



골짜기 안은 좁고 어두웠다. 나이를 짐작할 수 없는 거목들이 빽빽하게 우거져 달빛을 가렸고, 태어나서 처음 본 괴이한 식물이며 생물들이 사방에 가득했다.

그리고, 그중에는 제법 공격성이 강한 놈들도 있었다.

쉬익!

경신법을 펼치고 있던 나는 순간적으로 손을 뻗었다. 풀숲 사이에서 번개처럼 솟구쳐 오른 무언가가 손아귀에 잡힌 채로 발버둥친다.

취릿. 취리릿!

‘뭐야, 이건. 뱀?’

찬찬히 살펴보니 반은 맞고, 반은 틀렸다.

뱀은 뱀인데 평범한 뱀이 아니었다. 세모꼴의 대가리에 양옆으로 나 있는 뿔이 바로 그 증거다.

잠깐. 이거 어디서 많이 본 것 같은데.

뱀을 빤히 응시하던 나는 작게 중얼거렸다.

“미미……가 아니라, 천년독각사(千年毒角蛇)?”

취릿.

아니, 이게 여기서 왜 나와. 천년독각사는 천하에서도 보기 드문 독물이라고 하지 않았었나?

‘다시 보니까 조금 다른 것 같기도 한데.’

유사 중국이라 그런가. 짝퉁이 많네.

미미와 비교하자면 몸통은 크지만, 윤기나 뿔의 크기는 떨어지는 편이다.

손에 잡힌 뱀을 황당하게 바라보던 나는 저 멀리 던져 버린 뒤 속도를 올렸다. 저게 정말 천년독각사든 뭐든, 짐작대로 이 골짜기가 그리 안전한 곳이 아니라는 것만은 확실해 보였다.

‘역시 함정인가?’

들어오기 전, 짧은 시간을 소요했기 때문인지 흑호와 야수묘왕은 이미 멀찍이 앞선 상황.

그나마 다행인 부분은, 정말 망령이라도 되는지 족적도 찾아볼 수 없는 흑호와 달리 야수묘왕의 족적은 드문드문 남아 있다는 점이다.

쉬쉬쉭!

반 각 정도를 그렇게 달렸을까. 나는 저 멀리 가까워지는 드넓은 늪지대와 그 중심에서 익숙한 뒷모습을 발견하고 외쳤다.

“야율 대협! 멈춰! 닥돌 멈춰!”

“……안 그래도 멈춰 있었다.”

야수묘왕의 말은 사실이었다. 여전히 분노한 얼굴이긴 했지만 그는 제자리에 우뚝 서 있었고, 주위에는 독물과 맹수들의 사체가 널브러져 있었다.

“이건 뭡니까?”

“갑자기 사방에서 미친 듯이 덤벼들더군. 그 바람에 놈을 놓치고 말았다.”

강자에게 섣부르게 덤비지 않는 것은 인간이나 짐승이나 똑같다. 아니, 본능이 뛰어난 짐승이 오히려 더욱 몸을 사리는 법이다.

하지만 그럼에도 불구하고 야수묘왕의 앞길을 막아섰다는 것은…….

“혹시 그놈을 위해서?”

“모르지. 하지만 어떤 이유에서건 이상할 것은 없다. 이 땅은 원래 이런 곳이니까. 아마 백 년 전에도, 이백 년 전에도 마찬가지였겠지.”

묘한 대답이다. 마치 처음부터 잘 알고 있었다는 듯.

내가 의아한 눈빛을 보내자 야수묘왕이 굳은 얼굴로 말을 이었다.

“과거 오독문은 다른 부족과 달리, 맹수보다는 독물을 키우는 것에 집중했다.”

독은 어느 곳에서나 멸시받지만, 실상은 무엇보다 효율적인 무기다.

오독문의 입장에서는 더더욱 그랬을 거다. 그들은 자신들을 제외한 남만 전체를 적으로 돌렸고, 못해도 수십 배에 달하는 적들을 상대해야 했으니까.

“그렇게 만들어진 곳이 독혈지(毒血地)라고 했다. 남만이 아니라 천하를 통틀어도 가장 흉포하고 악랄한 맹수와 독물이 들끓는 장소. 오독문이 남긴 것 중 가장 치명적이면서도 은밀한 유산.”

“그 말씀은 혹시 여기가…….”

야수묘왕이 작게 고개를 끄덕였다.

“바로 그 독혈지다.”

“후. 어쩐지 길도 하나 없더라. 그런데 말씀하신 것만큼 위험한 것 같지는 않은데요. 숨도 쉴 만하고.”

물론 오는 길에 짝퉁 천년독각사를 만나고, 들숨 날숨 한 번에 탄산 같은 독기가 스며들긴 하지만 지금까지는 그럭저럭 괜찮았다.

물론 뒤이어 들려온 야수묘왕의 목소리를 들은 후에는 썩 괜찮지 못하게 되었지만.

“그렇겠지. 우리가 있는 곳은 독혈지 내에서도 외곽. 아직 입구에 불과하니까.”

“입구요?”

“기록에 따르면 백여 년 전, 남만의 각 부족에서 최고의 정예만을 선발해 독혈지에 진입했다. 등유(燈油)로 가득 찬 수백 개의 항아리와 독에 저항할 피독주(避毒珠)를 입에 물고. 결과가 어떻게 되었을 것 같으냐?”

“모두가 무사 귀환해서 오래오래 행복하게 살지는 않았을 것 같은데요.”

“한 사람도 돌아오지 못했다. 그 후 모든 것이 수포로 돌아갔고, 애뇌산이 지금까지도 금지(禁地)로 내려오는 가장 큰 이유지.”

야수묘왕이 가리킨 손끝을 따라 시선을 옮기자, 언뜻 봐도 수백 장 길이로 펼쳐진 커다란 늪이 있었다.

그 위에 내려앉은 안개를 물끄러미 바라보던 내가 조심스럽게 입을 뗐다.

“그런데, 이 동네 안개는 보통 녹색입니까?”

“그럴 리가. 안개는 보통 흰색이지.”

“저건 녹색인데요.”

“아. 그건 독무(毒霧)라서 그렇다.”

“……?”

마치 어머니께서 오늘 저녁은 된장찌개란다, 라고 말하는 수준의 자연스러움에 잠깐 당황한 내가 애써 침착하게 물었다.

“……도대체 절 어디로 데려오신 겁니까?”

“독혈지.”

“…….”

시벌, 저걸 지금 말이라고.

내 어이없는 눈빛에 야수묘왕이 입맛을 다셨다.

“나도 들어오고 나서야 알았다. 독혈지의 위치가 어디인지는 기록에도 정확히 나와 있지 않았으니까.”

빌어먹을 상황이다. 나는 백호가 여기까지 다른 이들을 데려올 수 있을까 생각하며 대답했다.

“그럼 여기보다 더 안으로 들어가면 뭐가 있는 겁니까?”

“그야 모르지. 다 죽었으니까.”

“그거 굉장히 위안이 되네요.”

“당시 본 궁의 궁주셨던 백상의 조부께서도 저곳에서 돌아가셨지. 백족 역사상 가장 강했던 전사라고 들었다.”

남만야수궁의 주인은 완전한 일족 세습으로 이루어지지 않는다.

야율목도 명목상의 소궁주일 뿐. 만약 궁주의 자리가 공석이 되면 부족 대회의가 열리고, 그중에서도 가장 강성한 사대 부족의 대족장 중 하나가 투표를 거쳐 궁주로 취임한다고 했다.

“야율 대협보다 말입니까?”

“알 수 없다. 강자의 기준은 늘 바뀌는 법이니. 하지만 나와 같은 시대에 계셨다면 지금쯤 야수묘왕이 아니라, 야수백왕(野獸白王)이 있었어도 이상하지 않을 것이다.”

야수묘왕이 이렇게까지 말하는 것을 보니, 중원의 기준으로는 최소 초절정 고수. 그것도 중단전을 열었던 수준 이상이었음이 분명했다.

‘문제는 그 정도의 고수가 남만 최정예 전사들과 함께 독혈지에서 전멸했다는 거고.’

그보다 더 큰 문제는 지금 내가 저곳으로 들어가야 한다는 거지.

하지만…….

“여기까지 와서 돌아갈 수는 없죠. 갑시다.”

담담하게 입을 연 내 모습에, 야수묘왕이 뜻밖이라는 듯한 표정을 지었다.

“의외군. 돌아가자고 할 줄 알았는데.”

“누가 그랬습니다. 남자가 한 번 칼을 뽑았으면 독혈지라도 썰라고.”

“……도대체 누가?”

“제가요.”

떨떠름하게 나를 쳐다보던 야수묘왕이 씩 웃었다.

“적 노께서 제자를 잘 키웠구나.”

“그, 따지고 보면 숱한 폭력과 억압의 시간이긴 했는데…… 미주알고주알 말해서 뭐 합니까. 어차피 제가 무슨 말을 하더라도 야율 대협은 듣지 않으실 거고.”

“그걸 말이라고 하느냐?”

까드득.

힘껏 말아쥔 커다란 주먹에서 뼈 어긋나는 소리가 울려 퍼진다. 야수묘왕의 입술 사이로 서늘한 목소리가 흘러나왔다.

“나는 묘족의 대족장이지만, 남만야수궁의 궁주이기도 하다. 그들의 핏값을 받아내야지.”

아마 이런 모습 때문일까? 그가 남만야수궁의 궁주가 될 수 있었던 이유는.

내가 새삼스러운 눈빛으로 바라보고 있을 때, 야수묘왕이 문득 입을 열었다.

“고맙다. 도와주어서.”

“그럼 어떡합니까. 사람들이 죽었는데. 여기에 혼자 두고 돌아갈 수는 없죠.”

“설령 저 안에 암천(暗天)이 없다 해도, 그렇게 할 테냐?”

“제가 그렇게 겁 많은 놈이 아니라서요.”

야수묘왕의 입가에 희미한 웃음이 맺혔다.

“중원에서는 너 같은 자를 협객(俠客)이라 부른다더군.”

“절 싫어하는 사람들은 보통 시벌놈이라고 합니다. 주로 미친놈 소리를 많이 듣는 편이고요.”

엄연한 사실이라 상처받지도 않는다. 그리고 그런 말을 했던 이들 중 대부분은 내 손에 죽었다. 이래서 사람은 언제나 입을 조심해야 하는 법이다.

‘협객이라.’

내가 정말 협객인지, 아직도 잘 모르겠다.

하다 보니 여기까지 왔고, 어쩌다 보니 그렇게 불리고 있을 뿐이다.

중원에는 협객. 현대에서는 영웅. 하지만 그게 뭐가 중요한가. 남들이 뭐라 부르건 나는 내가 하고 싶은 대로 해 왔고, 암천은 그중에서도 특히 마음에 들지 않는 존재였을 뿐이다.

‘그래. 한번 붙어 보자. 저 안에 뭐가 있건 간에.’

나 혼자라면 모를까. 야수묘왕과 함께라면 설령 남천마후가 기다리고 있다고 해도 승산이 있다.

저벅.

생각을 끝마친 내가 야수묘왕을 따라, 진녹색의 독무(毒霧)에 휩싸인 늪지대로 걸음을 내디딘 그때였다.

띠링. 띠링. 띠링.



- 퀘스트 조건, [제한 시간 안에 애뇌산 조사]를 완료했습니다!

- 돌발 퀘스트, [알 수 없는 징조]를 성공적으로 완료했습니다!

- 퀘스트 완료 보상이 주어집니다!

- 소량의 경험치와 명성을 획득했습니다!

- [상급 해독제]x20를 획득했습니다!



갑작스럽게 울려 퍼진 시스템 알림. 하지만 그것이 끝이 아니었다.

띠링.



- 숨겨진 장소, [독혈지]에 진입했습니다!

- [독혈지]는 과거 존재했던 오독문이 만들어 낸 가장 은밀한 장소로, 그들은 이곳에서 수많은 독물을 키우고 해독할 수 없는 극독을 만들어 냈습니다.

- 매우 희귀한 업적, [어케 찾았누]를 달성하셨습니다!

- 업적 달성 보상으로 [상급 피독주]를 획득했습니다!

- 연계 퀘스트가 생성되었습니다!

- 퀘스트, [님아, 그 늪을 건너지 마오]를 수락하시겠습니까?



“…….”

시발 거. 퀘스트 제목 꼬라지 봐라.

나는 볼수록 대답하기 싫어지는 홀로그램 창을 떨떠름하게 바라보다가, 이내 고개를 끄덕였다.



- 퀘스트, [님아, 그 늪을 건너지 마오]를 수락하셨습니다!



그리고 진녹색의 독무 속에서 본능적으로 한숨을 내쉰 그 순간, 깨달았다.

삐빅.



- [독무]의 패널티 효과가 발동했습니다!



“……!”

뭔가 단단히 잘못되었다는 것을.

삐빅! 삐빅! 삐비비빅!



- 공기 중에 스며들어 있던 독이 호흡기와 피부를 통해 신체 내부로 침투합니다!

- 당신의 특성, [천독불침]과 [열양지기]로 인하여 [중독]의 패널티가 감소합니다!

- 상태 이상, [미약한 중독]에 걸렸습니다!

- 모든 능력치가 10씩 하락합니다!

- [미약한 중독]이 일정 시간 이상 지속될 경우, 패널티 효과가 증가하며 죽음에까지 이를 수 있습니다!



“…….”

한숨 한 번 내쉰 것 정도로 중독에 걸려?

심지어 피부로 독이 침투한다고 하니 숨을 안 쉬어도 중독된다는 소리나 다름없다.

‘아니, 뭐 이런 개 같은 경우가.’

시작부터 어이가 없었지만 참았다. 내게는 때마침 이런 상황에서 가장 큰 효과를 발휘하는 물건이 하나 있었으니까.

‘인벤토리 오픈. 소환.’

검게 빛나는 보석이 박힌 반지. 사천당문의 신물인 만독지환(萬毒指環)을 꺼내어 손가락에 끼우자, 상태 이상이 해제되었다는 시스템 알림과 함께 잠시 무거워졌던 몸이 가뿐해진다.

‘역시.’

그리고 흐뭇하게 웃으며 만독지환을 쓰다듬은 나는, 이내 말없이 이쪽을 노려보는 누군가의 시선을 발견하고 흠칫 놀랐다.

“아. 깜짝이야. 뭡니까?”

“……흡. 독. 흐읍. 말 걸지. 흐읍. 마라.”

아, 이 양반도 있었지.

짜게 식은 눈빛으로 야수묘왕을 바라보던 나는, 업적 완료 보상으로 받은 상급 피독주를 던져 주었다.
```

## Final English reading copy

```markdown
# Chapter 636

The valley was narrow and dark. Ancient trees of unknowable age grew thickly enough to block out the moonlight, while strange plants and creatures I had never seen before covered every direction.

And some of them were quite aggressive.

*Hiss!*

I was using my movement technique when I suddenly reached out. Something that had shot up from the grass like lightning writhed in my grip.

*Crackle. Crackle!*

*What is this? A snake?*

After taking a closer look, I realized I was only half right.

It was a snake, but not an ordinary one. The horns growing from either side of its triangular head were proof enough.

Wait. Haven’t I seen this somewhere before?

I stared intently at the snake and muttered under my breath.

“Mimi… No, a Thousand-Year Poison Horned Snake?”

*Crackle.*

Why was this thing here? Wasn’t the Thousand-Year Poison Horned Snake supposed to be one of the rarest venomous creatures in the world?

*Now that I look at it again, it seems a little different.*

*Is it because this is basically China? There are knockoffs everywhere.*

Compared to Mimi, its body was larger, but its sheen and horns were inferior.

I stared at the snake in my hand with disbelief, then threw it into the distance and picked up speed. Whether it really was a Thousand-Year Poison Horned Snake or not, one thing seemed certain: just as I had guessed, this valley was not a safe place.

*Just as I thought. Is this a trap?*

Perhaps because I had wasted a short amount of time before entering, the Black Tiger and the Beast Miao King were already far ahead.

The one fortunate thing was that, unlike the Black Tiger—which left no footprints, as though it really were a wraith—the Beast Miao King’s tracks remained here and there.

*Swish, swish, swish!*

After running like that for about seven minutes, I spotted a vast swamp drawing closer in the distance, along with a familiar back standing at its center.

I shouted.

“Great Hero Yayul! Stop! Stop charging in headfirst!”

“……I had already stopped.”

The Beast Miao King was telling the truth. His face was still twisted with anger, but he was standing perfectly still, with the corpses of venomous creatures and ferocious beasts scattered around him.

“What happened here?”

“They suddenly attacked from every direction like mad. I lost sight of it because of them.”

Humans and beasts alike knew better than to recklessly attack someone stronger than themselves. If anything, beasts with sharper instincts were even more cautious.

And yet, they had still blocked the Beast Miao King’s path.

“Could it have been for that creature’s sake?”

“I don’t know. But whatever the reason, it isn’t strange. This land has always been like this. It was probably the same a hundred years ago, and two hundred years ago.”

It was a strange answer. He sounded as if he had known about this place from the beginning.

When I gave him a questioning look, the Beast Miao King continued with a stern expression.

“In the past, unlike the other tribes, the Five Poisons Sect focused on raising venomous beasts rather than ferocious animals.”

Poison was scorned everywhere, but in truth, it was one of the most efficient weapons in existence.

That was even more true from the Five Poisons Sect’s perspective. They had turned all of Nanman except themselves into enemies and had to fight opponents who outnumbered them by at least dozens of times.

“The place they created for that purpose was called the Poisonblood Grounds.[^1] A place where the most savage and vicious beasts and venomous creatures in all of Nanman—and even the entire world—ran rampant. The most lethal yet secret legacy left behind by the Five Poisons Sect.”

“Then does that mean this is…”

The Beast Miao King gave a small nod.

“This is the Poisonblood Grounds.”

“Huh. No wonder there wasn’t even a path. But it doesn’t seem as dangerous as you made it sound. I can still breathe.”

Of course, I had encountered a knockoff Thousand-Year Poison Horned Snake on the way here, and poisonous air had seeped into me like carbonation with every breath in and out, but I had been more or less fine so far.

That changed after I heard the Beast Miao King’s next words.

“It would be. We are only in the outskirts of the Poisonblood Grounds. This is barely the entrance.”

“The entrance?”

“According to the records, around a hundred years ago, only the finest elites from each Nanman tribe were selected to enter the Poisonblood Grounds. They carried hundreds of jars filled with lamp oil and held poison-warding pearls in their mouths. What do you think happened?”

“I doubt they all returned safely and lived happily ever after.”

“Not a single person returned. Everything came to nothing after that, and it is the main reason Ailao Mountain has remained a forbidden land to this day.”

I followed the direction of the Beast Miao King’s pointing finger and saw a massive swamp stretching for hundreds of zhang.

I gazed blankly at the mist resting over it, then cautiously opened my mouth.

“By the way, is the fog around here usually green?”

“Of course not. Fog is usually white.”

“That one is green.”

“Ah. That is because it is poisonous mist.”

“……”

For a moment, I was thrown off by how naturally he said it, as casually as a mother announcing, “We’re having soybean-paste stew for dinner tonight.” I forced myself to remain calm and asked,

“……Where exactly have you brought me?”

“The Poisonblood Grounds.”

“……”

*For fuck’s sake. He calls that an answer?*

At my utterly disbelieving stare, the Beast Miao King smacked his lips.

“I only found out after entering. The records did not state the exact location of the Poisonblood Grounds.”

It was a goddamn mess. As I wondered whether White Tiger could bring the others this far, I asked,

“Then what is deeper inside?”

“How would I know? Everyone died.”

“That’s incredibly reassuring.”

“Baeksang’s grandfather, who had been the Palace Lord of this Palace at the time, also died there. I heard he was the strongest warrior in the history of the Bai people.”

The position of Palace Lord of the Nanman Beast Palace was not passed down through a single family in an entirely hereditary succession.

Yayul Mok was only the nominal Young Palace Lord. If the position of Palace Lord became vacant, a tribal council would be held, and one of the great chieftains from the four most powerful tribes would be elected as Palace Lord by vote.

“Was he stronger than Great Hero Yayul?”

“That is impossible to know. The standards for strength are always changing. But if he had lived in the same era as me, it would not have been strange for there to be a Beast Bai King instead of a Beast Miao King.”

Judging by how highly the Beast Miao King spoke of him, Baeksang’s grandfather had clearly been at least a Supreme Peak master by Central Plains standards—someone who had opened the Middle Dantian, if not gone beyond that.

*The problem is that a master of that level was wiped out in the Poisonblood Grounds alongside Nanman’s elite warriors.*

*And the even bigger problem is that I have to go in there now.*

But still…

“We’ve come all this way. We can’t turn back now. Let’s go.”

At my calm declaration, the Beast Miao King looked surprised.

“That is unexpected. I thought you would suggest turning back.”

“Someone once said that if a man draws his sword, he should cut through even the Poisonblood Grounds.”

“……Who said that?”

“I did.”

The Beast Miao King stared at me with a dubious expression, then broke into a grin.

“Elder Jeok raised his Disciple well.”

“Well, if we’re being technical, it was years of violence and oppression… But what’s the point of going into every little detail? No matter what I say, Great Hero Yayul won’t listen anyway.”

“Is that something you say?”

*Crack.*

A sound like bones grinding out of alignment rang from the Beast Miao King’s tightly clenched fist. A chill entered his voice.

“I am the great chieftain of the Miao people, but I am also the Palace Lord of the Nanman Beast Palace. I have to collect the blood price for them.”

Perhaps this was why he had been able to become the Palace Lord of the Nanman Beast Palace.

As I looked at him in a new light, the Beast Miao King suddenly spoke.

“Thank you. For helping me.”

“What else could I do? People died. I couldn’t leave you here alone and turn back.”

“Even if there were no Dark Heaven inside, would you still do it?”

“I’m not such a coward.”

A faint smile formed at the corner of the Beast Miao King’s mouth.

“I have heard that people in the Central Plains call men like you chivalrous heroes.”

“People who dislike me usually call me a fucking bastard. I mostly get called a lunatic.”

Those were undeniable facts, so I was not offended. Besides, most of the people who had called me those things had died by my hand.

That was why people always had to watch their mouths.

*A chivalrous hero.*

I still did not know whether I was truly one.

I had simply ended up here after starting something, and somehow people had begun calling me that.

*A chivalrous hero in the Central Plains. A hero in the modern world.*

But what did that matter? Whatever other people called me, I had always done what I wanted. Dark Heaven had merely been an especially loathsome existence among the things I disliked.

*Fine. Let’s face it. Whatever is in there.*

I might not have had a chance alone, but with the Beast Miao King beside me, we had a chance—even if the Southern Heaven Demon Empress herself was waiting inside.

*Step.*

I had just finished my thoughts and followed the Beast Miao King into the swamp shrouded in deep green poisonous mist when—

*Ding. Ding. Ding.*

> **System**
>
> - **Quest condition:** **Investigate Ailao Mountain Within the Time Limit** has been completed!
>
> - **Unexpected Quest:** **Unknown Omen** has been successfully completed!
>
> - Quest completion rewards have been granted!
>
> - A small amount of **EXP** and **Fame** has been acquired!
>
> - **High-Grade Antidote** ×20 acquired!

The System notifications rang out without warning. But they were not over yet.

*Ding.*

> **System**
>
> - You have entered the hidden location, **Poisonblood Grounds**!
>
> - **Poisonblood Grounds** is the most secret location created by the former Five Poisons Sect. Countless venomous creatures were raised here, and deadly poisons for which no antidote existed were created.
>
> - You have achieved the extremely rare Achievement **How’d You Find This?**
>
> - You have acquired a **High-Grade Poison-Warding Pearl** as an Achievement reward!
>
> - A Chain Quest has been created!
>
> - Would you like to accept the Quest **My Good Sir, Do Not Cross That Swamp**?

“……”

*For fuck’s sake. Look at that goddamn quest title.*

I stared sourly at the holographic window. The longer I looked at it, the less I wanted to answer. In the end, I nodded.

> **System**
>
> - Quest **My Good Sir, Do Not Cross That Swamp** has been accepted!

And at the exact moment I instinctively sighed in the deep green poisonous mist, I realized.

*Beep.*

> **System**
>
> - The penalty effect of **Poison Mist** has activated!

“……!”

Something had gone seriously wrong.

*Beep! Beep! Beep-beep-beep!*

> **System**
>
> - Poison permeating the air is entering your body through your respiratory tract and skin!
>
> - Due to your traits, **Myriad-Poison Immunity** and **Scorching Yang Qi**, the penalty from **Poisoned** has been reduced!
>
> - You have been afflicted with the **Mildly Poisoned** status abnormality!
>
> - All stats have decreased by 10!
>
> - If **Mildly Poisoned** persists for a certain length of time, the penalty effect will increase and may even result in death!

“……”

I had been poisoned just from sighing once?

And if poison could enter through my skin, that meant I would get poisoned even if I stopped breathing.

*What the fuck kind of bullshit is this?*

It was absurd from the start, but I put up with it. Fortunately, I happened to have an item that was especially effective in situations like this.

*Open Inventory. Summon.*

I took out a ring set with a gleaming black jewel. The moment I put on the sacred treasure of the Sichuan Tang Clan, the Myriad-Poison Ring, a System notification announced that my status abnormality had been removed, and the heaviness that had briefly settled over my body vanished.

*Just as I thought.*

I smiled contentedly and stroked the Myriad-Poison Ring. Then I noticed someone silently glaring at me and flinched.

“Oh. You startled me. What is it?”

“……Hngh. Poison. Hngh. Don’t talk to me. Hngh.”

Oh, right. He was here too.

I gave the Beast Miao King a flat, chilled stare and tossed him the High-Grade Poison-Warding Pearl I had received as the Achievement completion reward.

[^1]: *Dokhyeolji*, literally “poison-blood grounds,” the name given to this deadly region by the Five Poisons Sect.
```
