<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0950.txt",
      "sha256": "5d24914fd4fef4fb26570b5629c72397e12a61cea1181cfa9d66f31680b91c87",
      "bytes": 17962
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a0058b6e1990dd105a0f2cc3af630e86f51a088868bcf1fab29335121831aeca",
      "bytes": 3012
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bbb6bd1bdb9407382aeed622923c33e7d8077914c1c9edfd5dc0c45aea7b5f65",
      "bytes": 233797
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6c981ab329afa39e6a9f65b0c86bf60a04dff7e3b0bda5a9c97bddcfef835c1f",
      "bytes": 759
    },
    {
      "path": "characters/Hanga.md",
      "sha256": "daff2381fc68293fd03231786a84222be94dc659df43c4b210323a1c8a58be38",
      "bytes": 568
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "da8fd96a48469955f9e58e03954c3f2070fae4415e4f01be2eb903739a5041bd",
      "bytes": 1449
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "5b3f2515a0c1533faba00080418512e94d59760640f662aec337fe192fe20fe7",
      "bytes": 622
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "0db8e5f9a3d9178c2b3078c93ee1ff4a71accaf4ca8f8f2bf6b4384e83b7ed3c",
      "bytes": 1061
    },
    {
      "path": "characters/Song Ho.md",
      "sha256": "06716179cb0e08b30e00a0c6e93560e0e85cd43097591f2de71516403578e91a",
      "bytes": 767
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "c5de233b80ebae3fdd1e01d31718c0133498f9e5c9c605506deee5e11b5882ee",
      "bytes": 685
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1efb275a0485bdab8f74bddeafc29157bc04997b8313766f8a1a4de940fca98a",
      "bytes": 267426
    }
  ],
  "estimated_tokens": 14185
}
-->

# Durable State Update — Chapter 950

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
1 and safe_through 950. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 950. Profile updates may replace only one
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
  "chapter": 950,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 950,
    "continuity_sources": [950],
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
    "Grassland forces are mobilizing toward Shanxi and are expected to reach thirty thousand; Jin Wikyung ordered evacuations around Datong and Saneum, considered withdrawing to Henan, and then walked toward gathered allies. He suspects Dark Heaven is behind the threat and fears its unrevealed forces.",
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
    949,
    948
  ],
  "open_questions": [
    "Who was the traveler who gave Jang Sam the silk pouch, and what are the modified pill’s exact effects and side effects?",
    "How widely has the improved Temporary Strength Pill spread, and who is distributing it?",
    "What is the Martial God’s identity, and what is his connection to the chosen one and the Bow Saint?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain, and what is their significance?"
  ],
  "safe_through": 949,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 매종학    | **Mae Jonghak**    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 하오문    | **Lower District Sect**          |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 하북팽가   | **Hebei Peng Family**            |
| 남궁세가   | **Nangong Family**               |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 화산     | **Huashan**            |
| 팔천협    | **Eight Spring Gorge** |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 항아 | **Hanga** | Local village boy who lives near Jang Taebo. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송호 | **Song Ho** | Elderly martial artist known as the Thousand-Faced Fox. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 정양 | **Jeongyang** | Shanxi location |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 삼매진화 | **Samadhi True Fire** | Internal-energy flame demonstrated by the unnamed old man. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남궁 | **Namgung** | Surname of the family led by Namgung Ryong. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 은영각주 | **Chief of the Hidden Shadow Pavilion** | Office formerly held by Song Ho. |
| 태산북두 | **Mount Tai and Northern Dipper of the Murim** | Honorific description of Shaolin's standing in the Murim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 요녕 | **Liaoning** | Northeastern region from which the Murong Family arrives. |
| 맹주부 | **Alliance Leader's Office** | Office directly serving the Alliance Leader. |
| 광서 | **Guangxi** | Region bordering Nanman. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 진화 | **evolution** | The transformation the Southern Heaven Demon Empress claims the rift will produce. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 중양절 | **Double Ninth Festival** | Festival used as the expected date for the invasion of the Central Plains. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 항아 | visiting_adult_to_local_child | little one | friendly and coaxing | Questions Hanga and offers food in exchange for information. |
| 항아 | 노인 | child_to_elder_stranger | Grandpa | childlike-familiar | Hanga calls the unnamed old man 할부지 after he arrives at her family’s home; this is distinct from her address to Jang Taebo. |
| 송호 | 청년 | elderly_martial_artist_to_younger_martial_artist | Young Hero | formal-polite | Song Ho calls out to the young man as 소협 at the chapter's end. |
| 송호 | 진태경 | senior_martial_artist_to_junior_martial_artist | you | familiar-polite | Uses 자네 while recognizing Taekyung and discussing his preliminary performance. |
| 매종학 | 송호 | savior_to_survivor | you | casual-familiar | Mae uses 자네 while speaking to Song Ho after his identity is recognized. |
| 송호 | 매종학 | rescued_survivor_to_savior | Great Hero; you | formal-deferential and familiar | Song Ho credits Mae with saving his life and addresses him as 대협. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 천면호리 | 매종학 | intelligence_chief_to_alliance_leader | Alliance Leader | formal and deferential | Requests that Mae move elsewhere with the others before he reports further. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 매종학 | 천면호리 | Alliance Leader to Hidden Shadow Pavilion Chief | Chief of the Hidden Shadow Pavilion | casual-but-commanding | Asks Song Ho's view of Taekyung's suspected target. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 949
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hanga.md

# Hanga (항아)

- **Safe through:** Chapter 936
- **Aliases:** None
- **Role:** Local village girl, Jang-pal’s daughter, who lives near Jang Taebo and regularly visits him.
- **Personality:** Curious, energetic, observant, and already attentive to the value of information and food.
- **Voice:** Childlike, direct, and inquisitive, with an occasional surprisingly worldly remark.
- **Relationships:** Calls Jang Taebo Grandpa; Jang Taebo is his elderly neighbor and only conversational companion.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 944
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 944
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 944
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Song Ho.md

# Song Ho (송호)

- **Safe through:** Chapter 853
- **Aliases:** Thousand-Faced Fox
- **Role:** Elderly Peak master known as the Thousand-Faced Fox, a martial artist with a prosthetic leg, and current Chief of the Hidden Shadow Pavilion, overseeing a vetted intelligence network that includes highly trained assassins.
- **Personality:** Outwardly genial and relaxed, but observant, forceful, and intimidating when pursuing information.
- **Voice:** Lightly genial and conversational, turning quietly coercive during interrogation.
- **Relationships:** He serves under Mae Jonghak's New Murim Alliance, commands the Hidden Shadow Pavilion, and recognizes Jin Taekyung as Jeok Cheongang's Disciple.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 944
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃950화



모두에게 있어, 그해 여름은 유난히도 짧고 혼란스러웠다.

이상할 정도로 변덕스러워진 날씨는 여러 이유 중 하나에 불과했다.

이제 홍수는 그리 놀라운 축에도 들지 못한다.

한여름의 어느 날에는 장맛비 대신 우박이 쏟아지기도 했고, 사상 최대의 폭염(暴炎)에 이어 새하얀 서리가 내려앉은 적도 있었으니까.

하루아침에 농사를 망친 이들은 주저앉아 통곡했고, 폭등하는 곡물값에 당장 내일의 끼니를 걱정할 처지가 되었다.

관부에서는 구휼미(救恤米)를 풀었으나 한 가마니의 쌀은 몇 사람의 손을 거쳐 한 홉으로 줄어들었다.

결국 굶주림을 참지 못한 이들은 산으로 향했다.

그곳에서 나무껍질을 벗겨 먹거나, 녹슨 농기구를 무기 삼아 산적이 되었다.

그러나 그마저도 얼마 가지 못할 것이다.

일평생 우직하게 논밭만 일구던 그들이 무엇을 할 수 있을까. 어설픈 산적을 기다리고 있는 것은 죽음뿐이다.

관군이건 무림인이건, 그들은 언젠가 토벌될 것이고 차가운 날붙이가 몸뚱어리를 가르는 순간에 이르러서야 문득 한 가지 의문을 떠올릴 터였다.

자신이 어째서 이렇게 된 걸까, 하는 의문을.

하지만 누구도 그 의문에 대한 답을 알지 못한다.

이 광활한 천하에서 벌어지는 일들은 종종 아무도 이해할 수 없을 정도로 난해하니까.

특히 지난 이 년간의 일을 돌이켜 보면 더더욱 그러했다.

“그 이야기 들었나? 불과 두어 달 전에 남만에서…….”

“그뿐만이 아닐세. 광서 땅이 피로 물들었어.”

“미치겠군. 세상이 어찌 돌아가는지.”

어딜 가나 숱한 이야기가 떠도는 것은 흔한 일이다.

그러나 몇 년 전과는 분위기가, 아니 공기부터가 달랐다.

객잔 안을 가득 채운 사람들의 목소리는 새벽 안개처럼 낮게 가라앉아 있었고, 눈빛과 얼굴에는 숨길 수 없는 근심으로 가득했다.

한때는 술안주요, 흥밋거리에 불과했던 무림의 소문들은 이제 현실의 칼날이 되어 조금씩 살갗을 파고들고 있었다.

그들은 더는 웃고 노래하지 못했다.

수십여 명씩 무리 지어 거리를 순찰하는 관군과 간혹 스쳐 지나가는 무림인들을 불안한 눈빛으로 바라보며, 날이 저물기 전에 집으로 향하는 발걸음을 재촉했다.

이제는 모두가 본능적으로 알고 있었다.

새로운 전란(戰亂)은 이미 시작되었다는 것을.

수십여 년 전 중원을 짓밟았던 십만의 마교도(魔敎徒)와는 비교도 안 될 재앙이, 자신들의 머리 위로 드리워지고 있다는 사실을.

그리고 무림이라는 울타리에 몸담은 이들은 작금의 현실을 누구보다 선명하고 또렷하게 느끼고 있었다.

“놈들이 이제 황실에까지 손을 뻗쳤다는군. 그것도 정마대전 무렵부터 장장 수십여 년간이나.”

“나 역시 개방을 통해 언질을 받았네.”

“암천의 힘이 생각했던 것 이상이야. 수포로 돌아갔기에 망정이지, 만약 놈들의 계획이 성공했다면…….”

무림인들, 특히 일문(一門)을 이끄는 문주와 가주들이 수십여 명씩 모이는 것은 이제 더 이상 특별한 일이 아니었다.

그들은 무거운 목소리로 현재의 상황에 대해 논의하고, 앞으로의 일을 예측했다.

그리고 그럴 때마다 빠지지 않고 등장하는 이름이 있었다.

“열화신룡이 이번에도 대단한 활약을 펼쳤더군. 이번 일로 황실의 적극적인 원조를 얻고, 천자의 총애도 받고 있다던데.”

“하면, 그 소문이 사실인가?”

“어떤 소문?”

“아직 듣지 못한 모양이군. 며칠 전 열화신룡이 황도를 떠날 때, 천자가 몸소 배웅까지 나와 그를 열후(列侯)에 봉했다는 소문 말일세.”

“그게 무슨…… 천자가 무림인에게 벼슬을, 그것도 열후라니. 그게 가당키나 한 일인가?”

“지켜본 이들이 한둘이 아닐세. 아무래도 황도이다 보니 하오문과 개방 쪽에서 정보를 입수하기까지 약간의 시간이 걸리긴 했지만, 사실인 듯하네.”

발 없는 말이 천 리를 가는 법.

암천을 외적으로 칭하며 전쟁을 선포한 황실의 포고문과 전례 없는 예우를 받으며 열후의 반열에 오른 진태경의 활약상은 순식간에 사람들의 입에 오르내렸다.

이제는 무려 황실까지 나섰다.

정마대전에도 두 손 놓고 지켜만 보고 있던 대국이, 헤아릴 수도 없을 만큼 무수한 군병과 물자를 지닌 그들이 나선다면 암천 따위는 바람 앞의 등불이나 다름없다.

아니, 정확히는 모두가 그렇게 예상했다.

자세한 상황을 알고 있는 소수의 몇몇 사람을 제외한다면.

푸드득!

거친 날갯짓과 함께 저 멀리 사라지는 전서응(傳書鷹)의 뒷모습을 지켜보던 노인은 손에 쥔 자그마한 종이를 펼쳤다.

그의 눈동자가 깨알처럼 적힌 글자를 훑을 때마다, 얼굴에 새겨진 검상(劍傷)이 조금씩 일그러졌다.

“그래, 그렇게 되었단 말이지.”

마른 입술 사이로 흘러나온 나직한 뇌까림.

한동안 제자리에서 무언가를 곰곰이 생각하던 노인은 한구석에 마련된 화로(火爐)에 들고 있던 종이를 던져넣었다.

그리고 젖지 않도록 기름을 먹인 전서(傳書)가 순식간에 타오르는 것을 끝까지 지켜본 후, 자신이 가야 할 곳으로 걸음을 옮겼다.

저벅. 탁.

절뚝이는 걸음으로 나아갈 때마다 울려 퍼지는 둔탁한 소음.

언뜻 보면 유생처럼 보이는 이들이 노인을 발견할 때마다 작게 고개를 숙였다.

“오셨습니까, 각주(閣主).”

“잠시, 광서에서의 일에 대해 보고드릴 것이 있습니다.”

“남궁세가(南宮世家)에서 급보가 들어왔습니다.”

“하북과 요녕, 그리고 섬서에서…….”

품 안에 한가득 죽편을 들고 지나가는 이도, 짤막한 인사만 건네고 떠나는 이도 있었지만, 그들 중 대부분은 새로운 정보를 노인에게 알려 주었고 그는 그럴 때마다 머릿속의 생각을 정리하고 가다듬었다.

그리고 마침내, 굳게 닫힌 문 앞에 섰다.

달칵.

마치 기다렸다는 듯이 열리는 문.

하지만 노인은 놀라지 않았다.

자신이 수천, 수만 리 밖의 일들을 속속들이 아는 것처럼 이 방의 주인 역시 마찬가지였으니까.

물론 비슷하지만 실상은 차원이 달랐다.

노인에게는 수많은 눈과 귀가 있지만, 상대는 혼자만의 힘으로 반경 백여 장 안에 벌어지는 모든 일을 파악할 수 있으니.

“무공을 수련 중이셨습니까.”

단출하기 그지없는 방 안으로 들어선 노인의 첫 마디에, 가부좌를 튼 채 앉아 있던 사내가 눈을 떴다.

“그랬지. 조금 전까지는.”

“죄송합니다. 아무래도 제가 의도치 않게 방해가 된 모양이군요.”

“마음 쓰지 말게. 분명 그럴 만한 일이 있었을 테니.”

싱긋 웃어 보이는 사내는 젊었다.

기껏해야 이립(而立) 어림으로 보이는 얼굴에, 탈의한 상반신은 한껏 압축된 근육이 완벽한 균형을 자랑하고 있었다.

물론 그마저도 옷을 걸친 순간, 어디서나 볼 수 있는 평범한 청년 중 한 사람이 되었지만.

“그래, 무슨 일인가?”

계속해서 흘러나오는 자연스러운 하대.

그러나 사내에게는 그럴 만한 자격과 연륜이 충분했다.

검성(劍星) 매종학은 천하 무림을 지탱하는 가장 거대한 기둥 중 하나니까.

“맹주(盟主)께 급히 보고드려야 할 일이 있어 찾아뵈었습니다.”

“급히 보고드려야 할 일이라.”

매종학의 입가에 맺혀있던 미소가 사라졌다. 준비된 자리에 앉은 그는 찻주전자를 기울이며 말을 이었다.

“혹 그 보고가, 산서(山西)에 관련된 일인가?”

쪼르륵.

차갑게 식어 있던 찻물이 잔을 채우기도 전에 김을 피워올린다. 매종학을 따라 착석한 노인은 삼매진화의 열기로 달구어진 찻잔을 어루만졌다.

“예.”

찻잔은 따뜻했다. 그러나 지금부터 나오는 이야기는 차갑고 어두울 것이다.

매종학은 그 사실을 노인의 표정에서 읽었다.

“말하게. 은영각주(隱影閣主).”

노인, 천면호리(天面狐狸) 송호가 대답했다.

“태원진가가 퇴각을 철회했습니다.”

“더 자세히.”

“산서 무림 전체가 움직이고 있습니다. 태원진가를 중심으로 삼십여 곳의 문파와 가문이 집결했고, 산서성부 역시 모든 병력을 동원하는 중입니다.”

“음.”

매종학은 나직이 침음성을 흘렸다.

더는 들을 것도 없다.

이건 말 그대로 총력전이다. 산서 무림뿐만이 아니라, 산서성 전체의 사활(死活)이 걸린 대전투가 될 것이다.

“산서의 전력은?”

“우선 태원진가를 필두로 오천여 명에 달하는 무인들이 대기중이고, 거기에 더하여 기병 일천을 포함한 관군 일만이 있습니다.”

도합 만 오천.

그야말로 바닥까지 긁어모은 병력이다.

그마저도 지난 이 년의 시간 동안 태원진가가 놀라운 부흥을 일궈 내지 못했더라면, 무려 오천이나 되는 무인이 집결하지도 못했을 것이다.

다만 가장 큰 문제는…….

“적들의 절반도 되지 않는군.”

매종학의 뇌까림에 천면호리는 무겁게 고개를 끄덕였다.

은영각에서 파악한 바에 의하면 남하 중인 초원의 군세는 최소 삼만에서 많게는 사만으로 불어날 터.

초원과 인접해 있는 탓에 산서성에 배치된 관군들은 상당한 정예들이지만, 전체 병력의 두 배가 넘는 기마군단의 파도는 그야말로 악몽 그 자체다.

“피해를 최소화하기 위해 우선 북부를 비우고, 중부에서 전투를 벌일 심산인 것 같습니다.”

“중부라면, 역시 근거지인 태원(太原)인가?”

“정확히는 태원에서 삼백 리가량 떨어진 정양(定襄)에서 결전을 치를 듯합니다.”

“정양이라. 정양…….”

작게 중얼거린 매종학은 불현듯 이 왠지 모를 익숙함의 정체를 깨달았다.

“그곳이로군. 팔천협(八天峽).”

“예. 맞습니다.”

천면호리가 침착한 어조로 말을 이었다.

“팔천협은 그 자체로 천혜의 요새나 다름없지요. 과거 정마대전 당시 마교의 대군을 성공적으로 격퇴했고, 이 년 전에도 태원진가의 승리에 결정적인 공헌을 했던 장소입니다.”

산서성의 중부와 북부의 경계선에 자리 잡은 팔천협은 항아리 모양의 협곡이다.

길은 가파르고, 입구는 좁으니 소수로 다수의 적을 상대하기에는 최적의 전장.

더군다나 상대의 전력 대부분이 기마병이라는 것을 감안한다면, 이만한 장소를 찾기도 힘들다.

문제는 그 기마병의 숫자가 물경 수만에 달하는 데다가, 아직 진정한 적은 정확한 실체를 드러내지도 않았다는 것.

“팔천협에서 결전이 벌어진다면, 태원진가가 승리할 가능성은 어느 정도라고 생각하나?”

“높게 쳐도 이 할. 아무리 전황이 태원진가 측에 유리하게 흘러간다 해도 그 이상은 힘듭니다.”

단호하게 대답한 천면호리의 눈빛이 깊숙하게 가라앉았다.

“적들의 군세가 유목민들만으로 이루어져 있다면 오 할 이상이었을 겁니다. 하지만…….”

“그래, 놈들을 잊으면 안 되지.”

암천.

새카만 먹구름은 어느덧 초원의 푸른 하늘마저 집어삼켰고, 그 존재만으로도 마치 덫처럼 모두의 발목을 옭아매고 있었다.

“태원진가를 향한 지원은…… 현재로서는 기대하기 힘듭니다.”

그렇게 말하는 천면호리의 낯빛은 어두웠다.

무림맹주의 오른팔이자 은영각의 주인인 그는 작금의 천하에서 누구보다 현실을 잘 알고 있는 사람 중 하나였으니까.

“이미 모두가 알고 있습니다. 섣부르게 움직였다간 놈들의 사술(邪術)에 휘말려 큰 화를 입을 수 있다는 사실을 말입니다.”

도무지 상식적으로는 이해할 수 없는 일이지만, 암천은 이미 이동진(移動陳)이라 알려진 사술을 여러 번 선보인 바가 있었다.

그로 인해 정파 무림의 태산북두라 불리는 소림 역시 극심한 피해를 입고 말았으니, 구파일방이나 오대세가라고 한들 예외일 수는 없다.

설령 무림맹 총단이 위치한 바로 이곳, 하남이라고 할지라도.

“그렇다면 지금 우리가 당장 동원할 수 있는 병력은…….”

“없습니다.”

“없다?”

재고의 여지도 없다는 듯이 딱 잘라 말하는 천면호리를, 매종학은 물끄러미 응시했다.

“자네에게 한 가지만 묻겠네. 부디 신중하게 대답해 주길 바라지.”

“말씀하십시오.”

“산서로 보낼 병력이 없다는 그 말, 한 치의 거짓도 없는 사실인가?”

“……!”

천면호리는 대답 대신 침묵을 택했다.

자신의 별호와 같은 일생을 살았던 그다.

스스로의 신분을 숨기고, 새빨간 거짓말을 사실처럼 늘어놓는 것은 숨 쉬는 것처럼 자연스러운 일이었다.

하지만 그런 천면호리도 눈앞의 상대, 검성 매종학의 투명한 눈빛 앞에서는 차마 거짓을 꾸며 낼 수 없었다.

“맹주께서도…… 알고 계시지 않습니까.”

천면호리가 무겁게 입술을 뗐다.

“이미 전력의 저울추가 크게 기울어진 바, 지금 산서를 돕는 것은 하책(下策)입니다. 즉각 태원진가에 정식으로 퇴각을 명하심이 옳습니다.”

“늦은 것 같네만.”

“그렇지 않습니다. 비록 남은 시일이 촉박하다고는 하나, 지체하지 않고 하남까지 전선을 물린다면 남은 병력을 보존하고 후일을 도모할 수 있습니다.”

“아니, 확실히 늦었어.”

매종학이 작게 고개를 저으며 덧붙였다.

“그들의 마음을 되돌리기에는.”

“……!”

“태원진가의 소가주는 영민한 인물이지. 언제나 모든 상황을 넓게 파악하고, 한번 결정을 내리는 것에 있어 신중하기 그지없네. 그렇기에 자네 또한 그를 무림맹 군사부(軍師部)에 추천하지 않았나?”

천면호리는 자신도 모르게 침음성을 흘렸다.

그토록 신중한 이가 가문의 명운을 건 결정을 내렸다면, 그건 두 번 다시 철회할 수 없다는 뜻이다.

그것이 설령 무림맹주의 명령이라 하더라도.

“하지만 이대로라면 산서를, 그들 모두를 잃을 수도 있습니다.”

“알고 있네. 저들이 이대로 물러선다면, 미처 피신하지 못한 애꿎은 양민들은 놈들에 의해 몰살당하리라는 것도.”

“……!”

“애써 외면하지 말게. 저들이 싸우고자 하는 것은, 자신들이 살아온 고향을 지키기 위해서만이 아니라는 사실을.”

순간 말문이 막힌 천면호리는 차마 매종학을 마주하지 못하고 눈을 감았다.

그래.

알고 있었다. 다만 애써 모른 척했을 뿐이다.

이건 전투가 아닌 전쟁이니까.

이 전쟁에서 승리하기 위해서는 십만이 넘는 백성보다, 수천 남짓의 무인들이 더욱 중요하니까.

“제 판단이…… 틀린 겁니까?”

“아니, 훌륭했네. 자네는 내가 아는 그 누구보다 뛰어난 군사야.”

예상치 못한 대답에, 천면호리는 감았던 눈을 떴다.

어느덧 매종학이 그를 바라보며 부드럽게 웃고 있었다.

“다만, 한 가지를 잊고 있었을 뿐이지.”

“그게 무엇입니까?”

“숲 전체를 살피기에 바빠, 그 안의 작은 나뭇가지를 보지 못했다는 것.”

바로 그 순간이었다.

스륵.

매종학의 손짓과 함께 뻗어 나온 기운이 굳게 닫혀 있던 문을 열어젖힌 것도.

뒤이어 은밀한 인기척과 동시에 한 인영(人影)이 바람처럼 들이닥친 것도.

“그래, 어떤 소식을 가져왔나?”

기다렸다는 듯한 매종학의 물음에, 맹주부 직속의 전령이 부복하며 대답했다.

“급보입니다! 하북팽가와 모용세가, 그리고 화산과 종남이 산서성을 구원하기 위해 각각 이천의 지원군을……!”

순간 굳어버린 천면호리는 뒷말을 들을 수 없었다.

자칫하면 본거지가 위태로울지도 모르는 상황에서 저토록 많은 병력을 지원군으로 파견하다니.

그가 배운 병법에서, 모두가 아는 상식에서 어긋난 일이다.

하지만…….

‘그래, 그런 것이었나.’

천면호리는 쓴웃음을 머금었다.

그리고 믿을 수 없는 소식을 전한 전령이 떠난 뒤에야, 긴 침묵을 깨트리며 입술을 뗐다.

“이제 알겠습니다. 제가 미처 보지 못한 그 가지의 이름을.”

“무엇인가?”

“협(俠)입니다.”

매종학은 부드럽게 웃었다.

무(武)를 쌓아, 협(俠)을 이루겠다 맹세했던 젊은 날의 자신을 떠올리며.

“두 번 다시 잊지 말게. 우리 모두가 무림인이라는 것을.”

중양절이 나흘 앞으로 다가온 그 날.

이천에 달하는 무인이 무림맹 총단을 떠나 북상(北上)했다.
```

## Final English reading copy

```markdown
# Chapter 950

For everyone, that summer was unusually short and chaotic.

The strangely capricious weather was only one of many reasons.

Floods no longer even counted as surprising.

One midsummer day, hail poured down in place of the monsoon rains. Once, after the worst heat wave in recorded history, a blanket of white frost settled over the land.

Those whose crops were ruined overnight collapsed and wept. With grain prices soaring, they were left wondering where their next meal would come from.

The government released famine relief rice, but by the time a sack of it had passed through a few hands, it had dwindled to a single cup.

In the end, those who could no longer endure their hunger headed for the mountains.

There they stripped bark from trees to eat, or took up rusted farm tools and became bandits.

But even that wouldn’t last long.

What could people who had spent their whole lives dutifully working the fields possibly do? All that awaited these clumsy bandits was death.

Whether by government troops or martial artists, they would eventually be hunted down. And only when cold blades cut through their bodies would a question suddenly occur to them:

*How had I ended up like this?*

But no one knew the answer.

Events unfolding across this vast land were often so difficult that no one could understand them.

Especially when one looked back on the past two years.

“Have you heard? Just a couple of months ago, in Nanman…”

“That’s not all. Guangxi has run red with blood.”

“This is driving me mad. What’s become of the world?”

Stories were always circulating wherever people gathered.

But compared to a few years ago, the atmosphere was different. No—the very air felt different.

The voices of the people filling the inn had sunk low as morning fog, and their eyes and faces were full of worry they could not hide.

Rumors about the Murim, once no more than something to accompany a drink or pass the time, had become blades of reality, slowly cutting into their skin.

They could no longer laugh and sing.

They watched the government troops patrolling the streets in groups of dozens and the occasional martial artist who passed by with anxious eyes, hurrying home before nightfall.

By now, everyone knew it instinctively.

A new war had already begun.

A catastrophe beyond comparison to the hundred thousand Demonic Cultists who had trampled the Central Plains several decades ago was looming over their heads.

And those who belonged to the world of the Murim felt the present reality more clearly than anyone.

“I hear they’ve reached as far as the Imperial Court. And they’ve been at it for decades, since around the time of the Great Faction War.”

“I heard as much through the Beggars’ Sect.”

“Dark Heaven is stronger than we imagined. Thank goodness their plan fell through. If it had succeeded…”

It was no longer unusual for dozens of martial artists to gather—especially Sect Leaders and Family Heads who led their own organizations.

In grave voices, they discussed the current situation and tried to predict what would come next.

And one name came up every time.

“The Blazing Flame Divine Dragon made another remarkable contribution. I hear this incident earned him the Imperial Court’s full support and the Son of Heaven’s favor.”

“Then is that rumor true?”

“What rumor?”

“You haven’t heard yet, it seems. A few days ago, when the Blazing Flame Divine Dragon left the Imperial Capital, the Son of Heaven himself came out to see him off and made him a marquis.”

“What? The Son of Heaven gave a martial artist an official title—and made him a marquis, no less? Is that even possible?”

“There were plenty of witnesses. Since it happened in the Imperial Capital, it took the Lower District Sect and the Beggars’ Sect a little while to get the information, but it seems to be true.”

News travels a thousand li without feet.

The Imperial Court’s proclamation declaring war on Dark Heaven as a foreign enemy, along with Jin Taekyung’s achievements and the unprecedented honors he had received as he was raised to the rank of marquis, spread from mouth to mouth in no time.

Now even the Imperial Court had stepped in.

The Great Nation, which had sat back and watched even during the Great Faction War, possessed more troops and supplies than anyone could count. If it joined the fight, Dark Heaven would be little more than a candle in the wind.

Or rather, that was what everyone expected.

Except for the handful of people who knew the full situation.

Flap, flap!

Watching the messenger eagle disappear into the distance with a harsh beat of its wings, the old man unfolded the tiny scrap of paper in his hand.

As his eyes passed over the minuscule writing, the sword scar on his face twisted ever so slightly.

“So that’s how it is.”

The quiet mutter slipped between his dry lips.

After standing still for a while, deep in thought, the old man tossed the paper into a brazier set in one corner of the room.

He watched until the oil-soaked missive, prepared to keep it from getting wet, had burned away in an instant. Then he set off for his destination.

Thud. Tap.

A dull sound rang out with each limping step.

Whenever the old man passed, those who looked like Confucian scholars lowered their heads slightly.

“Welcome, Chief of the Hidden Shadow Pavilion.”

“I have a brief report concerning what happened in Guangxi.”

“We’ve received an urgent message from the Nangong Family.”

“And from Hebei, Liaoning, and Shaanxi…”

Some passed with their arms full of bamboo slips; others offered only a brief greeting before leaving. But most of them gave the old man new information, and each time, he organized and refined his thoughts.

At last, he stopped in front of a firmly shut door.

Click.

The door opened as if it had been waiting for him.

But the old man wasn’t surprised.

Just as he knew the details of events taking place thousands, even tens of thousands, of li away, so did the master of this room.

Though they were alike in one way, the truth was on an entirely different level.

The old man had countless eyes and ears. His counterpart, however, could sense everything happening within a radius of more than three hundred yards by his own power alone.

“Were you practicing martial arts?”

At the old man’s first words as he entered the exceedingly plain room, the man sitting cross-legged opened his eyes.

“I was. Until just now.”

“I’m sorry. It seems I interrupted you without meaning to.”

“Don’t give it another thought. I’m sure you had a good reason.”

The man smiled gently. He was young.

His face looked barely thirty, and his bare upper body was covered in tightly packed muscles, perfectly balanced.

Of course, once he put his clothes on, he looked like any ordinary young man.

“So, what is it?”

The man continued to address the old man with the easy familiarity of a senior.

But he had more than enough standing and experience to do so.

Sword Saint Mae Jonghak was one of the greatest pillars supporting the Murim world.

“I’ve come because there’s something I must report to the Alliance Leader immediately.”

“Something you must report immediately.”

The smile on Mae Jonghak’s lips disappeared. He took his seat and tilted a teapot, continuing as he poured the tea.

“Is the report about Shanxi?”

Trickle.

Before the cold tea had even filled the cup, steam rose from it. The old man sat down across from Mae Jonghak and ran a hand over the teacup, heated by Samadhi True Fire.

“Yes.”

The cup was warm. But the news that followed would be cold and dark.

Mae Jonghak read as much from the old man’s expression.

“Speak, Chief of the Hidden Shadow Pavilion.”

The old man, Song Ho, the Thousand-Faced Fox, answered.

“The Jin Family of Taiyuan has rescinded its retreat.”

“Tell me more.”

“All of Shanxi Murim is mobilizing. More than thirty sects and families have gathered around the Jin Family of Taiyuan, and the Shanxi Provincial Office is also mobilizing every available troop.”

“Hmm.”

Mae Jonghak let out a low hum.

There was no need to hear more.

This was an all-out war in the truest sense. It would be a battle for the fate of all Shanxi Province, not just Shanxi Murim.

“What forces does Shanxi have?”

“First, more than five thousand martial artists are standing by, led by the Jin Family of Taiyuan. In addition, the government has ten thousand troops, including a thousand cavalry.”

Fifteen thousand in all.

They had scraped together every last man.

They wouldn’t even have managed to gather five thousand martial artists if the Jin Family of Taiyuan hadn’t accomplished an extraordinary resurgence over the past two years.

But the biggest problem was…

“Less than half the enemy’s numbers.”

At Mae Jonghak’s mutter, the Thousand-Faced Fox gave a solemn nod.

According to the Hidden Shadow Pavilion’s intelligence, the grassland army marching south would number at least thirty thousand, and as many as forty thousand.

Because it bordered the grasslands, The government troops stationed in Shanxi Province were highly capable. But the wave of cavalry, more than twice their total strength, was a nightmare in itself.

“The plan seems to be to clear out the north first, then fight in the central region to minimize casualties.”

“The central region would mean Taiyuan, their stronghold?”

“More precisely, they seem set to make their stand at Jeongyang, about three hundred li from Taiyuan.”

“Jeongyang. Jeongyang…”

Mae Jonghak murmured the name, then suddenly realized why it sounded so familiar.

“That place. Eight Spring Gorge.”

“Yes. That’s right.”

The Thousand-Faced Fox continued in a calm voice.

“Eight Spring Gorge is almost a fortress created by nature. During the Great Faction War, it was where the Demonic Cult’s great army was successfully repelled. And two years ago, it played a decisive role in the Jin Family of Taiyuan’s victory.”

Eight Spring Gorge, situated on the boundary between central and northern Shanxi Province, was a gorge shaped like a jar.

Its paths were steep and its entrance narrow, making it the perfect battlefield for a small force to fight a larger one.

And considering that most of the enemy forces were cavalry, it would be hard to find a better location.

The problem was that the cavalry numbered tens of thousands—and the true enemy still hadn’t revealed its full nature.

“If the decisive battle is fought at Eight Spring Gorge, what do you think are the Jin Family of Taiyuan’s chances of winning?”

“Even at the most generous estimate, twenty percent. No matter how much the battle turns in the Jin Family of Taiyuan’s favor, anything higher than that would be difficult.”

The Thousand-Faced Fox answered firmly, his eyes darkening.

“If the enemy forces consisted only of nomads, their chances would be over fifty percent. But…”

“Right. We can’t forget them.”

Dark Heaven.

The pitch-black clouds had already swallowed the blue skies over the grasslands. Their very presence had bound everyone’s feet like a trap.

“Right now, we can’t expect to send support to the Jin Family of Taiyuan.”

The Thousand-Faced Fox’s face was dark as he said it.

As the Murim Alliance Leader’s right hand and the head of the Hidden Shadow Pavilion, he was one of the people who understood the current state of the world better than anyone.

“Everyone already knows that if we act rashly, we could be caught in their dark arts and suffer a grave disaster.”

It was difficult to understand by any reasonable measure, but Dark Heaven had already used the dark art known as the Moving Formation several times.

As a result, Shaolin—the Mount Tai and Northern Dipper of the Murim—had suffered devastating losses. The Nine Sects and One Gang and the Five Great Families would be no exception.

Not even here in Henan, where the Murim Alliance’s headquarters was located.

“Then the forces we can mobilize right now…”

“None.”

“None?”

Mae Jonghak gazed steadily at the Thousand-Faced Fox, who had answered as if there were no room for reconsideration.

“I want to ask you one thing. Please answer carefully.”

“Go ahead.”

“Is it absolutely true that we have no troops to send to Shanxi?”

“…”

The Thousand-Faced Fox chose silence instead of answering.

He had lived a life worthy of his epithet.

Concealing his identity and spinning blatant lies as if they were the truth came as naturally to him as breathing.

But even the Thousand-Faced Fox could not bring himself to lie beneath the clear gaze of the man in front of him, Sword Saint Mae Jonghak.

“You know as well, Alliance Leader…”

The Thousand-Faced Fox finally parted his heavy lips.

“The balance of power has already tipped too far. Helping Shanxi now would be the worst choice. The right thing to do is order the Jin Family of Taiyuan to retreat at once.”

“I think it’s too late.”

“It isn’t. Even if time is short, if we pull the front line back to Henan without delay, we can preserve our remaining forces and plan for what comes next.”

“No. It’s definitely too late.”

Mae Jonghak gave a slight shake of his head, then added,

“To change their minds.”

“…”

“The Lesser Family Head of the Jin Family of Taiyuan is an astute man. He always sees the full picture and is exceedingly cautious before making a decision. Isn’t that why you recommended him to the Murim Alliance’s Strategist Corps?”

The Thousand-Faced Fox let out a quiet hum before he could stop himself.

If such a cautious man had made a decision that put his family’s fate on the line, it meant he could never take it back.

Not even if it was the Murim Alliance Leader’s order.

“But if this continues, we could lose Shanxi—all of them.”

“I know. If they retreat now, the innocent commoners who haven’t managed to flee will be massacred by the enemy.”

“…”

“Don’t turn your eyes away. They aren’t fighting only to protect the homes where they grew up.”

For a moment, the Thousand-Faced Fox was at a loss for words. Unable to meet Mae Jonghak’s gaze, he closed his eyes.

That was right.

He knew. He had only pretended not to.

This wasn’t a battle. It was a war.

To win it, a few thousand martial artists mattered more than a hundred thousand people.

“Was my judgment… wrong?”

“No. It was excellent. You’re a better strategist than anyone I know.”

At the unexpected answer, the Thousand-Faced Fox opened his eyes.

Mae Jonghak was looking at him with a gentle smile.

“You simply forgot one thing.”

“What was it?”

“You were so busy looking at the whole forest that you failed to see the small branch within it.”

It happened at that very moment.

Srrk.

With a motion of Mae Jonghak’s hand, a surge of qi reached out and flung open the firmly shut door.

Then, with the faint stir of a hidden presence, a figure swept in like the wind.

“What news have you brought?”

At Mae Jonghak’s question, as if he had been expecting the arrival, a messenger from the Alliance Leader’s Office bowed low and answered.

“Urgent news! The Hebei Peng Family, the Murong Family, Huashan, and the Zhongnan Sect are each sending two thousand reinforcements to save Shanxi Province…”

The Thousand-Faced Fox froze and couldn’t hear the rest.

To send such a large force as reinforcements when their own strongholds might be in danger?

That went against every military strategy he’d learned and every bit of common sense everyone knew.

But…

*So that’s what it was.*

The Thousand-Faced Fox smiled bitterly.

Only after the messenger, bearing news he could hardly believe, had left did he break the long silence.

“I understand now. I know the name of the branch I failed to see.”

“What is it?”

“Chivalry.”

Mae Jonghak smiled gently.

He remembered his younger self, who had sworn to build chivalry through martial arts.

“Don’t forget again. We’re all martial artists.”

That day, with the Double Ninth Festival only four days away, two thousand martial artists left the Murim Alliance headquarters and headed north.
```
