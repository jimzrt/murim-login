<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0688.txt",
      "sha256": "02b4078dfe75470a2e8e67c8bd563a0902c6f0447f820e332616d0bf801ea44e",
      "bytes": 18615
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "fbcd881ebca978797cc4e98fb9914a31be59b3d8f6ec1927d82da6181af79994",
      "bytes": 1729
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e481f1cea90304b302933f2feb072cdb2d3bbbe05c29d0e57751ca82290a67ac",
      "bytes": 204260
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "7d3de20fda7407c4c24af9e79ba7b99f5d7cb22535bccfebc6ec2e1ab8ed7124",
      "bytes": 980
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "b404c0bd05b0360f9067f8080445c1c88b84cbff70198a928fff0326ede65d6b",
      "bytes": 769
    },
    {
      "path": "characters/Black Hand.md",
      "sha256": "a47405363377e87a8296e49c737fb1556f6723ca1c6d7a8a50694d8e5b2dedae",
      "bytes": 788
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "dd4e556e288055d8dcd53f3dee971e56909b9376891613b4087cecd215ec3c8e",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "b321ab29976836bf0078d072788e3c3aeccbf70cda16ffbf26c5862880e5350d",
      "bytes": 1883
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "e52d1a04be06aeb67f7906653092de22776e719ca9e88da534d2cf04edfa8845",
      "bytes": 622
    },
    {
      "path": "characters/Yayul Cheok.md",
      "sha256": "1a7e96b6a4982927405674c06d1cd07342f40522a33edf61bf8fadb3987d225b",
      "bytes": 902
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c732c6e0b915fb40ebc0712e4137a1d00d0de261ab8f5e3a98f70aa047ca1d3f",
      "bytes": 211718
    }
  ],
  "estimated_tokens": 14433
}
-->

# Durable State Update — Chapter 688

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 688. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 688. Profile updates may replace only one
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
  "chapter": 688,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 688,
    "continuity_sources": [688],
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
    "Heugung is secretly the Beast Miao King and can transform between their identities through the Bone-Shrinking Technique at Great Completion.",
    "The Beast Miao King was never sealed and had been monitoring Yohi and Baeksang as a hidden contingency of the Southern Heaven Demon Empress.",
    "Heugung has taken control of the unconscious Jin Taekyung after Jin defeated the two Supreme Peak masters, while the exhausted White Tiger remains alive.",
    "Heugung has incapacitated Yohi with a sinister substance or energy after revealing his identity and withholding the genuine antidote.",
    "Heugung plans to bring Jin and Yohi to the Inner Palace and fabricate a story that Jin and the Murim Alliance plotted to invade and destroy Nanman.",
    "Heugung threatens to slaughter more than five thousand Yao people at Boshan and reduce Nanman's four great tribes to three to force Yohi's compliance.",
    "A blade-like wind attacks Heugung as he tries to lift Jin, and the outcome is unresolved."
  ],
  "continuity_sources": [
    687
  ],
  "open_questions": [
    "What created the blade-like wind, and did the attack injure or stop Heugung?",
    "Will Yohi and Jin remain under Heugung's control after the attack?",
    "Will Yohi submit to Heugung's fabricated account to save the Yao people at Boshan?",
    "Can Heugung still carry out the plan to mobilize Nanman against the Central Plains?"
  ],
  "safe_through": 687,
  "temporary_decisions": [
    "Render 궁주 as Palace Lord.",
    "Render 수마 as sleep demon.",
    "Render 사대 부족 as four great tribes.",
    "Render 삼대 부족 as three great tribes.",
    "Render 적자 as legitimate son."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 열화문    | **Fire Gate Clan**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 중원     | **Central Plains**                               |                                                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 일격     | **One Strike**                         |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 흑수 | **Black Hand** | Sadistic Dark Heaven agent and Supreme Peak master. |
| 흑수권마 | **Black Hand Fist Demon** | Sobriquet revealed by Black Hand. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 야율척 | **Yayul Cheok** | Beast Miao King and lord of the Nanman Beast Palace. |
| 평화 | **Peace Guild** | Guild name. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 석가 | **Shakyamuni** | Buddhist figure invoked by Hong Dao in his earlier conversation with Jeok Cheongang. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 호위장 | **Captain of the Guards** | The Sichuan City Lord's guard captain. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 오독문 | **Five Poisons Sect** | Formerly dominant Nanman faction destroyed by the Fire Gate Clan. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 독무 | **Poison Mist** | Deep green mist covering the Poisonblood Grounds swamp. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 수왕석 | **Beast King Stone** | Legendary sacred treasure of the Nanman Beast Palace. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 궁주전 | **Palace Lord's Hall** | The residence and hall of the Nanman Beast Palace's Palace Lord. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 시비 | 진태경 | household_servant_to_visiting_young_hero | Young Hero Jin | formal-polite | The maid summons Taekyung to meet the Family Head. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 야율척 | 진태경 | Nanman_Beast_Palace_Palace_Lord_to_Jeok_Cheongang's_Disciple | you / Disciple of Old Master Jeok / Jin Taekyung | rough, testing, and later welcoming | Yayul Cheok questions Taekyung as a suspected culprit, strikes him as a test, and then welcomes him after recognizing Jeok's Disciple. |
| 진태경 | 야율척 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Palace_Lord | Great Hero Yayul Cheok | formal and deferential | Taekyung gives Yayul Cheok a formal greeting as the nineteenth successor of the Fire Gate Clan. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |
| 남천마후 | 백상 | Dark Heaven controller to coerced Nanman leader | Great Chieftain Baeksang / Palace Lord | playful, taunting, and threatening | She repeatedly addresses Baeksang while mocking his grief, acknowledging his effort, and issuing her order. |
| 진태경 | 부족장 | captor to captured tribal chieftain | tribal chieftain | casual, coercive, and mocking | Jin promises to spare the captured chieftain if he answers questions properly. |
| 부족장 | 진태경 | captured tribal chieftain to overpowering enemy | Jin Taekyung | alarmed and desperate | The chieftain recognizes Jin by name while fleeing and then begs for his life. |
| 진태경 | 흑수 | hostile_martial_opponent | Black Hand | mocking and profane | Jin sarcastically addresses Black Hand after hearing his sobriquet. |
| 흑수 | 진태경 | hostile_Dark_Heaven_agent_to_enemy_martial_artist | Blazing Flame Divine Dragon Jin Taekyung | taunting and murderous | Black Hand identifies Jin while claiming that killing him will make the sobriquet famous. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 687
- **Aliases:** None
- **Role:** Baeksang is the temporary Palace Lord of the Nanman Beast Palace, an over-seventy Great Chieftain of the Bai people, and the leader of Nanman's general mobilization, with nearly ten thousand troops stationed in the Inner Palace.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with enduring grief over Hwi's death and a guarded but still powerful bond with his sworn elder brother that now leaves him visibly conflicted.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of deceased Baekhwi, whom the Great Snow Fiend killed; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 687
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace and a Supreme Peak master who secretly lived for decades under Heugung's identity through the Bone-Shrinking Technique.
- **Personality:** The Beast Miao King is calculating, patient, ruthless, and willing to endanger Nanman's people to advance Dark Heaven's grand plan.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He maintained his public bond with Baeksang while secretly monitoring Baeksang and Yohi for the Southern Heaven Demon Empress, and he now controls the Nanman Beast Palace through the Heugung identity.

### Black Hand.md

# Black Hand (흑수)

- **Safe through:** Chapter 686
- **Aliases:** Black Hand Fist Demon (흑수권마)
- **Role:** Black Hand was a sadistic Dark Heaven agent and Supreme Peak master who acted under orders associated with the Southern Heaven Demon Empress before his death.
- **Personality:** Black Hand is cruel, gleeful, predatory, and fascinated by the despair of his victims.
- **Voice:** Black Hand speaks in archaic first person with drunken mockery, humiliating insults, and casual threats.
- **Relationships:** Black Hand was the captor and torturer of Yohi and Heugung and an enemy of Jin Taekyung; the Great Snow Fiend was his senior and could overrule him under the Southern Heaven Demon Empress's orders.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 687
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 687
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner who is currently unconscious under the disguised Beast Miao King's control.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 687
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Yayul Cheok.md

# Yayul Cheok (야율척)

- **Safe through:** Chapter 673
- **Aliases:** Beast Miao King
- **Role:** Yayul Cheok is the over-eighty Beast Miao King, lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and great chieftain of the Miao people.
- **Personality:** Boisterous, warmhearted, forthright, playful, and politically conscious of the tribal coalition he leads.
- **Voice:** Rough, loud, convivial, and teasing, becoming authoritative when discussing Nanman's laws or political decisions.
- **Relationships:** Jeok Cheongang is an old acquaintance whom he respects; Baeksang is his sworn younger brother and childhood companion, and they fought together during the Great Faction War; Yayul Mok serves as his Young Palace Lord; Jin Taekyung is Jeok's Disciple whom he welcomes into the Nanman Beast Palace.

## Korean source

```text
＃688화



백상은 홀로 면경(面鏡)을 들여다보고 있었다.

남천마후가 선물한 그것은 보통의 면경과는 달리 전신을 비출 만큼 컸고, 표면은 흠집 하나 없이 매끈했다.

남만은 물론 중원에서도 쉽게 찾아보기 힘든 최상품.

하지만 백상이 면경을 바라보는 이유는 오직 한 가지. 그 안에서 자신을 쏙 빼닮은 아들의 얼굴을 발견할 수 있었기 때문이었다.

‘지금껏 이런 적은 없었는데.’

장장 사십여 년이다. 수도 없이 흔들리는 자신을 다잡으며 이 자리까지 왔는데…… 지금 그의 마음은 그 어느 때보다 동요하고 있었다.

‘그만큼 끝에 다다랐다는 거겠지. 수십 년의 세월을 버텨 온 이 대계가.’

백상이 마음속으로 뇌까리던 그때, 그의 등 뒤에서 문이 열림과 동시에 익숙한 얼굴이 모습을 드러냈다.

면경에 비친 호위장과 눈이 마주친 백상이 입을 열었다.

“모셔 왔나?”

사색에 잠겨 있던 주군의 뒷모습에, 순간 멈칫하던 호위장이 대답했다.

“오고 계십니다.”

“그럼 무슨 일로?”

“급보(急報)가 들어왔습니다.”

“급보라…….”

말꼬리를 흐린 백상이 손을 까딱였다. 손짓의 의미를 깨닫고 가까이 다가온 호위장이 낮은 목소리로 속삭였다.

“간밤에 삼백 리 밖 북쪽에서 거대한 화마가 확인되었습니다.”

“애뇌산이군.”

“예.”

“불을 지른 자는 진태경일 테고.”

“추가 확인을 해 봐야겠지만, 지금까지의 상황을 고려하면 그가 유력합니다.”

“진태경이 맞을 것이다. 또다시 공적에 눈이 먼 부나방들이 달려든 모양이군.”

“애뇌산 인근의 중소 부족들이 힘을 합쳤다고 합니다. 전사 오백에 맹수 일백을 거느리고 그를 습격했지만…….”

백상은 손을 내저어 호위장의 말을 막았다. 더 이상 들을 필요도 없는 이야기였다.

진태경은 급하게 끌어모은 어중이떠중이 오백으로 어찌할 수 있는 존재가 아니니까.

중과부적(衆寡不敵)이라는 네 글자도 상대가 누구냐에 따라 달라진다. 진태경은 명백히 논외에 속했다.

“결과는 이미 짐작하고 있으니 그것으로 되었다. 진태경은 그 후 어찌 되었지?”

“전사들을 패퇴시킨 뒤, 홀로 애뇌산으로 향했다 합니다.”

“분명 목적이 있을 터. 혹 독혈지(毒血地)인가?”

“불길이 워낙 거센 탓에 거기까지는 확인하지 못했다고 합니다. 초입부터 시작된 불길이 벌써 중턱까지 번졌습니다.”

“놈이 작정을 한 모양이군.”

애뇌산은 남만에서도 손꼽히는 절산(折算)이다.

험악한 산세와 깊은 계곡. 굽이굽이 늘어진 산줄기는 백 리나 뻗쳐 있으며 나이를 알 수 없는 거목으로 끝없이 뒤덮여 있다.

그런 애뇌산에 화마가 내려앉았으니, 아무리 빨라도 사흘 밤낮은 지나야 불길이 사그라들 기미가 보일 것이다.

‘어쩌면…… 산 전체가 전소(全燒)되어 버릴지도 모르지.’

우연이라면 기막힌 우연이다. 애뇌산에 화마가 침범한 것은 장장 이백여 년 만이었고, 당시 산 전체를 장작 삼아 오독문을 멸문시켰던 이 또한 열화문의 인물이었으니.

‘남만은 그렇게 평화를 되찾았지.’

하지만 과연 이번에도 그럴까.

면경 속 자신의 얼굴을 말없이 응시하던 백상이 무겁게 입을 열었다.

“인근에 거주 중인 모든 부족민을 대피시키고, 쓸 만한 전사 삼천을 선별하여 애뇌산을 봉쇄해라.”

묵묵히 보고를 이어 가던 호위장의 얼굴에 동요가 스쳤다.

“남만 전역에 총동원령을 내린 상황에, 그것도 삼천 명씩이나 말입니까?”

“만일을 대비해서라도 놈의 발을 묶어야 한다.”

“하오나 주군, 그 병력으로도 애뇌산 전체를 포위하는 것은…….”

“애뇌산은 광활한 면적과는 달리 드나들 수 있는 입구가 적다. 감안하여 배치해라.”

잠시 생각하던 호위장이 고개를 숙였다.

“존명.”

“다른 부족장들의 동태는?”

“보고드렸다시피 부족장 다섯 명이 사라졌습니다. 앞서 척후대로 출발한 두 부족장 휘하의 전사들도 마찬가지입니다.”

“결국 이렇게 되는군. 현실을 인정하지 않겠다는 거겠지.”

백상은 담담하게 중얼거렸다.

사라진 부족장들은 끝까지 말을 갈아타지 않은 이들이다.

야수묘왕을 향한 그들의 충성심은 굳건했고, 그중 몇몇은 회유하는 백상을 비웃으며 침을 뱉기까지 했다.

“주군, 놈들이 배반한 것이 틀림없습니다. 아직 늦지 않았으니 지금이라도 추격대를 보내심이…….”

호위장의 권유에 백상은 고개를 내저었다.

“얼마 전 누가 내게 그러더군. 병든 나무가 있다 하여 숲이 병든 것은 아니라고. 그중 일부만 솎아 내면 그만이라고.”

“그 말씀은…….”

“지난 수백여 년간, 이 땅에는 서른두 개의 부족이 공존해 왔지. 하지만 나는 종종 어떤 의문에 사로잡히고는 했다. 언제까지 이 형태를 유지해야 하는지에 대한 의문이.”

“……!”

자신의 말뜻을 알아차리고 눈을 크게 뜬 호위장을 향해, 백상이 깊게 가라앉은 목소리로 말을 이었다.

“서른둘이라는 숫자는 합심하여 뜻을 모으기에 너무 많았다. 지금부터는 병든 나무는 솎아 내고 숲을 정리해야 할 시간이다.”

축출. 혹은 제거.

긴 시간 이 땅을 통치해 왔던 왕을 몰아내고, 새로이 왕좌에 오른 권력자의 뜻은 명백했다.

입을 벌린 채 자신의 주군을 바라보던 호위장이 무거운 목소리로 입을 열었다.

“어찌하면 되겠습니까?”

“떠난다면 내버려 두어라. 그들이 본거지로 돌아가 전사들을 규합한다면, 우리는 명분과 힘을 동시에 갖추게 된다.”

호위장 역시 알고 있었다. 이미 힘의 저울추는 오래전에 기울었다는 것을.

그러나 그가 우려되는 것은 한 사람의 존재였다.

“만약 궁주(宮主). 아니, 야율척이 그들과 합류한다면 쉽게 흘러가지 않을 겁니다.”

호위장을 가만히 응시하던 백상이 문득 입을 열었다.

“오래전 중원에 머무를 때 재미있는 이야기를 들었지.”

“주군?”

“돌에서 태어난 어느 원숭이의 이야기였다. 그 성정과 힘이 어찌나 폭급하고 강했던지, 중원의 승려들이 떠받드는 석가여래(釋迦如來)가 나서서 그에게 내기를 제안했다고 하더군. 자신의 손바닥을 벗어날 수 있겠느냐고.”

담담한 목소리가 호위장의 귓가를 파고들었다.

“원숭이는 코웃음을 치며 수락했고, 구름을 타고 날아가 세상의 끝에 놓인 기둥 다섯 개에 낙서까지 적었다. 그리고 다시 돌아왔을 때, 자신이 보았던 그 기둥들이 석가여래의 손가락이었다는 것을 알게 되었지.”

백상은 면경을 향해 천천히 손을 펼쳤다.

거대한 궁주전이 그의 손바닥 안에 들어온 듯했다. 하늘과 강. 땅과 산. 설령 남만 전체를 비춘다 해도 그럴 터였다.

“야율척. 그자도 마찬가지다. 내가 이 자리에 오른 이상, 그는 결코 벗어나지 못해.”

“그 말씀은…….”

“그가 동쪽으로 향했다는 정보가 있다. 네가 직접 백족 전사 일천을 이끌고 야율척을 쫓아라.”

“존명.”

그 순간, 목례를 취한 호위장이 입술을 달싹였다.

- 송구하오나 상대는 야수묘왕입니다. 만일을 대비하여 백천대(白天隊)를 쓰심이.

하지만 백상은 말없이 고개를 가로저었다. 백천대는 그가 지난 수십여 년간 비밀리에 갈아 온 검이다. 가장 필요할 때 뽑아 휘둘러야 한다.

“지시는 여기까지다. 귀빈이 오셨으니 이만 물러가거라.”

호위장을 향한 말이었지만, 처음부터 줄곧 면경을 바라보던 그의 시선은 어느새 열린 문 앞에 서 있는 한 노인을 향하고 있었다.

“그럼 이만.”

호위장이 궁주전을 벗어나는 것을 확인한 백상이 천천히 돌아섰다.

“오셨소, 대장로.”

무덤덤하게 건넨 인사. 그러나 돌아온 것은 날카로운 한마디였다.

“그 더러운 주둥이 닥치지 못할까.”

쿵.

얼굴에 검버섯이 가득하고, 드러난 모든 살이 주름으로 가득한 노인이 지팡이를 짚으며 다가왔다.

진물이 흐르는 눈가에는 숨기지 못한 분노의 빛이 일렁이고 있었다.

“천하의 몹쓸 놈 같으니.”

“보아하니 대화를 엿들으신 모양이구려.”

“노부가 네놈의 시커먼 속내를 모를까. 들으라고 한 소리가 아니더냐?”

“대회의의 뜻을 거스르면서까지 흉수를 구하고, 남만야수궁을 배반한 흉수 야율척에 관해서라면. 맞소.”

“이놈!”

휘익! 탁.

노인이 온 힘을 다해 휘두른 지팡이가 백상의 손에 붙잡혔다.

이렇다 할 힘도, 공력도 느껴지지 않는 일격. 가볍게 지팡이를 빼앗은 백상이 가볍게 소매를 흔들자, 보이지 않는 기운이 노구(老軀)를 자리에 앉혔다.

“못 본 사이 많이 늙으셨소. 불같은 성미는 여전하신 것 같지만.”

노인이 몸을 파르르 떨었다.

“네놈이 이런 짓을 벌일 줄 알았다면, 진즉 이 손으로 때려죽였을 것이다.”

“하지만 그러기에는 너무도 많은 시간이 흘렀지. 야율척은 궁을 배신하고 도주했고, 묘족의 존망은 먼 옛날 과실주를 훔쳐먹다 걸려 당신에게 호된 꾸중을 듣던 한 어린아이에게 달렸소.”

“……!”

“이제는 케케묵은 과거를 뒤로하고 앞날을 생각해야 할 때요. 부족장과 소족장이 사라진 지금, 묘족의 대족장이 어떤 선택을 하느냐에 따라 모든 것이 달렸지.”

말없이 백상을 노려보던 노인, 묘족의 대장로가 무겁게 입술을 뗐다.

“기어코 남만을 손에 넣었구나. 그 추악한 탐욕으로.”

“뭐라 욕해도 상관없소. 간절히 원하는 것을 이루기 위해서는 못할 것이 없으니까.”

“넌 이제 남만야수궁의 궁주다. 무엇을 더 바라느냐? 수왕석(嘼王石)이라도 얻어 신이 되고자 하느냐?”

백상은 고개를 저었다.

“입으로만 전해지는 옛 신물 따위에는 관심 없소. 지금 내가 원하는 것은 앞으로의 일과, 대장로 당신의 현명한 선택이오.”

“노부가 기억하는 넌 이런 아이가 아니었다.”

“변했소. 다른 모든 것이 그렇듯이.”

“궁주는 널 믿었어. 노부가 그토록 경계하라 했음에도 하나뿐인 의형제를 믿었지.”

“모든 믿음에 보답할 필요는 없소.”

“아직 늦지 않았다. 지금이라도…….”

“나는 이미 오래전 강을 건넜소. 기호지세(騎虎之勢). 이제 대장로께서 호랑이의 등에 올라탈 차례요.”

으득.

한껏 힘이 들어간 주름진 주먹에서 뼈 어긋나는 소리가 들렸다.

“결국 노부더러…… 궁주를 배반하라는 뜻이냐?”

“그럴 리가.”

백상은 찻잔을 들며 말을 이었다.

“대장로를 비롯한 묘족 모두가 그를 배반하길 바라오.”

“……!”

“흐름을 잘 읽어야 할 거요. 일만이 넘는 동족들을 구하고 싶다면.”

“네 이놈!”

“명심하시오. 이건 처음이자 마지막 제안이라는 것을.”

백상은 찻잔을 기울였고, 대장로는 질끈 눈을 감았다.

그리고 잠시 후, 그의 입술 사이로 흘러나온 쉰 목소리가 짧은 적막을 깨트렸다.

“불가(不可).”

탁.

찻잔을 내려놓은 백상이 깊게 가라앉은 눈빛으로 대장로를 응시했다.

“그 대답, 후회하지 않겠소?”

“차라리 날 죽여라. 묘족 누구에게 물어도 답은 같을 것이다.”

“기대를 저버리지 않는군.”

짧게 대답한 백상이 손가락을 튕겼다.

닫혀 있던 문이 열리고 모습을 드러낸 백족 전사들에게, 그가 명령했다.

“뇌옥에 가두어라. 대장로를 비롯한 묘족의 수뇌부 모두.”

목례를 취한 백족 전사들이 대장로를 좌우에서 붙들고 일으켰다.

죽을 날이 다가온 노인이 카랑카랑한 목소리로 외쳤다.

“백상! 네 이놈! 하늘이 두렵지 않으냐!”

비명과도 같은 외침이 서서히 멀어질 때쯤, 백상은 빈 찻잔을 내려다보며 뇌까렸다.

“더 이상 무엇이 두렵겠소. 나를 이곳까지 이끈 것 역시 하늘의 뜻일진대.”

분명 하늘을 원망하던 때도 있었다.

정마대전이 막을 내린 뒤, 남만으로 돌아온 백상은 매일같이 취해 있었다.

오늘이 마지막인 사람처럼 술을 들이켰고, 다음 날 잠을 깨우는 햇살에 절망했다.



‘도대체 왜 나를 살린 거요. 왜!’



죽음보다 고통스러웠던 나날들.

그러나 언제까지 슬픔에 몸부림칠 수는 없었다. 그에게는 해야 할 일이 있었으니까.

반드시 해야 할 일이.

백상은 창밖 너머, 푸른 하늘을 바라보며 마음속으로 중얼거렸다.

‘정녕 이것이 당신의 뜻이오? 아니, 단 한 번이라도 나를 지켜본 적은 있소?’

그리고 언제나처럼, 하염없이 기다려도 대답은 돌아오지 않았다.

다음 순간, 백상의 귓가를 파고든 누군가의 낯선 목소리를 제외한다면.

“저어, 차를 채워 드릴까요?”

백상은 목소리가 들려온 방향을 따라 고개를 돌렸다.

반쯤 열린 문 앞, 예쁘장한 용모의 시비가 서서 그를 바라보고 있었다.

“필요 없다.”

“하지만 잔이 비었는걸요?”

“필요 없다고 하지 않았…….”

문득 흐려지는 말꼬리. 잠시 시비를 응시하던 백상이 입을 열었다.

“들어오너라.”

가라앉은 한 마디에 시비를 제지하려던 전사들이 물러나고, 문이 굳게 닫혔다.

종종걸음으로 백상의 앞까지 다가온 시비는 손에 들고 있던 찻주전자를 천천히 기울였다.

쪼르륵.

모락모락 솟아오르는 김과 함께 퍼져나가는 다향(茶香).

하지만 어째서일까, 독무를 들이킨 것처럼 욱신거리는 이 느낌은.

차오르는 찻잔을 말없이 지켜보던 백상이 불쑥 입을 열었다.

“그건 누구의 얼굴입니까, 마후(魔后).”

시비. 아니, 남천마후가 싱긋 웃으며 대답했다.

“내궁에서 일하던 어떤 아이. 아직 파릇파릇한 게 참 귀엽더라고. 참을 수 없을 정도로.”

“죽였습니까?”

“어머. 그게 그렇게 중요해?”

“그건…….”

“재미있네. 이미 수백 명이 죽었는데 고작 시비 하나의 목숨에 신경 쓴다는 게.”

침묵하던 백상이 담담한 목소리로 대답했다.

“만약 계획에 차질이 생길까 싶어서 여쭈었을 뿐입니다. 내궁에서 벌어지는 일은 금세 발각되니까요.”

“아하. 뭐, 정 그렇다면야.”

새치름하게 웃은 남천마후가 찻잔을 집어 들었다.

“당신이 걱정하는 일은 일어나지 않아. 만약 문제가 생겼다면 그건 내궁이 아니라 애뇌산에서겠지.”

“애뇌산이라면, 혹시?”

“그래, 진태경. 그 아이가 일을 저질렀어. 지금까지 연락이 닿지 않는 걸 보면 확실해.”

잠시 생각하던 백상이 입을 열었다.

“덫이었습니까?”

“맞아. 궁을 빠져나간 늙은 호랑이를 잡기 위해 놓은 덫이었지. 젊은 호랑이가 대신 걸려들 줄은 몰랐지만.”

딸칵.

찻잔을 내려놓은 남천마후가 웃음기 어린 목소리로 말을 이었다.

“물론, 그 젊은 호랑이가 덫을 부술 수 있을 만큼 강하다는 것도 몰랐고.”

“마후께서 자신할 만큼 철저한 덫이었나 보군요.”

“초절정 고수 둘. 그중 하나는 흑수권마고, 다른 하나는…….”

말을 멈춘 남천마후가 백상을 바라보며 빙긋 웃었다.

“어쨌든 강했어. 그것도 흑수권마보다 월등하게.”

“……!”

“놀라운 일이야. 그 두 사람이라면 야수묘왕도 처리할 수 있을 거라 생각했거든. 천주(天主)께서 괜히 그 아이에게 관심을 보이신 게 아니었던 거지.”

듣고 있는 백상으로서는 놀라움의 연속이었다.

초절정 고수 둘을 단신으로 처치한 것으로도 모자라, 바로 그 천주마저 진태경에게 관심을 보인다니.

동시에 자신의 판단이 틀리지 않았다는 것 역시 깨달았다.

‘진태경.’

도무지 종잡을 수 없는 한 청년의 얼굴이 눈앞을 스친다.

백상은 자신을 향해 웃고 있는 남천마후를 바라보며 입을 열었다.

“지금부터는 마후께서 직접 움직이시겠군요.”

초절정 고수는 강력한 전력이다. 백상은 그런 이들이 둘이나 죽었으니, 이제 남천마후가 나서는 것은 불가피하다고 생각했다.

적어도 다음 순간 들려온 그녀의 대답을 듣기 전까지는.

“아니? 내가 왜?”

피식 실소를 흘린 남천마후가 말을 이었다.

“신경 쓸 시간도 없어. 대마(大馬)가 죽었다 해도 지금의 형세는 뒤집히지 않으니까. 중요한 건 대계지.”

“그 말씀은 혹시?”

“이제 야수묘왕과 진태경은 상관없어. 내궁과 외궁의 방비를 철저히 해. 그리고 모든 병력을 끌어모아.”

자리에서 일어난 남천마후가 마치 춤추듯 걸음을 옮겼다.

환희와 즐거움이 가득한 목소리가 백상의 귓가를 파고들었다.

“사흘. 늦어도 사흘 뒤야.”

“……!”

“준비해. 그날, 모든 게 시작되고 끝날 테니.”

쿵.

문이 열리고, 닫혔다.

하지만 한참의 시간이 흐른 뒤에도, 백상은 얼어붙은 듯 움직이지 못했다.

그날이 다가오고 있었다.

자신이 세상 그 누구보다 염원했던, 그러나 누구보다 두려워했던 그 날이.
```

## Final English reading copy

```markdown
# Chapter 688

Baeksang was staring at himself in a full-length mirror.

Unlike an ordinary mirror, the one Southern Heaven Demon Empress had given him was large enough to reflect his entire body, and its surface was smooth without a single scratch.

It was the finest mirror one could find—not only in Nanman, but even in the Central Plains.

But there was only one reason Baeksang was looking into it.

He could see the face of his son, who looked exactly like him.

*This has never happened before.*

It had been more than forty years. He had steadied himself countless times whenever he wavered, and made it all the way to this position.

And yet his heart was more shaken now than ever.

*That must mean this grand plan, which has endured for decades, is finally nearing its end.*

Just then, a door opened behind him, and a familiar face appeared.

Baeksang met the Captain of the Guards’ eyes in the mirror and spoke.

“Have they brought him?”

The Captain of the Guards had momentarily hesitated at the sight of his lord’s back, which was sunk deep in thought. He answered.

“He is on his way.”

“Then what is the matter?”

“An urgent report has arrived.”

“An urgent report…”

Baeksang let his words trail off and crooked a finger.

The Captain of the Guards understood the gesture and approached, then whispered in a low voice.

“Last night, a massive wildfire was spotted to the north, three hundred li away.”

“Ailao Mountain.”

“Yes.”

“The one who started the fire would be Jin Taekyung.”

“We need further confirmation, but considering everything that has happened so far, he is the most likely culprit.”

“It was Jin Taekyung. Once again, it seems glory-blinded moths have rushed toward the flames.”

“They say the small and midsized tribes near Ailao Mountain joined forces. They attacked him with five hundred warriors and one hundred beasts, but…”

Baeksang waved a hand, cutting him off.

There was no need to hear the rest.

Jin Taekyung was not someone five hundred hastily gathered stragglers could do anything about.

The saying *the few cannot overcome the many* meant different things depending on who the opponent was. Jin Taekyung clearly lay outside the equation.

“I can already guess the result. What happened to Jin Taekyung afterward?”

“They say he routed the warriors, then headed toward Ailao Mountain alone.”

“He must have had a purpose. Could it have been the Poisonblood Grounds?”

“The fire was too fierce to confirm anything that far in. The flames began at the mountain’s entrance and have already spread halfway up.”

“He must have made up his mind.”

Ailao Mountain was one of Nanman’s most renowned precipitous mountains.

Its terrain was harsh, its valleys deep, and its winding mountain range stretched for one hundred li. Ancient trees of unknown age covered it endlessly.

Now that a wildfire had settled over Ailao Mountain, it would take at least three full days and nights before there was even a sign of the flames dying down.

*Perhaps the entire mountain will be burned to ash.*

If it had been a coincidence, it was a remarkable one.

It had been more than two hundred years since wildfire had invaded Ailao Mountain. And the person who had used the entire mountain as firewood to destroy the Five Poisons Sect at that time had also belonged to the Fire Gate Clan.

*That was how Nanman found peace again.*

But would it happen that way this time, too?

Baeksang silently stared at his own face in the mirror before opening his mouth heavily.

“Evacuate every tribesperson living nearby. Select three thousand capable warriors and blockade Ailao Mountain.”

The Captain of the Guards had continued his report impassively, but a flicker of agitation crossed his face.

“Three thousand? Even though a general mobilization has already been declared throughout Nanman?”

“We must tie his feet, if only to prepare for the unexpected.”

“But my lord, even with that force, surrounding all of Ailao Mountain…”

“Ailao Mountain is vast, but it has few entrances that can actually be used. Take that into account when deploying them.”

After thinking for a moment, the Captain of the Guards bowed his head.

“Understood.”

“What is the situation with the other chieftains?”

“As I reported, five chieftains have disappeared. The warriors under the two chieftains who departed earlier with the scouting party have disappeared as well.”

“So it comes to this in the end. They must be refusing to accept reality.”

Baeksang murmured calmly.

The missing chieftains were the ones who had never switched sides.

Their loyalty to the Beast Miao King had been unshakable. Some of them had even spat at Baeksang while mocking him for trying to win them over.

“My lord, there is no doubt that they have betrayed us. It is not too late. We should send a pursuit party even now…”

At the Captain of the Guards’ suggestion, Baeksang shook his head.

“Not long ago, someone told me this: Just because one tree is diseased, it does not mean the whole forest is sick. All you have to do is thin out the diseased trees.”

“What do you mean…”

“For the past several hundred years, thirty-two tribes have coexisted on this land. But I often found myself wondering how long we would have to preserve that arrangement.”

“……!”

The Captain of the Guards’ eyes widened as he understood Baeksang’s meaning.

Baeksang continued in a deeply sunken voice.

“Thirty-two is too many for everyone to join their hearts and unite behind one purpose. From now on, it is time to thin out the diseased trees and put the forest in order.”

Expulsion.

Or elimination.

The meaning of the new power who had driven out the king that had ruled this land for so long and climbed onto the throne himself was unmistakable.

The Captain of the Guards stared at his lord with his mouth open, then spoke in a heavy voice.

“What should we do?”

“If they leave, let them go. If they return to their bases and rally their warriors, we will gain both justification and strength.”

The Captain of the Guards knew it as well.

The scales of power had tipped a long time ago.

But there was one person he was worried about.

“If the Palace Lord—or rather, Yayul Cheok—joins them, things will not proceed so easily.”

Baeksang stared quietly at the Captain of the Guards before speaking.

“When I lived in the Central Plains long ago, I heard an interesting story.”

“My lord?”

“It was about a monkey born from stone. Its temperament and strength were so violent and powerful that Shakyamuni, whom the monks of the Central Plains worshiped, stepped forward and proposed a wager. He asked whether the monkey could escape from the palm of his hand.”

His calm voice pierced the Captain of the Guards’ ears.

“The monkey snorted and accepted. It rode the clouds to the edge of the world, where it even scribbled graffiti on five pillars. But when it returned, it discovered that the pillars it had seen were Shakyamuni’s fingers.”

Baeksang slowly spread one hand toward the mirror.

The enormous Palace Lord’s Hall seemed to fit inside his palm.

The sky and rivers. The earth and mountains.

Even if it reflected all of Nanman, it would still fit there.

“Yayul Cheok is the same. Now that I have risen to this position, he will never escape.”

“That means…”

“We have information that he headed east. Personally lead one thousand Bai warriors and pursue Yayul Cheok.”

“Understood.”

At that moment, the Captain of the Guards bowed and moved his lips.

“I beg your pardon, but our opponent is the Beast Miao King. To prepare for the unexpected, perhaps you should use the Baekcheon Unit.[^1]”

But Baeksang silently shook his head.

The Baekcheon Unit was the blade he had secretly honed for decades.

He had to draw and wield it when it was most needed.

“That is all. We have a distinguished guest, so you may withdraw.”

He was speaking to the Captain of the Guards, but his gaze, which had been fixed on the mirror from the beginning, had already shifted to an old man standing before the open door.

“Then I shall take my leave.”

After confirming that the Captain of the Guards had left the Palace Lord’s Hall, Baeksang slowly turned around.

“You have arrived, Head Elder.”

It was a dispassionate greeting.

But the reply was a sharp one.

“Can you not shut that filthy mouth of yours?”

THUD.

An old man whose face was covered in age spots approached with a cane.

Every inch of exposed flesh was covered in wrinkles.

Anger that he could not hide flickered in his eyes, clouded with discharge.

“You wretched bastard.”

“It seems you overheard our conversation.”

“Do you think this old man cannot see through your pitch-black intentions? Was that not why you said it aloud?”

“If you mean Yayul Cheok—the criminal who defied the will of the Tribal Grand Council to save a murderer and then betrayed the Nanman Beast Palace—then yes.”

“You bastard!”

WHOOSH! CLACK.

The old man swung his cane with all his strength, but Baeksang caught it in one hand.

There was no notable force or internal energy in the blow.

Baeksang easily took the cane away, then lightly shook his sleeve.

An invisible force made the old man’s aged body sit down where it stood.

“You have aged considerably since I last saw you. Though your fiery temper seems unchanged.”

The old man’s body trembled.

“If I had known you would do something like this, I would have beaten you to death with these hands long ago.”

“But too much time has passed for that now. Yayul Cheok betrayed the Palace and fled, while the fate of the Miao people rests on a child who long ago was caught stealing fruit wine and received a harsh scolding from you.”

“……!”

“Now is the time to leave that stale past behind and think about the future. With the Chieftain and Lesser Chieftain gone, everything depends on what choice the Great Chieftain of the Miao people makes.”

The old man, the Head Elder of the Miao people, glared at Baeksang in silence before slowly parting his lips.

“So you finally seized Nanman with that hideous greed of yours.”

“Call it whatever you like. There is nothing I will not do to obtain what I desperately desire.”

“You are now the Palace Lord of the Nanman Beast Palace. What more do you want? Do you wish to obtain the Beast King Stone and become a god?”

Baeksang shook his head.

“I have no interest in some ancient sacred treasure passed down only by word of mouth. What I want now is the future—and your wise choice, Head Elder.”

“The boy I remember was not like this.”

“I changed. Just as everything else has.”

“The Palace Lord trusted you. Even though I told him to be so wary, he trusted his one and only sworn brother.”

“There is no need to repay every act of trust.”

“It is not too late. Even now…”

“I crossed the river a long time ago. Once you are riding a tiger, you cannot get off. Now it is your turn to climb onto the tiger’s back, Head Elder.”

CRACK.

The sound of bones shifting came from the old man’s tightly clenched, wrinkled fist.

“So in the end, you are telling this old man to betray the Palace Lord?”

“Of course not.”

Baeksang picked up a teacup as he continued.

“I want every member of the Miao people, including you, to betray him.”

“……!”

“You should read the flow of things carefully. If you want to save more than ten thousand of your people.”

“You bastard!”

“Remember this. This is the first and last offer.”

Baeksang tilted the teacup.

The Head Elder squeezed his eyes shut.

A short silence passed before his hoarse voice broke it.

“Impossible.”

CLACK.

Baeksang set down the teacup and stared at the Head Elder with deeply sunken eyes.

“Will you not regret that answer?”

“Kill me instead. Ask anyone among the Miao people, and the answer will be the same.”

“You have not disappointed my expectations.”

Baeksang answered briefly, then snapped his fingers.

The closed door opened, revealing Bai warriors.

“Lock up the entire Miao leadership in the underground prison, including the Head Elder.”

The Bai warriors bowed, seized the Head Elder from either side, and lifted him to his feet.

The old man, whose day of death was approaching, cried out in a ringing voice.

“Baeksang! You bastard! Are you not afraid of Heaven?”

By the time his scream had gradually faded into the distance, Baeksang was looking down at the empty teacup and muttering.

“What more could I fear? What brought me this far was also Heaven’s will.”

There had certainly been a time when he resented Heaven.

After the Great Faction War ended and Baeksang returned to Nanman, he had been drunk every day.

He had poured alcohol down his throat as though each day were his last, then despaired when the sunlight woke him the following morning.

*Why did you save me? Why?*

Those days had been more painful than death.

But he could not writhe in sorrow forever.

He had things to do.

Things he absolutely had to do.

Baeksang looked at the blue sky beyond the window and murmured inwardly.

*Is this truly your will? No… Have you ever watched over me even once?*

And as always, no answer came, no matter how long he waited.

Except for the unfamiliar voice that pierced his ears the next moment.

“Um… Shall I refill your tea?”

Baeksang turned his head toward the voice.

A pretty-looking maid stood before the half-open door, looking at him.

“There is no need.”

“But your cup is empty.”

“I said there was no need…”

His words suddenly trailed off.

After staring at the maid for a moment, Baeksang spoke.

“Come in.”

At his subdued command, the warriors who had been about to stop the maid withdrew, and the door closed firmly behind her.

The maid took quick, small steps until she reached Baeksang, then slowly tilted the teapot in her hand.

Trickle.

Steam rose, carrying the fragrance of tea through the room.

But why?

Why did this throbbing sensation feel as though he had inhaled Poison Mist?

Baeksang silently watched the teacup fill before suddenly speaking.

“Whose face is that, Demon Empress?”

The maid—or rather, Southern Heaven Demon Empress—smiled sweetly and answered.

“Some girl who worked in the Inner Palace. She was still so fresh and lively. Cute enough to be unbearable.”

“Did you kill her?”

“Oh my. Is that so important?”

“That…”

“How interesting. Hundreds of people have already died, and you are worried about the life of one maid.”

Baeksang answered in a calm voice after a moment of silence.

“I was merely asking because I wondered whether it might interfere with the plan. Things that happen in the Inner Palace are discovered quickly.”

“Aha. Well, if that is what you mean…”

The Southern Heaven Demon Empress smiled coyly and picked up the teacup.

“The thing you are worried about will not happen. If anything has gone wrong, it would be at Ailao Mountain, not in the Inner Palace.”

“If you mean Ailao Mountain, then could it be…”

“Yes. Jin Taekyung. That child caused a little trouble. The fact that there has been no contact yet makes it certain.”

Baeksang thought for a moment before speaking.

“It was a trap?”

“That’s right. A trap laid to catch the old tiger who had left the Palace. I never expected the young tiger to get caught in it instead.”

CLICK.

The Southern Heaven Demon Empress set down her teacup and continued in a voice filled with amusement.

“Of course, I never expected that young tiger to be strong enough to break the trap, either.”

“It must have been a thorough trap, if you were so confident in it, Demon Empress.”

“Two Supreme Peak masters. One was the Black Hand Fist Demon, and the other…”

The Southern Heaven Demon Empress stopped speaking and smiled at Baeksang.

“Anyway, he was strong. Much stronger than the Black Hand Fist Demon.”

“……!”

“It is astonishing. I thought those two would be able to deal with the Beast Miao King. It seems the Lord of Heaven was not interested in that child for no reason.”

For Baeksang, it was one shock after another.

Jin Taekyung had not only killed two Supreme Peak masters single-handedly—the Lord of Heaven himself was also interested in him.

At the same time, Baeksang realized that his own judgment had not been wrong.

*Jin Taekyung.*

The face of an incomprehensible young man flashed before his eyes.

Baeksang looked at the Southern Heaven Demon Empress, who was smiling at him, and spoke.

“From here on, you will move personally, Demon Empress.”

A Supreme Peak master was a powerful asset.

With two such masters dead, Baeksang thought it was inevitable that the Southern Heaven Demon Empress would step forward.

At least, that was what he thought until he heard her answer the next moment.

“No? Why would I?”

The Southern Heaven Demon Empress let out a quiet laugh and continued.

“I do not have time to worry about that. Even if one of the major pieces has died, the current situation will not be overturned. What matters is the grand plan.”

“Do you mean…”

“The Beast Miao King and Jin Taekyung are no longer important. Strengthen the defenses of the Inner Palace and Outer Palace. Then gather every available force.”

The Southern Heaven Demon Empress rose from her seat and began walking as though she were dancing.

Her voice, filled with delight and joy, pierced Baeksang’s ears.

“Three days. Three days at the latest.”

“……!”

“Prepare yourself. On that day, everything will begin—and end.”

THUD.

The door opened.

Then closed.

But even after a long time had passed, Baeksang remained frozen in place, unable to move.

That day was drawing near.

The day he had longed for more than anyone else in the world—and feared more than anyone else.

[^1]: Baeksang’s secret elite unit, cultivated over decades.
```
