<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1181.txt",
      "sha256": "8f2009f5f22e013703b88d4591414a9392c9c2f82ec2c92bd5a985f8f0996e9b",
      "bytes": 11661
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b69fa4422271159de0a326116ff5a0aef95fbf68e1d1bc25d5319beaa3973a32",
      "bytes": 2073
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2372eff4014bbbfe2875ceb74264c004f7f386d353a549f999d2b18a5d322a72",
      "bytes": 248683
    },
    {
      "path": "characters/Cang Gong.md",
      "sha256": "42d7a636f0dd9c74fec7941316f9d799159a3b4288725e1134066c1ea3027bdc",
      "bytes": 779
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "eca4253a967061b1f5af491797f78160e59c584efd31289483487914a23d9ff7",
      "bytes": 760
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "f9d37376c46f2575ab39267f4e8465dc1a24a5c2dce81f1bad5a830314991d2d",
      "bytes": 1666
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "9e566effba625f9229372b7584acbc4e7c8c99924847623ce32a79e9d45e1841",
      "bytes": 1550
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "aa781f32e970850283d909ba8dde2af855badda4df86e86001122fbf275ee07f",
      "bytes": 1107
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "94360aeca67de19ae045e6f14256fb5193e308b1a773aaf620834017086bd3b8",
      "bytes": 623
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "969c7823190da14c49553e3afadbac88f63c6fd7ab39da3e8e13da7f59c905cf",
      "bytes": 1084
    },
    {
      "path": "characters/Song Ho.md",
      "sha256": "6402f350d78e0e68d35f663d71e95afc86b44a7a29965364c08082f6036c875e",
      "bytes": 768
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "603e3c49f5d38d12148c65f30dba06292ea6e50bd93d8155390005ac0494757a",
      "bytes": 295700
    }
  ],
  "estimated_tokens": 10656
}
-->

# Durable State Update — Chapter 1181

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
1 and safe_through 1181. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1181. Profile updates may replace only one
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
  "chapter": 1181,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1181,
    "continuity_sources": [1181],
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
    "The government-Murim army has split into three forces at the Qinghai-Xinjiang border; it plans to rendezvous with the Imperial Army near the Tianshan Mountains.",
    "Countless monsters have roared beyond the Tianshan Mountains as the forces approach.",
    "Taekyung and his group crossed the barren region in Xinjiang, where no living things were found; the cause remains unknown.",
    "Jeok Cheongang, the Slaughter Saint, Hyuk Mujin, Cheongpung, and Ju Hwaran know Taekyung comes from the realm of immortals; he has said he is human and around twenty-eight.",
    "Great Sir has not been told Taekyung’s secret; Jeok leaves that decision to Taekyung.",
    "Bow Saint knows Taekyung’s secret and questions whether the Martial God’s letter is truly right.",
    "The Lord of Heaven has awakened and regained greater strength; the process is not complete, but the Lord of Heaven says it will be.",
    "The Grand Mage serves the Lord of Heaven and awaits a command; none has been given.",
    "The Main Quest “Rift and Collapse” failed; “The Foreordained Collapse” warns that player choices can cause irreversible consequences.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon; Jin knows he is the Martial God and a former Player.",
    "An alert reported that Alpha had awakened; what Alpha is and what its awakening means remain unknown.",
    "Bow Saint grieves for someone she respected and admired, while denying that the person is Taekyung."
  ],
  "continuity_sources": [
    1180,
    1179
  ],
  "open_questions": [
    "What command will the Lord of Heaven give the Grand Mage?",
    "What remains to be completed, and what will happen when it is completed?",
    "What is Alpha, and what does its awakening mean?",
    "What caused the barren land around Taekyung’s group in Xinjiang?",
    "Who is the person Bow Saint misses?"
  ],
  "safe_through": 1180,
  "temporary_decisions": [
    "Render 대인 as Great Sir, following the established glossary."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 매종학    | **Mae Jonghak**    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 사천당가   | **Sichuan Tang Clan**            |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장문인    | **Sect Leader**                              |
| 대주     | **Squad Leader** / **Commander**             |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 도사      | **Daoist**                                                      |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송호 | **Song Ho** | Elderly martial artist known as the Thousand-Faced Fox. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 천하제일검 | **Number One Sword Under Heaven** | Mae Jonghak's title. |
| 검귀 | **Sword Demon** | Title used for the kind of swordsman Mukyung is said to resemble. |
| 청파낙조 | **Blue Wave, Falling Bird** | Technique name coined by the Demon Bird for Jin Mukyung’s strike. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 송호 | 진태경 | senior_martial_artist_to_junior_martial_artist | you | familiar-polite | Uses 자네 while recognizing Taekyung and discussing his preliminary performance. |
| 매종학 | 송호 | savior_to_survivor | you | casual-familiar | Mae uses 자네 while speaking to Song Ho after his identity is recognized. |
| 송호 | 매종학 | rescued_survivor_to_savior | Great Hero; you | formal-deferential and familiar | Song Ho credits Mae with saving his life and addresses him as 대협. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 천면호리 | 매종학 | intelligence_chief_to_alliance_leader | Alliance Leader | formal and deferential | Requests that Mae move elsewhere with the others before he reports further. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 매종학 | 천면호리 | Alliance Leader to Hidden Shadow Pavilion Chief | Chief of the Hidden Shadow Pavilion | casual-but-commanding | Asks Song Ho's view of Taekyung's suspected target. |

## Listed compact profiles

### Cang Gong.md

# Cang Gong (창공)

- **Safe through:** Chapter 1180
- **Aliases:** None
- **Role:** Cang Gong is the Eastern Heaven Demon Lord’s assumed identity, through which he became the East Depot’s Brush-Holding Eunuch and a power second only to the Emperor.
- **Personality:** Calculating and self-assured, he is driven by vengeance and believes the rulers and the world betrayed him first.
- **Voice:** Dry and sardonic, he delivers taunts and judgments in measured statements.
- **Relationships:** He was raised by a master and fellow disciples in the Maoshan Sect, whose members died resisting the forced relocation of the capital; Ma Sanbao is his disciple, and he regards Jin Taekyung as a potential recruit.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1179
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 1180
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Supreme Peak swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and guided by a strong sense of chivalry and responsibility; losses deepen his self-reproach and resolve to grow strong enough to protect others.
- **Voice:** Quiet and resonant, clipped and blunt, with dry sarcasm in familiar exchanges.
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, who shares his own grief and encourages him to keep trying; Cheol Mubaek died protecting Mukyung and left him the Shura Annihilating Fist manual; their father—the Jin Family Head—once apologized to Mukyung for his mother’s death in childbirth.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1180
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant, he is pragmatic and fiercely defiant; he protects those he cherishes and meets mounting responsibility with hope and a determination to endure.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the revived Undead King, formerly the Skeleton King, a friend.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 1180
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; with his younger brothers, he is openly affectionate and markedly overprotective.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and he considers the Jin Family indebted to the Dongting Fisherman and the other fallen defenders of Shanxi.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1180
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 1180
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Song Ho.md

# Song Ho (송호)

- **Safe through:** Chapter 1180
- **Aliases:** Thousand-Faced Fox
- **Role:** Elderly Peak master known as the Thousand-Faced Fox, a martial artist with a prosthetic leg, and current Chief of the Hidden Shadow Pavilion, overseeing a vetted intelligence network that includes highly trained assassins.
- **Personality:** Outwardly genial and relaxed, but observant, forceful, and intimidating when pursuing information.
- **Voice:** Lightly genial and conversational, turning quietly coercive during interrogation.
- **Relationships:** He serves under Mae Jonghak's New Murim Alliance, commands the Hidden Shadow Pavilion, and recognizes Jin Taekyung as Jeok Cheongang's Disciple.

## Korean source

```text
＃1181화



아주 잠깐, 세상이 멈춘 듯했다.

경악으로 부릅떠진 눈동자와 멍하니 벌어진 입술.

그 무수한 시선의 끝에, 저 멀리 굽이진 고원의 언덕을 새카맣게 뒤덮으며 쏟아지는 재앙의 물결이 있었다.

그아아아아!

심연 깊숙한 곳으로부터 솟아오르는 듯한 울림.

모두가 산이라고 믿었던 거대한 그림자가, 그 안에 웅크린 수많은 괴물들이 포효했다.

지축을 흔들고 세찬 빗줄기를 터트리며, 하늘과 맞닿은 고원의 공기보다 더한 한기(寒氣)를 적에게 심어 주었다.

그리고 그 한기의 이름은, 공포였다.

구구구구궁!

사람들은 제자리에 얼어붙은 채 그 믿을 수 없는 광경을 바라보았다.

수만, 혹은 수십만.

감히 헤아릴 수조차 없는 아득한 숫자의 괴물들이 붉은 눈동자를 빛내며 질주한다.

어떤 것은 사람의 얼굴에 호랑이의 팔다리를 지녔고, 어떤 것은 전각(殿閣)보다 거대한 몸뚱어리에 수십 개의 얼굴을 매달고 있었으며, 심지어는 독수리의 그것임이 분명한 날개를 활짝 펴고 창공을 가로지르는 그림자도 있었다.

“……원시천존(元始天尊)이시여.”

어느 도사의 입술 사이로 흘러나온 그 넋 나간 뇌까림은 곧 모든 이의 마음을 대변하는 것이기도 했다.

찰나의 섬광으로 적의 실체를 확인한 이라면 자신도 모르게 신의 존재를 떠올릴 수밖에 없었으니.

비록 구름과 별 사이 어딘가에 있을 그 대단한 존재의 정확한 이름도, 실체도 몰랐으나 그런 사소한 이유가 무슨 상관이란 말인가.

빛이 가장 간절해지는 순간은, 칠흑 같은 어둠에 갇혀 있을 때다.

바로 지금처럼.

‘이것이었나……!’

진위경은 이를 악물었다.

폐허가 되어 버린 도시와 찾아볼 수 없던 생명의 흔적.

그가 떠올렸던 의문에 대한 모든 답이, 소름 끼치도록 선명한 현실이 되어 수백 장 밖에서 들이닥치고 있었다.

무림 연합군의 선봉, 바로 이곳을 향해서.

“송 대협.”

나직한 부름에 담긴 뜻은 명백하다. 고개를 끄덕인 천면호리 송호가 언제 품에서 꺼냈는지 모를 자그마한 원통을 힘껏 내던졌다.

퍼어엉!

사천당가(四川唐家)의 장인들이 만든 신호용 폭죽이 화려하게 폭발한다.

허공을 수놓으며 천천히 떨어져 내리는 불똥 사이로 또다시 끔찍한 괴물들의 모습이 드러났다. 

그러나 그 빛은 십 리도 넘게 떨어진 후미까지 보일 만큼 밝았고, 맹렬한 폭발음은 잠시나마 사람들의 공포를 씻어 내 주었다.

그리고 진위경은, 지금 이 순간 자신이 해야 할 일이 무엇인지 알고 있었다.

‘지원군이 올 때까지 시간을 벌어야 한다.’

제아무리 촘촘하게 짜인 그물도 시간이 흐르면 헐거워지는 법.

단숨에 천산을 무너트릴 기세로 출진한 무림 연합군이었으나, 무려 한 달간 숨 돌릴 틈 없이 계속된 진격에 사람들은 이미 지쳐 있었고 척박한 땅과 부족한 식량은 그들을 한계까지 밀어붙였다.

그에 따라 피로는 누적되고, 막힘없이 흐르는 물줄기처럼 이어지던 발걸음이 뚝뚝 끊어지기 시작한 것은 당연지사.

하필이면 연합군 내에서도 병력의 질이 떨어지는 태원진가가 잠시 선봉을 맡았을 때 이런 일이 벌어진 것은 실로 엄청난 불행이었지만, 그들을 이끄는 것이 진위경이라는 사실은 불행 중 다행이었다.

그는 비록 두 아우만큼의 무공을 지니진 못했을지언정, 모두가 인정하는 지도자였으니.

“나, 태원진가의 소가주 진위경이 그대들에게 묻겠다!”

절정의 공력이 실린 외침이 고원을 흔들고, 횃불처럼 타오르는 두 눈동자가 불길을 쏟아낸다.

“무엇이 그리 두려운가!”

본능적으로 뒷걸음치던 이들이 문득 걸음을 멈추었다.

그러나 단지 그것으로는 사무치는 모든 공포를 이겨 낼 수 없다. 진위경은 자신을 향한 시선들을 마주한 채 재차 외쳤다.

“무엇을 위해 이곳에 왔는가!”

멈춰있던 걸음이 다시 앞으로 향하고, 떨리는 손끝이 칼자루를 잡았다.

그 물음에 대한 답은 그들 모두가 알고 있다.

천하를, 대의를 위해서.

소중한 것들을 지키기 위해서, 혹은 이미 잃어버린 것에 대한 복수를 위해서.

그렇기에 그들은 한 깃발 아래 섰고, 죽음을 각오했다.

“나도, 그대들도 무인으로서 이곳에 온 것이 아니다!”

대지의 떨림이 강해진다. 그에 따라 진위경의 음성도 가파르게 뻗어나갔다.

“우리는 한 명의 인간으로 이 자리에 섰다! 누군가의 자식이자, 어버이로서 각자의 것을 지키기 위하여!”

공포를 느낀 말들이 거세게 투레질했다. 육신과 정신의 피로가 혼란하게 뒤섞인 얼굴들이 보인다.

그러나.

그럼에도.

“당당하게 맞서라! 두려움을 떨쳐낼 수 없다면, 적과 함께 베어 버려라!”

차차차차창!

마치 손목을 옥죄이던 사슬을 끊어 내듯, 그들은 각자의 무기를 뽑았다.

동시에, 어느덧 백여 장 앞까지 도달한 괴물들의 파도를 향해 겨누었다.

가팔라진 호흡을 따라 새하얗게 흘러나오는 숨결.

모래알을 한 움큼 씹은 것처럼 입안이 꺼끌거리고, 가슴은 지금 당장이라도 터져버릴 것처럼 두방망이질 친다.

하지만 이제는 그 누구도 물러서지 않았다.

끝끝내 공포를 이겨 내지 못한 말들이 주인의 손길을 벗어나 사방으로 도망쳐도.

백여 장의 거리가 순식간에 반으로, 또 그 반으로 줄어들어도.

그리고 대도시의 전각과 눈높이를 나란히 하는 거대한 괴물이, 고원 곳곳에 깊숙이 몸을 누이고 있던 천근거석을 뽑아 내던진 그때에도.

후우우웅!

일순간, 비가 그쳤다.

아니, 정확히는 허공 높이 떠오른 커다란 바위가 그들의 머리 위로 떨어져 내리던 빗물을 가로막은 것이었다.

“아……!”

누군가의 탄식이 울려 퍼진 그때, 굳게 닫혀 있던 진위경의 입술이 열렸다.

“둘째야.”

스아아악.

구름 한 점 없는 하늘보다 푸르른 빛줄기가 솟아올랐다.

그것은 고요했고, 예리했다.

빗방울도, 바람도, 공기도.

그리고 족히 수백 년의 세월을 간직한 천근의 바위마저 소리 없이 단숨에 베어 가를 만큼.

서걱!

벼락과도 같은 섬광이 번뜩였고, 그것으로 끝이었다.

청파낙조(靑波落鳥).

한 사람의 검 끝에서 넘쳐흐른 푸른 파도는, 새가 아닌 거대한 바위를 수십 조각으로 가르며 언덕 아래로 떨어트렸다.

쿠구구궁!

먼지구름도 일어나지 않을 만큼 세찬 빗줄기 속에서, 마침내 괴물들의 추격을 떨쳐내고 되돌아온 태원진가의 젊은 검귀가 작게 중얼거렸다.

“진천대주라니까.”

진위경이 희미하게 웃었다.

“조금 전에는 형님이라고 부른 것 같은데?”

“……착각입니다.”

“저런, 아무래도 내가 잘못 들은 모양이구나.”

아이 달래듯 사근사근하게 대답한 진위경이 죽립을 건넸다.

“쓰거라. 고뿔 들라.”

형의 말투에 살짝 한숨을 내쉰 진무경은 죽립을 받아 들었다.

기름먹인 죽립을 턱끈까지 질끈 동여매자 거세게 휘몰아치는 빗방울도 더는 눈 앞을 가리지 못했다.

하지만 선명해진 시야로 보이는 세상은, 어찌하여 이다지도 칠흑빛일까.

드드드득!

사방에서 흘러넘치는 어둠에 대지가 몸을 떨었다.

그 기세가 꺾이긴커녕, 거칠 것 없이 질주하는 무수한 괴물들을 직시하며 진무경은 검파를 말아쥐었다.

가라앉은 호흡과 담담한 눈빛.

지금 그에게서는 한 터럭의 두려움도 찾아볼 수 없었다.

이 전투에서 승리할 자신이 있어서가 아니다. 

단지 맞서 싸워야 하는 이유가 있기에, 또한 그 이유에 대한 믿음이 있기에 흔들리지 않는 것이다.

‘그래, 믿고 있지. 나뿐만 아니라 우리 모두가.’

진무경은 한 사람을 떠올리고 있었다.

하루아침에 모든 것이 달라진, 그리고 이내 주위의 모든 것을 뒤바꾼 자신의 아우를.

비록 그는 이 자리에 없었으나, 그렇기에 다행이었다.

눈앞을 가득 메운 괴물들의 숫자가 많으면 많을수록, 진태경에게 향할 위협의 크기 역시 줄어들 테니.

‘그 녀석만큼은, 끝까지 살아남아야 한다.’

크게 심호흡한 진무경은 단단하게 구축된 방진(防陣)을 벗어나 앞으로 걸음을 내디뎠다.

그리고 그 한 걸음이, 인간과 괴물 사이에 놓여있던 마지막 거리였다.

후우우웅!

거센 파공성과 함께 내리꽂히는 괴물의 거대한 주먹이, 그 안에 담긴 끔찍한 악취가 콧속 깊숙이 스며들었지만 상관없었다.

이 전투의 결말이 어찌 될지는 몰라도, 모든 것이 끝났을 무렵에는 지금의 악취보다 더한 피비린내가 고원 전체를 뒤덮고 있을 테니까.

스아아아.

청파(靑波).

그 이름 그대로 푸른 파도를 닮은 강기가 다시금 솟구친다. 

허공을 짓누르며 떨어져 내리던 주먹을 소리 없이 조각내며, 선두의 괴물들을 고스란히 집어삼켰다.

콰드드드득!

잘려 나간 사지와 핏물이 사방에 흩뿌려진다.

이제는 인간도, 짐승도 아니게 되어 버린 괴물들이 구슬픈 단말마와 함께 허물어졌다.

그런데 어째서일까. 

그 썩어 문드러진 육신에서 흘러나온 악취는 진무경이 앞서 느낀 그것보다 독하지 않았고, 주위를 환하게 밝히며 사방을 난도질하는 푸른 검강에는 새로운 빛이 덧씌워지고 있었다.

서서히 내려앉는 태양을 따라 온유하게 세상을 물들이는 노을처럼.

혹은, 어디서 불어왔는지 모를 바람에 몸을 맡긴 꽃잎처럼.

‘아.’

마음속에서 울려 퍼진 탄성과 함께, 진무경은 이 이질적이면서도 따스한 힘의 정체를 깨달았다.

한 줄기의 바람처럼 조용히 전장으로 스며든, 저 자줏빛 강기가 누구로부터 비롯된 것인지도.

스륵.

허공에서 흩날리는 도포 자락.

그가 언제 이곳에 나타났는지, 또 어떻게 움직였는지 그들 중 누구도 정확히 알아차리지 못했다.

심지어 진무경조차도.

다만, 괴물들의 악취마저 지워 낸 진한 매화향만이 코끝을 감돌 뿐이었다.

“다행이군. 늦지 않아서.”

일찍이 검으로 극의를 이루었기에 천하제일검(天下第一劍)이요, 이 드높은 하늘 아래 감히 비견될 자가 없어 구름 위로 떠오른 가장 밝은 별.

검성(劍星) 매종학은 깊게 가라앉은 눈빛으로 입을 열었다.

“그럼 시작해 볼까.”

그 순간.

화아아아악!

마침내 만개(滿開)하며 흩날리는 자줏빛 매화 위로, 네 명의 십왕(十王)을 필두로 한 구파일방과 오대세가의 장문인들이 유성처럼 내리꽂혔다.

콰아아아앙!

짙은 어둠과 눈부신 빛줄기가, 온 힘을 다해 서로를 물어뜯기 시작했다.
```

## Final English reading copy

```markdown
# Chapter 1181

For a brief moment, it was as if the world had stopped.

Eyes wide with shock. Lips hanging open in a daze.

At the end of countless gazes, a wave of calamity poured over the distant, winding hills of the plateau, blackening them beneath its tide.

*Graaah!*

A deep rumble, as if rising from the depths of an abyss.

The vast shadow everyone had believed to be a mountain roared—the countless monsters crouched within it.

The earth shook. Torrential rain burst from the sky. They planted a chill in their enemies even deeper than the cold air of the plateau that touched the heavens.

And the name of that chill was fear.

*Rumble, rumble, rumble!*

Frozen in place, people stared at the unbelievable sight.

Tens of thousands. Perhaps hundreds of thousands.

An unfathomable number of monsters charged forward, their eyes gleaming red.

Some had human faces and the limbs of tigers. Others had bodies larger than pavilions, with dozens of faces hanging from them. One shadow even spread wings unmistakably like an eagle’s and swept across the sky.

“…Primordial Heavenly Venerable.”

The dazed mutter that slipped from one Daoist’s lips spoke for everyone.

Anyone who’d glimpsed the enemy in that flash of lightning couldn’t help but think of the gods.

They didn’t know the exact name or form of that mighty being who must exist somewhere among the clouds and stars. What did such a trivial detail matter?

The moment you long for light most desperately is when you’re trapped in pitch darkness.

Just like now.

*So this was it…!*

Jin Wikyung gritted his teeth.

The ruined city. The absence of any trace of life.

The answers to every question he’d asked came rushing toward them, hundreds of zhang away, so clear and horrifying that they became reality.

Straight toward the Murim allied forces’ vanguard. Straight toward where they stood.

“Great Hero Song.”

The meaning in the quiet call was clear. Song Ho, the Thousand-Faced Fox, nodded and hurled a small cylinder with all his might. No one knew when he’d taken it from inside his robes.

*Boom!*

A signal firework made by the artisans of the Sichuan Tang Clan burst in a dazzling explosion.

Through the sparks drifting slowly down and painting the sky, the hideous monsters appeared once more.

Yet the light was bright enough to reach the rear of the army, more than ten li away, and the fierce blast briefly washed away the people’s fear.

Jin Wikyung knew what he had to do now.

*We have to buy time until reinforcements arrive.*

Even the tightest net loosens as time goes by.

The Murim allied forces had set out with enough momentum to bring down Tianshan in a single stroke. But after a month of nonstop advance with no chance to catch their breath, the people were already exhausted. The barren land and lack of food had pushed them to their limits.

Their fatigue had naturally piled up, and their march—once as steady as an unobstructed river—had begun to falter.

It was a terrible stroke of misfortune that this happened when the Jin Family of Taiyuan, one of the weaker forces in the alliance, had taken the vanguard for a short time. But the fact that Jin Wikyung was leading them was one small piece of good fortune amid the bad.

Though his martial arts weren’t on the same level as his two younger brothers’, he was a leader everyone acknowledged.

“I, Jin Wikyung, Lesser Family Head of the Jin Family of Taiyuan, ask you this!”

His shout, infused with Peak internal energy, shook the plateau. His blazing eyes poured fire.

“What are you so afraid of!”

The people who’d instinctively started to retreat stopped in their tracks.

But that alone wouldn’t overcome all the fear gripping them. Facing the gazes turned toward him, Jin Wikyung shouted again.

“What did you come here for!”

The halted feet began moving forward again. Trembling fingers closed around sword hilts.

They all knew the answer.

For the world. For the greater cause.

To protect what they held dear, or to avenge what they’d already lost.

That was why they’d stood beneath one banner and prepared to face death.

“Neither I nor any of you came here as martial artists!”

The ground trembled harder. Jin Wikyung’s voice rang out with rising force.

“We stand here as human beings! As someone’s children, as someone’s parents, here to protect what’s ours!”

The frightened horses snorted fiercely. Faces muddled by exhaustion of body and mind came into view.

And yet—

Even so—

“Face them with your heads held high! If you can’t cast off your fear, then cut it down along with the enemy!”

*Clang, clang, clang!*

As if breaking chains that had bound their wrists, they drew their weapons.

Together, they pointed them toward the wave of monsters, now less than a hundred zhang away.

Their breath came fast, white puffs spilling from their mouths.

Their mouths felt gritty, as if they’d chewed a handful of sand. Their hearts hammered as though they might burst at any moment.

But now, not a single person retreated.

Even as the horses that couldn’t overcome their fear broke free of their masters and bolted in every direction.

Even as the hundred zhang between them shrank by half, then half again.

Even when a giant monster, its height level with the pavilions of a great city, uprooted a massive boulder that had lain deep in the plateau and hurled it at them.

*Whoooosh!*

For an instant, the rain stopped.

No—in truth, a great boulder high in the air had blocked the rain falling over their heads.

“Ah…!”

As someone let out a cry, Jin Wikyung’s tightly closed lips parted.

“Little brother.”

*Shing!*

A ray of blue, bluer than a cloudless sky, shot upward.

It was quiet, and it was sharp.

Raindrops, wind, air—

Even a boulder weighing a thousand geun, holding centuries of history, was cut through in an instant without a sound.

*Slice!*

A flash like lightning blazed—and that was all.

**Blue Wave, Falling Bird.**

The blue wave that overflowed from one man’s sword split the enormous boulder—not a bird—into dozens of pieces and sent them tumbling down the hill.

*Rumble!*

Through the torrential rain, too heavy for even a cloud of dust to rise, the young Sword Demon of the Jin Family of Taiyuan had finally shaken off the monsters’ pursuit and returned. He muttered under his breath,

“I told you I’m the Commander of the Heaven Shaking Squad.”

Jin Wikyung smiled faintly.

“I thought you called me ‘hyungnim’ a moment ago.”

“…You must have imagined it.”

“Oh dear. I must have misheard.”

Jin Wikyung answered gently, as if soothing a child, and handed him a bamboo hat.

“Put it on. You’ll catch a cold.”

With a small sigh at his older brother’s tone, Jin Mukyung accepted the hat.

He tied the chin strap of the oil-treated bamboo hat tight. The fierce raindrops no longer obscured his vision.

But why did the world look so pitch-black now that he could see it clearly?

*Rumble!*

The earth shuddered beneath the darkness pouring in from every direction.

The monsters’ momentum hadn’t diminished. Staring at the countless creatures charging ahead without hesitation, Jin Mukyung tightened his grip on his sword hilt.

His breathing was steady, his gaze composed.

There wasn’t a trace of fear in him.

Not because he was confident he’d win this battle.

He simply had a reason to fight—and believed in that reason. That was why he didn’t waver.

*That’s right. I believe in him. And so does everyone else.*

Jin Mukyung thought of one person.

His younger brother, whose whole life had changed overnight—and who had then changed everything around him.

He wasn’t here, but that was a good thing.

The more monsters filled the view before them, the smaller the threat to Jin Taekyung would be.

*That guy, at least, has to survive to the end.*

Jin Mukyung took a deep breath, stepped out of the tightly formed defensive formation, and walked forward.

That single step was the last distance between humans and monsters.

*Whoooosh!*

A monster’s enormous fist plunged down with a fierce burst of air. Its horrible stench seeped deep into his nose, but he didn’t care.

Whatever the outcome of this battle, by the time it was over, the stench of blood would blanket the entire plateau—worse than anything he smelled now.

*Shhhhh.*

Blue Wave.

True to its name, a blue wave of Force surged up once again.

It silently carved apart the fist bearing down on them, swallowing the monsters at the front whole.

*Crunch!*

Severed limbs and blood sprayed in every direction.

The monsters, no longer human or beast, collapsed with mournful final cries.

But why?

The stench rising from their rotting bodies wasn’t as foul as the one Jin Mukyung had smelled before. And a new light was layered over the blue Sword Force that blazed through the surroundings, illuminating and tearing through everything in its path.

Like the sunset, gently coloring the world as the sun slowly sank.

Or like a flower petal surrendering itself to a breeze from nowhere.

*Ah.*

With a cry echoing in his heart, Jin Mukyung understood what this strange yet warm power was.

He also understood who had given rise to that purple Force, which had slipped quietly onto the battlefield like a passing breeze.

*Swish.*

The hem of a robe fluttered in midair.

No one had noticed exactly when he appeared, or how he’d moved.

Not even Jin Mukyung.

All that remained was the rich scent of plum blossoms, lingering at the tip of his nose and erasing even the monsters’ stench.

“Good. I’m not too late.”

Having reached the pinnacle of the sword long ago, he was the Number One Sword Under Heaven. With no one beneath this vast sky who could compare to him, he was the brightest star above the clouds.

The Sword Saint, Mae Jonghak, spoke, his eyes sinking deep.

“Then let’s begin.”

At that moment—

*Fwoosh!*

Above the purple plum blossoms that finally bloomed and scattered, the leaders of the Nine Sects and One Gang and the heads of the Five Great Families plunged down like meteors, led by four of the Ten Kings.

*Boom!*

Deep darkness and dazzling beams of light began tearing into each other with all their might.
```
