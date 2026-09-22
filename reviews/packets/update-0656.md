<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0656.txt",
      "sha256": "3c568e0b43b28ab776fd8f865befbadb61b0a7b906fe302a898710e45090c622",
      "bytes": 14503
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7ad5c97cd46e10c2688c053a5dd2346b90d6eb0e8135ef5597d822fce10e8dbd",
      "bytes": 2049
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "07cc77963df7c51a4c7538858e36f8523d904b45434140bd98e990ec51bac94e",
      "bytes": 200296
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "520b708dbb4bf171da6dbf618d55d80a8429ab87f160b75f9914f998d7802e3c",
      "bytes": 800
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "f9d2aa270f7dfe0ca3abbbd2c1706ddb6160c224ed042eae1804ccda7c1d2584",
      "bytes": 814
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "ea7080e1a4f2a75620da2e2f085c32ecb8a435ca038e1085505a8f5a1510768a",
      "bytes": 769
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "657b788d8863f11f318df47ed3553a24b1e3ddf7532c906982cc3a74e5daa613",
      "bytes": 1936
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f19c5fb9216ff219b0762d55092f31a249cb95c7db8761a875128ae7501a0bfd",
      "bytes": 622
    },
    {
      "path": "characters/Namho.md",
      "sha256": "550a3f25e706e15de61db985335e294ed946ec1eef1be133ab78f2d0500b7f4e",
      "bytes": 843
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "9085612bf8efecd67c9b1c0ddc8962c20fa563e7ec1240b7e05669e49d2d92a5",
      "bytes": 585
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "564aa67f448016a98d38d674e8ba8b7766e959ad4bbf5ec6ed9929910f978241",
      "bytes": 871
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e1c51468df24b15e30318fcc6adc99254481d44af8e49443afda05aac083a41b",
      "bytes": 206083
    }
  ],
  "estimated_tokens": 12034
}
-->

# Durable State Update — Chapter 656

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 656. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 656. Profile updates may replace only one
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
  "chapter": 656,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 656,
    "continuity_sources": [656],
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
    "Jin remains in the Nanman Beast Palace's Inner Palace as the Third Young Master of the Jin Family of Taiyuan and head of the Fire Dragon Pavilion.",
    "The Fire Dragon Pavilion was attacked after Jin left, and Dark Heaven is suspected of organizing or enabling the assault.",
    "Yohi's Western Yao Estate was attacked by a Supreme Peak master, killing more than a hundred Yao warriors and beasts.",
    "Jin and Yayul Mok believe Dark Heaven directly intervened and likely deployed a Supreme Peak master, but the motive is unknown.",
    "Baeksang and the Beast Miao King are the only two known Supreme Peak masters in Nanman.",
    "Heugung genuinely loves Yohi and had promised to cooperate with Jin.",
    "Heugung visited Yohi with four guards, who were killed; a wrist believed to be his was found, but his death is unconfirmed.",
    "Faint footprints indicate that a third party abducted or confronted Heugung and Yohi rather than the incident being their staged attack.",
    "Yohi and Heugung remain missing from the Inner Palace.",
    "Yohi's nearly scentless pouch remains a possible clue.",
    "Baeksang arrived before the Beast Miao King and declared that the guilty party was coming out on their own."
  ],
  "continuity_sources": [
    655
  ],
  "open_questions": [
    "Who was the Supreme Peak attacker, and what did Dark Heaven seek by intervening directly?",
    "Are Heugung and Yohi alive, and where were they taken?",
    "What can be learned from Yohi's nearly scentless pouch?",
    "Who was Baeksang accusing when he said the guilty party was coming out on their own?",
    "Is Baeksang truly colluding with Dark Heaven despite the evidence of third-party intervention?"
  ],
  "safe_through": 655,
  "temporary_decisions": [
    "Retain Force for 강기.",
    "Retain Supreme Peak for 초절정.",
    "Retain Sound Transmission for 전음.",
    "Render 서요부 as Western Yao Estate and 동이부 as Eastern Yi Estate.",
    "Render 향낭 as scent pouch."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 상태               | **Status**                     |
| 태원     | **Taiyuan**            |
| 대사      | **Master** for a senior Buddhist monk                           |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 축골공 | **Bone-Shrinking Technique** | A martial art that stretches and shrinks bone and flesh to alter the user's appearance. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |
| 서요부 | **Western Yao Estate** | Yohi's residence in the western part of the Inner Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 야율목 | 남호 | Nanman Young Palace Lord to elderly guest and Hidden Shadow Pavilion agent | old man | respectful and familiar | Yayul Mok uses the honorific 노인장 while praising Namho's knowledge of White Tigers. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 야율목 | 야수묘왕 | son_to_father | Father | formal and deferential | Yayul Mok calls out to the Beast Miao King after the rescue party arrives. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 흑웅 | 진태경 | Nanman great chieftain to Central Plains ally and covert contact | you | cautious and informal | Heugung uses 자네 in private Sound Transmission while explaining the missive and Baeksang's alleged collusion. |
| 진태경 | 흑웅 | Central Plains investigator to covert informant and prospective witness | Heugung | blunt and confrontational | Jin questions Heugung's reliability, challenges his claims, and demands proof. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 655
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes, and one of only two Supreme Peak masters in Nanman.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle, opposes the Nanman Beast Palace joining the Murim Alliance, remains distrustful of the Central Plains, and is alleged by Heugung to have colluded with Dark Heaven.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 655
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, is responsible for the forces stationed at Ailao Mountain, has ordered Ju Hwaran, Song Ilseom, and Hyuk Mujin to investigate the Blood Monk in Guizhou, and met the Martial God twice more than fifty years ago.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 655
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung presents as foolish and easily flattered in public but is capable of concealed planning, disguise, and covert contact.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung genuinely loves Yohi and had promised to cooperate with Jin Taekyung; he disappeared alongside Yohi after the assault on the Fire Dragon Pavilion, and his death remains unconfirmed after a severed wrist believed to be his was found at her estate.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 652
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 652
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 655
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 654
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 655
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

## Korean source

```text
＃656화



사방이 고요했다.

시신을 수습하던 전사들.

지금 막 도착한 것이 분명해 보이는 부족장들.

한 사람의 예외도 없었다. 서요부(西瑤部)의 모두가 움직임을 멈춘 채 이곳을 바라보고 있었다.

아니, 그들의 시선이 향하고 있는 것은 오직 하나. 바로 나였다.

그리고 다음 순간.

“죄인이 제 발로 걸어 나오는군.”

적막을 깨트리는 서늘한 목소리가 울려 퍼진다.

깊숙이 가라앉아 있는 백상의 눈동자를 마주한 그 순간, 나도 모르게 헛웃음이 흘러나왔다.

“하.”

섬광처럼 찾아온 깨달음. 지금 이 상황이 어떻게 흘러가고 있는지, 더 이상 생각해 볼 필요도 없었다.

백상이 인사말 대신 건넨 한 마디에 모든 것이 함축되어 있었으니까.

‘죄인이라.’

잠시 망각하고 있었다. 나 또한 흉수의 모든 조건에 부합하는 인물이라는 것을.

등잔을 들어 멀리 비춰 볼 것이 아니라, 발밑부터 살펴봐야 했었다.

“백 숙부, 그게 무슨…….”

의아함이 담긴 눈빛으로 백상을 바라보던 야율목이 뭔가를 깨닫고 입을 다물었고, 어쩌면 나보다도 빠르게 사태를 파악했을 남호는 작게 탄식했다.

“허, 나도 늙었군. 이런 얕은 수작에 걸려들 줄이야.”

남호의 말은 절반만 맞았다.

이건 분명 얕은 함정이었지만, 그 아래에 파 놓은 구덩이는 깊을 것이다.

한 번 발을 디딘 이상 쉽게 빠져나올 수 없을 만큼.

‘빌어먹을.’

늪에 잠긴 기분이다. 가슴이 답답하고 입안은 모래라도 씹은 것처럼 까끌거렸다.

지그시 눈을 감았다가 뜨자, 어느덧 재판장이 되어 버린 주위 상황이 일목요연하게 느껴졌다.

“지금 백상 대족장님께서 하신 말씀 들었나?”

“죄인이라니. 그럼 설마 저 한족이……?”

곳곳에서 낮은 목소리로 수군거리는 전사들. 이 자리에서 저들의 위치는 참관인이다.

“내 진즉 이럴 줄 알았지. 그러니 처음부터 한족들을 내치자고 누누이 말하지 않았나!”

“으음. 그래도 아직 속단하기에는 이르오.”

“속단은 무슨. 이런 상황에서도 그런 말이 나오나? 감히 이런 짓을 벌일 만한 흉수는 진태경, 저 작자뿐일세!”

속삭이는 전사들과 달리, 언성을 높여 내 죄를 성토하는 부족장들은 배심원들이다. 그리고…….

“당당하군. 마치 아무 잘못도 없다는 것처럼.”

백상. 모두의 앞에서 입을 연 그가 이 빌어먹을 재판의 판사다.

나는 덤덤하기 그지없는 백상의 표정을 바라보며 입술을 뗐다.

“당당할 수밖에 없지. 나는 아무 잘못도 없으니까.”

이제는 더 이상 예의 따위를 논하는 게 우습다.

짤막한 내 대답에 부족장 중 하나가 발끈한 얼굴로 호통쳤다.

“놈! 감히……!”

“감히. 뭐?”

스아아아!

말과 동시에 흘려 보낸 기파(氣波)가 부족장을 향해 쏘아지자, 앞으로 나선 부족장의 얼굴이 백지장처럼 새하얗게 물들었다.

“흡.”

이미 백척간두(百尺竿頭)다.

단 한 걸음만 잘못 내디뎌도 추락하는 상황.

흐름에 따라 주도권을 내어 준다면 그것으로 끝장이다.

나는 조용하게, 그러나 강대한 기파를 흘려 보내며 입을 열었다.

“개나 소나 낄 수 있는 자리가 아니다. 찌그러져 있어.”

“……!”

꿀꺽.

그리고 누군가의 목울대가 크게 일렁인 그 순간이었다.

“소란스럽군.”

묵직한 음성이 바람을 타고 울려 퍼진다.

반사적으로 고개를 돌린 사람들의 시선 끝에, 모두가 알고 있는 한 사람이 요서부의 대문을 넘어 걸어오고 있었다.

‘야수묘왕.’

부릅뜬 호목과 산등성이처럼 장대한 체구.

흡사 태산과도 같은 중압감을 뿜어내는 야수묘왕의 등장에 좌중의 인물들이 황급히 한쪽 무릎을 꿇었다.

“궁주를 뵙습니다!”

하나의 목소리가 되어 울려 퍼지는 외침.

이와 같은 모두의 경외 속에서, 또 다른 부족장들을 거느린 채 천천히 걸음을 옮기던 야수묘왕이 문득 입을 열었다.

“혹시 앞서 말한 그 개나 소에 나도 포함되느냐?”

누구에게 던진 물음인지는 명백하다. 나는 고개를 저었다.

“아닙니다.”

“그렇다면 한 가지 묻겠다.”

깊게 가라앉은 야수묘왕의 목소리가 귓가를 파고들었다.

“태원진가의 진태경. 오늘 이곳에서 벌어진 이 참사와 네가 어떤 연관이 있느냐?”

야수묘왕이 이런 질문을 던지는 이유는, 추궁이나 의심 때문이 아니라 오히려 도와주기 위해서다.

그 사실을 누구보다 잘 알고 있는 나는 망설임 없이 대답했다.

“아무런 연관도 없습니다.”

즉각 내뱉은 내 대답에 곳곳에서 수군거림이 흘러나왔다.

그리고 다음 순간, 야수묘왕을 향해 묵묵히 예를 표하던 한 사람이 몸을 일으켰다.

“지난해, 서쪽 숲에서 화재가 일어났다. 만취한 백족 전사들의 부주의로 벌어진 문제였고, 그로 인해 이백여 마리의 가축과 삼십여 개의 가옥이 불탔지.”

백상이 건조한 목소리로 말을 이었다.

“죄를 지었다면 필벌(必罰)은 마땅한 것. 하여 이 손으로 직접 동족의 전사 일곱을 베어야 했다. 한데 처형 전 유언을 남기라 일렀더니, 하나같이 이리 말하더군.”

감정을 알 수 없는 눈동자는 나를 바라보고 있었지만, 이어지는 백상의 목소리는 야수묘왕을 향하고 있었다.

“나는 결백하다. 술도 마시지 않았고, 불도 지르지 않았다.”

“……!”

“다름 아닌 내궁에서 두 명의 대족장이 사라지고 백여 명의 전사가 몰살당했다. 이는 얄팍한 말 한마디로 면피(免避)할 수 있는 상황이 아니지.”

야수묘왕은 지그시 눈을 감았고, 나는 백상을 응시하며 입을 열었다.

“듣고 있자니 기분 묘해지네. 나도 모르는 사이에 벌써 흉수가 된 것 같고.”

“정말로 결백하다면, 입증해라.”

“입증?”

“그래. 가장 간단하고 손쉬운 방법이지. 네가 흉수가 아니라는 증거를 댄다면 해결될 문제일 테니까.”

내가 뭐라 대답할 틈도 없었다.

말을 끝마치기가 무섭게 돌아선 백상이, 오가는 대화에 웅성거리던 좌중을 향해 이렇게 외쳤기 때문이었다.

“나, 백족의 대족장 백상은 죄인을 추궁하기에 앞서 스스로 결백함을 밝히고자 한다. 이는 하늘과 땅, 그리고 나와 함께 있던 열다섯 명의 부족장을 비롯한 일백의 전사들이 입증할 것이다!”

“……!”

빌어먹을. 처음부터 이걸 노린 거였나?

백상이 충분한 알리바이를 만들어 두었을 거라는 건 충분히 예상했지만, 그 사실을 밝히는 시점과 흐름이 너무나도 절묘했다.

그리고 마치 이 순간만을 기다려 왔다는 듯, 백상을 따르는 부족장들은 누구보다 앞장서서 목소리를 높였다.

“궁주께 아룁니다. 백상 대족장의 말은 한 치의 거짓도 없는 진실이며, 그는 연회가 끝난 직후 우리와 함께 남백부(南白部)에 머무르고 있었습니다.”

“경파족장의 말이 옳습니다! 저를 비롯한 납호족(拉祜族) 역시 하늘에 맹세합니다!”

“와족도 백상 대족장의 말을 보증하겠습니다! 참극이 벌어질 무렵, 우리는 내일 대회의를 대비한 회동을 하고 있었습니다!”

곳곳에서 터져 나오는 부족장들의 호응에 내 뒤에 서 있던 남호는 침음성을 흘렸고, 야수묘왕의 표정은 무거워졌다.

절반에 달하는 부족장들이 스스로 특정 파벌에 가담했음을 노골적으로 밝히고 있었지만, 지금 이 순간만큼은 야수묘왕을 포함한 누구도 그 사실을 지적할 수 없었다.

남만야수궁. 그것도 다름 아닌 내궁에서 두 명의 대족장이 사라지고 일백에 달하는 생명이 참혹하게 몰살당했으니까.

이건 엄청난 중대사다. 공공연한 비밀이 되어 버린 파벌 싸움 따위는 잔물결로 취급할 수 있을 만큼.

그리고…… 마침내 그 순간이 왔다.

“태원진가의 진태경. 이제 네게 묻겠다. 그때 넌 어디에 있었느냐?”

피할 수 없는 질문. 거부할 수 없는 대답.

느껴진다. 백상의 물음이, 사람들의 시선이 보이지 않는 올가미가 되어 내 전신을 옭아매는 것이.

그리고 그와 동시에, 허리춤에 닿은 누군가의 손길이 있었다.

툭.

굳이 고개를 돌려 확인하는 멍청한 짓은 하지 않았다.

이 손길의 주인이 아까부터 줄곧 내 등 뒤에 서 있던 남호라는 사실은 이미 알고 있었으니까.

‘그런데 왜?’

남호가 이러한 행동을 하는 것에는 분명한 이유가 있기 마련.

나는 감각을 최고조로 곤두세운 채 계속해서 손가락의 움직임을 느꼈다.

비록 그 순간은 그리 길지 않았고, 옷깃을 스치는 정도의 미세한 움직임이었으나 나는 이내 그가 전하고자 하는 바를 깨달을 수 있었다.

‘이건…….’

그것은 글씨였다.

짧지만 분명한 뜻을 품고 있는 두 글자.

‘무언(無言).’

남호는 내게 아무 말도 하지 말라고 전하고 있었다.

혹은, 지금 하려는 말을 다시 한번 생각해 보라는 뜻일지도 몰랐다.

그만큼 상황이 불길하게 흘러가고 있었으니까.

‘만약 내가 흑웅과의 만남을 사실 그대로 말한다면?’

그래도 믿어 줄지 의문이다.

아니, 되려 백상과 그를 따르는 부족장들에게 역공당할 가능성이 크다.

흑웅은 아무도 눈치채지 못하게 거처를 빠져나왔다고 했고, 축골공(縮骨功)을 이용해 모습마저 바꾼 상태였다.

‘한마디로 말해서, 입증할 수가 없어.’

최소한 흑웅이 이 자리에 있다면 모를까, 그가 남겨 두고 간 손목이 증언을 해 주지 않는 이상 내 알리바이 입증은 물 건너갔다고 봐야 한다.

하지만 그렇다고 해서 아무 이유도 없이 자리를 비웠다고 말하는 건 스스로 무덤을 파는 꼴이다.

그러니 결국 내가 할 수 있는 대답은 처음부터 정해진 것이나 다름없었다.

“처소.”

수많은 생각이 뇌리를 스쳐 지나갔지만, 그사이에 흘러간 시간은 짧았다. 그리 늦지 않게 대답한 나는 심호흡하며 말을 이었다.

“연회가 끝난 직후 처소에 머무르고 있었다. 그리고 습격을 받았고.”

“습격?”

아직 이에 관한 소식을 들은 이보다, 듣지 못한 이들이 더 많다.

새로운 소식에 좌중이 웅성거리자 야수묘왕이 굳은 얼굴로 입을 열었다.

“진태경의 말은 분명 사실이다. 나 역시 부족을 분간할 수 없는 살수들이 저들을 노렸다는 보고를 들었지.”

이 갑작스러운 상황에 동요하던 야율목도 애써 침착한 목소리로 말을 받았다.

“맞습니다. 저를 비롯한 내궁 호위들 일부가 한 식경 전쯤 현장에 도착했고, 주위를 순찰하던 전사들이 죽은 것 또한 확인했습니다.”

야수묘왕에 이어 야율목까지 거들고 나서자, 주위의 웅성거림이 더욱 커진다.

하지만 처음부터 줄곧 한 사람, 백상을 응시하던 나는 다시 한번 일이 잘못되었다는 것을 깨달았다.

“내궁에서 또 다른 참변이 일어났다는 소식은 나도 들었다.”

차가운 목소리. 무덤덤한 눈빛.

나직하게 뇌까린 백상이 야율목을 향해 말을 이었다.

“하지만 그토록 간단히 내궁에 침입하여 순찰을 돌던 전사들을 제거하고 습격을 벌이다니. 정체가 밝혀지지 않은 살수들이 제법 강했던 모양이군. 그렇지 않느냐?”

미처 말릴 틈도 없이, 야율목의 입술이 열렸다.

“그렇습니다. 살수는 삼십여 명에 달했는데 그들 한 사람 한 사람이 정예 전사 못지 않았…….”

야율목의 말은 끝까지 이어지지 못했다. 아니, 이어질 수 없었다.

다음 순간, 모두의 귓가를 파고드는 백상의 목소리 때문이었다.

“화왕의 진전을 이은 초절정 고수를 죽일 만큼 말이냐?”

“……!”

“……!”

“만약 이 서투르기 짝이 없는 암살 시도가 진태경의 발을 묶기 위함이었다면, 그건 그것대로 이해할 수 없는 일이다. 가만히 놔둬도 처소에 머물러 있었을 자를 구태여 건드려 이목을 끈 셈이니까. 생각할수록 희한하지 않느냐?”

좌중의 공기가 요동치고, 크게 뜨인 수십여 쌍의 눈동자가 쏘아 보내는 시선에 얼굴이 따끔거린다.

하지만 그와는 반대로 마음은 되레 담담해졌다.

이 위기를 빠져나올 자신이 있어서?

아니다. 나는 이미 반쯤 상황을 받아들이고 있었다.

이 함정은 크고 깊었다. 내 생각을 훨씬 뛰어넘을 만큼.

‘도대체 언제부터. 어디까지가 계획이었던 거지?’

해소되지 않은 의문을 담아 백상을 응시하던 나는 불쑥 입을 열었다.

“이대로 끝은 아닌 것 같은데.”

즉각 말뜻을 알아들은 백상이 고개를 끄덕였다.

“감이 좋군.”

“더 할 말이 남았나?”

“아니. 그 대신 보여 줄 것은 있지.”

딱.

건조한 대답과 함께 백상이 손가락을 튕기자, 반쯤 부서진 요서부의 대문으로부터 희미한 인기척이 가까워졌다.

저벅저벅.

보폭이 짧고 불규칙하며, 걸음이 느리다.

마치 병에 걸린 사람처럼. 혹은…….

‘나이 지긋한 노인처럼.’

왠지 모르게 낯익은 인기척의 주인을 알아차린 나는 지그시 눈을 감았다. 그리고 누군가의 늙수그레한 목소리와 함께 눈을 떴을 때.

“배, 백족의 우투리. 대족장님의 부름을 받고 왔습니다.”

서요부의 대문 앞에는 소면 가게의 늙은 주인장이 서 있었다.
```

## Final English reading copy

```markdown
# Chapter 656

Everything was silent.

The warriors gathering the corpses.

The tribal chieftains who had clearly just arrived.

Not a single person was the exception. Everyone in the Western Yao Estate had stopped moving and was staring at this place.

No—their gazes were focused on only one thing.

Me.

And then, the next moment—

“The culprit is walking out on his own two feet.”

A cold voice rang out, shattering the silence.

The instant I met Baeksang’s deeply sunken eyes, a hollow laugh escaped me before I knew it.

“Ha.”

The realization came like a flash of light. I no longer needed to think about how this situation was unfolding.

Everything was contained in the one sentence Baeksang had offered in place of a greeting.

*The culprit.*

For a moment, I had forgotten.

I, too, fit every condition of the culprit.

I should not have been holding up a lantern and searching the distance. I should have been looking at the ground beneath my own feet.

“Uncle Baek, what do you—”

Yayul Mok was looking at Baeksang with a puzzled expression when he realized something and fell silent. Namho, who had perhaps grasped the situation even faster than I had, let out a quiet sigh.

“Huh. I must be getting old. I can’t believe I fell for such a shallow trick.”

Namho was only half right.

This was undoubtedly a shallow trap, but the pit dug beneath it would be deep.

Deep enough that once I stepped inside, I would not be able to climb out easily.

*Damn it.*

I felt as though I had sunk into a swamp. My chest felt tight, and my mouth was gritty, as though I were chewing sand.

I closed my eyes briefly, then opened them again. The situation around me had transformed into a courtroom, and I could see it all with perfect clarity.

“Did you hear what Great Chieftain Baeksang just said?”

“He called him the culprit. Then could that Han Chinese man really be…?”

The warriors whispered in low voices here and there. In this place, they were the spectators.

“I knew this would happen. Didn’t I keep saying from the beginning that we should drive the Han Chinese out?”

“Hm. Even so, it’s too early to jump to conclusions.”

“Too early? How can you say that in a situation like this? The only person capable of committing such a crime is that man, Jin Taekyung!”

Unlike the whispering warriors, the chieftains raising their voices to denounce my crimes were the jury.

And then—

“How bold. As if you haven’t done anything wrong.”

Baeksang, who had opened his mouth before everyone, was the judge of this damn trial.

I looked at his utterly impassive expression and parted my lips.

“I have no choice but to be bold. I haven’t done anything wrong.”

At this point, it was laughable to discuss manners.

One of the chieftains flared up at my brief answer and shouted,

“You bastard! How dare you—!”

“How dare I what?”

Ssshhk!

As I spoke, the wave of qi I released shot toward the chieftain. The chieftain who had stepped forward went as pale as a sheet.

“Ghk.”

I was already balanced atop a hundred-foot pole.

One wrong step, and I would fall.

If I surrendered the initiative to the flow of events, it would all be over.

I quietly released an overwhelming wave of qi and spoke.

“This isn’t a place where any dog or cow can butt in. Sit down and stay out of it.”

“……!”

Gulp.

And it was at that moment, when someone’s throat bobbed heavily, that—

“This is noisy.”

A deep voice carried over the wind.

At the end of the gazes of the people who turned their heads reflexively, a man everyone knew was walking through the gate of the Western Yao Estate.

*The Beast Miao King.*

His tiger-like eyes were wide open, and his body was as immense as a mountain ridge.

He radiated pressure as imposing as Mount Tai itself. At his appearance, everyone present hurriedly dropped to one knee.

“We pay our respects to the Palace Lord!”

Their voices rang out as one.

Amid the reverence of everyone present, the Beast Miao King slowly advanced with several other chieftains behind him. Then he suddenly opened his mouth.

“Am I included among those dogs and cattle you mentioned?”

It was obvious who he was asking. I shook my head.

“No.”

“Then I have a question.”

The Beast Miao King’s deeply lowered voice pierced my ears.

“Jin Taekyung of the Jin Family of Taiyuan. What connection do you have to this tragedy that occurred here today?”

The Beast Miao King had asked the question not to interrogate or suspect me, but to help me.

I knew that better than anyone, so I answered without hesitation.

“None whatsoever.”

My immediate answer drew whispers from all around us.

And then, the next moment, one person who had been silently paying his respects to the Beast Miao King rose to his feet.

“Last year, a fire broke out in the western forest. It happened because of the carelessness of drunken Bai warriors, and as a result, more than two hundred livestock and more than thirty houses burned down.”

Baeksang continued in a dry voice.

“If a crime has been committed, punishment must follow. Thus, I had to cut down seven of my fellow warriors with this hand. But when I told them to leave their final words before their executions, every one of them said the same thing.”

His emotionless eyes were looking at me, but his next words were directed at the Beast Miao King.

“I am innocent. I did not drink, and I did not start the fire.”

“……!”

“Two great chieftains have disappeared from the Inner Palace, and more than a hundred warriors have been massacred. This is not a situation that can be escaped with a single shallow excuse.”

The Beast Miao King slowly closed his eyes. I stared at Baeksang and opened my mouth.

“Listening to you, I’m starting to feel rather strange. It seems I’ve already become the culprit without even knowing it.”

“If you are truly innocent, prove it.”

“Prove it?”

“That’s right. It is the simplest and easiest method. If you produce evidence that you are not the culprit, then the matter will be resolved.”

I did not even have time to answer.

The moment Baeksang finished speaking, he turned around and shouted toward the crowd, which had been murmuring over the exchange.

“I, Baeksang, great chieftain of the Bai people, wish to establish my own innocence before interrogating the culprit. Heaven and earth, along with the fifteen chieftains and the hundred warriors who were with me, will all attest to it!”

“……!”

*Damn it. Was this what he had been aiming for from the beginning?*

I had fully expected Baeksang to have established a sufficient alibi, but the timing and flow with which he revealed it were too perfect.

As though they had been waiting for this very moment, the chieftains following Baeksang raised their voices more loudly than anyone.

“Palace Lord, I report to you. Every word spoken by Great Chieftain Baeksang is the complete truth. He remained with us at the Southern Bai Estate immediately after the banquet ended.”

“The Jingpo Chieftain is correct! I, along with the Lahu people, swear it before Heaven!”

“The Wa people will also vouch for Great Chieftain Baeksang! Around the time the tragedy occurred, we were meeting to prepare for tomorrow’s Tribal Grand Council!”

The chieftains’ responses erupted from every direction. Namho, standing behind me, let out a low groan, while the Beast Miao King’s expression grew heavy.

Nearly half the chieftains were openly declaring that they had joined a particular faction, but at this moment, no one—not even the Beast Miao King—could point it out.

Two great chieftains had disappeared from the Nanman Beast Palace.

And close to a hundred people had been brutally slaughtered in the Inner Palace, of all places.

This was an enormous matter of state—serious enough that the factional struggle, which had become an open secret, could be treated as nothing more than a ripple on the water.

And then…

At last, the moment arrived.

“Jin Taekyung of the Jin Family of Taiyuan. Now I will ask you. Where were you at that time?”

An unavoidable question.

An answer I could not refuse to give.

I could feel Baeksang’s question, along with the gazes of the people around me, wrapping around my entire body like an invisible noose.

And at the same time, someone’s hand touched my waist.

Tap.

I did not make the foolish move of turning my head to check.

I already knew that the owner of that hand was Namho, who had been standing behind me all this time.

*But why?*

There had to be a clear reason for Namho’s actions.

I sharpened my senses to their limit and continued to feel the movement of his fingers.

It lasted only a short while, and the movement was so faint that it merely brushed against my clothes, but I soon understood what he was trying to convey.

*This is…*

He was writing.

Two short characters with a clear meaning.

*No words.*

Namho was telling me not to say anything.

Or perhaps he meant for me to think one more time about what I was about to say.

That was how ominously the situation was unfolding.

*What if I tell them the truth about meeting Heugung?*

Would they even believe me?

No. There was a strong possibility that Baeksang and the chieftains following him would counterattack instead.

Heugung had said he slipped out of his residence without anyone noticing, and he had even changed his appearance with the Bone-Shrinking Technique.

*In short, I can’t prove it.*

If Heugung were here, it might be different. But unless the wrist he had left behind could testify for me, I had to consider proving my alibi impossible.

But saying that I had left my quarters for no reason would be like digging my own grave.

In the end, the answer I could give had been decided from the very beginning.

“My quarters.”

Countless thoughts flashed through my mind, but little time passed. I answered without much delay, then took a deep breath and continued.

“I remained in my quarters immediately after the banquet ended. Then I was attacked.”

“Attacked?”

There were still more people who had not heard about it than those who had.

The crowd began murmuring at the new information, and the Beast Miao King spoke with a stiff expression.

“What Jin Taekyung says is true. I, too, heard a report that assassins whose tribe could not be identified had targeted them.”

Yayul Mok, who had been shaken by this sudden turn of events, followed up in a voice that was deliberately calm.

“That is correct. Some of the Inner Palace guards, myself included, arrived at the scene about half an hour ago. We also confirmed that the warriors patrolling the area had been killed.”

After the Beast Miao King, Yayul Mok also came to my aid, and the murmuring around us grew louder.

But I had been staring at one person the entire time—Baeksang. And I realized once again that things had gone wrong.

“I also heard that another tragedy occurred in the Inner Palace.”

Baeksang murmured in a cold voice, his eyes utterly impassive, then continued toward Yayul Mok.

“But to infiltrate the Inner Palace so easily, eliminate the patrolling warriors, and launch an attack… Those unidentified assassins must have been quite strong. Wouldn’t you agree?”

Before I had time to stop him, Yayul Mok’s lips parted.

“That’s right. There were around thirty assassins, and every one of them was as skilled as an elite warrior—”

Yayul Mok’s words did not reach the end.

No—they could not.

Because Baeksang’s voice pierced everyone’s ears in the next moment.

“Strong enough to kill a Supreme Peak master who inherited the Fire King’s legacy?”

“……!”

“……!”

“If this clumsy assassination attempt was intended to tie Jin Taekyung down, that would be just as difficult to understand. He was going to remain in his quarters even if left alone, so they deliberately attacked him and drew everyone’s attention. Isn’t it strange the more you think about it?”

The air around us churned. Dozens of pairs of wide-open eyes shot their gazes at me, and my face prickled beneath them.

But in contrast, my heart grew calmer.

Was it because I was confident I could escape this crisis?

No.

I had already half accepted the situation.

This trap was large and deep—far beyond anything I had imagined.

*When did it begin? How much of this was part of the plan?*

I stared at Baeksang, my unanswered questions weighing on me, then suddenly opened my mouth.

“I don’t think this is the end.”

Baeksang immediately understood what I meant and nodded.

“Good instincts.”

“Do you still have something to say?”

“No. But I do have something to show you.”

Snap.

With his dry answer, Baeksang snapped his fingers. From the half-destroyed gate of the Western Yao Estate, a faint presence began to draw closer.

Step. Step.

The footsteps were slow, with short and irregular strides.

Like someone who was ill.

Or perhaps—

*Like an elderly man.*

I recognized the owner of the strangely familiar presence and slowly closed my eyes. Then, when I opened them again to the sound of an old man’s voice—

“B-Bai people’s Utu-ri. I came at the great chieftain’s summons.”

The old owner of the noodle shop was standing in front of the Western Yao Estate’s gate.
```
