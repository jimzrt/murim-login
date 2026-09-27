<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1161.txt",
      "sha256": "a9e33fe0477e1fccb411566e4b409406f395b028d83b6b5fd11f2f0a7fa136a8",
      "bytes": 11460
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "51e091abf173f016c841e92fe080ff0373036ae5e4334476451981c133f6e664",
      "bytes": 2099
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2fd0de0ff721805936794bca4b9ad70fd4d20f40fbc76e97c8e8c5be179dfa5d",
      "bytes": 247561
    },
    {
      "path": "characters/Cang Gong.md",
      "sha256": "55d3b2745fe9597a49ab649f98baa4c2524dc5c6a684ded1dde5b8ca1c8e599b",
      "bytes": 779
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "df37ada3e01d4ddb7ade8f6fe3629af42e523ac714db66a25eea6103c2e2a192",
      "bytes": 777
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "22414f301b5c53278d1ce647552671058ac26177288e1f207278e79799973908",
      "bytes": 760
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7c077708e5498bc4d06cb715a3147665ee19c42e55c2df9b59f35a649a89fead",
      "bytes": 1709
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "6156037857d71c653203545fd09be45c1494e52e6c0fcd7fa2a99ff70fc926bf",
      "bytes": 623
    },
    {
      "path": "characters/Morgoth.md",
      "sha256": "cd6781da8b43b2af993ae277bacbcf79e472bd2a34d4bf18c4dd1ec89261c3e4",
      "bytes": 768
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "53fc8e5ad606c50cc7c1a30963993d01e43b8e22e969d4341588df84d8be434b",
      "bytes": 293737
    }
  ],
  "estimated_tokens": 8888
}
-->

# Durable State Update — Chapter 1161

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
1 and safe_through 1161. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1161. Profile updates may replace only one
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
  "chapter": 1161,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1161,
    "continuity_sources": [1161],
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
    "Morgoth's three-day deadline and demand for Cheon Taemin and Jin Taekyung as tribute remain in effect.",
    "Cheon Taemin remains unconscious in a recovery capsule in a hidden Pentagon chamber.",
    "Jin believes Cheon Taemin was the Martial God and The Helper, and suspects Asmodeus was not completely erased; these identities and suspicions are unconfirmed.",
    "The World Hunter Federation was ordered to mobilize for Moscow against Morgoth and his monsters; Jin intended to go alone.",
    "The Skeleton King reached Morgoth's palace disguised as Jin Taekyung and refused to become his Guardian.",
    "The Skeleton King absorbed power and some abilities from the Arch Lich, Leviathan, and Behemoth; Morgoth inferred that he had encountered a Doppelganger.",
    "The Skeleton King wields the Hero's Sword, an Ego Sword; Morgoth cannot explain how an undead can use it.",
    "After seeing the Skeleton King's willingness to sacrifice himself, Morgoth tries to capture him alive rather than erase him.",
    "Morgoth wounds the Skeleton King and severs his left arm during the capture attempt.",
    "The Skeleton King directs a final strike with the Hero's Sword at his own neck, triggering a vast eruption at the Dragon Lair; the result is unknown.",
    "The Skeleton King can hear the dead spirits and regards them as his people; he suspects he may once have been human, but has no memories and sometimes experiences déjà vu.",
    "Morgoth was summoned by Asmodeus from beyond distant stars and space, but does not know why; he says he is not devoted to Asmodeus."
  ],
  "continuity_sources": [
    1159,
    1160
  ],
  "open_questions": [
    "Were Cheon Taemin, the Martial God, and The Helper the same person?",
    "Was Asmodeus completely erased?",
    "Who escaped through Area 52 in Jin's likeness?",
    "What will happen when Morgoth's three-day deadline expires?",
    "Did the Skeleton King and Morgoth survive the eruption, and what happened to the Dragon Lair?"
  ],
  "safe_through": 1160,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 화산     | **Huashan**            |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 와이번 | **Wyvern** | High-tier dragonkin monster. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |
| 언데드 | **undead** | Supernatural beings that are neither dead nor alive. |
| 드래곤 | **Dragon** | The species to which Morgoth belongs. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |

## Listed compact profiles

### Cang Gong.md

# Cang Gong (창공)

- **Safe through:** Chapter 1141
- **Aliases:** None
- **Role:** Cang Gong is the Eastern Heaven Demon Lord’s assumed identity, through which he became the East Depot’s Brush-Holding Eunuch and a power second only to the Emperor.
- **Personality:** Calculating and self-assured, he is driven by vengeance and believes the rulers and the world betrayed him first.
- **Voice:** Dry and sardonic, he delivers taunts and judgments in measured statements.
- **Relationships:** He was raised by a master and fellow disciples in the Maoshan Sect, whose members died resisting the forced relocation of the capital; Ma Sanbao is his disciple, and he regards Jin Taekyung as a potential recruit.

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 1160
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Ares Guild Master and humanity's greatest Hunter, the Slayer who defeated the Demon King and created the first Mana Cultivation Method during the Great Cataclysm; after more than twenty years in seclusion, he remains unconscious in a secret area within Area A.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1160
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1160
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he protects those he cherishes and is learning to face the fear of leaving them in danger without letting it paralyze him.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the Skeleton King a friend; he trusts Sama Pyo despite suspecting his betrayal, was regarded as a worthy successor by Peng Cheolhu, and received the Martial God’s message through the Bow Saint.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1160
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Morgoth.md

# Morgoth (모르고스)

- **Safe through:** Chapter 1160
- **Aliases:** None
- **Role:** Morgoth is a Dragon and the sovereign of a vast palace who seeks to recruit the Skeleton King as his Guardian.
- **Personality:** Composed and intellectually curious, he pursues the unknown with consuming greed and will abandon restraint when confronted with something unprecedented.
- **Voice:** He speaks in polished, courteous, formal phrasing, often asking measured questions while expressing condescension or fascination.
- **Relationships:** Asmodeus summoned Morgoth, though Morgoth says he is not devoted to him; Morgoth offers the Skeleton King the role of Guardian, which the Skeleton King refuses.

## Korean source

```text
＃1161화



폭풍.

그것은 말 그대로 모든 것을 휩쓸고 파괴하는 힘의 폭풍인 동시에, 충돌로 말미암은 거대한 폭발이었다.

꽈아아아앙!

하늘이 쪼개지는 듯한 굉음과 함께 뒤흔들리는 세상 속, 영혼에 각인된 흉포함도 잊어버린 채 멍하니 드래곤 레어를 바라보고 있던 몬스터들은 불현듯 드리워지는 어둠을 느낄 수 있었다.

곧이어 들이닥친, 상상하지 못했던 힘도.

- ……!

부릅뜬 눈동자와 벌어진 입. 마지막으로 원초적인 공포로 인해 얼어붙어 버린 두 다리까지.

괴물들은 그 어떤 단말마도 흘리지 못했다.

아니, 정확히는 최후의 순간 내지른 그 애처로운 비명조차 아득한 굉음에 파묻혀 지워졌다.

미증유(未曾有)라는 표현이 부족하지 않을 만큼 끔찍한 충돌의 여파에, 그들은 힘없이 휩쓸렸고 처참하게 뭉개졌다.

구구구구궁-!

수천, 수만 개의 유성이 하늘을 뒤덮는다면 이런 광경일까.

엄청난 힘의 폭발로 인해 헤아릴 수조차 없이 수많은 파편으로 변모한 거성(巨城)은 허공을 물들이며 내리꽂혔고, 그 파괴적인 곡선의 끝에는 어느새 석상처럼 굳어 있던 몬스터들이 있었다.

쾅! 콰과과광!

파괴와 죽음.

단숨에 일대를 지배한 그 두 개의 단어에 하늘과 땅이 몸을 떨었다.

모든 것이 뒤섞인다.

뒤덮이고, 허물어진다.

막을 수 있는 방법도, 먼 곳으로 도망칠 시간도 주어지지 않았다.

어지간한 포탄으로는 제대로 된 타격조차 입힐 수 없다는 질긴 가죽과 피부도. 합금보다도 단단한 뼈와 그로부터 비롯된 엄청난 내구성도.

마지막으로 이 모든 것을 가능케 한 상위 몬스터 특유의 강력한 마력도.

그들에게 주어진 그 무엇으로도 코앞까지 닥친 죽음을 피할 수는 없었다.

제아무리 용맹한 투견이라 한들 호랑이에게 잡아먹힐 수밖에 없는 것처럼, 강한 힘은 그보다 더욱 강한 힘에 꺾이기 마련이었으니.

퍼걱! 콰지지직!

두 다리가 짓뭉개진 오우거가 괴성을 내지르고, 찰나의 순간 날아든 파편에 몸뚱어리의 절반이 날아간 트롤이 몸을 부르르 떨다 고꾸라진다.

드래곤의 후예이자 창공의 주인을 자처하던 와이번들도 이제는 두 번 다시 날아오를 수 없을 것이다.

폭발의 중심지에 가장 가까웠던 그들은 그 여파에 닿는 즉시 절명했거나, 혹은 긍지와 같던 날개를 잃은 채 힘없이 추락하고 있었으니까.

거대한 드래곤 레어를 넘어 사방으로 뻗어 나간 힘의 폭발은 그만큼 강력했고, 그 안에 담겨 있던 미증유의 마력은 일대에 머무르고 있던 몬스터 군단을 덮쳤다.

끝없이, 탐욕스럽게.

영원히 끝나지 않을 것만 같던 이 죽음의 파도는, 무려 수만 마리의 몬스터를 집어삼킨 후에야 서서히 잦아들기 시작했다.

그리고 그 모든 것의 중심에서, 한 존재가 눈을 떴다.

파스슥.

호리호리한 신형을 타고 흘러내리는 잿가루.

드래곤 레어, 아니 이제는 폐허라는 단어조차 무색할 잿더미 속에서 몸을 일으켜 세운 모르고스는 문득 고개를 돌려 주위를 바라보았다.

대지진이라도 일어난 것처럼 뒤집힌 대지와 산처럼 쌓인 괴물들의 사체.

어느덧 강이 되어 흐르고 있는 녹색 핏물과 갈라진 먹구름의 틈새 사이로 이 끔찍한 광경을 엿보고 있는 한 줄기의 햇빛까지.

하지만 지금 이 순간, 흑요석처럼 빛나는 흑룡의 두 눈동자에는 단 한 줌의 분노조차 담겨 있지 않았다.

“장관이군.”

바싹 말라붙은 입술 사이로 흘러나온 외마디 감탄.

그것이 전부였다.

한순간의 방심으로 인해 수많은 부하를 잃었음에도, 모르고스는 조금도 신경 쓰지 않았다.

정확히는 신경 쓸 이유가 없었다.

이런 사소한 희생과는 비교도 할 수 없을 만큼 귀중하고 흥미로운 보물을 손에 넣게 되었으니까.

“무언가를 얻기 위해서는 그에 합당한 대가를 치러야 하는 법이지. 그렇지 않나?”

혼잣말과도 같은 물음이었지만, 이에 대한 대답은 그리 오래 지나지 않아 돌아왔다.

다름 아닌 그의 발치에서.

“닥……쳐.”

고장난 라디오처럼 흐릿하게 들려오는 목소리에, 모르고스는 안도의 한숨을 내쉬었다.

“기운이 남아 있어서 다행이군. 자네가 소멸할까 봐 얼마나 마음을 졸였는지 몰라.”

그 말은 결코 과장이 아니었다.

조금 전, 각기 다른 두 갈래의 거대한 기운이 충돌하며 발생한 힘의 여파는 실로 무시무시했다.

만약 모르고스가 전력을 다해 스스로를 보호하지 않았다면, 지금쯤 그의 전신을 뒤덮은 것은 먼지가 아닌 그 자신의 핏물이었을지도 몰랐다.

“덕분에 뜻하지 않은 피해가 생기긴 했지만…… 어쩌겠나. 이 또한 누군가가 정한 순리겠지.”

모르고스는 빙긋 웃으며 어깨에 쌓인 먼지를 털었다. 뿌옇게 흩날리는 그것처럼, 하등한 몬스터 따위의 죽음은 그에게 있어 아무것도 아니었다.

지금의 그에게 있어서는 오직 단 하나, 눈앞의 존재만이 가장 큰 관심사이자 목적일 뿐.

“고맙네. 잘 버텨 줘서. 자네는 모든 면에서 내 예상을 뛰어넘었어.”

사실, 뛰어넘었다는 표현으로도 부족했다.

상대가 소멸을 각오하고 스스로를 향해 내지른 그 일격은, 모르고스가 아득한 세월 동안 잊고 있던 감각을 일깨워 주었으니까.

툭. 투두둑.

어느샌가 그의 발치를 적셔 오는 액체.

마치 은덩이를 녹여낸 듯한 자신의 은빛 핏물과, 손바닥을 뚫고 삐죽 솟아 있는 검신을 바라보던 모르고스가 미간을 찡그렸다.

“그래, 이게 바로 고통이었지.”

무려 천년 만에 느껴 보는 감각.

그렇기에 더욱 아팠고, 쓰렸다.

그리고 그것은 그가 마지막으로 고통을 느꼈던, 동시에 고통보다 더욱 큰 치욕을 느껴야만 했던 그 날의 기억 때문일지도 몰랐다.

“……아스모데우스.”

속삭이듯 작게 뇌까린 모르고스는 과거의 기억을 떨쳐내듯, 단숨에 [영웅의 검]을 뽑아 움켜쥐었다.

파창!

두 개로 분리된 검신이 땅 깊숙이 처박힌다.

이제는 머리밖에 남지 않은 주인의 모습을 거울처럼 비추면서.

“스켈레톤 킹. 저주받은 망령들의 왕이여.”

모르고스는 천천히 허리를 굽혀 자신을 노려보는 스켈레톤 킹을, 눈동자 대신 시퍼런 귀화(鬼火)가 일렁이고 있는 해골을 어루만졌다.

“보이는가? 자네의 본모습이.”

“닥치라고…… 했다.”

“분노를 가라앉히게. 그저 인정하고 받아들이면 돼. 자신이 어디에서부터 비롯되었으며, 누구와 함께해야 하는지.”

최면처럼 울려 퍼지는 매혹적인 음성.

그러나 스켈레톤 킹은 조금도 흔들리지 않았다.

당장이라도 끊어질 듯한 의식의 끈을 부여잡은 채, 자신에게 남은 한 줌의 기운을 쥐어 짜내어 입을 열었다.

“역시, 넌 그 녀석과 달라.”

“그 녀석?”

“그래. 아주 시건방지고, 간악하기 짝이 없는 인간이지. 하지만…….”

바로 그 녀석이, 진태경이 언젠가 말했다.

너는 단지 너일 뿐이라고.

그리고.

“내 친구다.”

“……!”

“나를 그 빌어먹을 어둠 속에서 건진 것도, 지금까지 알지 못했던 새로운 세상을 알려 준 것도 그 녀석이었어.”

많은 것을 보았다.

많은 것을 배웠다.

어둠과 죽음만이 들끓던 게이트를 벗어나, 빛나는 태양 아래에서 모두와 어울렸다.

기쁜 날도, 슬픈 날도 있었으나 그 모든 순간이 눈부셨다.

더는 혼자가 아니었으니까.

함께하고 있었으니까.

그것으로 되었다.

“그러니까, 괜히 병신 같은 헛소리로 시간 낭비하지 말고 마음의 준비나 해두는 게 좋을 거다.”

스켈레톤 킹은 웃었다.

그 어느 때보다 밝고, 환하게.

“곧, 내 친구들이 찾아올 테니까.”

그 순간.

팟.

마치 호롱불이 꺼지듯, 텅 빈 동공에 일렁이던 귀화가 불현듯 사라졌다.

“……친구들, 이라고?”

더는 버티지 못하고 마침내 의식의 끈을 놓아 버린 스켈레톤 킹의 마지막 말을, 모르고스는 홀로 곱씹었다.

친구.

익숙하지만, 처음 듣는 것처럼 낯선 단어다.

한때 또 다른 세상의 인간 사회에서 긴 세월을 보냈음에도 불구하고, 그는 친구라는 존재에 대해 좀처럼 이해하지 못했다.

피 한 방울조차 섞여 있지 않은 그들이 왜 서로를 각별히 생각하며, 때로는 목숨까지 내놓는 어리석은 선택을 하는지도.

그 사실을 너무나도 잘 알고 있는 모르고스로서는 그저 흥미롭고 놀라울 따름이었다

첫 번째로는 저주받은 언데드 몬스터에 불과한 스켈레톤 킹이 이토록 인간적인 면모를 보여 준다는 점에서.

그리고 두 번째로는.

‘진태경.’

어쩌면 스켈레톤 킹이라는 존재를 이토록 특별하게 변화시켰을지도 모르는, 한 인간에 대해서.

‘알아내야 할 것이 많아졌군.’

물론 진태경에 관한 정보는 이미 알고 있었다.

새로운 시대의 구원자. 이 세상의 중심이자 모두의 앞에 선 젊은 영웅.

진태경은 천태민 다음으로 모르고스가 가장 경계해야 할 대상 중 하나였고, 그 생각은 여전히 변함없었다.

다만, 지금까지와는 다른 강렬한 호기심이 추가되었을 뿐.

“그래, 준비를 해 둬야겠군. 자네의 조언대로.”

대답이 없는 백골을 향해 중얼거린 모르고스는 어느덧 울림이 멎은 대지를 바라보았다.

갈라진 먹구름의 틈새로 고개를 내민 빛줄기 때문일까. 온통 뒤집히고 갈라진 그곳은, 마계(魔界)나 다름없던 칠흑색의 빛깔과 그 안에 스며들어 있던 농도 짙은 마력을 상당 부분 잃은 상태.

그러나 모르고스는 개의치 않았다.

자신의 심장에 담긴 끝없는 힘. 무한에 가까우면서도 지극히 순수한, 타락의 결과물인 마력을 천천히 일으켜 세웠다.

아니, 그러려고 했다.

다음 순간, 예상치 못했던 누군가의 기척을 느끼기 전까지는.

우우우우웅.

당장이라도 활화산처럼 터져 나올 것만 같던 마력이, 동시에 흑룡의 두 눈동자가 깊이 가라앉는다.

그렇게 불안하게 흔들리는 공기와 멈춰 버린 바람 사이로, 굳게 닫혀 있던 모르고스의 입술이 열렸다.

“실례했군. 손님이 온 줄도 모르고 있었으니.”

나직한 음성을 따라 흩어지는 거무스름한 안개.

그 너머로, 누군가의 대답이 울려 퍼졌다.

“궁금해서 물어보는 건데.”

담담하지만, 용암처럼 들끓고 있는 그 목소리가.

“지금 손에 들고 있는 게 뭐지?”
```

## Final English reading copy

```markdown
# Chapter 1161

A storm.

A storm of power that swept away and destroyed everything in its path—and, at the same time, a colossal explosion born of collision.

KABOOOOOM!

As the world shook beneath a roar that seemed to split the sky, the monsters staring blankly at the Dragon Lair, having forgotten even the savagery etched into their souls, suddenly felt darkness fall over them.

Then came an unimaginable force.

—!

Eyes wide, mouths agape. And finally, their legs frozen by primal fear.

The monsters could not even let out a death cry.

No—in their final moments, the pitiful screams they managed were swallowed and erased by the deafening roar.

The impact was so horrific that “unprecedented” hardly did it justice. They were swept away helplessly, crushed into ruin.

RUMBLE, RUMBLE—!

Would this be what it looked like if thousands upon thousands of meteors covered the sky?

The colossal castle, reduced to countless fragments by the tremendous blast of power, stained the air as it plunged down. At the end of its destructive arc stood the monsters, frozen like statues.

CRASH! CRASH-CRASH-CRASH!

Destruction and death.

Those two words ruled the area in an instant, and sky and earth shuddered beneath them.

Everything mingled.

Buried. Crumbling.

There was no way to stop it, no time to flee to safety.

Their tough hides and skin—so resilient that ordinary artillery could barely scratch them. Their bones, harder than alloys, and the immense durability those bones gave them.

And finally, the powerful magical power unique to superior monsters, which had made all this possible.

Nothing they had could save them from the death rushing toward them.

However brave a fighting dog might be, it would still be eaten by a tiger. Great strength was bound to yield to greater strength.

CRUNCH! CRACK!

An ogre with both legs crushed let out a shriek. A troll, half its body torn away by a fragment that had flashed past in an instant, shuddered and fell.

Even the Wyverns, descendants of Dragons who claimed the sky as their domain, would never fly again.

Those closest to the explosion’s center had either died the moment the shock wave reached them or were now falling helplessly, their proud wings gone.

The explosion of power spread in every direction beyond the vast Dragon Lair. Its unprecedented magical power engulfed the monster army that had been in the area.

Relentlessly. Greedily.

This wave of death, which seemed as if it would never end, only began to subside after swallowing tens of thousands of monsters.

And at the center of it all, one being opened his eyes.

*Psshh.*

Ash slid down his slender frame.

Morgoth rose from the ashes of what had been the Dragon Lair—no, the word “ruins” could hardly describe it now—and turned to survey his surroundings.

The earth was overturned as if by a massive earthquake, and monster corpses were piled up like mountains.

Green blood flowed in rivers. Through a break in the dark clouds, a single shaft of sunlight peered down at the dreadful scene.

Yet in this moment, not a hint of anger shone in the Black Dragon’s obsidian eyes.

“What a sight.”

That was all he said, the brief exclamation escaping through his cracked lips.

Nothing more.

Though a moment’s carelessness had cost him countless subordinates, Morgoth didn’t care in the slightest.

More precisely, there was no reason to care.

He had gained a treasure far more precious and fascinating than those trifling losses could ever be.

“To obtain something, one must pay a price worthy of it. Don’t you agree?”

It sounded like a question to himself, but the answer came before long.

From right at his feet.

“Shut… up.”

At the faint voice, as hazy as a broken radio, Morgoth breathed a sigh of relief.

“I’m glad you still have enough strength to speak. I was worried you might be erased.”

He wasn’t exaggerating.

The shock wave from the collision of two immense, utterly different forces had been truly terrifying.

If Morgoth hadn’t protected himself with all his might, his entire body might now have been covered not in dust, but in his own blood.

“Still, there was some unintended damage… What can you do? This, too, must be the order of things, determined by someone.”

Morgoth smiled and brushed the dust from his shoulder. Like the dust drifting away in a pale cloud, the deaths of inferior monsters meant nothing to him.

Now, only one thing mattered to him. The being before him was his greatest interest and sole objective.

“Thank you. For holding on so well. You exceeded my expectations in every way.”

In truth, even “exceeded” didn’t begin to cover it.

The blow his opponent had unleashed against himself, prepared to be erased, had awakened a sensation Morgoth had forgotten over the course of ages.

Tap. Drip, drip.

Liquid began to wet his feet.

Morgoth frowned as he looked at his own silver blood, like molten silver, and the blade protruding through his palm.

“Yes. So this is pain.”

A sensation he hadn’t felt in a thousand years.

That was why it hurt more. Stung more.

Perhaps it was because of the memory of the last day he had felt pain—and, at the same time, endured a humiliation greater than the pain itself.

“…Asmodeus.”

Morgoth murmured the name in a whisper, then, as if to shake off the memories of the past, yanked the [Hero’s Sword] free and gripped it.

*Crash!*

The blade, split in two, plunged deep into the ground.

Reflecting its owner’s form, now reduced to a head.

“Skeleton King. King of the cursed wraiths.”

Morgoth slowly bent down toward the Skeleton King, who glared up at him. He stroked the skull, where blue ghostly flames flickered in place of eyes.

“Can you see it? Your true self.”

“I told you… to shut up.”

“Calm your anger. You only need to acknowledge and accept it. Where you come from, and whom you belong with.”

His captivating voice rang out, almost like a hypnotic spell.

But the Skeleton King didn’t waver in the slightest.

Clinging to a thread of consciousness that seemed ready to snap, he squeezed out the last bit of strength he had and spoke.

“You really are different from that guy.”

“That guy?”

“Yeah. An arrogant, downright devious human. But…”

That guy—Jin Taekyung—had once told him:

You’re just you.

And—

“He’s my friend.”

“……!”

“He’s the one who pulled me out of that godforsaken darkness. He’s the one who showed me a new world I’d never known.”

He had seen so much.

He had learned so much.

He had left the Gate, where only darkness and death churned, and spent time with everyone beneath the shining sun.

There had been happy days and sad days, but every moment had been dazzling.

Because he wasn’t alone anymore.

Because he was with them.

That was enough.

“So don’t waste your time with any more of that stupid bullshit. You’d better get ready.”

The Skeleton King smiled.

Brighter and more radiant than ever.

“My friends will be here soon.”

At that moment—

*Flick.*

Like a lamp going out, the ghostly flames flickering in his empty eye sockets suddenly vanished.

“…Your friends, you say?”

Morgoth mulled over the Skeleton King’s final words alone. At last, the Skeleton King could hold on no longer and let go of consciousness.

Friend.

A familiar word, yet strange, as if he’d never heard it before.

Even though Morgoth had spent a long time in human society in another world, he had never been able to understand the idea of a friend.

Why did people with not a drop of blood in common care so deeply for one another? Why did they sometimes make the foolish choice to lay down their lives?

Morgoth knew all too well that they did such things. Why they did so remained a source of fascination and astonishment to him.

First, that the Skeleton King—nothing more than a cursed undead monster—could show such humanity.

And second—

*Jin Taekyung.*

A human who might have changed the Skeleton King into this extraordinary being.

*There’s more I need to find out.*

Of course, Morgoth already knew about Jin Taekyung.

The savior of a new age. The center of this world, a young hero who stood at the head of them all.

After Cheon Taemin, Jin Taekyung was one of the people Morgoth had to watch most carefully. That hadn’t changed.

He had simply gained a powerful curiosity about him unlike anything he’d felt before.

“Yes. I’ll have to get ready, as you advised.”

Morgoth murmured to the silent skull, then looked out over the earth, where the rumbling had finally stopped.

Perhaps it was because of the shaft of light peeking through the split dark clouds. The place, overturned and cracked all over, had lost much of its pitch-black color—like the Demon Realm—and much of the dense magical power that had seeped through it.

But Morgoth didn’t care.

He slowly roused the endless power in his heart: the magical power that was nearly infinite and utterly pure, the product of corruption.

No—he was about to.

Until he sensed someone unexpected.

*Vwoom.*

The magical power that seemed ready to erupt like an active volcano subsided. At the same time, the Black Dragon’s eyes grew dark.

Then, amid the unsteadily trembling air and the wind that had come to a stop, Morgoth’s tightly closed lips parted.

“My apologies. I didn’t realize we had a guest.”

Dark mist drifted away as he spoke in a low voice.

Beyond it, someone answered.

“I’m asking because I’m curious.”

The voice was calm, yet seething like lava.

“What’s that you’re holding?”
```
