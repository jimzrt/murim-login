<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0981.txt",
      "sha256": "2504e6e0c052adf637f97a3edbf96494cd75658f73ff65ea6cb6401f58eaed7b",
      "bytes": 12890
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "25a5261b6a081033c50f202c5a4eeee8d6deaebc27a7b533ded6ea7b3c3d5e13",
      "bytes": 1336
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "534144353e21b1e77df6e1cab1ddd1ec71ab53581386f9d3c49a34452f7ba359",
      "bytes": 235946
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "d459bbb6856ea60f76d38906b258dca8c46e38b338e03813a9f2a6b173976507",
      "bytes": 1005
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "18bd2bcafa840c68fd8c05aae5483b83171d81dadef4b9b716761e2a0297bcd2",
      "bytes": 1325
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "892928eae819736baf5008a155f9d53b66848f93e382b719812a50d1a5c581fd",
      "bytes": 1374
    },
    {
      "path": "characters/Jamukha.md",
      "sha256": "17ef671717b9f656870a698ba4056d22334dcf0e3db7dcc3d026801477dfce29",
      "bytes": 611
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "aef2e5875c28f02f131267d58255e94fb4899df1bf8cd3893f76b825da70a9f4",
      "bytes": 1517
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "0c1da907d8f76addcb5f08b912b40b97297e7f713a2e3428080b64e2c0bb9772",
      "bytes": 1479
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "45582ef8d515012f28dc7b2f8824679a29102b4b51f367e12795028219eaa01a",
      "bytes": 622
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "2ae3e1257e9d234a35f47a63bd682186fba092287bb1f334634e99e6419fa77c",
      "bytes": 898
    },
    {
      "path": "characters/Temur.md",
      "sha256": "f7b27b3e2e8fb24d459681ef083b1715373b06106e172a7f04c4e4a9a4ff56a3",
      "bytes": 664
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "72b0d9a52c66f2121e2ec65972b15461f692c3f85e248be2e14d1cd9eccceea1",
      "bytes": 271880
    }
  ],
  "estimated_tokens": 12376
}
-->

# Durable State Update — Chapter 981

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
1 and safe_through 981. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 981. Profile updates may replace only one
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
  "chapter": 981,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 981,
    "continuity_sources": [981],
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
    "Temur submitted to Jin Wikyung and the Jin Family of Taiyuan as his lord.",
    "The Jin Family’s surviving nomads surrendered, and the Murong Family was killed or captured.",
    "Jin Mukyung has awakened with three broken bones and severe muscle pain; Jeok Cheongang and the Bow Saint helped treat his internal injury.",
    "Taekyung is withholding the casualty details from Mukyung, who has recognized his forced cheerfulness and demanded the truth.",
    "The Emperor remains gravely ill with Blood Soul Gu; the treatment said to require him to die once remains unresolved.",
    "The conditions of Cheol Mubaek, Wipeng, and Peng Cheolhu remain unknown."
  ],
  "continuity_sources": [
    979,
    980
  ],
  "open_questions": [
    "Who was sacrificed in the battle, and how many people died?",
    "What does the Lord of Heaven intend, and how will the broader conflict unfold?",
    "What are the conditions of Cheol Mubaek, Wipeng, and Peng Cheolhu?",
    "Can the Emperor be treated for Blood Soul Gu, and what does the treatment requiring him to die once entail?"
  ],
  "safe_through": 980,
  "temporary_decisions": [
    "Render 병신노복 in the transforming-robot exchange as “crippled old servant”; it is Mukyung’s mistaken hearing, not a name or title."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 철무백    | **Cheol Mubaek**   |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 무림맹    | **Murim Alliance**               |
| 하북팽가   | **Hebei Peng Family**            |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 팔천협    | **Eight Spring Gorge** |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 북천 | **North Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 중양절 | **Double Ninth Festival** | Festival used as the expected date for the invasion of the Central Plains. |
| 검귀 | **Sword Demon** | Title used for the kind of swordsman Mukyung is said to resemble. |
| 마조 | **Demon Bird** | Title given by the revealed impostor who wore Chinggen’s face. |
| 북천마군 | **North Heaven Demon Lord** | Title of Murong Baek. |
| 모용위진 | **Murong Wijin** | Head Elder of the Murong Family directing the battlefield. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 혁무진 | 철무백 | junior_to_respected_Peak_master | Great Hero Cheol | deferential | Begins a formal greeting with 철무백 대협 before being stopped. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 벽력도왕 | 진태경 | elder martial master to younger rival | you | boisterous and confrontational | Peng addresses Taekyung as 네놈 while discussing Peng Dojin. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 테무르 | 자무카 | fellow_khan_to_elder_khan | Khan Jamukha | formal-respectful | Temur affirms Chinggen’s public praise of Jamukha. |
| 진무경 | 마조 | hostile opponents | you | blunt and insulting | Mukyung directly insults the Demon Bird, refusing to call him Master. |
| 마조 | 진무경 | hostile opponents | you | familiar and blunt, with admiration | Calls him a young Sword Demon and speaks to him with growing respect. |
| 자무카 | 진무경 | hostile opponents | you | familiar, blunt, and patronizing | Jamukha uses 자네 while urging Mukyung to submit and become his hunting dog. |
| 진태경 | 북천마군 | hostile opponents | you | casual, taunting, and profane | Taekyung teases and insults him during their standoff. |
| 북천마군 | 궁성 | hostile martial opponents | Bow Saint | calm and formally familiar | Addresses her directly while acknowledging her effort. |
| 북천마군 | 자무카 | lord to subordinate | my lord | formal-deferential | Jamukha answers the Demon Lord’s command with 하명하십시오. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 970
- **Aliases:** Tiger of Mount Heng
- **Role:** Cheol Mubaek is the ninth-generation successor of the Shura Annihilating Fist and the Peak master known as the Tiger of Mount Heng, now out of seclusion and active in the rebuilding of the Mount Heng Sword Sect.
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** His master, the Fist Hero, was a great fist master whose arms were severed by the Blood Soul Fat Demon; he is a close friend and peer of Lee Cheonbaek, a paternal uncle and protector of Lee Seowol, and considers Jin Taekyung, Jin Mukyung, and Hyuk Mujin Benefactors for protecting Seowol and enabling the Mount Heng Sword Sect's survival.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 970
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 980
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jamukha.md

# Jamukha (자무카)

- **Safe through:** Chapter 979
- **Aliases:** None
- **Role:** Jamukha was the ruler of the western steppe and a former eastern-steppe chieftain recruited into Dark Heaven by Murong Baek; Jin Taekyung killed him.
- **Personality:** Patient and ambitious, he was willing to feign loyalty to gain the power to rule the steppe and north.
- **Voice:** Not established
- **Relationships:** Peng Cheolhu defeated him more than fifty years ago; Murong Baek spared and recruited him, but Jamukha’s loyalty to him was feigned.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 980
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Supreme Peak swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and guided by a strong sense of chivalry, refusing to abandon what he believes is right.
- **Voice:** Quiet and resonant, clipped and blunt, with dry sarcasm in familiar exchanges.
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, whose concealed grief Mukyung perceptively challenges; their father—the Jin Family Head—once apologized to Mukyung for his mother’s death in childbirth.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 979
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 979
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 972
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu is the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family.
- **Personality:** Boisterous, hot-tempered, argumentative, and protective toward those connected to his close friend Hong Dao; relentlessly disciplined in training, having continued every day after the Great Faction War.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** Long-standing rival and friend of Jeok Cheongang; close friend of Hong Dao; protective toward Hong Dao's Disciple Unnamed; father of Peng Cheolyeong; longtime friend and former youthful rival of Murong Baek, who has now betrayed and attacked him.

### Temur.md

# Temur (테무르)

- **Safe through:** Chapter 979
- **Aliases:** None
- **Role:** Temur is the surviving chieftain of the northern grasslands who submitted to Jin Wikyung and the Jin Family of Taiyuan.
- **Personality:** Hot-tempered and proud of his khan lineage, Temur chose survival over loyalty and now recognizes with guilt that his actions have led his followers to slaughter.
- **Voice:** Blunt, heated, and confrontational
- **Relationships:** The real Chinggen was Temur’s cousin and sworn brother through the anda oath, but was killed; Temur now submits to Jin Wikyung as his lord.

## Korean source

```text
＃981화



어느 정도의 시간이 흘렀는지는 진무경도 몰랐다.

다만 모든 이야기가 끝나고 오랫동안 이어진 침묵 끝에, 진무경이 할 수 있었던 말은 하나뿐이었다.

“피곤하군.”

그렇게 진무경은 홀로 남게 되었다.

부서질 듯이 아픈 몸뚱어리를 일으켜 세운 그는, 침상에 상반신을 기댄 채 멍하니 창밖을 응시했다.

저 멀리 동쪽으로부터 번져오는 서광(曙光) 아래, 수하와 함께 전각을 떠나는 아우의 뒷모습을 보며 조금 전 들었던 목소리를 다시금 떠올렸다.



‘오천.’



고작 두 글자다.

그것은 수천이나 되는 생명의 무게를 담기에는 터무니없이 짧았고, 비현실적으로 느껴졌다.

그러나 그것은 틀림없는 현실이었다.



‘삼천여 명이 죽고, 그 외에는 전부 크고 작은 부상을 입었지. 불구가 된 이들도 많아.’



그날, 팔천협에 집결한 만 오천의 산서인들 중 삼분지 일이 죽거나 다쳤다고 했다.

비록 그중 상당수는 비교적 무위가 떨어지던 산서성부의 관병(官兵)들이었으나, 그들 역시 이 땅에 뿌리내리고 살아가는 ‘우리’ 중 하나였음을 진무경은 알고 있었다.



‘……대승(大勝)이로군.’

‘그래, 대승이지. 역사에 남을.’



비록 오천여 명의 사상자가 발생하긴 했지만, 하룻밤 사이에 무려 삼만이 훌쩍 넘어가는 대군을 궤멸시켰다.

머릿수로도, 전력 면으로도 압도적인 외적(外敵)을 상대로 엄청난 승리를 거두었으니 대국 역사의 한 자락을 새로 써 내려갔다고 해도 결코 과언이 아니다.

하지만 위대한 승리를 입에 담으면서도, 누구 한 사람 기쁜 모습을 보이지 않았다.

남의 것을 빼앗는 자는 승리에 취해 기뻐하지만, 지키기 위해 맞서 싸운 이는 승리의 과정에서 잃어버린 것에 슬퍼한다.

이승을 떠난 이들이 남기고 간 시신과 핏물의 무게는, 오롯이 살아남은 자들이 감당해야 하는 법이다.



‘하북팽가는 절반 이상의 전력을 잃었어. 벽력도왕(霹靂刀王) 팽 대협께서는 아직도 의식을 회복하지 못하셨고.’



긴 세월의 흐름 속에서도 하북을 호령하던 팽가의 대호(大虎)는 극심한 부상에서 깨어 나오지 못하고 있었다.

벗이라고 생각했던 북천마군의 배신은 그 누구도 예상치 못했던 것이었고, 갑작스러운 기습을 가한 그의 무공은 결코 벽력도왕의 아래가 아니었으니.



‘자무카와 북천마군을 쓰러트린 후에도 상황은 쉽게 흘러가지 않았어. 아마 유목민들을 굴복시키지 않았다면 우리도 훨씬 더 큰 희생을 치러야 했을 만큼.’



전장에 합류한 지 상당한 시간이 흘렀음에도, 막바지에 다다른 그때까지도 모용세가의 전력은 비교적 온전했다.

아마 자무카가 살아서 그 광경을 보았다면, 뒤늦게나마 진실을 깨닫고 몸을 떨었을 것이다.

그가 테무르를 이용하여 동부 초원의 부족민들을 화살받이로 앞세웠듯이, 북천마군 또한 자무카로 하여금 모용세가의 희생을 최소화했다는 것을.

약육강식(弱肉强食)의 법칙은 어디에서나 통용되는 법이었다.



‘그렇게 마지막 전투가 시작됐지.’



최후를 직감한 모용세가는 온 힘을 다해 발악했다.

곳곳에서 아군이 죽어 나가는 와중에도 꺼내지 않았던 잠력단(潛力團)을 복용했고, 자무카의 죽음이 알려진 후에도 뜻을 꺾지 않았던 서부 초원의 유목민들과 함께 퇴로를 뚫었다.

그 숫자가 물경 오천.

산서인들과 하북팽가는 드높은 사기와는 달리 이미 오랫동안 이어진 전투로 지쳐 있었고, 한계 이상의 힘을 얻은 수천의 적들은 세 명의 초절정 고수들을 피해 사방으로 흩어져 허술해진 포위망을 찢고 도주했다.

아니, 도주하려 했다.

깊은 밤의 어둠 사이로 비집고 들어오는 어스름한 새벽빛 너머, 온 세상을 떨어 울리는 함성이 들려오기 전까지는.

이곳에 나타나서는 안 될 깃발들 아래로 모습을 드러낸 세 갈래의 군세(軍勢)를 마주하기 전까지는.



‘그건 우리도 예상하지 못했어. 생각했던 것보다도 훨씬 빠르게 도착했으니까.’



피에 젖어 향기를 잃은 중양절의 국화 대신, 화산(華山)의 매화향이 산등성이를 가득 메웠다고 했다.

무려 일백의 절정 고수들을 앞세워 돌격한 일단의 무리는 무림맹(武林盟)의 깃발을 휘날리며 적들을 휩쓸었고, 끔찍한 격전 끝에 고요함이 찾아들었던 비좁은 협곡에는 새로운 손님들이 찾아왔다.

휘황찬란한 황금빛 갑옷을 번뜩이고, 말안장에 앉아 질풍처럼 나아가는 그들을 세상은 이렇게 불렀다.

금의위(錦衣衛).



‘그것으로, 끝이었지.’



짙은 피 안개가 협곡을 넘어 너른 분지를 감싸 안았다.

새벽을 알리는 서광과 함께 사방에서 밀려든 지원군들은 적들을 휩쓸었고, 궁성과 화왕은 전장을 지배했으며, 진태경은 마지막까지 저항하던 모용세가의 대장로. 모용위진의 가슴에 창날을 박아넣었다.

그날의 전투는, 전쟁은 그렇게 막을 내렸다.

중양절의 시작과 끝을 장식한 채.

위대한 승리에 대한 기쁨과 그보다 더욱 무겁고 큰 슬픔을 남긴 채.

그렇게 꼬박 사흘이 흘러, 마침내 의식을 회복한 진무경에게 그간의 모든 이야기를 들려준 아우는 창밖 너머로 멀어져 가고 있었다.

떠나기 전, 낡은 서책(書冊) 한 권을 남기고.



‘전해 달라고 하셨어. 너, 아니 형한테.’



문을 나서며 흘리듯이 덧붙인 아우의 마지막 한마디를 떠올리며, 진무경은 이제 막 잠에서 깨어난 사람처럼 눈을 깜빡였다.

“……아.”

억눌린 외마디 신음.

서서히 희뿌옇게 물들어 가는 시야 속에서, 진태경의 뒷모습은 더 이상 보이지 않았다.

다만 그의 무릎에 놓인 서책의 겉면에 적힌 네 글자만이 선명하게 두 눈동자에 틀어박힐 뿐이었다.

수라멸권(修羅滅拳).

그것은 어느 노강호가 마지막으로 이 세상에 남긴 흔적이자, 태원진가의 검귀(劍鬼)에게 남긴 사문의 유산이었다.

사흘 전 그날 함께 등을 맞대고 싸웠으나, 끝끝내 살아남지 못한 또 한 명의 희생자.

‘철 대협.’

진무경은 항산호 철무백을 떠올렸다.

마조(魔鳥)라는 강적에 맞서 싸우는 자신에게 찰나의 시간을 벌어 주기 위해 목숨을 내걸었던 그를.

피에 젖은 이빨을 드러내며 웃던 마지막 모습과 이 년 전의 어느 날 항산검문을 떠나는 그에게 다가와 농담처럼 건넸던 목소리도 함께.



‘자네가 그렇게 무공에 환장한다며?’

‘예?’

‘그래서 말인데, 소월이한테 관심 없나?’

‘아니, 갑자기 그게 무슨 말씀이신지…….’

‘말 그대로일세. 내 워낙 가진 것이 없어 금은보화는 내주지 못하겠지만, 두 사람이 맺어지기만 한다면 수라멸권의 비급이라도 기꺼이…….’

‘철 숙부!’

‘어허. 귀청 떨어지겠다. 이제 문주가 됐다고 벌써부터 상전 노릇이라도 하려는 게냐?’



이상한 일이었다.

그저 스쳐 지나가는 인연이라 생각했는데, 껄껄 웃던 그의 웃음소리가 유난히도 선명하게 기억나는 것은.

가슴 한구석을 짓누르는 이 무거운 아릿함은.

‘그래, 그런 것이었나.’

진무경은 그제야 자신을 휘감고 있는 이 감정들의 정체를 깨달았다.

슬픔. 분노. 그리고…….

이미 잃어버린 것에 대한, 스스로를 향한 자책.

‘강했다면. 그날의 내가 조금 더 강했더라면.’

지킬 수 있었다. 더 많은 이들을 살릴 수 있었다.

하지만 그러지 못했다.

죽을힘을 다해 노력했음에도, 하루가 십 년처럼 느껴지는 칠흑 같은 어둠 속에서 쉼 없이 검을 휘둘렀음에도 닿지 못했다.

‘만약 내가 아니라 네가, 아니 너희가 있었다면 모든 것이 달라졌겠지.’

청풍을 만나고 처음으로 벽을 느꼈다.

놀라운 속도로 발전을 거듭해가는 진태경의 모습이, 사그라들었던 마음속 갈망에 불을 지폈다.

처음 검은 잡은 그 날부터 천재(天才)라 불렸지만, 두 사람의 진면목을 본 후에야 비로소 깨달았다.

그가 하늘이 내린 재능을 받았다면, 저들은 하늘에서 가져온 것이라고.

‘내가…… 내가 어떻게 해야 너희에게 닿을 수 있을까. 더는 빼앗기지 않을까.’

무어라 형용할 수 없는 감정의 소용돌이.

진무경이 공허한 눈빛으로 아우의 뒷모습이 사라진 창밖을 바라보던 그 순간이었다.

툭.

굳게 닫혀 있는 문틈 사이로 들려온 미세한 소음.

그리고 뒤이어 귓가를 파고드는 익숙한 목소리.

“야, 무진아. 너 혹시 그때 생각나냐?”

떠난 줄 알았던 아우의 음성에 진무경이 눈을 크게 뜬 그때, 어색하게 느껴질 만큼 딱딱한 대답이 울려 퍼졌다.

“음. 어, 언제를 말씀하시는 겁니까.”

“왜 있잖아. 우리 정찰조 만들어서 한창 뺑이 칠 때.”

“아. 아아. 예. 기억납니다.”

“어, 그때 진짜 못 볼 꼴 많이 봤다. 그냥…… 어느 순간부터 나 스스로가 너무 한심하고 화가 나더라고. 내가 왜 이것밖에 안 되는지. 오며 가며 얼굴 익힌 저 사람들이 왜 죽어야 하는지.”

“…….”

“그런데 제일 열 받는 게 뭔지 알아?”

보이지 않는 문 너머에서, 진태경은 등을 기댄 채 혼잣말처럼 말을 이었다.

“이게 시발, 아무리 애를 써도 익숙해지지 않아. 변하는 게 없어.”

그 순간, 진무경의 눈가가 파르르 떨렸다.

통증조차 잊은 채 온 힘을 다해 주먹을 쥐고, 질끈 눈을 감은 그의 귓가로 목소리는 계속해서 흘러들었다.

“항상 똑같더라. 지금보다 더 강해지면 나쁜 일을 막을 수 있을 거라고 생각했는데. 검기 쓰고, 강기 쭉쭉 뽑아내면 그때처럼 좆 같은 일은 없을 줄 알았는데…….”

문틈 사이로, 나직한 한숨이 흩어졌다.

“아니야. 아니더라고. 결국은 매번 기분이 더러워지더라고. 내 욕심이었던 거지.”

더, 더, 더.

강해질수록 무언가를 원하는 마음은 커져만 간다. 소망은 원대해지고, 책임감은 터질 듯이 부풀어 오른다.

진무경은 소년 시절의 자신을 떠올렸다.

그저 검이 좋아 한없이 휘두르기만 했던 그 소년에게, 지금 같은 책임감이 있었던가에 대해 생각했다.

가진 것이라고는 그저 재능뿐, 가문의 부흥 따위는 생각하지도 않았던 그때를.

그리고 계속해서 또렷하게 귓가를 파고드는 음성을 들었다.

“그래도 알고는 있지. 그렇다고 다 때려치우면 여기서 끝장이라는 거.”

진태경은 이제 대답을 기다리지 않았다. 연기처럼 어색한 맞장구를 이어 가던 혁무진 역시 마찬가지였다.

마치 다른 누군가에게 들려주기 위한 것처럼 목소리는 계속해서 이어졌다.

“노력하면 돼. 당장 내가 할 수 있는 최선을 다하면 돼. 변하는 게 없다고 절망하고 포기하면, 그때는 진짜 지옥이 시작되거든. 내가 이만큼 해서 그나마 덜 빼앗겼다는 걸 뒤늦게 알게 되거든.”

“……!”

“그러니까, 하던 대로만 하면 되는 거야. 지금까지 그랬듯이 앞으로도 계속해서.”

씁쓸함이 담긴 목소리가 서서히 잦아든다. 어느 순간 짧게 내려앉은 침묵 속, 돌연 맹렬한 파공성이 일었다.

후웅, 딱!

“악! 왜 때려요!”

“대답을, 이 새끼야. 사람이 말을 하면 적당히 맞장구도 치고 해야지. 괜히 어색하게시리.”

“아니, 진짜 이러시깁니까? 어차피 저한테 하는 말도 아니…… 읍, 읍!”

숨 막히는 소리와 함께 무언가가 질질 끌려가는 마찰음을 들으며, 진무경은 흐릿하게 웃었다.

그리고 이내 문틈 사이를 비집고 빠져나갈 만큼 또렷한 목소리로, 전각을 빠져나가는 불청객들을 배웅했다.

“고맙다. 진심으로.”

그의 목소리를 들은 듯, 잠시 멈췄던 발걸음이 이내 빠르게 사라졌다.
```

## Final English reading copy

```markdown
# Chapter 981

Jin Mukyung didn’t know how much time had passed.

But after all the stories had been told, and a long silence had followed, there was only one thing he could say.

“I’m tired.”

And so Jin Mukyung was left alone.

He raised his body, aching as if it might break apart, and leaned his upper half against the bed. Then he stared blankly out the window.

Beneath the first light spreading from the distant east, he watched his younger brother’s back as he left the pavilion with a subordinate. He recalled the words he’d heard moments ago.

*Five thousand.*

Just two syllables.

Far too short to hold the weight of thousands of lives. It didn’t feel real.

But it was, without a doubt, reality.

*Of the five thousand casualties, over three thousand died. The rest suffered injuries, big and small, and many were left crippled.*

Of the fifteen thousand people of Shanxi who’d gathered at Eight Spring Gorge that day, a third had been killed or wounded.

Many of them had been government soldiers from the Shanxi Provincial Office, relatively weak in martial arts. But Jin Mukyung knew they, too, were part of *us*—people who had put down roots and lived on this land.

*…A great victory.*

*Yeah. A great victory. One for the history books.*

More than five thousand had become casualties, but in a single night they’d annihilated an army of well over thirty thousand.

They’d won an incredible victory against foreign enemies who outnumbered and overpowered them. It was no exaggeration to say they’d written a new page in the history of the Great Nation.

And yet, not a single person looked happy as they spoke of the great victory.

Those who took what belonged to others reveled in their victories. But those who fought to protect what was theirs mourned what they’d lost along the way.

The bodies and blood left behind by those who’d departed this world were a burden the survivors alone had to bear.

*The Hebei Peng Family lost more than half its forces. Great Hero Peng, the Thunderbolt Saber King, still hasn’t regained consciousness.*

The great tiger of the Peng Family, who’d lorded over Hebei for generations, still hadn’t woken from his grievous injuries.

No one could have anticipated that the North Heaven Demon Lord—someone he’d considered a friend—would betray him. And the martial arts he’d used in his sudden ambush were in no way inferior to those of the Thunderbolt Saber King.

*Even after we took down Jamukha and the North Heaven Demon Lord, things didn’t go smoothly. If we hadn’t subdued the nomads, we would probably have suffered much heavier losses.*

Even though they’d joined the battlefield quite some time ago, the Murong Family had remained relatively intact until the fighting was nearly over.

If Jamukha had lived to see it, he would have realized the truth too late—and trembled.

Just as he’d used Temur to put the tribes of the eastern steppe in front as human shields, the North Heaven Demon Lord had used Jamukha to minimize the Murong Family’s losses.

The law of the survival of the fittest applied everywhere.

*That’s when the final battle began.*

Knowing their end was near, the Murong Family fought with everything they had.

While their allies were dying all around them, they took the Temporary Strength Pill they’d held back until then and fought to open an escape route alongside the western steppe nomads who’d refused to abandon their cause even after Jamukha’s death.

Their number was a staggering five thousand.

The people of Shanxi and the Hebei Peng Family were exhausted from the long battle, despite their soaring morale. The thousands of enemies, strengthened beyond their limits, scattered in every direction to avoid the three Supreme Peak masters, tearing through the weakened encirclement and fleeing.

No—they tried to flee.

Until, beyond the dim dawn light creeping through the darkness of night, they heard a roar that shook the whole world.

Until they faced three armies emerging beneath banners that should never have appeared here.

*We didn’t expect that either. They arrived much sooner than we thought.*

They said the scent of plum blossoms from Huashan had filled the ridge, replacing the chrysanthemums of the Double Ninth Festival, soaked in blood and stripped of their fragrance.

A group led in a charge by a hundred Peak masters swept through the enemy beneath the fluttering banner of the Murim Alliance. New guests also arrived in the narrow gorge, which had fallen quiet after the terrible battle.

Their brilliant golden armor gleamed as they rode forward like the wind, seated in their saddles. The world called them the Embroidered Uniform Guard.

*And that was the end of it.*

A dense fog of blood flowed over the gorge and wrapped around the broad basin.

With the first light of dawn, reinforcements swept in from every direction and crushed the enemy. The Bow Saint and the Fire King dominated the battlefield, while Jin Taekyung drove his spearhead into the chest of Murong Wijin, Head Elder of the Murong Family, who had resisted until the very end.

The battle—and the war—ended that day.

It began and ended with the Double Ninth Festival.

It left behind joy at a great victory—and a sorrow heavier and greater still.

Three full days had passed like that. At last, Jin Mukyung had regained consciousness, and his younger brother had told him everything that had happened. Now that brother was walking away, growing smaller beyond the window.

Before he left, he’d left behind an old book.

*He asked me to give it to you. No—to hyung.*

Remembering his brother’s last words, tossed out as he walked through the door, Jin Mukyung blinked like someone who’d only just woken from sleep.

“…Ah.”

A stifled groan escaped him.

Through his vision, slowly clouding over, he could no longer see Jin Taekyung’s back.

Only the four characters written on the cover of the book resting on his knees stood out, sharply etched in his eyes.

Shura Annihilating Fist.

It was the last trace an old master had left in this world—and the legacy of his martial lineage, entrusted to the Sword Demon of the Jin Family of Taiyuan.

Another victim who’d fought back-to-back with him that day, three days ago, but hadn’t survived.

*Great Hero Cheol.*

Jin Mukyung thought of Cheol Mubaek, the Tiger of Mount Heng.

He’d risked his life to buy a moment for Mukyung as he fought a powerful enemy—the Demon Bird.

He remembered the last sight of him, grinning with bloodied teeth. He also remembered a day two years ago, when Cheol had come up to him as he was leaving the Mount Heng Sword Sect and asked, as if making a joke—

*“I hear you’re crazy about martial arts.”*

*“Pardon?”*

*“So, I was wondering—are you interested in Seowol?”*

*“I’m sorry, what are you talking about all of a sudden…?”*

*“Exactly what I said. I don’t have much to offer, so I can’t give you gold or silver, but if the two of you got together, I’d gladly give you the Shura Annihilating Fist manual…”*

*“Uncle Cheol!”*

*“Goodness. You’ll burst my eardrums. You’ve barely become Sect Leader and you’re already trying to boss me around?”*

It was strange.

He’d thought of Cheol as no more than a passing connection. So why was the sound of his hearty laughter so vivid in his memory?

Why did this heavy ache press down on one corner of his chest?

*So that’s what this is.*

Only then did Jin Mukyung realize what the emotions surrounding him were.

Sorrow. Anger. And…

Self-reproach for what he’d already lost.

*If I’d been stronger. If I’d been just a little stronger that day.*

He could have protected them. He could have saved more people.

But he hadn’t.

Even though he’d tried with all his might, even though he’d swung his sword without rest through the pitch-black darkness where each day felt like ten years, he hadn’t been able to reach them.

*If it had been you instead of me—or you all—everything would have been different.*

The first time he met Cheongpung, Mukyung had felt a wall between them.

Jin Taekyung’s astonishingly rapid growth had rekindled the longing in his heart that had once died down.

He’d been called a genius from the day he first picked up a sword. But only after seeing the two of them for what they truly were had he finally understood.

If he’d been born with talent bestowed by Heaven, then those two had brought theirs down from Heaven.

*How can I… How can I reach you? How do I stop losing people?*

An indescribable whirlpool of emotions.

That was when Jin Mukyung, his eyes empty, stared out the window where his younger brother had disappeared.

*Tap.*

A faint sound came from the crack beneath the firmly shut door.

Then a familiar voice reached his ears.

“Hey, Mujin. Remember that time?”

Jin Mukyung’s eyes widened. He’d thought his younger brother had left, but now he heard his voice again. A stiff reply followed, stiff enough to sound awkward.

“Um. W-Which time do you mean?”

“You know, when we formed that recon squad and kept busting our asses.”

“Oh. Ah, yes. I remember.”

“Yeah, I saw a lot of things I wish I hadn’t back then. I just… at some point, I started feeling so pathetic and angry at myself. Why was I only this good? Why did all those people whose faces I’d gotten to know, passing them back and forth, have to die?”

“…”

“But you know what pissed me off the most?”

On the other side of the unseen door, Jin Taekyung leaned back against it and continued, as if talking to himself.

“This goddamn feeling never gets any easier, no matter how hard I try. Nothing changes.”

Jin Mukyung’s eyes trembled.

He clenched his fist with all his strength, forgetting even the pain, and squeezed his eyes shut. The voice continued in his ears.

“It’s always the same. I thought if I got stronger than I am now, I could stop bad things from happening. I thought if I could use Sword Energy and put out Force like it was nothing, I’d never have to go through shit like that again…”

A quiet sigh drifted through the crack beneath the door.

“No. That’s not how it is. I still feel like shit every time. It was just me being selfish.”

More, more, more.

The stronger a person became, the more they wanted. Their hopes grew grander, and their sense of responsibility swelled until it felt ready to burst.

Jin Mukyung thought of himself as a boy.

Had the boy who’d swung his sword endlessly simply because he loved it ever felt the kind of responsibility he felt now?

Back then, all he had was talent. He hadn’t even thought about restoring the family’s fortunes.

He listened as the voice continued to reach his ears, clearer with every word.

“But I know, right? If we just throw in the towel, it’s over.”

Jin Taekyung no longer waited for a reply. Hyuk Mujin, who’d been offering awkward responses like a puppet, didn’t either.

As if he were speaking for someone else to hear, Jin Taekyung continued.

“We just have to keep trying. Do the best we can with what we can do right now. If you despair and give up because nothing changes, that’s when hell really begins. Because later, you realize that all the effort you put in meant fewer people were taken from you.”

“……!”

“So just keep doing what you’ve been doing. Keep at it, like you always have.”

The bitterness in his voice slowly faded. A brief silence fell—and then, all at once, a fierce whistle cut through the air.

*Whoosh—thwack!*

“Ow! Why’d you hit me?”

“Answer me, you bastard. When someone’s talking, you’re supposed to give them a little something back. Don’t make it so damn awkward.”

“Seriously, you’re doing this now? You’re not even talking to me… Mmph, mmph!”

Hearing a strangled noise and the scrape of something being dragged away, Jin Mukyung smiled faintly.

Then, with a voice clear enough to slip through the crack in the door, he saw the unwelcome guests off as they left the pavilion.

“Thank you. Truly.”

It seemed they’d heard him. Their footsteps paused for a moment, then quickly disappeared.
```
