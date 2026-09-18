<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0372.txt",
      "sha256": "3bd015ac74499d3033844d9af47194aee4cc27c84a55d1896ee767bb1736bbca",
      "bytes": 13084
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "26fe436f845d46ed19a6be1ee767690ed81b934f8d1396eb49541b64f821cbbd",
      "bytes": 2598
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "efa0d02eb5b1db9876301544ea2304dead7a728b8a491e28a8bf7cc13d7738d6",
      "bytes": 129783
    },
    {
      "path": "characters/Cheongpung the Ancient Sword.md",
      "sha256": "84a8dd92e7cde14e21f7a3c78c4c0e7327e9d5dd6ff5692d565a0126a557075a",
      "bytes": 683
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "8b95216792f26ef4d0dc5868cbcfe8cc271e74816c81186dee8970b319f1852b",
      "bytes": 894
    },
    {
      "path": "characters/Extinction Divine Nun.md",
      "sha256": "ebddc3205098f10ecdece489a400c05b359dca388d690e7679932dc97099aa03",
      "bytes": 655
    },
    {
      "path": "characters/Hanga.md",
      "sha256": "c64a8b13b4eab8967da190f6085020c4a3f574fa27a36ee4bba9b22adadd7c8a",
      "bytes": 568
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "9185dd59ab80b710562de655d9ba29549bb23f85f8e649057bdba7100d1af95d",
      "bytes": 1390
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "a7bdd9076daba9c582a115f7e2b945e6aca131e3e4f70073b0efc4983d4e81e2",
      "bytes": 655
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "9cafc2fd0c527fb8cd17ca101f561faf1293de5895c0e51323f37757ef382d50",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "cbb8fcffa6d7c70c2439b71368e18bfc95e9f331d715f3c4d849946f516b5627",
      "bytes": 99027
    }
  ],
  "estimated_tokens": 11051
}
-->

# Durable State Update — Chapter 372

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 372. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 372. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings (Arabic digits allowed in titles such as 1팀장; do not romanize). At
least one endpoint must occur in the source. The controller drops pairs already
in the address ledger. Do not invent risk-register rows. Beat plot paragraphs
are plain strings; continuity and translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 372,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 372,
    "continuity_sources": [372],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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

## Prior durable context

```json
{
  "active_continuity": [
    "The Sichuan Tang Clan is rebuilding seven days after the Three-Gate Bloodbath, which caused catastrophic casualties and ongoing funerals.",
    "Most Dark Heaven attackers involved in the Sichuan assault are dead or captured; the Third Fiend has been captured by an unidentified figure, while the Second Fiend's fate is unknown.",
    "Jin Taekyung is awake after exhausting himself, has reached the Supreme Peak realm and manifested Force, and is publicly known as the Blazing Flame Divine Dragon.",
    "Jeok Cheongang is alive but remains weakened and is recovering his strength.",
    "Dong Feng's dantian and martial arts were destroyed while shielding Jeok Cheongang; the Divine Physician is Mungyeong's Master.",
    "Mungyeong is the Slaughter Saint and Dong Feng's Disciple; Jin Taekyung now knows Mungyeong's identity.",
    "Hyuk Mujin and Gung Gibang are badly wounded after fighting the Third Fiend, and the Seven Fairies intervened to save Hyuk Mujin from being torn apart.",
    "Cheongpung remains a Supreme Peak master and is at the Sichuan Tang Clan with the Thousand-Year Poison Horned Snake Mimi.",
    "Tang Sadok remains among the critically wounded patients at the Sichuan Tang Clan.",
    "The Lord of Heaven temporarily possessed the Western Heaven Demon Lord's body and escaped after One Annihilation.",
    "The Myriad-Poison Ring remains in Jin Taekyung's possession and cannot be appraised by the System.",
    "Extinction Divine Nun is alive and serving as Emei Sect Leader; she and Cheongpung the Ancient Sword are investigating a strange formation linked to Dark Heaven."
  ],
  "continuity_sources": [
    371
  ],
  "open_questions": [
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Why did Mungyeong tell the companions that Jin Taekyung ordered the rescue of Emei?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?",
    "What is the purpose of the strange formation linked to Dark Heaven and the captured Third Fiend?",
    "How will Dark Heaven respond to the failed Three-Gate Bloodbath?"
  ],
  "safe_through": 371,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon.",
    "Use Mimi for 미미 and Mimi-chan for 미미쨩.",
    "Use Third Fiend for singular 삼괴 references and Three Fiends for collective references.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, and 신니 as Venerable Nun in forms of address."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 하오문    | **Lower District Sect**          |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 마교     | **Demonic Cult**                                 |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 시스템              | **System**                     |
| 스킬               | **Skill**                      |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 청풍고검 | **Cheongpung the Ancient Sword** | Alias of the Qingcheng Sect's Sect Leader; distinct from Cheongpung. |
| 멸절신니 | **Extinction Divine Nun** | Presumed-dead Supreme Peak master and Heaven-Shaking Venerable Nun’s only Senior Aunt. |
| 항아 | **Hanga** | Local village boy who lives near Jang Taebo. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 청성파 | **Qingcheng Sect** | Sect named in Baek Museong's comparison about disciplinary rules. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 서역 | **Western Regions** | Region from which the glasses were imported. |
| 기관진식 | **mechanisms and formations** | Fifth preliminary assessment category. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 삼괴 | **Three Fiends** | Collective form used by the Western Heaven Demon Lord for the Qilian Three Fiends. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 서천마군 | 청풍 | commander_to_young_opponent | you | gentle and taunting | Uses 자네 while identifying Cheongpung and discussing the Blood Lord. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 청풍고검 | 멸절신니 | sect_leader_to_senior_sect_leader | Venerable Nun | formal-deferential | Cheongpung the Ancient Sword addresses her as 신니 while praising Jin and Cheongpung. |

## Listed compact profiles

### Cheongpung the Ancient Sword.md

# Cheongpung the Ancient Sword (청풍고검)

- **Safe through:** Chapter 371
- **Aliases:** None
- **Role:** Sect Leader of the Qingcheng Sect and a Supreme Peak martial artist who mobilizes the sect to help Jin Taekyung find the Divine Physician at Mae Jonghak's request.
- **Personality:** Straightforward, genial, and willing to help with matters he considers worthwhile.
- **Voice:** Warm, plainspoken, and good-humored.
- **Relationships:** Mae Jonghak specifically asked him to assist Jin Taekyung, and he commits the Qingcheng Sect and its wider lay-disciple network to the search for the Divine Physician.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 371
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival.

### Extinction Divine Nun.md

# Extinction Divine Nun (멸절신니)

- **Safe through:** Chapter 371
- **Aliases:** None
- **Role:** Living Emei Sect Leader and Supreme Peak master who joins Cheongpung the Ancient Sword in investigating a strange formation linked to Dark Heaven.
- **Personality:** Not established beyond the fear and shock her sudden reappearance caused among the Emei disciples and the Third Fiend.
- **Voice:** Not established.
- **Relationships:** She is Heaven-Shaking Venerable Nun’s only Senior Aunt and was believed to have died after withdrawing from worldly affairs thirty years earlier.

### Hanga.md

# Hanga (항아)

- **Safe through:** Chapter 346
- **Aliases:** None
- **Role:** Local village girl, Jang-pal’s daughter, who lives near Jang Taebo and regularly visits him.
- **Personality:** Curious, energetic, observant, and already attentive to the value of information and food.
- **Voice:** Childlike, direct, and inquisitive, with an occasional surprisingly worldly remark.
- **Relationships:** Calls Jang Taebo Grandpa; Jang Taebo is his elderly neighbor and only conversational companion.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 371
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is a legendary wandering martial master and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, and casually threatening or violent when dissatisfied. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 371
- **Aliases:** None
- **Role:** Mungyeong is a young medical apprentice and Disciple of Dong Feng who is secretly the Slaughter Saint.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** Initially timid and deferential, he becomes clear, composed, and eloquent when arguing for mercy and justice.
- **Relationships:** Dong Feng is his Master; Jeok Cheongang recognizes him as the Slaughter Saint, and he has now disguised himself as First Fiend to intercept the fleeing Third Fiend.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 371
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃372화



“이곳일세.”

“절벽이네요? 평범한.”

다른 사람들과 함께 가파른 절벽 앞에 멈춰선 나는 주위를 둘러봤다.

백여 장에 달하는 높이와 온통 단단한 암석으로 이루어진 절벽의 풍경은 그리 특별해 보일 것도 없었다.

‘여기에 무슨 진법이 있다고?’

하지만 의문이 해결되는 데까지는 그리 오랜 시간이 필요하지 않았다.

문득 느껴지는 기시감을 따라 천천히 걸어간 나는 황갈색의 암벽 앞에서 걸음을 멈췄다.

“이건…….”

모든 것에는 흐름과 결이 있다. 보이지도, 만질 수도 없는 기운이라고 해도 그 범주를 벗어날 수 없다.

그리고 초절정의 경지에 오르며 진일보한 감각은, 부자연스러운 기의 흐름을 감지해 내기에 충분했다.

“진법(陳法)?”

내 중얼거림에 대답하는 목소리가 있었다.

“정확히는 환영진(幻影陳)이다.”

건조한 눈빛으로 내 얼굴을 훑어본 문경, 아니 살성이 앞으로 나서며 손을 뻗었다.

막대한 기의 움직임과 함께 단단하던 암벽이 안개처럼 사라지고 시커먼 동혈의 입구가 모습을 드러낸다.

“아주 개눈깔은 아니로군.”

“어, 예?”

“되묻지 마라.”

한마디를 툭 흘린 살성은 대꾸할 시간도 주지 않고 동혈을 향해 걸음을 옮겼다.

‘저게 욕이야, 칭찬이야.’

이거 묘하게 기분 나쁘네.

그렇다고 막상 화를 내는 것도 뭐한 것이, 살성의 말과 행동에서는 나에 대한 어떤 악감정도 느껴지지 않았다. 그저 다른 사람들을 대하는 것처럼 무미건조한 딱딱함만이 느껴질 뿐이다.

이러니 듣는 사람으로서는 화가 나기보다 머쓱해질 수밖에.

“…….”

물론 상대가 상대인지라 좋게좋게 넘어가려는 것도 있다.

살성이 그렇다는데 뭐 어쩔 거야. 좀 기분 나쁘더라도 참아야지.

몽정 얘기를 꺼내놓고도 멀쩡히 서 있는 것만으로도 감지덕지다.

‘살성을 쌀성으로 만들어 버릴 뻔했는데, 이 정도면 양반이지.’

그런 생각을 하고 있을 때, 옆에서 낮은 웃음소리가 들려왔다. 고개를 돌려보니 입꼬리를 씰룩거리는 적천강이 보였다.

“갑자기 왜 웃으세요?”

“그냥. 살성 저놈도 어지간히 솔직하지 못한 놈이구나, 하는 생각이 들어서.”

“예?”

“되묻지 마라.”

“……?”

뭐지. 최신 유행어인가.

그 말을 끝으로 휘적휘적 걸어가는 적천강의 뒷모습을 바라보던 나와 두 장문인은 시커먼 동혈을 향해 걸음을 내디뎠다.

‘그나저나…….’

이런 곳이 숨겨져 있었다니.

심지어 사천의 중심인 성도에서 한나절이면 올 수 있는 거리다. 평범한 양민의 걸음으로 한나절이니, 무공을 익힌 이들이라면 말할 것도 없다.

나는 끝없이 이어지는 동굴을 걸으며 주위를 둘러봤다.

‘입구부터 엄청 넓네. 사천당문의 지하 뇌옥보다 몇 배는 더.’

오면서 간략히 들었다. 바로 이 동굴에서 암천의 흉수들이 머물렀다고.

그렇게 많은 숫자가 어디에서 튀어나왔나 했더니, 여기에 숨어서 때를 기다리고 있었던 모양이다.

‘그런데 여기까지는 어떻게 들어온 거지?’

서천마군의 지휘 아래, 당문에 쳐들어온 적들의 숫자만 삼백여 명이다.

거기에 더해 청성과 아미로 향한 놈들까지 합친다면 결코 무시할 수 없는 머릿수가 된다.

‘사천성 치안이 그 정도로 개판인가. 아니, 아무리 그래도 개방과 하오문이라면 알아차렸을 것 같은데.’

한 줄기 의문을 품은 채 얼마나 걸었을까.

장정 열 명이 나란히 걸어도 될 만한 넓은 길이 끝나고 마침내 새로운 공간이 모습을 드러냈다.

그 순간, 나도 모르게 혼잣말이 흘러나왔다.

“……허. 이것 봐라.”

족히 천여 명은 수용하고도 남을 것 같은 면적. 천장에 박힌 수십 개의 야명주(夜明珠)가 은은한 빛을 뿌리고, 한구석에는 건량과 벽곡단이 가득 쌓인 항아리와 병장기 등이 놓였다.

그러나 내가 가장 놀란 것은 따로 있었다.

‘저게 뭐야.’

동굴 바닥 전체를 뒤덮고 있는 기이한 문양들.

마치 정교한 톱니바퀴처럼, 일정한 배치로 새겨진 그것들은 마치 오래전 잊힌 고대 왕국의 유적지 같았다.

“혹시 저게 아까 말씀하신 그……?”

내 물음에 청성파의 장문인인 청풍고검이 무거운 얼굴로 고개를 끄덕였다.

“맞네. 저것이 빈도가 말했던 기이한 진법일세.”

설마 했는데, 진짜 진법이었다니.

성라대연에서 진법을 포함한 각종 기관진식을 겪어 본 적이 있었지만 저만큼 크고, 이상한 건 처음 봤다.

‘이 정도면 기이한 걸 넘어서 기형적인데.’

어쩌면 신비로우면서도 위험해 보이는 문양 때문일지도 모른다.

나와 비슷한 생각을 했는지 적천강이 입을 열었다.

“그런데 저 괴상한 문양은 도대체 뭐지?”

“그것이…… 저희 쪽에서도 아직 알아낸 바가 없습니다.”

청풍고검에 이어 멸절신니가 말을 보탰다.

“지금으로서는 속단할 수 없소. 진법의 일부를 본떠 여러 석학과 명사들에게 보여 주었으나 아는 이가 없더구려. 아무도 모르는 서역(西域)의 문자일 가능성도 완전히 배제할 수 없겠소.”

그런데 그때, 나도 모르게 입술 사이로 한마디가 튀어나왔다.

“어, 이거 문자 아닌데?”

“……?”

“……?”

“……?”

모두의 시선이 나를 향해 쏠렸다. 동굴에 들어온 이래 시종일관 침묵을 지키던 살성이 불쑥 입을 열었다.

“근거는?”

“그, 근거요?”

“그렇게 주장하는 데에는 합당한 근거가 있을 터. 되묻지 말고 대답해라.”

당연히 있다. 수만 권의 책을 독파하며 지식을 쌓은 유명한 학자도, 일평생 무림을 종횡하며 수많은 경험을 한 무림의 명사도 반박할 수 없는 확실한 근거가.

‘통합 언어 팩.’

시스템의 힘으로 모든 언어를 자동으로 통역해 주는 [통합 언어 팩].

이것만 있으면 의사소통은 물론이고 글자를 읽고 쓰는 것까지 아무 문제가 없다.

현대에서 스켈레톤 워로드와 대화를 할 수 있었던 이유도 [통합 언어 팩] 덕분이었다.

그러나 패시브 스킬처럼 상시 적용되는 해석 기능에도 진법을 이루는 문양은 처음 모습 그대로였다. 이건 저 문양이 문자가 아니라는 확실한 근거다.

문제는…….

‘이걸 어떻게 설명하냐.’

괜히 말했다. 그냥 가만히 있을걸.

하지만 이미 너무 늦어 버렸다. 점점 깊어지는 살성의 눈빛에, 나는 더듬더듬 입을 열었다.

“찌, 찌.”

“찌찌?”

쌀성의 눈썹이 꿈틀거렸다. 처음으로 보이는 감정 표현. 몽정 사건을 떠올렸음이 분명하다.

“아, 아니, 찌찌가 아니고요.”

“그럼. 젖인가?”

“…….”

제발. 감정이라고는 한 톨도 느껴지지 않는 얼굴로 그런 말 하지 마.

“아니, 그게 아니고요.”

내가 황급히 손을 내젓던 그때, 적천강이 불쑥 끼어들었다.

“지금 내 제자를 겁박하는 건가? 감히 이 화왕의 후인이자 열화문의 소문주를?”

“겁박이라. 할 필요도 없지만 못 할 것도 없지.”

“우연찮게 구명의 은을 입어 참으려고 했는데, 문가(文家), 네놈이 이리 나온다면 노부도 가만히 있을 수 없지.”

점점 험악해지는 분위기 속. 나는 두 눈을 질끈 감으며 외쳤다.

“찌, 찍었는데요!”

“……!”

“……!”

“……!”

“예전에 책에서 본 것 같기도 하고…… 제 느낌상 글자가 아닌 것 같아서, 찍었습니다.”

순간 내려앉은 고요한 침묵. 들릴락 말락 하게 한숨을 내쉰 살성이 적천강에게 물었다.

“그래서, 저놈이 화왕의 후인이자 열화문의 소문주라고?”

잠시 말이 없던 적천강이 대답했다.

“생각해 보니 정식으로 입문식을 치르진 않았군.”

“…….”

“그러니까 엄연히 따지자면 본문의 정식 제자는 아닌 게지. 즉, 아직까지 이 녀석은 태원진가 소속이라고 봐야…….”

나와 시선이 마주친 적천강이 슬그머니 시선을 회피했다.

“여기까지 하겠네.”

“…….”

뭘 여기까지 해. 이미 할 말 다 해 놓고.

스승과 제자 간의 신뢰가 박살 나는 현장을 눈앞에서 목격한 멸절신니와 청풍고검이 떨떠름한 얼굴로 화제를 돌렸다.

“크흠. 어찌 되었건 이 기이한 진법에 관한 문제는 계속해서 알아봐야 할 것 같소.”

“지, 진 도우와 적 선배님의 고견이 큰 도움이 되었습니다.”

하나도 도움이 안 됐다는 건 하늘도 알고 땅도 알고 여기 있는 모두가 안다.

뒷골목 똥개도 안 믿을 소리로 상황을 일단락한 청풍고검이 그늘진 얼굴로 멸절신니에게 말했다.

“그나저나 참으로 믿을 수 없는 일입니다. 고작 진법으로 그 많은 숫자를 불러오다니. 허, 참.”

“그러게 말이오. 이런 일이 가능하다는 건 천하 각지 어디에서도 놈들이 나타날 수 있다는 것 아니겠소?”

잠깐, 지금 뭐라고?

설명하지 못하는 답답함과 찌찌의 후유증에 땅만 쳐다보고 있던 나는 고개를 번쩍 쳐들었다.

“왜 그러시는가, 진 시주?”

“아니. 방금 두 분께서 진법에 관해 나누신 이야기를 저는 처음 듣는 것 같아서요.”

“음? 이동진(移動陳) 말인가?”

“……이동진이요?”

“그렇다네. 삼괴의 말에 의하면 저 기이한 진법은 이동진이라고 불린다더군. 어디까지 믿어야 할지 알 수 없는 허무맹랑한 소리지만…… 암천은 저 진법을 통해 수백 리 거리를 뛰어넘어 이동했다고 하네.”

이동진. 이동진이라니.

갑자기 각진 뿔테 안경을 쓴 평론가가 걸어 나와서 이 진법의 별점은 네 개 반입니다, 라고 해도 지금만큼 당황스럽진 않을 거다.

‘이거, 어디서 많이 듣던 건데.’

거리를 뛰어넘어 수백 명을 이동시키는 진법이라니.

다시 떠올릴수록 가슴이 거세게 뛰고 입술이 바싹 마른다.

만약, 이동진이라 불리는 이 진법이 지금 내가 생각하고 있는 ‘그것’이라면?

‘아니, 그럴 리가.’

그러나 애써 부정하는 속마음과는 달리, 나도 모르게 목울대가 크게 일렁였다.

“혹시, 이 진법. 지금도 가동되는 겁니까?”

두 장문인을 향한 물음이었지만, 대답이 흘러나온 것은 살성의 입이었다.

“삼괴. 놈을 이곳에서 직접 잡았지.”

“……이동진을 통해 도주하려 했군요.”

“그래. 하지만 그건 놈의 생각일 뿐이었다.”

“그 말씀은…….”

“후에 놈이 실토한 대로 진법을 가동하려 했지만, 아무런 일도 일어나지 않았다.”

“아.”

“한 가지는 확실하지. 저 진법에서는 아무런 기의 흐름도 느껴지지 않는다. 이제는 힘을 완전히 상실한 껍데기에 지나지 않아.”

고저 없는 목소리로 설명을 끝마친 살성이 한 마디를 덧붙였다.

“지금까지 드러난 정황을 보건대, 암천은 틀림없는 마교의 후신(後身)이다. 마교가 보유한 괴공절학(怪功絶學)은 셀 수도 없이 많으니 어떤 기이한 술법이 있다고 한들 이상하지 않지.”

마교가 어떤 곳인지는 오래전부터 귀에 못이 박이도록 들어 왔다.

사마외도(邪魔外道) 그 자체라 할 수 있는 강대한 종교 집단.

비록 최종적으로는 정마대전에서 패배했지만, 상당한 기간 천하 무림을 상대로 압도할 수 있었던 것은 마교가 보유한 괴공절학 덕택이었다.

‘그럼 이 진법도 마교로부터 전해진 수많은 괴공절학 중 하나라고?’

생각해 봐도 도저히 모르겠다. 예전에 봤던 퓨전 판타지 소설에서 자주 나오던 소재라 그런가. 괜히 더 헷갈리는 기분이다.

‘묵형에서는 잘만 넘어가던데. 후, 완결도 안 나는 걸 괜히 봐 가지고.’

그래도 혹시 모르니 진법의 배치와 문양 정도는 외워 두기로 했다.

내가 뚫어져라 이동진을 보며 머릿속에 새겨 나가던 그때, 살성이 문득 입을 열었다.

“네 태도를 보아하니 뭔가 아는 것 같은데. 혹 짚이는 것이라도 있느냐?”

“…….”

이건 뭐라고 변명을 해야 하나.
```

## Final English reading copy

```markdown
# Chapter 372

“This is the place.”

“It’s a cliff, isn’t it? A pretty ordinary one.”

I stopped in front of the steep cliff with the others and looked around.

The cliff was over a hundred zhang high and made entirely of solid rock, but there was nothing particularly special about it.

*There’s supposed to be a formation here?*

However, it didn’t take long for my question to be answered.

Following the strange sense of déjà vu I suddenly felt, I walked slowly until I stopped in front of a yellowish-brown rock wall.

“This is…”

Everything has a flow and a grain. Even something as invisible and untouchable as qi cannot escape that principle.

And the senses I had honed after reaching the Supreme Peak realm were more than enough to detect the unnatural flow of qi.

“A formation?”

A voice answered my mutter.

“More precisely, an illusion formation.”

Mungyeong—or rather, the Slaughter Saint—stepped forward and extended a hand after scanning my face with dry eyes.

Along with the tremendous movement of qi, the solid rock wall vanished like mist, revealing the entrance to a dark cavern.

“You’re not completely blind, at least.”

“Uh, what?”

“Don’t ask again.”

The Slaughter Saint tossed out that one remark and walked toward the cavern without even giving me time to respond.

*Was that an insult or a compliment?*

It left a strangely unpleasant feeling.

But even so, getting angry would have been awkward. There was no hostility toward me in the Slaughter Saint’s words or actions. They were merely as dry and stiff as the way he treated everyone else.

So instead of making the listener angry, his words could only leave them feeling awkward.

“…”

Of course, the identity of the person saying it had something to do with my willingness to let it slide.

What else was I supposed to do if that was just how the Slaughter Saint was? Even if it bothered me a little, I had to put up with it.

Considering that I was still standing after bringing up wet dreams, I should be grateful.

*I nearly turned the Slaughter Saint into the Rice Saint, so this is practically getting off easy.*[^1]

I was thinking that when I heard a low chuckle from beside me. I turned my head and saw Jeok Cheongang twitching the corners of his mouth.

“Why are you laughing all of a sudden?”

“Nothing. I was just thinking that the Slaughter Saint is remarkably incapable of being honest.”

“What?”

“Don’t ask again.”

“…”

What was this? Was it some new catchphrase?

After saying that, Jeok Cheongang strode away. The two Sect Leaders and I followed him into the dark cavern.

*Come to think of it…*

I couldn’t believe a place like this had been hidden here.

It was even close enough to reach from Chengdu, the heart of Sichuan, in half a day. That was at an ordinary commoner’s walking pace, so people who knew martial arts could get here much faster.

I walked through the seemingly endless cavern, looking around.

*The entrance alone is huge. It’s several times larger than the underground prison beneath the Sichuan Tang Clan.*

I had heard a brief explanation on the way here. The murderous criminals of Dark Heaven had stayed in this very cavern.

So this was where they had been hiding and waiting for the right moment. That explained where so many of them had appeared from.

*But how did they get in here in the first place?*

There had been over three hundred enemies who attacked the Tang Clan under the Western Heaven Demon Lord’s command.

If the ones who went to Qingcheng and Emei were added to that number, it became a force that couldn’t be ignored.

*Was security in Sichuan Province really that terrible? No, even so, wouldn’t the Beggars’ Sect and the Lower District Sect have noticed them?*

I had been walking with that question in mind for who knew how long when the passage—wide enough for ten grown men to walk abreast—finally ended, revealing a new space.

Without meaning to, I muttered,

“…Huh. Look at this.”

The area was large enough to accommodate well over a thousand people. Dozens of night-shining pearls embedded in the ceiling cast a soft glow, while jars and containers full of dry rations and fasting pills, along with weapons, were stacked in one corner.

But that wasn’t what surprised me most.

*What is that?*

Strange patterns covered the entire floor of the cavern.

Carved in regular arrangements like intricate gears, they looked like the ruins of an ancient kingdom forgotten long ago.

“Is that perhaps the thing you mentioned earlier…?”

At my question, Cheongpung the Ancient Sword, the Sect Leader of the Qingcheng Sect, nodded gravely.

“That is correct. That is the strange formation I mentioned.”

I had wondered if that was really what they were talking about, but it was actually a formation.

I had experienced various mechanisms and formations at the Star-Array Grand Banquet, but I had never seen anything so large or strange.

*This has gone beyond strange and become downright malformed.*

Perhaps it was because of the patterns, which looked mysterious yet dangerous.

Jeok Cheongang seemed to have the same thought and spoke up.

“But what in the world are those bizarre patterns?”

“We have not yet been able to determine that either.”

Extinction Divine Nun added to Cheongpung the Ancient Sword’s words.

“We cannot make a hasty judgment at this point. We copied part of the formation and showed it to several learned scholars and famous figures, but none of them recognized it. We also cannot completely rule out the possibility that it is writing from the Western Regions, unknown to anyone here.”

But then, before I knew it, a sentence slipped out between my lips.

“Uh, that isn’t writing.”

“…”

“…”

“…”

Everyone’s eyes turned toward me. The Slaughter Saint, who had remained silent ever since we entered the cavern, suddenly spoke.

“What is your basis?”

“My… basis?”

“If you claim that so confidently, there must be a sound reason. Answer me without asking another question.”

Of course I had a reason. A solid reason that neither a renowned scholar who had accumulated knowledge by reading tens of thousands of books nor a famous martial artist who had traveled throughout the Murim all his life could refute.

*The Integrated Language Pack.*

The *Integrated Language Pack* translated every language automatically through the power of the System.

With it, communication wasn’t the only thing I could manage. I could also read and write.

It was thanks to the *Integrated Language Pack* that I had been able to speak with the Skeleton Warlord in the modern world.

Yet even though its interpretation function was always active like a passive Skill, the patterns forming the formation had remained exactly as they were.

That was definitive proof that those patterns were not writing.

The problem was…

*How am I supposed to explain that?*

I shouldn’t have said anything. I should have just kept my mouth shut.

But it was already too late. As the Slaughter Saint’s gaze grew more intense, I stammered,

“Bo… bo.”

“Boobs?”

The Rice Saint’s eyebrow twitched. It was the first emotion he had shown. He had clearly remembered the wet-dream incident.

“Ah, no, not boobs.”

“Then breasts?”

“…”

Please. Don’t say things like that with a face that didn’t show a single trace of emotion.

“No, that’s not what I meant.”

I was waving my hands frantically when Jeok Cheongang suddenly interrupted.

“Are you threatening my Disciple? How dare you threaten the heir of the Fire King and the Young Sect Leader of the Fire Gate Clan?”

“Threatening him? It isn’t necessary, but it isn’t beyond me either.”

“I was trying to let it pass out of gratitude for the favor of saving my life, but if you, Mun, are going to act like this, then this old man cannot remain still either.”

As the atmosphere grew increasingly hostile, I squeezed my eyes shut and shouted,

“I guessed!”

“…”

“…”

“…”

“I think I saw something like it in a book before… and it just felt like it wasn’t writing, so I guessed.”

A heavy silence settled over the cavern.

The Slaughter Saint let out a barely audible sigh before asking Jeok Cheongang,

“So that fellow is the heir of the Fire King and the Young Sect Leader of the Fire Gate Clan?”

Jeok Cheongang was silent for a moment before answering.

“Now that I think about it, he never went through the formal initiation ceremony.”

“…”

“So strictly speaking, he isn’t an official Disciple of our sect. In other words, he should still be considered a member of the Jin Family of Taiyuan…”

Jeok Cheongang’s eyes met mine, and he quietly looked away.

“That will be all.”

“…”

What did he mean, that would be all? He had already said everything there was to say.

Extinction Divine Nun and Cheongpung the Ancient Sword had just witnessed the complete destruction of trust between Master and Disciple. With awkward expressions, they changed the subject.

“Ahem. In any case, it seems we will have to continue investigating this strange formation.”

“F-Fellow Daoist Jin and Senior Jeok’s insights were a great help.”

Heaven and earth knew that they hadn’t helped at all. Everyone here knew it, too.

Even a stray dog in a back alley wouldn’t believe that.

After bringing the situation to an end with that unbelievable statement, Cheongpung the Ancient Sword spoke to Extinction Divine Nun with a troubled expression.

“More importantly, this is truly unbelievable. To summon such a large number of people with nothing but a formation. Honestly…”

“Indeed. If such a thing is possible, does that not mean they could appear anywhere throughout the land?”

Wait. What did they just say?

I had been staring at the ground, frustrated by my inability to explain myself and still suffering from the aftermath of the boob incident. I abruptly raised my head.

“What is the matter, Benefactor Jin?”

“No, it’s just… I think this is the first time I’ve heard the two of you mention something about the formation.”

“Hmm? You mean the Moving Formation?”

“…The Moving Formation?”

“That is correct. According to the Third Fiend, that strange formation is called a Moving Formation. We cannot know how much of their absurd story to believe, but they say Dark Heaven used that formation to leap across hundreds of li.”

A Moving Formation. They said it was a Moving Formation.

Even if a critic wearing angular horn-rimmed glasses had suddenly walked out and announced, “This formation gets four and a half stars,” I wouldn’t have been any more bewildered than I was now.

*This sounds familiar.*

A formation that could move hundreds of people across hundreds of li.

The more I thought about it, the harder my heart pounded and the drier my lips became.

What if this formation called a Moving Formation was *that thing* I was thinking of?

*No, that can’t be.*

But despite my desperate denial, my Adam’s apple bobbed heavily.

“Is this formation still operational?”

I had asked the two Sect Leaders, but it was the Slaughter Saint who answered.

“The Third Fiend. I caught him here myself.”

“…He tried to escape through the Moving Formation.”

“That was his intention. But that was all it was.”

“What do you mean?”

“According to what he later confessed, he tried to activate the formation, but nothing happened.”

“Oh.”

“One thing is certain. No flow of qi can be felt from that formation. It has completely lost its power and is now nothing more than an empty shell.”

After explaining in his flat voice, the Slaughter Saint added one more thing.

“Judging from the circumstances that have come to light, Dark Heaven is without a doubt the successor to the Demonic Cult. The Demonic Cult possesses countless monstrous martial arts and supreme techniques, so it would not be strange if they had any number of bizarre arts.”

I had heard what sort of place the Demonic Cult was so many times that it had practically been beaten into my head.

A powerful religious organization that could be called demonic, heterodox arts incarnate.

Although it had ultimately lost the Great Faction War, the reason it had been able to overwhelm the Murim of the entire land for so long was because of the monstrous martial arts and supreme techniques it possessed.

*So this formation is one of the countless bizarre techniques passed down from the Demonic Cult?*

No matter how much I thought about it, I couldn’t figure it out. Maybe it was because this was a trope I’d seen so often in the fusion-fantasy novels I had read before. Somehow, that only made it more confusing.

*They got away with it just fine in* Mukhyung. *Ugh. I shouldn’t have read a novel that never even got an ending.*

Even so, just in case, I decided to memorize the formation’s arrangement and patterns.

I was staring intently at the Moving Formation and carving it into my mind when the Slaughter Saint suddenly spoke.

“Judging by your attitude, you seem to know something. Does it remind you of anything?”

“…”

What excuse was I supposed to make?

[^1]: In Korean, *sal* means “slaughter,” while *ssal* can mean “rice” and also evokes *ssada*, slang for ejaculating—tying the wordplay to the wet-dream incident.
```
