<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0949.txt",
      "sha256": "919efa6bc6b8e2f73207b0bd6f9113b69bda4727c0a0487e4d924ed873f14b3e",
      "bytes": 14534
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a67f90ba91cef6e5e259810fa2bfc3ec795d6959afb1716171532babaea1d7c3",
      "bytes": 2923
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bbb6bd1bdb9407382aeed622923c33e7d8077914c1c9edfd5dc0c45aea7b5f65",
      "bytes": 233797
    },
    {
      "path": "characters/Chinggen.md",
      "sha256": "90dbcb7920db5cdf8f54f4b818bac4fd2e459a15a58d4cfcc21a63b8485372aa",
      "bytes": 577
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "700a0ddce3ad9d43f0ee95a3b1112e9b31cc4a3348478eadf6cbd5dbf1591a86",
      "bytes": 759
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "e8b6051a979eeda2be87ec9cccdf6da4d1c4847095e20f1980261faccf8d4e21",
      "bytes": 1289
    },
    {
      "path": "characters/Lee Cheonbaek.md",
      "sha256": "f24c1420229bea9193fdeb7efea5de403bd041d754bfef427da4722b1e96aa1b",
      "bytes": 3231
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "72a838b5c0eb92a0f743bd3c84a9e6270c229e466f8b7d75f5e3cd5b62fa9e58",
      "bytes": 1071
    },
    {
      "path": "characters/Temur.md",
      "sha256": "460341371e54cadef2bd130197b2e919cc68800af986be643cd627b66fb3a36b",
      "bytes": 616
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "ca261203b925151175c2ef0cea3ab3b3fa5638a77fc638824a37ace66e10e587",
      "bytes": 954
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1efb275a0485bdab8f74bddeafc29157bc04997b8313766f8a1a4de940fca98a",
      "bytes": 267426
    }
  ],
  "estimated_tokens": 11511
}
-->

# Durable State Update — Chapter 949

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
1 and safe_through 949. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 949. Profile updates may replace only one
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
  "chapter": 949,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 949,
    "continuity_sources": [949],
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
    "The Emperor was poisoned with Blood Soul Gu, which reached his marrow; the Divine Physician said his vitality was at its limit and could not guarantee survival for another couple of months.",
    "The Divine Physician says the Emperor’s only path to survival requires him to die once; the method is not yet explained.",
    "Taekyung’s System Quest requires him to remove the Blood Soul Gu from the Emperor’s head and successfully treat him; its reward and failure consequence are unknown.",
    "At least ten thousand grassland troops are heading toward Shanxi and may arrive within seven days; Peng Cheolyeong suspects an alliance with Dark Heaven, and the Jin Family of Taiyuan is preparing for battle.",
    "War against Dark Heaven is imminent; its main force has been targeting Shanxi as a foothold for invading the Central Plains, with the Double Ninth Festival the expected date.",
    "Taekyung was appointed Marquis of Shangshan and Thousand Captain, with a thousand Embroidered Uniform Guards entrusted to him to fight the foreign enemy.",
    "The improved Temporary Strength Pill has circulated for months and may create a dangerous, addictive drive for strength across Murim; its full effects and distribution network remain unknown.",
    "An unconscious bandit chief is being taken to the Nangong Family for possible interrogation; he may hold important information about the pill.",
    "Jang Sam abruptly rose from Level 40 to Level 60, attacked Taekyung while apparently irrational, and is unconscious and being taken to the Nangong Family.",
    "Jang Sam’s silk pouch, received from an unknown traveler in Hubei, likely contained a modified Temporary Strength Pill; its effects and side effects remain unconfirmed.",
    "The Bow Saint once wondered whether Pung Yang might have been the chosen one; the Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s hidden iron chest contained old bamboo slips, recent papers, and a small silk pouch of unknown significance."
  ],
  "continuity_sources": [
    948,
    947
  ],
  "open_questions": [
    "Who was the traveler who gave Jang Sam the silk pouch, and what are the modified pill’s exact effects and side effects?",
    "How widely has the improved Temporary Strength Pill spread, and who is distributing it?",
    "What is the Martial God’s identity, and what is his connection to the chosen one and the Bow Saint?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain, and what is their significance?"
  ],
  "safe_through": 948,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 위팽     | **Wipeng**         |
| 이천백    | **Lee Cheonbaek**  |
| 이소월    | **Lee Seowol**     |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 암천     | **Dark Heaven**                  |
| 무인     | **martial artist**                               | Default term                                          |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 표국     | **Escort Bureau**                            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 항산     | **Mount Heng**         |
| 팔천협    | **Eight Spring Gorge** |
| 본가      | **our family / this family**                                    |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 산음 | **Saneum** | Jin Family branch location |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 요녕 | **Liaoning** | Northeastern region from which the Murong Family arrives. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 테무르 | 칭겐 | fellow_chieftain | Chinggen | familiar and argumentative | Temur addresses his fellow chieftain by name while defending their khan lineage. |
| 칭겐 | 테무르 | fellow_chieftain | Temur | familiar and cautioning | Chinggen uses Temur's name while warning him not to act rashly. |
| 진위경 | 이소월 | host_to_new_sect_leader | Young Lady | formal-polite | Jin Wikyung addresses Lee Seowol as 소저 before accepting her oath. |
| 이소월 | 진위경 | new_sect_leader_to_lesser_family_head | Lesser Family Head | formal-deferential | Lee Seowol refers to Jin Wikyung as 소가주님 when describing his summons. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진위경 | 막내 | older brother to younger brother | my youngest | intimate and informal | Jin Wikyung uses 막내야 affectionately for Jin Taekyung. |

## Listed compact profiles

### Chinggen.md

# Chinggen (칭겐)

- **Safe through:** Chapter 948
- **Aliases:** None
- **Role:** Chinggen is a Khan of the northern grasslands, ruling alongside Temur over tens of thousands of horses and warriors.
- **Personality:** Prudent, restrained, and attentive to the danger posed by the gathering's other powers
- **Voice:** Measured, familiar, and cautioning
- **Relationships:** Temur is his brother and fellow Khan; they shared life and death since childhood and brought peace and prosperity to the grasslands.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 948
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 926
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung's eldest brother and future Family Head who protects and mentors him, commands Wipeng and the Jin Family's forces, has worked with Jeok Cheongang, maintains a political connection with Hongcheon, Prince Shangshan's hidden loyal retainer, and wants Taekyung to tell him his untold stories when the current crisis is over; Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Lee Cheonbaek.md

# Lee Cheonbaek (이천백)

- **Safe through:** Chapter 129
- **Aliases:** Blood Wolf Sword
- **Role:** Former Sect Leader of the Mount Heng Sword Sect, killed during the Red Wind Band’s assault; father of Lee Seogeun and Lee Seowol
- **Personality:** Grief-stricken, resolute, and fiercely vengeful
- **Voice:** Quietly mournful when addressing his son; firm and uncompromising when declaring revenge
- **Relationships:** Deceased father of Lee Seogeun and Lee Seowol; also father of a deceased Young Sect Leader; former leader of the Mount Heng Sword Sect; longtime close friend and peer of Cheol Mubaek

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 499
- **Aliases:** None
- **Role:** Lee Seowol is the eighteen-year-old Sect Leader of the reconstructed and rapidly growing Mount Heng Sword Sect, a vassal of the Jin Family of Taiyuan who still awaits Taekyung’s answer to her marriage proposal.
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek; younger sister of the deceased Young Sect Leader, Lee Seogeun, and Lee Seogwang; Cheol Mubaek's niece and protected charge, to whom he entrusted the Shura Annihilating Fist manual; has proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist; during her farewell with Taekyung, she asked him to address her as Young Lady rather than Sect Leader.

### Temur.md

# Temur (테무르)

- **Safe through:** Chapter 948
- **Aliases:** None
- **Role:** Temur is a Khan of the northern grasslands, ruling alongside Chinggen over tens of thousands of horses and warriors.
- **Personality:** Hot-tempered, reckless, proud of his khan lineage, and inclined to dismiss distant threats while indulging in celebration.
- **Voice:** Blunt, heated, and confrontational
- **Relationships:** Chinggen is his brother and fellow Khan; they shared life and death since childhood and brought peace and prosperity to the grasslands.

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 501
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and Commander of the Jin Dragon Squad; one of the Jin Family’s three Peak masters
- **Personality:** Loyal, observant, teasing, capable, and resigned to Jin Wikyung’s impulsive behavior. Respects the dead and urges others to live on their behalf.
- **Voice:** Weary and knowing, with dry humor when addressing Jin Wikyung or Jin Taekyung. Uses Sound Transmission when appropriate.
- **Relationships:** Trusted guard and retainer of Jin Wikyung; a reliable senior ally of Jin Taekyung. He has fought beside the Jin Family in major battles, including the conflict with Mount Heng, and remains alert to threats connected with Dark Heaven. The Human Butcher has claimed him as a personal target in a planned attack.

## Korean source

```text
＃949화



모든 일에는 전조(前兆)가 있다.

지진이 가까워지면 땅 울림과 함께 무수한 날짐승들이 일제히 날아오르고, 태풍이 들이닥치기 전에는 새털구름이 하늘을 가득 메우는 것처럼.

천벌이나 다름없는 자연재해조차 그럴진대, 한낱 인간이 벌이는 일이라면 더 무슨 말이 필요할까.

지금으로부터 불과 며칠 전, 몇몇 이들은 초원에서 전해지는 심상치 않은 징조를 느낄 수 있었다.

그것도 아주 또렷하면서도 분명하게.

‘유목민들이. 아니, 초원 전체가 움직이고 있다.’

옅은 어둠이 내리깔린 드넓은 대전(大殿) 내부. 장대한 체구의 사내는 말 없이 눈앞에 놓인 지도를 응시했다.

장정 서넛을 합친 것만큼이나 커다란 지도에는 대륙 전체의 지형과 지명으로 빼곡하게 채워져 있었으나, 그의 시선은 오직 한곳에 못 박혀 있을 뿐이었다.

산서(山西).

사내가 일평생을 나고 자란 고향이자, 선조들이 지켜온 땅.

지금으로부터 삼백여 년 전, 천하를 피로 물들이던 전란의 끄트머리에서 한 사람이 이 땅에 다다랐다.

성은 진가요, 이름은 무량이라.

그는 본래 환영받지 못하는 이방인이었으나, 태원(太原)에 이르러 주춧돌을 내려놓고 깃발을 세우니 그것이 곧 태원진가의 시작이었다.

‘그분께서도 모르셨겠지. 본가가 이토록 장구한 세월을 이겨 낼 수 있으리라고는.’

삼백여 년.

아득한 세월이다.

보는 이로 하여금 탄성을 자아내던 화려한 꽃도, 모두를 압도시킬 만큼 높고 크던 거목(巨木)도 반복되는 겨울과 시간 앞에서 쓰러졌다.

그러나 변방의 잡초는, 태원진가는 지금까지도 이 땅을 지키고 있다.

흐드러지게 피었다가, 꺾이고, 부서지고, 다시 일어나며.

“흥망성쇠(興亡盛衰)라.”

나직하게 뇌까린 사내, 진위경은 천천히 말을 이었다.

“본가의 흥(興)은 이미 오래전에 지났고, 망(亡)은 간신히 피할 수 있었지. 하여 이제는 틀림없이 성(盛)할 일만 남았다고 생각했는데…….”

진위경은 웃었다. 씁쓸하게.

“헛다리 한 번 제대로 짚었군. 자네도 그리 생각하지 않나?”

듣는 이 하나 없는 넋두리도, 혼잣말도 아니다.

철탑처럼 무겁고 호수처럼 고요하게 자신의 자리를 지키고 있던 위팽이 입을 열었다.

“지금 주군의 모습을 보고 있자니, 문득 옛 생각이 나는군요.”

“옛 생각?”

“사실 옛날이라고 부를 만큼 오래된 일은 아닙니다. 고작 이 년 전이니까요.”

“항산검문(恒山劍門)…….”

“맞습니다. 그때도 주군께서는 이런 모습이셨죠.”

위팽은 귀검(鬼劍)이라는 별호처럼 서늘한 목소리로 말을 이었다.

“싸움은 시작도 안 했습니다. 검을 뽑기도 전에 내려놓으실 생각이십니까?”

“그리 보이나?”

“그렇게 보입니다. 지금 제 눈에는.”

가장 가까운 충복의 단호한 대답에 진위경은 입술을 깨물었다.

즉각 부정하지 못하는 스스로의 모습이 부끄러워서.

그와 더불어 찰나의 오기로나마 결정을 내리지 못하게 만드는 현실이 암담해서.

“나는…… 본가의 소가주일세. 짧은 말 몇 마디, 사소한 행동 하나에 수많은 목숨이 걸려 있어.”

비단 태원진가뿐만이 아니다.

산서 무림 전체가 진위경의 의지에 따라 움직인다.

태원진가는 명실상부한 산서성의 패자이며, 그는 사실상 가주나 다름없으니까.

그리고 지금 이 순간에도 수만에 달하는 인마(人馬)의 파도는 이 땅을 향해 짓쳐 들고 있다.

“이미 산서성부를 통해 대동(大同)과 산음(山陰) 일대의 백성들을 대피시키라는 서한을 보냈네. 애꿎은 피해를 최대한 막아야 할 테니.”

대동과 산음은 초원과 가장 가까이에 인접한 현읍(縣邑).

국경을 넘어선 초원의 군세가 가장 먼저 짓밟고 지나갈 곳이기도 했다.

“항산검문 역시 마찬가지야. 물러서기에는 아직 늦지 않았네. 그것만이 멸문(滅門)을 피할 유일한 방법이지.”

“이 문주가 과연 그 제안을 받아들이리라 생각하십니까?”

“제안이 아닐세. 이건 명령이야.”

진위경은 가라앉은 목소리로 말을 이었다.

“다른 선택지가 없으니 지금쯤이면 그녀도 현실을 받아들였겠지.”

지난 이 년간, 태원진가의 깃발 아래에 몸을 의탁한 항산검문도 눈부신 성장을 이루었다.

여인의 몸으로 새롭게 문주가 된 이소월은 모두가 생각했던 것 이상으로 뛰어난 수완가였다.

전대 문주이자 부친이었던 혈랑검 이천백이 공포와 무력으로 항산검문을 세웠다면, 그녀는 특유의 영민함과 지도력으로 몰락 직전의 위기에 처해 있던 문파를 재건시켰다.

세간의 이목을 집중시킬 정도로.

그러나 제아무리 성장에 성장을 거듭했다 하더라도, 코앞에 닥친 위기를 헤쳐 나갈 수는 없을 것이 분명했다.

“삼만.”

진위경이 무거운 눈빛으로 위팽을 응시했다.

“놈들이 산서성에 이를 때쯤이면 삼만으로 불어나 있을 걸세.”

지난 며칠 간의 시간은 잔인하리만치 빠르게 흘렀다.

초원 곳곳에 흩어져 있던 유목민들이 집결하고 있다는 급보를 접한 어느 날, 초원의 교역로에 자리 잡은 여러 표국과 상단이 사라졌다.

물론 그들의 생사도, 흉수도 뻔했다.

“놈들의 목적은 분명하네. 뒤에 누가 있는지도.”

진위경은 테무르와 칭겐에 대해 잘 알고 있었다.

두 사람이 초원의 실력자로 급부상할 수 있었던 결정적인 이유 중 하나는, 태원진가의 지원이 있었기 때문이기도 했다.

“테무르는 강하지만 지극히 단순하고, 칭겐은 심계가 깊고 신중하나 지닌바 그릇이 작지. 절대로 이런 짓을 벌일 위인들이 아니야. 그럴 만한 힘도 없고.”

초원의 유목민들이 활과 돌격창으로 대륙을 질타했던 시대는 이미 오래전에 저물었다.

그들이 세운 제국은 흔적도 없이 사라졌고, 광활하나 황량한 들판으로 내쫓긴 유목민들은 동족끼리의 반목과 쇠퇴를 거듭했다.

“그들의 힘은 익히 입증된 바가 있네. 하지만 그 정도로는 중원을 넘보기에는 아직 부족해.”

어느덧 칸이라 불리게 된 테무르와 칭겐도 결국 초원의 여러 대족장(大族長) 중 한 사람에 불과하다.

반면 중원은 어떠한가.

각 성마다 적게는 수천에서, 많게는 일만이 넘어가는 대국의 병사와 저력 있는 무림 문파가 존재한다.

분열된 초원.

단결된 중원.

이 사이에는 너무나도 깊고 넓은 간격이 있다.

유목민들이 선조들의 위업을 이어 천하를 지배할 날은 두 번 다시 오지 않을 것이다.

또 다른 거대한 힘이 개입하지 않는 한은.

“내가 두려워하는 것은 삼만의 유목민들이 아닐세.”

진위경은 앞에 놓인 커다란 지도를 노려보았다.

마치 이 빼곡한 그림과 글자 어디에선가, 숨어 있던 무언가가 튀어나오기만을 기다리는 듯이.

“암천. 아직 드러나지 않은 놈들의 힘이, 나는 두렵네.”

지난 이 년간 태원진가는 늘 승승장구해 왔다.

그러나 축하와 환호의 나날 속에서, 진위경은 밤마다 찾아오는 끔찍한 악몽에 몸부림쳤다.

죽은 자들이 나오는 악몽을.



‘죽여라!’

‘한 걸음도 물러서지 마라!’



차차차창!

팔천협(八天峽).

적과 아군, 그리고 배신자들이 뒤엉켜 서로를 향해 짐승처럼 달려들던 피의 협곡에서 진위경은 매일 밤을 헤매었다.

‘소가주님. 괜찮으십…… 커헉!’

언제나 웃으며 인사를 건네던 가솔이 피를 흩뿌리며 쓰러지는 것을 보았고.

‘사, 살려 주시오. 제발. 제발.’

또 다른 적을 상대하기 위해 눈을 부릅뜬 채 죽어 가는 항산검문의 무인을 지나쳤으며.

‘네놈이, 태원진가가 우리에게 무슨 짓을 했는지 아느냐!’

수십여 년의 기다림 끝에 비로소 숨겨 두었던 칼을 빼 든 배신자들과 맞닥트렸다.

그들과 쉴 새 없이 검을 섞고, 마침내 쓰러트리고, 한 사람과 마주했다.

‘주위를 둘러보아라. 처참하게 죽어 가는 저들을 보며 무슨 생각이 드느냐?’

핏물에 젖어 붉게 물든 수염.

메마른 눈빛과 목소리.

분명 오래전 죽었을 대장로는, 서늘한 숨결과 함께 자신의 핏줄을 향해 말하고 있었다.

‘네가 조금 더 신중했더라면. 영민했더라면……. 오늘 같은 참극을 막을 수 있지 않았을까?’

기억에는 없는 말이다.

당연했다.

그것은 진위경이 스스로에게 던지는 물음이었으니까.

진위경은 알고 있었다.

악몽 속의 대장로도, 그가 뱉은 모든 말도 결국 진위경 자신으로부터 비롯된 것이라는 사실을.

하지만 그 사실을 알고 있음에도, 악몽은 끊이질 않고 반복되었다.

지금 이 순간에도.

“주군.”

불현듯 귓가를 파고드는 위팽의 목소리에, 진위경은 지금 막 잠에서 깬 사람처럼 천천히 눈을 깜빡였다.

그리고 어느덧 자신의 몸이 식은땀으로 축축하게 젖어 있다는 것을 깨달았다.

“……제기랄. 꼬락서니하고는.”

진위경은 외마디 욕설과 함께 실소를 터트렸다.

우습기 짝이 없었다.

비에 젖은 생쥐처럼 벌벌 떨고 있는 자신의 모습이.

사방에서 조여 오는 중압감에 숨 쉬는 것조차 버거워하는 이 한심한 놈의 손에 산서 무림. 아니, 산서성 전체의 명운(命運)이 달렸다는 것이.

그나마 한 줄기 위안이 되는 것은, 오랜 시간을 함께한 이가 곁에 있다는 사실뿐이었다.

“속하가 한 말씀 드려도 되겠습니까.”

잠시 내려앉은 침묵 속에서 울려 퍼지는 목소리.

위팽은 진위경의 대답을 기다리지 않고 말을 이었다.

“분명 적들은 강합니다. 삼만의 유목민에 아직 드러나지 않은 암천의 전력까지 더해진다면……. 주군의 판단대로 돌이킬 수 없는 일이 벌어질지도 모르지요.”

“관부와 힘을 합쳐도 승산을 장담하기 어렵네. 지원군이 없는 한, 산서성의 전력을 총동원하여 쏟아부어도 감당할 수 없어.”

진위경이 씁쓸하게 덧붙였다.

“설령 천운이 닿아 지원군이 제때 도착하더라도, 병력이며 규모가 턱없이 부족하겠지. 당연한 일이야. 나로서도 같은 입장이라면 결코 가문을 비울 수 없을 테니까.”

성동격서(聲東擊西).

광활하기 그지없는 초원은 산서성은 물론 요녕, 하북, 섬서에까지 맞닿아 있다.

산서성을 향해 남하하던 대군세가 말머리를 비트는 순간, 지원군을 파병한 문파와 가문은 새로운 표적이 된다.

더군다나 암천에게 이동진(移動眞)이라는 기이한 사술(邪術)이 있는 한, 누구도 쉽게 문파와 가문을 비우지 못할 것이다.

그들에게도 지켜야 할 것이 있으니까.

“산서를 버리고 하남으로 향할 생각일세. 사람들이 있는 한, 가문은 사라지지 않아.”

이 선택은 최선도, 차선도 아니다.

최악을 면하기 위한 차악이다.

그리고 이처럼 수많은 희생을 막고자 하는 진위경의 마음을, 위팽 역시 모르지 않았다.

“주군께서 그렇게 명하신다면, 속하는 따르겠습니다.”

“위팽. 자네…….”

“하지만 주군, 기억나십니까?”

위팽은 담담하게 말을 이었다.

“이 년 전. 누군가가 그런 말을 했습니다. 한 번 물러서기 시작하면 뒷걸음질만 치다 돌부리에 걸려 넘어질 수밖에 없다고.”

“……!”

“압니다. 적들이 강하다는 것도. 주군께서 어떤 마음으로 그러한 결정을 내리셨는지도. 그러나…….”

크게 심호흡한 위팽은 자신이 믿고 따르는 주군을 향해 포권을 취했다.

“우리 태원진가도, 아니 산서 무림도 강해졌습니다.”

망설임 없이 돌아선 위팽은 굳게 닫혀있던 문을 열었다.

스륵.

그 순간. 진위경은 보았다.

천천히 열리는 문 너머, 무장을 갖춘 채 기다리고 있는 수많은 사람들을.

그들의 선두에 선 익숙한 얼굴들을.

“항산검문의 이소월. 외적에 맞서 싸우기 위해 왔습니다.”

차차창!

무복 차림을 한 이소월.

그리고 그녀의 뒤에 시립한 항산검문의 무인 삼백이 병장기를 뽑아 땅 깊숙이 꽂았다.

“이 문주. 이게 도대체…….”

진위경은 말을 잇지 못했다.

지금으로부터 이 년 전, 태원진가의 깃발 아래에서 충성을 맹세한 수십여 명의 문주와 가주들을 보았기 때문이었다.

저마다의 무장을 갖춘 채 서늘한 눈동자를 빛내는 그들 사이로, 지금 막 모습을 드러낸 한 사람도 함께.

“무슨 고민이 그리도 많으십니까.”

마치 오랫동안 말하는 법을 잊은 사람처럼 거칠고 어색한 목소리.

넝마 같은 옷을 걸친 청년은 진위경을 보며 웃었다.

홀쭉 패인 볼이 도드라질 만큼.

“형님.”

“……!”

마침내 긴 폐관을 끝마치고 세상으로 나온 아우의 모습에, 진위경은 차오르는 격동을 이기지 못하고 눈을 감았다.

그리고 찰나의 어둠 속에서 조금 전 위팽의 입을 빌려 들었던, 이 자리에 없는 막내아우의 음성을 떠올렸다.

‘한 번 물러서기 시작하면, 뒷걸음질만 치다 돌부리에 걸려 넘어질 수밖에 없다.’

확신할 수 없다. 무엇이 옳고 그른 선택인지.

그러나 가야 할 길은 정해졌다.

저벅.

진위경은 걸음을 옮겼다.

태원진가의 소가주를 기다리고 있는 그들을 향해.

피비린내가 풍겨 오는 컴컴한 미래를 향해.
```

## Final English reading copy

```markdown
# Chapter 949

Everything has a warning sign.

When an earthquake is near, the ground trembles and countless birds take to the sky all at once. Before a typhoon strikes, feather-shaped clouds fill the heavens.

If even natural disasters, as terrible as divine punishment, come with warnings, what more need be said of something done by mere humans?

Just a few days ago, some people had sensed something ominous coming from the grasslands.

And they had sensed it with perfect clarity.

*The nomads. No—the entire grasslands are on the move.*

Inside the vast hall, dimness settling over it, a broad-shouldered man silently studied the map before him.

The enormous map, as large as three or four full-grown men, was packed with the terrain and place names of the entire continent. But his gaze was fixed on only one place.

Shanxi.

The hometown where he had been born and raised all his life, and the land his ancestors had protected.

A little over three hundred years ago, near the end of the war that had drenched the world in blood, a man had arrived here.

His family name was Jin, and his given name was Muryang.

He had been an unwelcome outsider, but when he reached Taiyuan, he laid down a foundation stone and raised his banner. That was the beginning of the Jin Family of Taiyuan.

*He probably never knew. That our family would endure for so many years.*

A little over three hundred years.

An unimaginable stretch of time.

Even gorgeous flowers that made onlookers gasp, even towering trees so tall and grand they awed everyone who saw them, had fallen to the passing winters and the relentless march of time.

But the weeds on the frontier—the Jin Family of Taiyuan—still protected this land.

Blooming in profusion, then broken, shattered, and rising again.

“Rise and decline, flourishing and fading…”

Jin Wikyung murmured the words, then slowly continued.

“Our family’s rise was long ago, and we only barely avoided ruin. So I thought surely all that remained was for us to flourish…but…”

Jin Wikyung smiled bitterly.

“I really did get that wrong. Don’t you think so, too?”

It wasn’t a lament to no one, nor was he talking to himself.

Wipeng, who had held his place like a heavy iron tower, calm as a lake, spoke up.

“Looking at you now, my lord, I’m reminded of the past.”

“The past?”

“It wasn’t long enough ago to call it the past, actually. It was only two years ago.”

“The Mount Heng Sword Sect…”

“That’s right. You looked just like this then, too.”

Wipeng continued in a chilly voice befitting his nickname, Ghost Sword.

“The fight hasn’t even started. Are you thinking of laying down your sword before you’ve even drawn it?”

“Is that how it looks?”

“That’s how it looks to me.”

At the firm answer from his most trusted retainer, Jin Wikyung bit his lip.

He was ashamed of himself for being unable to deny it at once.

And the reality that was keeping him from making a decision even out of a moment’s stubbornness felt bleak.

“I’m…the Lesser Family Head of our family. Countless lives depend on a few words or some small action of mine.”

And it wasn’t only the Jin Family of Taiyuan.

All of Shanxi Murim moved according to Jin Wikyung’s will.

The Jin Family of Taiyuan was unquestionably the foremost power in Shanxi Province, and he was, for all intents and purposes, the Family Head.

Even now, a wave of tens of thousands of men and horses was surging toward this land.

“I’ve already sent a letter through the Shanxi Provincial Office, telling them to evacuate the people around Datong and Saneum. We have to prevent as many needless casualties as we can.”

Datong and Saneum were the districts closest to the grasslands.

They would be the first places trampled by the grassland army after it crossed the border.

“The Mount Heng Sword Sect is no different. It’s not too late to retreat. It’s the only way to avoid being wiped out.”

“Do you really think the Sect Leader will accept that proposal?”

“It’s not a proposal. It’s an order.”

Jin Wikyung continued in a subdued voice.

“She has no other choice. By now, she must have accepted reality.”

Over the past two years, the Mount Heng Sword Sect had grown remarkably under the Jin Family of Taiyuan’s banner.

Lee Seowol, who had become its new Sect Leader as a woman, had proven far more capable than anyone had expected.

If the former Sect Leader—her father, Lee Cheonbaek, the Blood Wolf Sword—had built the Mount Heng Sword Sect through fear and force, she had rebuilt the sect with her characteristic intelligence and leadership, rescuing it from the brink of collapse.

So much so that she had drawn the attention of the world.

But no matter how much the sect had grown, there was no question it couldn’t weather the crisis right on its doorstep.

“Thirty thousand.”

Jin Wikyung looked at Wipeng, his gaze heavy.

“By the time they reach Shanxi Province, they’ll have grown to thirty thousand.”

The past few days had passed with merciless speed.

One day, urgent word arrived that nomads scattered across the grasslands were gathering. Then several Escort Bureaus and merchant houses along the grassland trade routes disappeared.

Their fate was obvious. So were the culprits.

“Their goal is clear. And so is who’s behind them.”

Jin Wikyung knew Temur and Chinggen well.

One of the decisive reasons the two had risen so quickly to become powers on the grasslands was the support they’d received from the Jin Family of Taiyuan.

“Temur is strong, but utterly simple. Chinggen is calculating and cautious, but he lacks the stature for this. Neither of them would ever pull something like this. They don’t have the strength for it, either.”

The age when the nomads of the grasslands had thundered across the continent with bows and lances had long since passed.

The empire they built had vanished without a trace, and the nomads, driven out to vast but desolate plains, had fallen into repeated feuds with their own people and continued to decline.

“Their strength has already been proven. But it’s still not enough to threaten the Central Plains.”

Temur and Chinggen, now called khans, were still just two among the many Great Chieftains of the grasslands.

But what of the Central Plains?

Every province had the Great Nation’s soldiers, numbering anywhere from several thousand to over ten thousand, as well as powerful Murim sects.

A divided grasslands.

A united Central Plains.

The gap between them was far too deep and wide.

The day the nomads carried on their ancestors’ great legacy and ruled the world would never come again.

Not unless another enormous power intervened.

“I’m not afraid of thirty thousand nomads.”

Jin Wikyung glared at the enormous map before him.

As if he were waiting for something hidden to spring out from among its dense lines and characters.

“Dark Heaven. I’m afraid of the power they haven’t revealed yet.”

For the past two years, the Jin Family of Taiyuan had gone from strength to strength.

But amid the days of celebration and cheers, Jin Wikyung had writhed each night beneath the same terrible nightmare.

A nightmare of the dead.

“Kill them!”

“Don’t give up an inch!”

Clang! Clang! Clang!

Eight Spring Gorge.

In that blood-soaked gorge where enemies, allies, and traitors had been tangled together, charging at one another like beasts, Jin Wikyung wandered every night.

“Lesser Family Head, are you all right—? Cough!”

He saw a family retainer who had always greeted him with a smile collapse, spraying blood.

“P-Please, spare me. I beg you. I beg you.”

He passed a Mount Heng Sword Sect martial artist who was dying with his eyes wide open, hurrying to face another enemy.

“Do you know what you—you, the Jin Family of Taiyuan—did to us?!”

He came face-to-face with the traitors who had finally drawn the swords they’d hidden away after waiting for decades.

He crossed swords with them without pause, finally brought them down, and came face-to-face with one man.

“Look around you. What do you think as you watch them die so horribly?”

A beard soaked red with blood.

A dry gaze and voice.

The Head Elder, who had surely died long ago, spoke to his own bloodline, his breath cold.

“If you’d been a little more careful. A little wiser…could you have prevented a tragedy like this?”

Those weren’t words he remembered hearing.

Of course not.

They were the questions Jin Wikyung asked himself.

Jin Wikyung knew.

The Head Elder in his nightmare, every word he spoke—it all came from Jin Wikyung himself.

But even knowing that, the nightmare never stopped. It kept repeating.

Even now.

“My lord.”

At Wipeng’s voice, which suddenly pierced his ears, Jin Wikyung slowly blinked as if he’d just woken up.

Only then did he realize his body was drenched in cold sweat.

“…Damn it. Look at me.”

Jin Wikyung let out a short curse, then gave a bitter chuckle.

It was ridiculous.

There he was, trembling like a drowned rat.

And the fate of Shanxi Murim—no, of all Shanxi Province—rested in the hands of this pathetic man, who could barely breathe under the pressure closing in from every direction.

The only small comfort was that someone who had been by his side for so long was still there.

“May I say something, my lord?”

His voice rang out through the brief silence.

Wipeng continued without waiting for Jin Wikyung’s answer.

“The enemy is undoubtedly strong. If the thirty thousand nomads are joined by the forces of Dark Heaven they’ve yet to reveal…then, as you’ve judged, something irreversible may happen.”

“Even if we join forces with the government, we can’t be sure we’ll win. Without reinforcements, we couldn’t handle them even if we threw the full strength of Shanxi Province into the fight.”

Jin Wikyung added bitterly,

“Even if fortune smiles on us and reinforcements arrive in time, their numbers will be woefully inadequate. That’s only natural. If I were in their place, I’d never leave my family unprotected, either.”

A feint to the east, strike in the west.

The vast grasslands bordered not only Shanxi Province, but Liaoning, Hebei, and Shaanxi as well.

The moment the great army heading south for Shanxi Province turned its horses around, the sects and families that had sent reinforcements would become new targets.

And as long as Dark Heaven possessed the strange dark art of the Moving Formation, no one could easily leave their sect or family undefended.

They had things to protect, too.

“I’m thinking of abandoning Shanxi and heading to Henan. As long as our people survive, our family won’t disappear.”

This wasn’t the best choice, or even the second-best.

It was the lesser of two evils, to avoid the worst.

And Wipeng understood Jin Wikyung’s desire to prevent as many people as he could from being sacrificed.

“If that is your command, my lord, I will obey.”

“Wipeng. You…”

“But my lord, do you remember?”

Wipeng continued calmly.

“Two years ago, someone said that once you start retreating, you’ll keep backing away until you trip over a rock and fall.”

“...!”

“I know. I know the enemy is strong. And I know what moved you to make this decision. But…”

After taking a deep breath, Wipeng clasped his hands toward the lord he trusted and followed.

“Our Jin Family of Taiyuan has grown stronger. No—Shanxi Murim has grown stronger.”

Without hesitation, Wipeng turned and opened the tightly shut door.

The door slid open softly.

At that moment, Jin Wikyung saw them.

Beyond the slowly opening door, countless people waited, armed and ready.

At their head stood familiar faces.

“Lee Seowol of the Mount Heng Sword Sect. I’ve come to fight against the foreign enemy.”

Clang! Clang! Clang!

Lee Seowol, dressed in martial attire.

Behind her, three hundred martial artists of the Mount Heng Sword Sect drew their weapons and drove them deep into the ground.

“Sect Leader Lee. What in the world is all this…?”

Jin Wikyung couldn’t finish his sentence.

He had seen the dozens of Sect Leaders and Family Heads who had sworn allegiance beneath the Jin Family of Taiyuan’s banner two years ago.

And among them, all standing with their own weapons and cold eyes, was someone who had just appeared.

“What is there to think so hard about?”

The young man’s voice was rough and awkward, as if he’d forgotten how to speak for a long time.

Wearing clothes like rags, he smiled at Jin Wikyung.

His gaunt cheeks were hollow enough to stand out.

“Hyung.”

“...!”

At the sight of his younger brother, who had finally emerged into the world after a long seclusion, Jin Wikyung closed his eyes, unable to contain the surge of emotion rising within him.

And in the instant of darkness, he recalled the voice of his youngest brother, who wasn’t there, speaking through Wipeng just moments ago.

“Once you start retreating, you’ll keep backing away until you trip over a rock and fall.”

He couldn’t be sure which choice was right or wrong.

But the road ahead was decided.

Step.

Jin Wikyung began to walk.

Toward the people waiting for the Lesser Family Head of the Jin Family of Taiyuan.

Toward the dark future, already thick with the stench of blood.
```
