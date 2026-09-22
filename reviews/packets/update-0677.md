<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0677.txt",
      "sha256": "6f756fe162319ce976311ac509b85c56ca4d248457560894a0ca1633272a0322",
      "bytes": 13372
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "041473b8051719e5d06be36b5e79129fea09ee35804e6cde183e8114d9000003",
      "bytes": 1406
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6c78ffaa1ea268bd2774e6a91268e4e10199d6311a9d431b27a1aba295079287",
      "bytes": 202892
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "7db8b04ccdfb2d6216955743e1edee6b0404490acccbfa4ffc5078a8281d9033",
      "bytes": 1071
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "afd3f3f357d4f2acb623db91d432b6d01fbf2da2d350b81b55fe531d74a1000c",
      "bytes": 830
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f510cf6a75b365ea5cb094415ecc4dc93bc6548fdfff0ef9c9ed0639515e94bd",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "1f837ed5712a5fd5443dfd1cee733fa3eeb84a01caffb82aaf6a816cca436353",
      "bytes": 735
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "698d6172dcfe6c471c013e5fe9a9f67f44d8079e0bdd4d568f06f72131a5e0d8",
      "bytes": 1858
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a1cf5bde069f82259acf09560fcd1ff59be43aedecea81ab628e60129162a0d7",
      "bytes": 622
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "e12533aa1dba312df6435eb4c9c32c2719f670a3b6794979f9e7fc9e943c9969",
      "bytes": 628
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7e200d58e8e3a1187e0dd4b39d26d7a3ce0752ab097097d71117da83357ea7b8",
      "bytes": 209462
    }
  ],
  "estimated_tokens": 11518
}
-->

# Durable State Update — Chapter 677

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 677. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 677. Profile updates may replace only one
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
  "chapter": 677,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 677,
    "continuity_sources": [677],
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
    "Jin Taekyung has entered the Poisonblood Grounds alone with Muyaho to investigate the blood scent and confront the suspected enemy.",
    "Muyaho swallowed a poison-warding pearl, adapted to the Poisonblood Grounds, and continues accompanying Jin Taekyung through its Poison Mist and venomous beasts.",
    "The Nanman Beast Palace dispatched troops to the Poisonblood Grounds several days earlier to eliminate Five Poisons Sect remnants and other dangers; Jin suspects they may have been killed.",
    "Yohi and Heugung were abducted together and are imprisoned in an unknown location with their internal energy sealed.",
    "Heugung speaks formally and respectfully after the abduction, unlike his usual manner toward Yohi."
  ],
  "continuity_sources": [
    676
  ],
  "open_questions": [
    "Who captured Yohi and Heugung, and where are they being held?",
    "Did Dark Heaven or the unidentified Supreme Peak figure kill the Nanman Beast Palace troops in the Poisonblood Grounds?",
    "Can Jin Taekyung rescue Yohi and Heugung from the unknown captor?",
    "Is the Southern Heaven Demon Empress present in the Poisonblood Grounds?"
  ],
  "safe_through": 676,
  "temporary_decisions": [
    "Use formal, restrained English for Heugung's post-capture speech.",
    "Preserve Jin Taekyung's blunt profanity and irreverent no-brakes narration."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 살기     | **killing intent**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 세종기지 | **King Sejong Station** | Korean Antarctic research station used in Taekyung's comparison. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 요족 | **Yao people** | One of Nanman's four great tribes, led by Yohi. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 독무 | **Poison Mist** | Deep green mist covering the Poisonblood Grounds swamp. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 흑웅 | 진태경 | Nanman great chieftain to Central Plains ally and covert contact | you | cautious and informal | Heugung uses 자네 in private Sound Transmission while explaining the missive and Baeksang's alleged collusion. |
| 진태경 | 흑웅 | Central Plains investigator to covert informant and prospective witness | Heugung | blunt and confrontational | Jin questions Heugung's reliability, challenges his claims, and demands proof. |
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |
| 남천마후 | 백상 | Dark Heaven controller to coerced Nanman leader | Great Chieftain Baeksang / Palace Lord | playful, taunting, and threatening | She repeatedly addresses Baeksang while mocking his grief, acknowledging his effort, and issuing her order. |
| 진태경 | 부족장 | captor to captured tribal chieftain | tribal chieftain | casual, coercive, and mocking | Jin promises to spare the captured chieftain if he answers questions properly. |
| 부족장 | 진태경 | captured tribal chieftain to overpowering enemy | Jin Taekyung | alarmed and desperate | The chieftain recognizes Jin by name while fleeing and then begs for his life. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 676
- **Aliases:** None
- **Role:** Baeksang is the temporary Palace Lord of the Nanman Beast Palace, an over-seventy Great Chieftain of the Bai people, and the leader of Nanman's general mobilization, with nearly ten thousand troops stationed in the Inner Palace.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with enduring grief over Hwi's death and a guarded but still powerful bond with his sworn elder brother that now leaves him visibly conflicted.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of his deceased only child Baekhwi, whom the Great Snow Fiend killed during the Great Faction War; despite his bond with Yayul Cheok, he has chosen to oppose the Beast Miao King's escape and has surrounded Wonhu's remaining force with Bai warriors.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 676
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** The Beast Miao King is fierce and vigilant, yet pragmatic and willing to sacrifice his position to protect Nanman's survival and the greater cause over personal revenge.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, and is Yayul Mok's father while jointly risking their positions to rescue Jin Taekyung and prevent war with the Central Plains.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 676
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 676
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung presents as foolish and easily flattered in public but is capable of concealed planning, disguise, and covert contact.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung genuinely loves Yohi and had promised to cooperate with Jin Taekyung; he and Yohi were abducted together and are imprisoned in an unknown location, with his internal energy sealed and his speech unusually formal.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 675
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner still facing public execution at noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 675
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 676
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, manipulates Heugung alongside Baeksang, and was abducted with Heugung into an unknown prison where her internal energy is sealed.

## Korean source

```text
＃677화



철컥. 구구궁.

갑작스럽게 열린 석문(石門)과 함께 흘러나오는 빛.

어둠에 익숙해져 있던 흑웅과 요희가 본능적으로 몸을 움츠리며 신음하던 그때, 누군가의 목소리가 그들의 귓가를 파고들었다.

“오호, 꼴이 제법 볼만한데.”

“……!”

“……!”

“그래, 남만의 야만족들이라면 응당 이래야지.”

취한 듯 흐느적거리는 목소리에, 두 사람의 신형이 파르르 떨렸다.

말에 담긴 조롱과 비웃음에 모멸감을 느껴서?

아니다. 그것은 두려움과 공포 때문이었다.

‘이 목소리는…….’

상대의 정체를 알아차린 요희는 전신의 피가 싸늘하게 식는 듯한 감각에 사로잡혔다.

어찌 잊겠는가. 마치 유령처럼 나타나 휘하의 전사들을 몰살시키고, 단 한 수만에 흑웅을 외팔이로 만들어 버린 악귀(惡鬼)의 목소리를.

요희의 머리가 새하얗게 물든 그때, 한껏 숨죽인 흑웅의 속삭임이 들려왔다.

“명심하시오. 절대 눈을 떠서는 안…….”

퍼엉!

“커헉!”

한 줄기 파공성과 함께 울려 퍼지는 비명.

비록 조언에 따라 질끈 눈을 감고 있던 요희는 볼 수 없었지만, 내상으로 검붉은 핏물을 쏟아 내고 있을 흑웅의 모습을 떠올리는 것은 그리 어려운 일이 아니었다.

“그만! 그만하세요!”

“쿠, 쿨럭. 요희, 가만히 있…….”

퍼엉! 털썩.

다시 한번 울려 퍼지는 파공성에, 요희는 참지 못하고 눈을 떴다.

전신이 결박된 채 쓰러져 있는 흑웅. 그리고 한 됫박은 될 법한 핏물을 토해 낸 그의 앞에 우뚝 선 악귀가 보였다.

“다, 당신.”

“제법 영악한 계집이라고 들었는데, 헛소문이었군.”

떨리는 입술 사이로 흘러나온 요희의 음성에, 악귀가 누런 이를 드러내며 씩 웃었다.

산발이나 다름없는 흰 머리와 가늘게 찢어진 실눈. 요서부에서는 복면으로 얼굴을 가리고 있었지만 분명 눈앞의 노인은 그 악귀가 맞았다.

“왜 저놈의 말을 듣지 않았느냐. 노부의 얼굴을 보지 않았다면 일각이라도 더 연명할 수 있었을 터인데.”

“……!”

“뭐, 이렇게 된 이상 별수 없지. 두 연놈 모두 사이좋게 저승길로 보내는 수밖에.”

어깨를 으쓱한 노인은 왜소하기 짝이 없는 체격에 비해 비정상적으로 긴 팔을 뻗었다.

이유를 알 수 없는 반점으로 가득한 손바닥이 가까워지는 만큼 짙어지는 죽음의 냄새.

마지막임을 직감한 요희가 몸부림치려던 그 순간이었다.

“그만하면 됐다, 흑수(黑手).”

반쯤 열린 석문 틈새로 흘러나온 한마디에, 흑수라 불린 노인이 손을 거두며 한숨을 내쉬었다.

“거, 이제는 눈치 보여서 장난도 못 치겠군.”

보이지 않는 누군가가 대답했다.

“그 말, 지금 내게 한 말이냐?”

만년설(萬年雪)처럼 냉막한 목소리에, 흑수가 입맛을 다셨다.

“그럴 리 있겠소. 혼잣말이오, 혼잣말.”

“천둥벌거숭이처럼 구는 것은 여기까지다. 설마 마후(魔后)께서 내리신 명을 잊은 것은 아니겠지.”

흑수의 얼굴이 일그러졌다.

“천둥벌거숭이라. 이 나이에 그런 말을 들을 줄은 몰랐구려.”

“하면 나이에 맞는 언행을 보이면 될 터. 대계(大計)를 코앞에 두고 경거망동했다가는 내가 용서치 않을 것이다.”

“…….”

“대답한 것으로 알지.”

어떤 인기척도 느낄 수 없었지만, 요희는 석문 밖의 누군가가 사라졌다는 것을 깨달았다. 얼마 지나지 않아 들려온 흑수의 중얼거림 때문이었다.

“빌어먹을 노괴(老怪) 같으니.”

흑수에게는 그저 사소한 불평이었을지 몰라도, 요희는 경악과 두려움을 드러내지 않기 위해 안간힘을 써야 했다.

‘이자뿐만이 아니었다니.’

갑작스럽게 끼어든 냉막한 목소리의 주인이 누구인지는 모른다. 하지만 두 사람이 주고받는 대화만으로도 깨달을 수 있었다.

그는 눈앞의 악귀도 고분고분하게 만드는 연배와 무위의 소유자라는 것을.

그리고 거기에 더해…….

‘마후. 분명 마후라 했어.’

짧은 대화 도중에 등장한 두 글자. 마후.

그리고 그 단어가 누구를 지칭하는 것인지, 요희는 이미 알고 있었다.

‘남천마후(南天魔后).’

기이할 정도로 아름답고, 아름다운 것 이상으로 위험하다고 알려진 암천의 핵심 인물.

남천마후에 관한 모든 것은 극비리로 취급되는 정보였지만, 남만에서도 단 네 명뿐인 대족장인 요희는 예외였다.

무엇보다 그녀에게는 믿고 기댈 만한 백상이라는 거목이 있었다.



‘내 곁에 선다면, 그대가 원하는 것을 주지.’



그건 여인의 몸으로 대족장의 자리에 오른 직후, 처음으로 대면한 자리에서 백상이 했던 말이었다. 그에 요희는 이렇게 물었었다.



‘제게 무엇을 주실 생각이죠?’

‘막대한 재화와 영향력. 그리고 요족의 부흥.’

‘흥미롭네요. 하지만 거절하겠어요.’

‘이유는?’

‘백상 대족장님의 제안을 승낙한다 해도 제가 원하는 만큼의 대가를 얻지 못할 테니까요. 전 보기보다 야망이 크거든요. 지켜지지 않을 약속 때문에 야율 궁주를 적으로 돌릴 만큼 순진하지도 않고요.’

‘이번에 대족장의 자리에 오르면서 요서부를 물려받았겠군. 그곳에 믿을 만한 심복들이 있나?’

‘물론이죠. 그런데 갑자기 그건 왜…….’

‘늦었지만 축하하는 의미로 선물을 보낼까 싶어서. 우선은 황금 다섯 수레 정도면 충분하겠지.’

‘……!’

‘오늘은 이만 돌아가거라. 제안에 응할 생각이라면 내일 이 시간에 다시 만나도록 하지.’



황금 다섯 수레라니.

감히 상상도 못 했던 막대한 금액에 처음에는 반신반의하던 요희였지만, 그녀를 기다리고 있던 누렇게 번쩍이는 황금 더미를 직접 확인한 뒤에는 확신할 수밖에 없었다.

백상은 반드시 약속을 지킨다는 것을.

만약 그의 곁에 선다면, 자신이 원하는 대가 이상을 얻을 수 있으리라는 것을.

그렇게 다음 날, 뜬눈으로 밤을 지새운 요희는 곧장 백상을 찾아갔고 자신의 판단이 옳았음을 깨달았다.

아니, 옳았다고 믿었다.

눈앞의 악귀가 찾아오기 전까지는.

“호오, 이 계집년 좀 보게.”

언제 기분이 상했냐는 듯, 흑수는 술에 취한 사람처럼 흐릿하게 웃었다.

“눈깔을 동그랗게 뜬 걸 보아하니, 이게 뭔가 감이 잡힌 모양이로구나. 응?”

“나, 나는…….”

“뭐, 대강의 이야기는 노부도 들어서 알고 있다. 덕분에 우리가 준비하는 일이 쉽게 풀렸다고 했지. 그 부분에 있어서만큼은 백상, 그놈이 야만족답지 않게 제법 일 처리를 잘했어.”

요희는 동공이 거세게 흔들렸다.

암천의 주구 노릇을 한 것으로도 모자라 죽을 위기에 처한 지금의 상황이 도무지 믿어지지 않았다.

“그럴 리가. 그럴 리가 없어. 나는 몰랐…….”

“몰랐던 것이냐. 아니면 모르는 척했던 것이냐.”

“……!”

“안 물어봐도 알겠군. 하긴, 십 년이 넘도록 백상 그놈을 따랐으니 대족장씩이나 되는 년이라면 응당 의구심을 품었겠지.”

낄낄 웃는 흑수의 모습을, 요희는 그저 멍하니 바라볼 수밖에 없었다.

눈앞의 악귀가 하는 말은 모두 사실이었으니까.

첫 시작은 미미했다. 일 년에 한 번 열리는 대회의에서 백상의 의견에 손을 들어 주었고, 그가 내리는 몇 가지 사소한 지시를 따르기만 하면 황금과 영향력이 넝쿨째 굴러 들어왔다.

그러나 세월이 흐를수록 의심은 짙어졌고, 불과 몇 달 전부터 자주 들려오기 시작한 암천이라는 두 글자에는 불안해지기 시작했다.

하지만 그뿐이었다. 그녀는 자신의 마음속에 자리 잡은 의심과 불안감을 애써 외면하고 억눌렀다.

모든 것을 밝히고 수습하기에는 지금까지 얻은 것들이 너무 많았으니까.

요족의 부족민들은 서서히 약화하던 부족을 다시 일으킨 요희를 우러러보고 있었고, 어린 계집 취급하던 부족장들은 먼저 고개를 숙였다.

그토록 강한 야수묘왕도, 백상도 결국은 언젠가 한 줌의 흙으로 돌아갈 터. 그때가 되면 공석이 된 권좌(權座)도 노려봄 직했다.

여인의 몸으로 궁주의 자리에 올라, 남만야수궁의 역사를 새로 쓰는 것이다.

그러나 요희가 매일 밤 되새기던 원대한 야망은, 바로 지금 송두리째 무너지고 있었다.

“그래도 네년은 노부에게 감사해야 할 것이다. 요족의 전대 대족장이 급사하지 않았다면, 너처럼 멍청한 계집이 어찌 지금까지 호사를 누리며 살았겠느냐.”

“그, 그 말은 설마.”

“여러모로 까다로운 늙은이였지. 무공은 형편없었지만, 대신 눈치가 빨랐거든. 때마침 요족에 역병이 돌아 손쉽게 처리할 수 있었지.”

씩 웃은 흑수가 말을 이었다.

“참으로 희한하지 않더냐? 늙을 대로 늙은 대족장은 그렇다 치더라도, 그 뒤를 이어야 할 세 아들이 죽고 대족장이 늘그막에 얻은 서녀(庶女)에게까지 차례가 돌아갔으니.”

“……!”

“그때 백상, 그놈의 표정이 참으로 볼만했지. 어떻게든 그 늙은이를 설득해 보겠다며 끝까지 시간을 끌더니…… 그래도 명줄 하나는 질긴 놈이라 그런지 달려들진 않더군. 아쉬운 일이야.”

요희는 공허한 눈동자로 흑수를 바라보았다. 그녀는 더 이상 놀랄 만한 일도, 기력도 남아 있지 않았다고 생각했다.

하지만, 이 역시 혼자만의 착각에 불과했다.

“그래도 계집치고는 제법이었다. 목숨이 위태로운 와중에도 추종향(追蹤香)이라, 그 조심성은 늙은 아비에게 물려받은 건가?”

추종향. 거무스름한 흑수의 입술 사이로 흘러나온 세 글자에 가녀린 신형이 덜컥 굳는다.

그리고 요희의 마지막 희망마저 산산조각 내 버린 흑수는 즐거움을 참지 못했다.

“왜, 노부가 모를 줄 알았더냐?”

흑수는 파르르 눈동자에 담긴 절망을 읽고 낄낄 웃었다.

그는 지금까지 수도 없이 이러한 감정을 마주했지만, 이러한 순간마다 솟구치는 희열은 조금도 무뎌지지 않았다.

“저런. 이 풋내나는 계집아. 어리석은 아해야.”

흑수라는 이름처럼, 검은 반점으로 뒤덮인 손바닥이 새하얀 뺨을 쓰다듬는다.

“참으로 아름답구나. 마후께서 탐내실 만해.”

노인은 먹잇감을 앞에 둔 맹수처럼 입을 벌렸다. 온통 썩거나 기괴하게 뒤틀린 이빨에서는 끔찍한 악취가 풍겼다.

“마음 같아서는 일장에 너희를 쳐 죽이고 싶지만…… 내 이번만큼은 참아 주마. 그보다 먼저 해야 할 일이 있거든.”

마치 거미줄에 걸린 벌레처럼 굳어 버린 요희를 남겨 둔 채, 흑수는 자리에서 일어났다.

그리고 이미 의식을 잃고 쓰러진 흑웅을 힐끗 바라본 그가 석문으로 다가가던 그 순간.

구구구궁!

흑수는 들을 수 있었다.

사방을 울리는 굉음과 함께, 멀리서 들려오는 듯한 누군가의 외침을.

- 나와! 이 개새끼들아아!

크아아앙!

이제, 먼 길을 찾아온 손님을 맞이하러 갈 시간이었다.



* * *



적들을 부르는 내 방식은 간단했다.

깨고, 부수고, 박살 냈다.

독무? 독물? 어디 선가에 숨어 호시탐탐 지켜보고 있을 적들?

상관없다. 나는 핸들이 고장난 8톤 트럭처럼 미친 듯이 날뛰며 독혈지의 모든 것을 때려 부수기 시작했다.

적들이 나오지 않을 수 없도록.

그리고 이런 내 노력은 얼마 지나지 않아 결실을 맺었다.

“혈기왕성한 젊은이로군.”

“찾아온다면 야수묘왕일 줄 알았는데…… 네놈이 바로 그 진태경이냐?”

목소리를 따라 천천히 돌아선 나는 볼 수 있었다.

약이라도 한 것처럼 흐느적거리는 땅딸막한 늙은이와 고향이 남극 세종기지인지 한기를 풀풀 풍기는 장신의 노인을.

이토록 상반된 두 사람이었지만, 그들에게도 공통점은 있었다.

첫째. 초절정 고수라는 것.

둘째. 결코 살려서 보내지 않겠다는 의지가 엿보이는 살기를 뿜어낸다는 것.

그리고 두 노인을 보며 잠깐 고민하던 나는, 준엄하게 입을 열었다.

“한 놈은 빠져 있어라. 강호의 법도에 따라 차례대로 상대해 줄 테니.”

대답은 금방 돌아왔다.

쉬이잉, 콰광!

그래, 시발. 안 먹힐 줄 알았다.
```

## Final English reading copy

```markdown
# Chapter 677

*Click. Rumble.*

Light spilled out through the stone gate as it suddenly opened.

Heugung and Yohi, whose eyes had grown accustomed to the darkness, instinctively shrank back and groaned. Then a voice bored into their ears.

“Oh-ho. Now this is a sight worth seeing.”

“……!”

“……!”

“Of course. This is how the barbarians of Nanman ought to look.”

The voice swayed as if its owner were drunk, and both their bodies trembled.

Was it because they felt humiliated by the mockery and ridicule in his words?

No. It was because of fear. Because of terror.

*That voice…*

Yohi recognized the speaker and felt as though the blood throughout her body had turned cold.

How could she forget it? The voice of the Fiend who had appeared like a ghost, slaughtered the warriors under her command, and turned Heugung into a one-armed man with a single move.

Just as Yohi’s mind went blank, she heard Heugung whispering with bated breath.

“Remember this. You must never open your eyes—”

*Boom!*

A sharp blast of displaced air rang out alongside a scream.

Yohi had squeezed her eyes shut as he advised, so she could not see what had happened. But it was not difficult to imagine Heugung coughing up dark-red blood from his internal injuries.

“Stop! Please, stop!”

“Cough, cough. Yohi, stay still—”

*Boom! Thud.*

Another blast of displaced air rang out, and Yohi could no longer endure it. She opened her eyes.

Heugung lay on the floor with his entire body bound. Standing before him was the Fiend, who had forced him to vomit what looked like a full doe measure[^1] of blood.

“You…”

“I heard you were a fairly clever woman, but I see that was nothing more than a false rumor.”

The Fiend revealed yellow teeth in a grin as Yohi’s voice slipped between her trembling lips.

His white hair was nearly as disheveled as a bird’s nest, and his eyes were narrow slits. He had hidden his face behind a mask in the Western Yao Estate, but there was no doubt that the old man before her was the same Fiend.

“Why didn’t you listen to that fellow? If you hadn’t seen this old man’s face, you might have lived for another fifteen minutes.”

“……!”

“Well, what’s done is done. I suppose we’ll just have to send both of you on your way to the afterlife together.”

The old man shrugged and extended an arm that was unnaturally long compared to his pitifully small frame.

The closer his palm came, the stronger the smell of death grew. His hand was covered in spots whose origins Yohi could not identify.

Just as Yohi realized this was the end and tried to struggle—

“That’s enough, Black Hand.”

The words came through the gap in the half-open stone gate. The old man called Black Hand withdrew his hand with a sigh.

“Come on. Now I can’t even have a little fun without having to watch myself.”

Someone Yohi could not see answered him.

“Are you saying that to me?”

The voice was as cold and remote as eternal snow. Black Hand clicked his tongue.

“Of course not. I was talking to myself. Just talking to myself.”

“Stop acting like a reckless brat. You haven’t forgotten the order given by Her Majesty the Demon Empress, have you?”

Black Hand’s face twisted.

“A reckless brat? I never thought I’d be called that at my age.”

“Then act your age. If you behave rashly with the great undertaking so close at hand, I will not forgive you.”

“……”

“I’ll take your silence as an answer.”

Yohi felt no presence at all, but she realized that the person outside the stone gate had disappeared when she heard Black Hand muttering a moment later.

“Damn old monster.”

Perhaps it had been nothing more than a minor complaint to Black Hand, but Yohi had to struggle with all her might not to reveal her shock and fear.

*It wasn’t just him.*

She did not know who owned the cold voice that had suddenly cut into their conversation. But she could tell from the brief exchange between the two of them.

*That person possesses enough seniority and martial prowess to make even the Fiend before me obey him.*

And on top of that…

*The Demon Empress. He definitely said the Demon Empress.*

Two words that had appeared in the middle of their short conversation.

The Demon Empress.

Yohi already knew whom that word referred to.

*The Southern Heaven Demon Empress.*

A core figure of Dark Heaven, known for being unnaturally beautiful—and even more dangerous than she was beautiful.

Everything concerning the Southern Heaven Demon Empress was treated as top-secret information. But Yohi was one of Nanman’s four Great Chieftains, so she was an exception.

More importantly, she had a great tree named Baeksang whom she could trust and rely on.

> “If you stand by my side, I will give you what you want.”

That was what Baeksang had said when they first met, shortly after Yohi had risen to the position of Great Chieftain.

Yohi had asked him in return:

> “What do you intend to give me?”

> “Vast wealth and influence. And the restoration of the Yao people.”

> “Interesting. But I’ll refuse.”

> “Why?”

> “Even if I accept Great Chieftain Baeksang’s offer, I won’t receive the reward I want. I have greater ambitions than I appear to. Nor am I naive enough to make Palace Lord Yayul my enemy over a promise that may never be kept.”

> “You inherited the Western Yao Estate when you took the position of Great Chieftain. Do you have any trustworthy subordinates there?”

> “Of course. But why are you suddenly asking about that…?”

> “I was thinking of sending a gift, albeit late, as a congratulatory gesture. Five carts of gold should be enough to start with.”

> “……!”

> “Go home for today. If you intend to accept my proposal, come meet me again at this time tomorrow.”

Five carts of gold.

At first, Yohi had been half-convinced and half-doubtful at the enormous sum, which she had never even dared imagine. But after seeing the piles of gold waiting for her with her own eyes, she had no choice but to believe.

Baeksang always kept his promises.

If she stood by his side, she could obtain even more than the reward she wanted.

The following day, after spending the entire night awake, Yohi had gone straight to Baeksang and realized that her judgment had been correct.

No. She had believed it was correct.

At least until the Fiend before her came looking for her.

“Oh-ho. Look at this little bitch.”

As if he had never been offended, Black Hand smiled hazily like a drunk.

“Judging by those round, wide-open eyes, I suppose you’ve figured out what this is about. Hmm?”

“I, I…”

“Well, this old man has heard the general story. They said our preparations went smoothly thanks to you. At least in that regard, Baeksang did a decent job for a barbarian.”

Yohi’s pupils shook violently.

She could not believe the situation she was in: not only had she served as a pawn of Dark Heaven, she was now in danger of dying.

“That can’t be. It can’t be. I didn’t know…”

“Did you not know? Or did you pretend not to know?”

“……!”

“I don’t even need to ask. After all, you followed that bastard Baeksang for more than ten years. A woman who had risen to become a Great Chieftain would naturally have had her doubts.”

Yohi could only stare blankly at Black Hand as he chuckled.

Everything the Fiend before her said was true.

It had begun with something insignificant. Once a year, at the Tribal Grand Council, she had raised her hand in support of Baeksang’s opinions. She had followed a few minor orders he gave her, and gold and influence had rolled toward her in abundance.

But as the years passed, her suspicions had deepened. Then, several months ago, she began hearing the name Dark Heaven with increasing frequency, and unease had taken root in her heart.

But that was all.

Yohi had deliberately ignored and suppressed the doubts and anxiety that had taken hold inside her.

She had gained too much to reveal everything and try to clean up the mess.

The people of the Yao tribe looked up to Yohi, who had revived their slowly weakening tribe. The tribal leaders who had treated her like a little girl were the first to lower their heads.

Even the mighty Beast Miao King and Baeksang would eventually return to the earth as a handful of soil. When that time came, she might even be able to reach for the vacant throne.

She would rise to the position of Palace Lord as a woman and rewrite the history of the Nanman Beast Palace.

Yet the grand ambition Yohi had revisited every night was collapsing completely at this very moment.

“Even so, you should be grateful to this old man. If the previous Great Chieftain of the Yao people hadn’t died suddenly, how could a stupid woman like you have lived in luxury until now?”

“Th-that can’t mean…”

“He was a troublesome old man in many ways. His martial arts were pathetic, but he was quick to notice things. Fortunately, a plague broke out among the Yao people at just the right time, so he was easy to deal with.”

Black Hand continued with a grin.

“Isn’t it strange? The Great Chieftain was already old enough to die, so perhaps that part was understandable. But then his three sons, who were supposed to succeed him, died as well, and the position passed all the way to the old man’s illegitimate daughter, born in his later years.”

“……!”

“Baeksang’s expression back then was truly something to see. He dragged things out to the bitter end, insisting he would somehow persuade the old man… Still, perhaps the bastard had a strong survival instinct, because he never came charging in. What a shame.”

Yohi stared at Black Hand with hollow eyes. She thought she had no more strength left to be shocked by anything.

But that, too, was only a delusion of her own.

“You did fairly well for a woman, though. Even with your life in danger, you prepared a tracking scent. Did you inherit that caution from your old father?”

Tracking scent.

At the three words that slipped from Black Hand’s dark lips, Yohi’s delicate body suddenly went rigid.

Black Hand had shattered even Yohi’s last hope, and he could not contain his amusement.

“Why? Did you think this old man wouldn’t know?”

Black Hand chuckled as he read the despair trembling in her eyes.

He had faced this emotion countless times before, but the exhilaration that surged through him in moments like this had never dulled in the slightest.

“Oh, you poor thing. You inexperienced little girl. What a foolish child.”

Just as his name suggested, Black Hand’s palm was covered in black spots as it stroked her snow-white cheek.

“You’re truly beautiful. Beautiful enough for Her Majesty the Demon Empress to covet.”

The old man opened his mouth like a predator facing its prey. A terrible stench wafted from his teeth, all of them either rotten or twisted grotesquely out of shape.

“I’d like nothing more than to kill you both with a single palm strike, but… I’ll restrain myself this time. There’s something I have to do first.”

Leaving Yohi frozen like an insect caught in a spider’s web, Black Hand rose from his seat.

He glanced at Heugung, who had already collapsed unconscious, and approached the stone gate.

That was when—

*Rumble-rumble-rumble!*

Black Hand heard it.

Along with a thunderous roar that shook the entire area, someone’s distant shout reached his ears.

—Come out, you fucking bastards!

*GRAAAAAWR!*

It was time to go welcome the guest who had come such a long way.

* * *

My method of calling out enemies was simple.

I broke things, wrecked things, and smashed them to pieces.

Poison Mist? Venomous beasts? Enemies hiding somewhere and watching for a chance to strike?

I didn’t care.

I rampaged like an eight-ton truck with a broken steering wheel, smashing everything in the Poisonblood Grounds.

I had to make sure the enemies had no choice but to come out.

And my efforts bore fruit before long.

“What a vigorous young man.”

“I expected the Beast Miao King if someone came looking for us… So you’re Jin Taekyung?”

Following the voices, I slowly turned around and saw them.

A short, squat old man swaying as though he were drugged, and a tall old man radiating such cold that I wondered if his hometown was King Sejong Station in Antarctica.

The two old men could not have been more different, but they had things in common.

First, they were both Supreme Peak masters.

Second, they were emitting killing intent that made it clear they had no intention of letting me leave alive.

After studying the two old men for a moment, I spoke sternly.

“One of you step aside. I’ll face you one at a time, according to the customs of the martial world.”

The answer came immediately.

*Whoosh—KWA-BOOM!*

Yeah, fuck. I knew that wouldn’t work.

[^1]: A *doe* is a traditional Korean unit of volume, roughly 1.8 liters.
```
