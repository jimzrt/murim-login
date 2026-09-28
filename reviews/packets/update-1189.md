<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1189.txt",
      "sha256": "78713e0d11013483876fd93eaf0fd0b05daced0d002d03100ed28bb1b7c82e0c",
      "bytes": 11255
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e97b32497c2d9c289b6d1be2d7c2ee6984b15a6f4cddf86905b1364c8fbd7962",
      "bytes": 2053
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0821386659bc3addb778ca5fcefcff90bf100119ece13916b00f44e929e9de3b",
      "bytes": 248927
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "9bfd6552136793502f6a6438e16c39f711dab5836a39adb4021dbe750867386a",
      "bytes": 760
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "7ce6770ce4d06afb7a6dbca467e067d472213010efc4377098db55ec1b42a493",
      "bytes": 668
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "72c3fc0b469baba7080e5459794252596628c0529fc221762728ccfb6fd0e406",
      "bytes": 1701
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7950d918d068f339d867d9ae5a5738a771202568a1dbf7221c92f364c496bfe8",
      "bytes": 1550
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "aa03c0b36a58cfa219208ac65256d94edda2c1924e96772bd5fc0a40c744ea5d",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6592233b34dcd7f1d0f74935310ed387046c3f86f1869fa5f218139dd6824a3a",
      "bytes": 295903
    }
  ],
  "estimated_tokens": 9378
}
-->

# Durable State Update — Chapter 1189

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
1 and safe_through 1189. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1189. Profile updates may replace only one
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
  "chapter": 1189,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1189,
    "continuity_sources": [1189],
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
    "A sinister mist separated Jeok Cheongang and unconscious Taekyung from the Bow Saint, the Slaughter Saint, Gung Gibang, Hyuk Mujin, Ju Hwaran, and Song Ilseom; Jeok is fighting monstrous beings within it.",
    "In the mist, Jeok encountered a being wearing Jangcheon’s appearance and attacked it; whether it is connected to the real Jangcheon is unknown.",
    "The group is following Mae Jonghak’s contingency plan after the allied forces missed their deadline; the Murim Alliance and Imperial Army are drawing Dark Heaven’s attention away from the desert.",
    "The Lord of Heaven has awakened and regained strength, but says the process is incomplete; the Grand Mage awaits a command.",
    "The Main Quest “Rift and Collapse” failed; “The Foreordained Collapse” warns that player choices can cause irreversible consequences.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon; Jin knows he is the Martial God and a former Player.",
    "An alert reported Alpha’s awakening; what Alpha is and what its awakening means remain unknown.",
    "Taekyung has experienced unexplained chest pain and difficulty sleeping; the Slaughter Saint also wonders whether Taekyung used his full strength while affected by the fasting pill."
  ],
  "continuity_sources": [
    1188,
    1187
  ],
  "open_questions": [
    "What is the being wearing Jangcheon’s appearance, and is it connected to the real Jangcheon?",
    "What is causing the mist’s power, and what has happened to the separated companions?",
    "What is the source of Taekyung’s chest pain and sleeplessness, and did he use his full strength against the fasting pill’s effects?",
    "What remains to be completed for the Lord of Heaven, and what command will he give the Grand Mage?",
    "What is Alpha, and what does its awakening mean?"
  ],
  "safe_through": 1188,
  "temporary_decisions": [
    "Render 진인사대천명 as “Do all that man can, then await Heaven’s will.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 열화문    | **Fire Gate Clan**               |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 제자     | **Disciple**                                 |
| 노부      | **this old man / I**                                            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 장천 | **Jangcheon** | Name Jeok Cheongang gave to the orphan who later became Jopil; means “Vast Sky.” |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천라지망 | **net over heaven and earth** | Jeok Cheongang's figurative threat to pursue a culprit everywhere. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 수강 | **Palm Force** | Force generated through a palm technique. |
| 암초 | **reef** | Reefs blocking the narrow water route. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 장천 | 적천강 | disciple_to_master | Master | deferential and pleading | Jangcheon repeatedly begs Jeok Cheongang to accept him as his Disciple. |
| 적천강 | 장천 | master_to_disciple | you / fool | blunt and gruff | Jeok rejects Jangcheon’s pleas, questions his choices, and threatens to send him down the mountain. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 기자 | 진태경 | Japanese reporter to celebrated foreign Hunter | Jin-sama | formal and reverent | Japanese reporters repeatedly address Jin with the honorific 사마. |
| 진태경 | 기자 | Hunter to Japanese reporter | reporter; you | blunt and insulting | Jin rebukes a reporter for talking back after criticizing Yamamoto's delayed arrival. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1188
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 1178
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1188
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and follows his own path rather than pursuing grand causes; though he turned his back on the world, he wants Taekyung to pursue righteousness, practice chivalry, and win people’s hearts, and fiercely protects those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, and shares familiar, teasing camaraderie with the Slaughter Saint; he accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1188
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant, he is pragmatic and fiercely defiant; he protects those he cherishes and meets mounting responsibility with hope and a determination to endure.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the revived Undead King, formerly the Skeleton King, a friend.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1188
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃1189화



- 그. 아. 아. 아. 아!

그것은 인간이 내지르는 비명도, 살아 있는 생명체가 낼 수 있는 소리도 아니었다.

이미 한 차례의 죽음을 겪으며 고통을 잊은 괴물에게 남아 있던 유일한 것.

바로 그의 타락한 영혼이 연소(燃燒)되었음을 알리는 경종이자, 두 번째 죽음을 알리는 마지막 단말마였다.

콰아아아아!

광포하게 공간을 휩쓸며 뻗어나가는 멸염신권(滅炎神拳)의 겁화.

뒤이어 터져 나온 아득한 섬광과 그보다 더한 굉음까지.

구구구구궁!

지면이 요동치고, 혼탁하게 뒤섞인 불씨와 잿가루가 이리저리 흩날린다.

그리고 그 너머에, 천천히 허물어지는 그림자가 있었다.

장천.

아니, 장천의 환영을 뒤집어쓰고 있던 한 마리의 괴물이.

‘흑귀(黑鬼).’

적천강은 그것의 정체를 즉각 알아보았다.

망자의 육신과 넋을 재료로 삼아 새로운 삶을 부여받은 괴물.

죽은 것도, 산 것도 아닌 그들은 천주 휘하의 무수한 괴물 중에서도 가장 기묘하면서도 강력한 존재들이었다.

그래, 그야말로…….

‘역시, 마법(魔法)인가.’

피부를 스치는 바람조차 이질적인 공간.

단순한 진법이라기에는 너무나도 정교하면서도 괴이한 현상들.

내심 마음속에 품고 있던 그 짐작이 확신으로 변한 순간, 적천강은 일대를 둘러싼 기의 흐름이 요동치는 것을 알아차렸다.

그 변화의 원인도 함께.

스아아아.

불현듯 밀려온 한풍이 공간을 일그러트리던 아지랑이를 짓누르고, 흩날리던 불씨와 잿가루를 가라앉힌다.

그리고 그것은 단순한 바람이 아닌, 또 다른 무언가의 출현을 알리는 기파(氣波)였다.

“그래, 왔더냐.”

적천강은 가라앉은 눈빛으로 새로운 불청객들을 바라보았다.

동, 서, 남, 북.

어느덧 사방을 점하며 나타난 네 개의 그림자가 그를 바라보고 있었다.

각기 다른 얼굴, 하지만 어딘가 닮아 있는 얼굴로.

- 스승님.

하나로 합쳐 울리는 네 줄기의 음성.

처음 만난 그날처럼 흙투성이 몰골을 한 어린 장천이.

제자로 받아달라 간청하던 소년 장천이.

어느덧 청년기에 접어든 장천과, 떠나던 날의 장천이 그곳에 있었다.

더는 되돌아갈 수 없는 그 날의 모습으로.

- 스승님. 제가 왔습니다. 천아가 왔습니다.

네 명의 장천이 동시에 말하며 걸음을 옮기자, 일대를 빈틈없이 에워싼 무수한 괴물들 역시 포위망을 좁혔다.

오직 단 한 사람을 위한 천라지망(天羅蜘網).

그러나 놈들이 피워올리는 그 짙은 살의 속에서도, 적천강은 담담하게 입을 열었다.

“참 희한한 일이군. 노부가 모르는 제자가 넷이나 더 있었다니.”

- 스승님. 어찌 저를 잊으실 수 있습니까?

마치 한 몸인 양, 사방에서 울리는 목소리에 적천강이 쓴웃음을 지었다.

“잊지 않았다. 단지 이제는 기억으로만 간직하기로 다짐했을 뿐.”

환영을 뒤집어쓴 괴물들에게 하는 말이 아닌, 이 자리에 없는 옛 제자에게 하는 말.

설령 아무 곳에도 닿지 못할 목소리라 해도 상관없었다.

오늘에서야 확실하게 알게 되었으니까. 지금이 아니라면 말할 수 없을 테니까.

만약 살아 있는 장천이 눈앞에 나타났더라도, 자신의 선택은 달라지지 않았으리라는 것을.

“노부는 못난 스승이었고, 너는 못난 제자였다. 허나 우리가 서로에게 지은 죄는 이번 생이 아닌, 언젠가 만날 먼 훗날에 갈음하도록 하자.”

엎질러진 물은 주워 담을 수 없고, 지나간 시간은 돌이킬 수 없는 법.

그러므로 중요한 것은 바로 지금이며, 현재의 적천강에게는 지켜야 할 소중한 것이 남아 있었다.

“그러니, 천아야.”

적천강은 과거 그랬던 것처럼 부드러운 음성으로 옛 제자의 이름을 입술 끝에 실어 떠나보냈다.

지금까지도 자신의 기억 속에 선명하게 각인되어 있는 그날의 얼굴들을 차례대로 바라보면서.

자신의 등에서 전해지는 누군가의 온기와 숨결을 느끼면서.

그는 살아 있음을 느꼈고, 살아남아야 함을 다짐했다.

“너를, 파문(破門)하겠다.”

그 순간.

화악-!

어두컴컴한 안개 사이로, 섬광이 터져 나왔다.

아니, 그것은 빛만큼이나 밝게 타오르는 화염이자 마침내 몸을 일으킨 불의 거인이었다.

콰아아아!

염화일로(炎火一路)의 열기가 공간을 일그러트린다.

단 한 걸음, 삼십여 장에 달하던 거리가 지워지고 크게 뜨여진 괴물들의 눈동자가 성큼 가까워진다.

콰드드득!

더 이상의 말도, 생각도 필요 없었다.

화왕(火王) 적천강은 눈앞에 보이는 모든 것들을 짓뭉갰다.

전후좌우를 가리지 않고 적들이 물밀듯이 밀려들었지만, 그는 자신의 주위에서 일어나는 모든 일을 빠짐없이 보고 느끼고 있었다.

눈으로, 귀로, 때로는 오감을 넘어선 육감(六感)으로.

- 구워어어!

여덟 개의 팔과 세 개의 머리.

흡사 전설 속 아수라(阿修羅)와 같은 모습을 띤 일단의 괴물들이 달려든다.

이제는 인간의 것인지, 짐승의 것인지도 분간할 수 없는 여러 개의 팔이 미친 듯이 휘몰아치며 적천강의 머리 위로 쏟아졌다.

정확히는, 적천강이 있던 그 자리로.

파가가가각!

헛되이 허공을 가르며 내리꽂힌 공격이 지면을 난도질한 그때, 누군가의 음성이 괴물들의 귓가를 파고들었다.

나직하지만 불길처럼 뜨거운, 그래서 한편으로는 얼음장보다 더 차갑게 느껴지는 그 목소리가.

“심장은 몇 개냐.”

그리고 그것이 마지막이었다.

화륵, 푸화아아악!

의식이 끊어지는 그 순간까지도 괴물들은 자신들이 언제, 어떻게 죽었는지도 알지 못했다.

어느샌가 땅을 박차고 솟아오른 적천강이 길게 뽑아낸 수강(手罡)을 내리그었다는 것도.

그 안에 실린 끔찍한 열기가 심장은 물론 모든 장기를 불태웠다는 사실 역시도.

하지만 적천강을 지켜보고 있던 네 쌍의 눈동자는 아니었다.

처음부터 이 순간만을 노리고 있던 그들은 약속이라도 한 듯이 단 한 치의 오차도 없이 움직였다.

스아아악!

일순간 예리하게 날 선 감각을 통해 스며든, 소름 끼칠 만큼 낮고 희미한 파공성.

수십 마리에 달하는 괴물들을 단숨에 녹여 버린 적천강은, 어느덧 코앞까지 들이닥친 그 불길한 기운을 즉시 감지했다.

그것이 하나가 아니라는 사실도.

하지만 그 속도와 안에 담긴 힘은, 적천강이 예상했던 것 이상이었다.

“……!”

느려진 찰나의 시간 속, 적천강은 모든 감각을 통해 사각(死角)에서 날아드는 네 줄기의 강기를 느꼈다.

그리고 이성이 아닌 본능에 가까운 움직임으로, 온 힘을 다해 몸을 비틀었다.

서걱!

서늘한 절삭음과 함께 핏물이 튀었다.

고약한 악취와 독기까지 스민 괴물들의 녹색 핏물이 아닌, 살아 있는 인간의 붉은 피가.

그러나 아릿하게 전해져 오는 고통 속에서도, 아슬아슬하게 중심을 되찾아 착지한 적천강은 만족스럽게 웃었다.

실로 다행이었다.

비록 그의 피륙은 상했을지언정, 진태경은 털끝 하나 다치지 않았으니.

다만 안도감에서 비롯된 그 미소는 그리 오래가지 못했다.

조금 전의 공격으로 입은 부상은 그리 심하지 않았으나, 현재의 전황은 명백히 그에게 불리했으니까.

제자를 지키며 싸워야 하는 스승과 죽음을 두려워하지 않고 달려드는 수많은 괴물.

그중에서도 가장 큰 문제는, 지금 이 순간에도 신중하게 거리를 재며 빈틈을 노리고 있는 네 마리의 흑귀였다.

‘강하다. 생각 이상으로.’

지금껏 상대했던 여타의 흑귀들보다 최소 한 수, 어쩌면 두 수 가까이 앞서는 듯한 느낌.

그 이유가 일대를 에워싼 마법의 영향인지, 아니면 저들이 흑귀 중에서도 특별히 강력한 개체인지 그로서는 알 방법이 없었으나 한 가지는 확실했다.

‘어려운 싸움이 되겠군.’

사실, 어려움이라는 표현조차도 부족했다.

개개인의 역량도 역량이지만, 생각을 공유하는 하나의 유기체처럼 움직이는 네 명의 초절정 고수는 적천강과 같은 강자라도 결코 경시할 수 없는 상대였으니까.

이는 살아 있는 인간이라 해도 마찬가지일진대, 거기에 더해 놈들은 감정도 고통도 느끼지 못하는 괴물들.

심지어 모든 상황은 적들에게 유리하게 흘러가고 있었다.

지금 이 순간조차도.

- 크워어어어!

흉성을 내지르며 재차 달려드는 괴물들과 그 사이로 모습을 감춘 흑귀들을 보며, 적천강은 놈들의 의도를 명확하게 깨달았다.

‘차륜전(車輪戰)……!’

커다란 바위를 빠르게 깨트리기 위해서는 날카로운 정과 무거운 망치가 필요하지만, 충분한 시간만 주어진다면 간혹 떨어지는 소나기만으로도 충분하다.

천천히, 그러나 계속해서 떨어지는 물방울이 단단한 바위의 표면을 두드리며 틈새를 만들어 내는 것이다.

그리고 흑귀들의 지휘 아래 끝도 없이 밀려드는 저 괴물들은 작고 가벼운 물방울도, 소나기 따위도 아니었다.

파도.

거칠게 휘몰아치는 파도다.

망설임 없이 목숨을 내던지는 맹목적인 광기와, 어떤 암초든 반드시 부숴내고야 마는 힘이 실린.

하지만 적천강은 그저 제자리에 서서 부서지기만을 기다리는 바위가 아니었다.

‘단숨에 끝낸다.’

그의 본질은 불이요, 천하의 누구보다 커다란 불꽃을 피워올렸기에 화왕이라.

으득.

적천강은 이를 악물었다.

어느덧 붉게 타오르는 안광이 거무스름한 안개를 꿰뚫고, 전신을 타고 올올히 피어오르는 아지랑이를 따라 공간이 뒤틀렸다.

화아아아.

용암과도 같은 기운이 사지 백해를 타고 솟구친다. 천천히 열리는 입술 사이로 수증기 같은 숨결이 흘러나왔다.

“모조리, 죽여 주마.”

바위라면 녹이고, 파도라면 증발시킬 것이다.

설령 그 자신마저 재가 되어 사그라질지라도, 모든 것이 불타 버린다 해도 열화문의 불씨는 꺼지지 않는다.

아니, 적천강의 그것보다 더욱 크고 거대한 불길이 솟아오를 것이다.

“오너라!”

모든 준비를 끝낸 거인의 포효가 사방을 떨어울린 그 순간.

“어우, 깜짝이야. 귀청 터지겠네.”

“……!”

적천강은 역류할 뻔한 공력을 가까스로 부여잡았다.
```

## Final English reading copy

```markdown
# Chapter 1189

“Grrrraaaaaah!”

It wasn’t a scream a human could make—or even a sound any living creature could produce.

It was all that remained of a monster that had already died once and forgotten pain.

A warning bell announcing that his corrupted soul had burned away. The final death cry that heralded his second death.

*Fwoooooom!*

The hellfire of the Flame-Extinguishing Divine Fist swept wildly through the space.

Then came a blinding flash, followed by an even louder roar.

*RrrrRUMBLE!*

The ground shook. Embers and ash, churning in the murky air, scattered in every direction.

Beyond them, a shadow slowly crumpled.

Jangcheon.

No—one of the monsters wearing Jangcheon’s face.

*Black Ghost.*

Jeok Cheongang recognized it at once.

A monster given new life using the body and soul of the dead.

Neither dead nor alive, they were the strangest and most powerful among the countless monsters under the Lord of Heaven.

Yes, this was surely—

*Magic, after all.*

A space where even the wind brushing his skin felt alien.

Phenomena too intricate and bizarre to be explained by a mere formation.

The suspicion he had been harboring became certainty. Jeok Cheongang felt the flow of qi surrounding the area begin to churn.

And he sensed the cause of the change, too.

*Shhhhh.*

A sudden cold wind swept in, pressing down on the heat haze that distorted the space and settling the drifting embers and ash.

It wasn’t an ordinary wind. It was a wave of qi announcing the arrival of something else.

“So, you’ve come.”

Jeok Cheongang looked at the new intruders with steady eyes.

East, west, south, and north.

Four shadows had appeared, each holding a position around him and gazing his way.

Different faces, yet somehow alike.

“Master.”

Four voices rang out as one.

There was Jangcheon as a dirt-covered child, just as he’d looked the day they first met.

Jangcheon as a boy, pleading to be accepted as a Disciple.

Jangcheon, now a young man.

And Jangcheon as he’d looked on the day he left.

All frozen in forms from a day that could never be taken back.

“Master. I’ve come. Cheon-ah is here.”

The four Jangcheons spoke together and stepped forward. At the same time, the countless monsters encircling the area closed in.

A net over heaven and earth, drawn tight for one man alone.

Yet even amid the monsters’ thick killing intent, Jeok Cheongang spoke calmly.

“What a strange business. Four more Disciples I never knew I had.”

“Master. How could you forget me?”

The voice rang out from every direction, as if all four shared a single body. Jeok Cheongang gave a bitter smile.

“I haven’t forgotten. I simply resolved to keep you as a memory now.”

He wasn’t speaking to the monsters wearing the illusion. He was speaking to his old Disciple, who wasn’t there.

It didn’t matter if his voice reached no one. Only now had he understood for certain. If he didn’t say it now, he might never get the chance.

Even if the living Jangcheon had appeared before him, his choice would have been the same.

“I was a wretched Master, and you were a wretched Disciple. But let’s settle the debts we owe each other—not in this life, but some distant day when we meet again.”

Spilled water couldn’t be gathered up, and time that had passed could never be turned back.

What mattered was now. And Jeok Cheongang still had something precious to protect.

“So, Cheon-ah.”

Just as he had long ago, Jeok Cheongang gently let the name of his old Disciple leave his lips.

His eyes moved from one face to the next, taking in the features still etched vividly in his memory.

He felt the warmth and breath of someone on his back.

He felt alive—and resolved to stay that way.

“I cast you out of the sect.”

In that instant—

*Whoosh!*

A flash erupted in the dark mist.

No. It was a flame burning as bright as light—and a giant of fire, finally risen to his feet.

*Fwoooooom!*

The heat of the Flamefire Path distorted the space.

One step. Nearly a hundred yards vanished, and the monsters’ wide eyes rushed closer.

*Crunch!*

No more words or thoughts were needed.

The Fire King, Jeok Cheongang, crushed everything in front of him.

Enemies surged in from every direction, but he saw and felt everything happening around him.

With his eyes, his ears, and sometimes with a sixth sense beyond the other five.

“Grrrraah!”

A group of monsters charged at him, each with eight arms and three heads.

They looked like asuras from legend. Their many arms—impossible to tell apart as human or beast—whipped wildly, raining blows down on Jeok Cheongang’s head.

Or, more precisely, the spot where he had been.

*Crack-crack-crack!*

Their attacks cut through empty air and carved up the ground. Then a voice pierced the monsters’ ears.

Quiet, yet hot as fire—and all the colder for it.

“How many hearts do you have?”

That was the last thing they heard.

*Fwoosh—SPLAT!*

Even as their consciousness faded, the monsters didn’t know when or how they had died.

They didn’t know Jeok Cheongang had launched himself off the ground, extended his Palm Force, and slashed downward with it.

Nor that the horrific heat within it had burned not only their hearts, but every organ in their bodies.

But the four pairs of eyes watching Jeok Cheongang did know.

They had been waiting for this moment from the start, and moved together as if on cue, without a hair’s breadth of error.

*ShhhhK!*

A low, faint whistle slipped into his senses, keen as a blade and chilling enough to raise goose bumps.

Jeok Cheongang, who had just melted dozens of monsters in an instant, immediately sensed the ominous energy rushing right up to him.

He sensed that there was more than one.

But their speed—and the power they carried—exceeded anything he’d expected.

“……!”

In that slowed instant, Jeok Cheongang sensed four lines of Force closing in from his blind spots.

He twisted with all his might, moving by instinct more than reason.

*Shhk!*

Blood sprayed with a cool slicing sound.

Not the monsters’ green blood, with its foul stench and poisonous fumes, but the red blood of a living human.

Even through the sting of pain, Jeok Cheongang regained his balance at the last possible moment and landed with a satisfied smile.

What a relief.

His flesh was injured, but Jin Taekyung hadn’t so much as been scratched.

But the smile brought on by that relief didn’t last long.

His wound wasn’t serious. The battle, however, was clearly turning against him.

A Master fighting to protect his Disciple, against countless monsters charging without fear of death.

And the greatest problem of all: the four Black Ghosts, carefully measuring their distance and looking for an opening even now.

*Strong. Stronger than I expected.*

They seemed at least a full step above the other Black Ghosts he had faced—perhaps even two.

He didn’t know whether that was because of the Magic surrounding the area or because these four were particularly powerful specimens. But one thing was certain.

*This will be a tough fight.*

In truth, even that didn’t begin to describe it.

Their individual strength was formidable, but the four Supreme Peak masters moved like one organism, sharing their thoughts. Even Jeok Cheongang couldn’t afford to underestimate them.

The same would be true even if they were living humans. But these monsters felt neither emotion nor pain.

And the situation was going their way in every respect.

Even now.

“Grrrraaaah!”

The monsters roared and charged again, while the Black Ghosts vanished among them. Jeok Cheongang understood their intentions at once.

*They’re taking turns wearing me down…!*

To break a huge rock quickly, you needed a sharp chisel and a heavy hammer. But given enough time, even the occasional rain shower could do the job.

Drop by drop, the water struck the hard surface of the rock, wearing it down and making cracks.

And the monsters surging without end under the Black Ghosts’ command were neither light raindrops nor a passing shower.

They were waves.

Raging waves, bearing the force to smash through any reef—and a blind madness that made them hurl their lives away without hesitation.

But Jeok Cheongang wasn’t a rock that would simply stand still and wait to be worn down.

*I’ll finish this in one blow.*

His nature was fire. He had raised a greater flame than anyone under heaven, and so he was the Fire King.

*Crack.*

Jeok Cheongang clenched his teeth.

His eyes glowed red, piercing the dark mist. Space warped along the heat haze rising strand by strand from his entire body.

*Fwoooosh.*

An energy like molten lava surged through his limbs and every part of his body. A breath like steam escaped between his slowly parting lips.

“I’ll kill every last one of you.”

If they were rocks, he would melt them. If they were waves, he would make them evaporate.

Even if he himself turned to ash, even if everything burned away, the Fire Gate Clan’s flame would never die.

No—the blaze that rose from it would become even greater than his own.

“Come!”

The giant’s roar shook the air in every direction as he completed his preparations.

“Whoa, that scared the hell out of me. My ears are going to burst.”

“……!”

Jeok Cheongang barely managed to rein in the internal energy that had nearly turned back on him.
```
