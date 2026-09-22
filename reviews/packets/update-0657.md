<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0657.txt",
      "sha256": "f274e02757e598157602e5cd763438845d6adccf39138956818b083f922c354c",
      "bytes": 13455
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9d54745c9d1b9a5f7d4fb4909d9e5717f0f0a95218451627a94ffb33fe73ed9a",
      "bytes": 2283
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "ad1a49ceb4f059b7cbc76e6443ae3f2e0e94626f045fc0cb6ab217ce14e6c7d2",
      "bytes": 200768
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "0c907d4520b2e102b52cb993efc73f291ab6f61b9c7cdca98cb7554c70f51ea5",
      "bytes": 828
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "bc76cb8a22980996bfc040966c0b0df6d3106c7f0d0626a657ac81bb81bf17ba",
      "bytes": 814
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "f0184e1b716b5c28750c7d7ed26e2424cab63df2fc8b82209fe222cab96c13b6",
      "bytes": 769
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f16d084d654fbd34014b5981d136d5cb84e633fe81f92c7102cf93b28e9c9cf6",
      "bytes": 1936
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "97e3b090579a4d95003fc075bbf42700e519840bc6a492f49dcd35fab93b0b90",
      "bytes": 622
    },
    {
      "path": "characters/Namho.md",
      "sha256": "58527a8aac51aeb341333b5549b5a3959f86f8087738127b4195e82cafcf0e59",
      "bytes": 843
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "b7198571c239902e1d06c1ea0b672f445fd95112bcdf045eba995c6f7b594eaa",
      "bytes": 871
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e1c51468df24b15e30318fcc6adc99254481d44af8e49443afda05aac083a41b",
      "bytes": 206083
    }
  ],
  "estimated_tokens": 11851
}
-->

# Durable State Update — Chapter 657

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 657. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 657. Profile updates may replace only one
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
  "chapter": 657,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 657,
    "continuity_sources": [657],
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
    "Baeksang has publicly accused Jin of the Inner Palace massacre and backed his own alibi with fifteen chieftains and one hundred warriors.",
    "Namho has warned Jin not to reveal his unverifiable meeting with Heugung, while Baeksang has summoned Utu-ri as a witness."
  ],
  "continuity_sources": [
    656
  ],
  "open_questions": [
    "Who was the Supreme Peak attacker, and what did Dark Heaven seek by intervening directly?",
    "Are Heugung and Yohi alive, and where were they taken?",
    "What can be learned from Yohi's nearly scentless pouch?",
    "Is Baeksang truly colluding with Dark Heaven despite the evidence of third-party intervention?",
    "What testimony or evidence will Utu-ri provide, and how will it affect the accusation against Jin?"
  ],
  "safe_through": 656,
  "temporary_decisions": [
    "Retain Force for 강기 and Supreme Peak for 초절정.",
    "Retain Sound Transmission for 전음.",
    "Render 서요부 as Western Yao Estate and 동이부 as Eastern Yi Estate.",
    "Render 향낭 as scent pouch.",
    "Render 무언 as No words and 남백부 as Southern Bai Estate."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 열화문    | **Fire Gate Clan**               |
| 무림맹    | **Murim Alliance**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 중원     | **Central Plains**                               |                                                       |
| 사숙     | **Martial Uncle**                            |
| 퀘스트              | **Quest**                      |
| 귀가      | **your family**                                                 |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 은자 | **silver nyang** | Silver currency unit. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 천라지망 | **net over heaven and earth** | Jeok Cheongang's figurative threat to pursue a culprit everywhere. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 인시 | **Insi** | The traditional time period from three to five in the morning. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 화원 | **Fire Courtyard** | Courtyard associated with Jin Taekyung and Ju Hwaran's final walk before leaving Sichuan. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 묘시 | **the hour of the Rabbit** | Traditional time period following Insi. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |
| 서요부 | **Western Yao Estate** | Yohi's residence in the western part of the Inner Palace. |
| 우투리 | **Utu-ri** | The old owner of the noodle shop summoned by Baeksang. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 시비 | 진태경 | household_servant_to_visiting_young_hero | Young Hero Jin | formal-polite | The maid summons Taekyung to meet the Family Head. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
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
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 흑웅 | 진태경 | Nanman great chieftain to Central Plains ally and covert contact | you | cautious and informal | Heugung uses 자네 in private Sound Transmission while explaining the missive and Baeksang's alleged collusion. |
| 진태경 | 흑웅 | Central Plains investigator to covert informant and prospective witness | Heugung | blunt and confrontational | Jin questions Heugung's reliability, challenges his claims, and demands proof. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 656
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes, and one of only two Supreme Peak masters in Nanman.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle, opposes the Nanman Beast Palace joining the Murim Alliance, remains distrustful of the Central Plains, and is alleged by Heugung to have colluded with Dark Heaven.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 656
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, is responsible for the forces stationed at Ailao Mountain, has ordered Ju Hwaran, Song Ilseom, and Hyuk Mujin to investigate the Blood Monk in Guizhou, and met the Martial God twice more than fifty years ago.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 656
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung presents as foolish and easily flattered in public but is capable of concealed planning, disguise, and covert contact.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung genuinely loves Yohi and had promised to cooperate with Jin Taekyung; he disappeared alongside Yohi after the assault on the Fire Dragon Pavilion, and his death remains unconfirmed after a severed wrist believed to be his was found at her estate.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 656
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 656
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 656
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 656
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

## Korean source

```text
＃657화



큰 거 온다.

순간 뇌리에 떠오른 직감은 틀리지 않았다. 불과 얼마 전, 흑웅과 함께 앉아 있던 소면 가게의 늙은 주인장이 모습을 드러낸 것이다.

‘시발.’

진짜 큰 게 왔네.

내심 욕설을 중얼거린 나는 늙은 주인장을 바라보았다.

아니, 그를 바라보는 것은 나뿐만이 아니었다. 순식간에 자신을 향해 수많은 시선이 쏠리자, 검버섯이 핀 입술 사이로 떨리는 목소리가 흘러나왔다.

“배, 백족의 우투리. 대족장님의 부름을 받고 왔습니다.”

야수묘왕이 굳은 얼굴로 입을 열었다.

“처음 보는 얼굴이군. 저자는 누구지?”

백상이 눈짓하자 늙은 주인장이 냉큼 대답했다.

“소인은 외궁의 서문 근처에서 소면을 팔고 있습니다. 반평생을 넘게 업으로 삼았지요.”

나는 늙은 주인장의 말과 행동을 통해 몇 가지 새로운 사실을 알게 됐다.

첫째. 늙은 주인장의 이름은 우투리고, 백족이다.

둘째. 우투리는 소면 가게에서 봤던 것과는 달리 말도 잘하고, 귀도 밝다. 한마디로 원기왕성하다. 지리산에 아기 장수 우투리가 있었다면 남만에는 소면 장수 우투리가 있었다.

셋째. 나이가 무색할 만큼 정정한 저 백족 늙은이는, 아마도 자신이 보고 들은 모든 것을 백상에게 말했을 것이다.

마지막 넷째. 나는 아무래도 좆 된 것 같다.



‘이해하시오. 여기 주인장 연배가 구순이 넘어서 귀가 어둡거든.’



흑웅 개새끼야.

소면 가게에서 그가 했던 말은 틀려도 한참 틀렸다.

‘귀가 어둡긴, 시벌.’

어두워진 건 내 미래다.

구십이 넘었다는 주인장은 열 걸음이나 떨어진 야수묘왕의 말도 알아들을 수 있을 만큼 귀가 밝았다.

“우투리, 그대를 부른 이유는 한 가지 사실을 확인하기 위해서다. 이 자리에 있는 이들 중 낯익은 얼굴이 있나?”

“예에.”

백상의 물음에 늙은 주인장은 망설임 없이 고개를 끄덕였고, 나는 새롭게 알게 된 정보에 하나를 더 추가해야 한다는 걸 깨달았다.

다섯째. 우투리는 귀가 밝을 뿐 아니라, 상당한 시력과 기억력의 소유자다.

그 사실을 짐작할 수 있었던 이유는 간단했다.

처음 서요부에 발을 디딘 순간부터 늙은 주인장의 시선은 줄곧 내 얼굴을 힐끔거리고 있었으니까.

“저기 서 있는 젊은이입니다. 가장 키가 크고 체격 좋은.”

소면 그릇을 내려놓을 때만 해도 사시나무처럼 덜덜 떨리던 손이, 어째서인지 이번에는 조금의 미동도 없다.

‘제기랄.’

정확히 나를 향하는 그의 손가락에 나는 입을 다물었고, 좌중의 분위기는 술렁였으며, 백상이 치밀하게 짜 놓은 각본은 결말을 향해 달려가고 있었다.

“그가 확실한가? 단 한 치의 거짓도 없어야 하네.”

백상의 물음에 마른침을 꿀꺽 삼킨 늙은 주인장이 대답했다.

“예, 틀림없습니다. 소인이 나이가 들어 늙긴 했지만, 코앞의 손님을 못 알아볼 정도는 아니지요. 체격이 워낙 컸고, 호랑이 가면을 쓰고 있어서 유독 기억이 남았습니다요.”

“지금 외궁에는 열 중 다섯이 가면을 쓰고 있을 터. 단지 그 정도의 이유로 수상한 자가 있다고 고변(告變)한 건가?”

“그, 그건 아닙니다. 주위를 서성거리다가 자리에 앉아 소면을 시켜 먹었는데, 그 무렵부터 수상쩍다고 느낀 게지요.”

“수상쩍었다? 정확히 어떤 점이 그랬나?”

“그러니까 그것이…….”

나를 힐끔거리던 늙은 주인장이 조심스럽게 말을 이었다.

“가면 때문이긴 합니다요.”

“가면?”

“예에. 소면을 먹는데도 가면을 끝까지 안 벗지 뭡니까. 마치 얼굴을 보여 주면 큰일이라도 날 것처럼 말입니다.”

“그렇군. 계속하게.”

“한데 나중에 국물을 마실 때 영 답답했는지 가면을 슬쩍 올리더군요. 그때 처음이자 마지막으로 얼굴을 봤습니다요.”

그때였구나.

얼굴을 대놓고 드러낸다면 한족임이 들통날 것 같았고, 그렇다고 벗지 않는다면 의심을 살 것 같았다.

해서 일부러 코 아래까지만 가면을 올린 채 소면을 먹다가, 마지막에서야 잠깐 올렸던 건데…….

‘오늘내일할 것 같은 노인네가 그걸 보고 기억할 줄이야.’

처음에는 과한 경계심이 의심을 불렀고, 나중에는 늙은 주인장의 존재를 간과했던 것이 지금의 상황으로 돌아왔다.

그리고 백상은 특유의 담담한 어조로 이 상황의 종지부를 찍고 있었다.

“혼자였나?”

“아닙니다. 웬 중년 사내와 동석했습니다.”

“또 다른 중년 사내라. 그 후에는?”

“거의 동시에 자리를 뜨더니, 이내 서문 쪽 대로(大路)로 향했습니다요.”

“그자의 얼굴을 기억하고 있는가?”

“예에, 물론입죠. 소인이 외궁에서 평생을 살았지만, 근방에서는 처음 보는 낯선 얼굴이었던 터라 기억이 생생합니다. 저 젊은이도 마찬가지였고요.”

“그렇다면 대회의 기간에 넘어온 외부의 부족민이 분명할 테니, 용모파기를 만들어 조사하면 금방 밝혀지겠군. 하면 그들이 언제쯤 떠났나?”

“인시(寅時) 무렵이었고, 일 다경 정도를 머무르다가 자리를 떴습니다. 지금 외궁에서는 일정 시간마다 폭죽을 쏘아 올리고 있어서 똑똑히 기억하고 있습지요.”

늙은 주인장의 대답에는 조금의 막힘도 없었고, 눈빛과 어조는 확신에 가득 차 있었다.

그리고 그를 통해 원하는 대답을 모두 얻어 낸 백상은 작게 고개를 끄덕였다.

“협조해 주어 고맙군. 이만 물러가게. 내 따로 사람을 시켜 상을 내리지.”

“가, 감사합니다. 감사합니다, 대족장님!”

늙은 주인장은 허리를 굽실거리며 사라졌다.

아마 그는 이 자리에서의 일로 매우 후한 포상을 받을 거다. 손님 서너 명만으로도 꽉 들어차던 작은 노점은 커다란 객잔으로 바뀔 테고, 소면을 삶던 주름진 손으로 은자를 세게 되겠지.

하지만 그가 늘그막에 잡은 기회는, 내게 최악의 위기가 되어 돌아왔다.

“참으로 묘한 일이군. 내궁에 있어야 할 자가 은밀히 빠져나와 정체불명의 인물과 접촉하고, 그 직후에 이러한 참극이 일어났다니.”

“…….”

“이미 네가 앞서 했던 말이 거짓임이 밝혀졌지만, 애뇌산의 일을 생각해서라도 마지막 기회를 주지. 항변하겠나?”

백상의 나직한 목소리가 귓가를 파고든 그 짧은 순간, 수많은 생각이 뇌리를 스쳤다.

어느덧 요서부는 숨 막히는 침묵에 잠겼고, 모두의 시선은 내 얼굴을 향하고 있었다.

바로 그때였다.

남호의 손가락이 다시 한번 내 등을 스친 것은.

스륵.

달아날 도(逃).

한 글자였지만, 남호가 말하고자 하는 뜻은 충분히 전해졌다.

‘우선 이 자리를 벗어나서 후일을 도모해라.’

만약 남호가 무공을 익힌 몸이었다면, 이와 같은 전음을 보냈겠지. 아마 내가 그와 같은 입장이었더라도 그랬을 것이다.

‘차라리 사실대로 말했다면 상황이 나아졌을까.’

문득 떠오른 의문에 스스로 답했다. 아니었을 거라고.

물론 지금보다는 조금 나았을지도 모르겠다. 하지만 백상은 철저하게 준비했고, 어떻게든 지금과 같은 상황으로 나를 내몰았을 것이다.

당장 늙은 소면 가게 주인장의 말이 거짓말이라 우길 수도 있겠지만…… 글쎄. 백상이 그 말에 순순히 속아 줄 만큼 멍청했다면 여기까지 오지도 않았을 거다.

‘게다가 백상 정도의 고수라면 우리를 습격한 살수들의 상흔(傷痕)만 봐도 알아차리겠지. 대부분이 내 솜씨가 아니라는 걸.’

내 말을 입증해 줄 흑웅의 존재가 없는 이상, 사실 그대로를 말해도 당당한 흉하가 될 뿐이었다.

‘하긴, 그래도 구라 치다 걸린 흉수보다는 나았겠지만.’

어차피 결국 외통수였다. 어떻게 해도 피할 수 없는.

그리고 지금 이 순간조차 상황은 벼랑 끝으로 내달리고 있었다.

스슥.

미세한 소음이 짧은 침묵 너머로 귓가를 파고든다.

피에 젖은 모래 알갱이가 가죽신에 짓밟히고, 동시에 펄럭인 수십여 개의 옷자락이 화원의 꽃들을 스쳤다.

나를 중심으로 순식간에 완성된 포위망.

그 선두에, 백상이 있었다.

“다시 묻겠다. 항변은?”

항변이라.

나는 심사숙고한 끝에 대답했다.

“더러워서 안 해, 이 씨부랄 새꺄.”

“……!”

“……!”

아마 이런 대답은 미처 예상하지 못했던 모양이다. 의외라는 눈빛으로 나를 바라보던 백상이 고개를 끄덕였다.

“스스로 죄를 인정하는 건가?”

“거짓말을 한 것만은 인정하지. 내가 멍청했다.”

“결국, 끝까지 부인하겠다는 뜻이군.”

“너 같으면 인정하겠냐? 아니, 애초에 죄가 없으니 인정하고 말 것도 없다. 피할 수 없는 함정에 발을 디딘 게 좆 같을 뿐이지.”

“만약 억울하다면 순순히 투항해라. 시시비비(是是非非)를 명확히 가려 줄 테니.”

“퍽이나 그러겠다, 시시발발 새끼야.”

코웃음 섞인 내 대답에 백상의 눈동자가 깊게 가라앉았다.

“그럼 어쩔 수 없군.”

그와 동시에.

스릉. 츠츠츠츠!

빛살처럼 뽑혀 나온 새하얀 검신으로부터 눈부신 광휘가 솟구쳤다. 검강(劍罡)이 깃든 애검을 늘어트린 백상이 느릿하게 걸음을 내디디며 입을 열었다.

“남만야수궁의 전사들은 들어라. 지금부터 전력을 다해 죄인 진태경을 포박할 것이니, 한 치의 실수도 용납되어서는…….”

그리고 그 순간. 어디선가 터져 나온 포효 같은 외침이 이어지려는 백상의 목소리를 뒤덮었다.

“백상!”

감히 백족의 대족장을 이렇게 부를 수 있는 사람은, 남만을 통틀어 단 한 사람뿐이다.

“모두 멈추지 못할까!”

화아아악!

사방을 짓누르는 강대한 기파(氣波).

서서히 좁혀 들어오던 포위망을 말 한마디로 정지시킨 야수묘왕이 이글거리는 눈동자로 백상을 노려보았다.

“이게 무슨 짓이냐.”

거친 기세에 모두가 몸을 떨었지만 백상은 달랐다. 그는 담담한 목소리로 대답했다.

“궁주께서 보고 계시는 그대로입니다. 이 자리에서 죄인 진태경을 포박할 것입니다.”

“잊었느냐? 그는 무림맹의 각주이며, 우리의 오랜 우방(友邦)인 열화문의 사람이다.”

“다른 누구도 아닌 남만야수궁의 궁주께서, 단지 그런 이유로 흉수를 비호하시는 겁니까?”

“헛소리! 저 녀석은 흉수가 아니다. 애뇌산에서의 일을 벌써 잊었느냐! 이런 짓을 할 명분도 없고, 이유도 없어!”

“하지만 그를 본 증인과 명백한 정황이 있지요.”

“그런…….”

“애뇌산의 일은 저를 비롯한 이 자리의 모두가 똑똑히 기억하고 있습니다. 그러니 수고를 무릅쓰고 포박하고자 하는 것입니다. 물론 그가 저항한다면 생사불문(生死不問)이라는 조건이 앞에 붙겠지만 말입니다.”

“백상!”

“아직 끝나지 않았습니다.”

백상의 서늘한 목소리가 이어졌다.

“만약 진태경이 무력으로 이 자리를 벗어난다면, 남만 전체에 천라지망(天羅蜘網)을 펼쳐 전력을 다해 추살할 것입니다. 그전에 저자의 휘하에 있는 다른 한족들은 좋은 본보기가 되겠지요.”

“……!”

사실상 중원과의 전쟁도 불사하겠다는 뜻이 담긴 백상의 말에 야수묘왕은 눈을 부릅떴고, 야율목은 일그러진 얼굴로 외쳤다.

“숙부!”

“이는 군신(君臣)이 아닌 부족장들 간의 대화다. 아무런 권한도 없는 소궁주는 빠져라.”

“하지만 어찌! 어찌 감히 홀로 그런 독단(獨斷)을 내릴 수 있단 말입니까!”

“독단이라…….”

작게 뇌까린 백상이 문득 고개를 들어 하늘을 바라본다.

어느덧 사방에 내려앉아 있던 짙은 어둠이 흩어지고, 동쪽으로부터 환한 빛이 서서히 번져 오고 있었다.

“보이느냐? 벌써 묘시(卯時)다. 동이 트고 있어.”

“갑자기 그게 무슨.”

“지금 이 자리에서 이틀 차 대회의를 시작한다면 어떻겠느냐? 물론 새로운 안건은…….”

츠츠츠.

백상의 손에 들린 검이 한층 강렬한 빛을 피워올렸다.

“한족 진태경에 대한 생사(生死).”

그리고 그 순간. 이 세상에서 오직 한 사람만이 들을 수 있는 종소리가 내 귓가를 파고들었다.

띠링.



- 돌발 퀘스트, [양자택일(兩者擇一)]이 생성되었습니다!
```

## Final English reading copy

```markdown
# Chapter 657

*Something big is coming.*

The instinct that flashed through my mind was not wrong. The old owner of the thin-noodle shop where I had been sitting with Heugung just moments ago had appeared.

*Fuck.*

Something really big had come.

I cursed inwardly as I stared at the old shopkeeper.

No, I was not the only one looking at him. As countless gazes instantly converged on him, a trembling voice emerged from between his age-spotted lips.

“U- Utu-ri of the Bai people. I came at the great chieftain’s summons.”

The Beast Miao King spoke with a grim expression.

“I’ve never seen this face before. Who is he?”

At Baeksang’s signal, the old shopkeeper hurriedly answered.

“I sell thin noodles near the West Gate of the Outer Palace. I’ve made a living at it for more than half my life.”

From the old shopkeeper’s words and actions, I learned several new things.

First. The old shopkeeper’s name was Utu-ri, and he was a member of the Bai people.

Second. Unlike when I had seen him at the noodle shop, Utu-ri spoke clearly and had excellent hearing. In short, he was full of energy. If Jirisan had its baby hero Utu-ri, Nanman had a noodle-selling Utu-ri.[^1]

Third. This Bai elder, whose vitality belied his age, had probably told Baeksang everything he had seen and heard.

And fourth. I was probably completely screwed.

*You have to understand. The owner here is over ninety, so his hearing is bad.*

*You fucking bastard, Heugung.*

What he had said at the noodle shop had been wrong. Very wrong.

*His hearing is bad, my ass.*

The thing that had grown dim was my future.

The shopkeeper, who was supposedly over ninety, had hearing sharp enough to catch every word spoken by the Beast Miao King ten paces away.

“Utu-ri, there is one reason I called you here. I wish to confirm one fact. Do you recognize anyone among those gathered here?”

“Yes.”

The old shopkeeper nodded without hesitation at Baeksang’s question, and I realized I had to add one more item to the list of things I had learned.

Fifth. Utu-ri possessed not only excellent hearing, but also remarkable eyesight and memory.

The reason I could guess that much was simple.

From the moment the old shopkeeper had first set foot in the Western Yao Estate, his gaze had kept darting toward my face.

“That young man standing over there. The tallest one, with the largest build.”

The hand that had trembled like an aspen tree when he set down the bowls of noodles was, for some reason, perfectly still this time.

*Damn it.*

His finger pointed directly at me. I shut my mouth, the atmosphere around us began to stir, and the script Baeksang had meticulously prepared raced toward its conclusion.

“Are you certain it was him? There must not be the slightest lie in your answer.”

The old shopkeeper swallowed hard before answering Baeksang’s question.

“Yes, without a doubt. I may be old and worn-out, but I’m not so blind that I can’t recognize a customer standing right in front of me. His build was exceptionally large, and he was wearing a tiger mask, so he stood out in my memory.”

“Half the people in the Outer Palace must be wearing masks right now. Did you report him as suspicious for no reason beyond that?”

“N-No, that wasn’t it. He lingered nearby, then sat down and ordered noodles. That was when I began to feel something was strange.”

“Strange? What exactly was strange?”

The old shopkeeper, who had been glancing at me, continued cautiously.

“It was because of the mask, sir.”

“The mask?”

“Yes. Even while eating the noodles, he never took it off. It was as if something terrible would happen if he showed his face.”

“I see. Continue.”

“But later, when he drank the broth, the mask must have felt too restrictive, because he raised it slightly. That was the first and only time I saw his face.”

So that was when it happened.

If I openly revealed my face, they might realize I was Han Chinese. But if I never removed the mask, I would arouse suspicion.

So I had deliberately raised it only to just below my nose while eating the noodles, then lifted it properly for a moment at the very end…

*Who would have thought that old man, who looked like he could die tomorrow, would notice and remember that?*

At first, my excessive caution had drawn suspicion. Later, overlooking the existence of the old shopkeeper had brought me to this situation.

And now Baeksang was putting an end to it all in his uniquely calm voice.

“Were you alone?”

“No. He was sharing a table with some middle-aged man.”

“Another middle-aged man. What happened after that?”

“They left almost at the same time, then headed toward the main road by the West Gate.”

“Do you remember that man’s face?”

“Yes, of course. I’ve lived in the Outer Palace all my life, but he was a stranger I had never seen in the area, so I remember him vividly. The same goes for that young man.”

“Then they were certainly outsiders who entered during the Tribal Grand Council. If we make likenesses of them and investigate, it should be easy to identify them. When did they leave?”

“It was around Insi, and they stayed for about the time it takes to drink a cup of tea before leaving. The Outer Palace has been setting off firecrackers at regular intervals, so I remember the time clearly.”

The old shopkeeper answered without a single hesitation. His eyes and voice were filled with certainty.

Having obtained every answer he wanted through the old man, Baeksang gave a small nod.

“Thank you for your cooperation. You may withdraw now. I’ll have someone give you a reward separately.”

“Th-Thank you. Thank you, Great Chieftain!”

The old shopkeeper bowed repeatedly as he disappeared.

He would probably receive an extremely generous reward for what he had done here. The small stall that had been packed whenever three or four customers showed up would become a large inn, and the wrinkled hands that had boiled noodles would soon be counting silver nyang.

But the opportunity he had seized in his old age had returned to me as the worst crisis of my life.

“What a strange matter. Someone who should have been in the Inner Palace secretly slipped out, made contact with an unidentified figure, and then this tragedy occurred immediately afterward.”

“……”

“Your earlier statement has already been exposed as a lie, but even considering what happened at Ailao Mountain, I will give you one final opportunity. Do you wish to make a defense?”

In the brief moment Baeksang’s low voice pierced my ears, countless thoughts flashed through my mind.

By then, the Western Yao Estate had fallen into suffocating silence, and everyone’s gaze was fixed on my face.

That was when it happened.

Namho’s finger brushed against my back once again.

Sssrk.

*Escape.*

It was only one word, but I understood exactly what Namho meant.

*Get out of here first. We’ll make plans for later.*

If Namho had known martial arts, he would have sent me this kind of Sound Transmission. If I had been in his position, I probably would have done the same.

*Would things have improved if I had simply told them the truth?*

I answered my own sudden question.

No.

Of course, things might have been a little better than they were now. But Baeksang had prepared thoroughly. He would have driven me into a situation like this somehow.

I could insist that the old noodle-shop owner’s statement was a lie, but… please. If Baeksang were stupid enough to fall for that so easily, he never would have made it this far.

*Besides, a master like Baeksang would realize just by looking at the wounds on the assassins who attacked us that most of them weren’t my handiwork.*

Without Heugung there to corroborate my statement, telling the truth would only make me a shameless culprit.

*Though I suppose that would still be better than being a culprit caught lying.*

Either way, I was trapped. There was no way to avoid it.

And even now, the situation was racing toward the edge of a cliff.

Sssrk.

A faint sound pierced my ears through the brief silence.

Blood-soaked grains of sand were crushed beneath leather shoes, while dozens of fluttering hems brushed against the flowers in the garden.

An encirclement had formed around me in an instant.

At its head stood Baeksang.

“I’ll ask you again. Do you wish to make a defense?”

A defense.

After thinking long and hard, I answered.

“I’m not doing it. This whole thing is too damn filthy, you fucking bastard.”

“……!”

“……!”

They probably had not expected an answer like that. Baeksang looked at me with surprise, then nodded.

“Are you admitting your guilt?”

“I admit only that I lied. I was stupid.”

“So in the end, you mean to deny it to the very end.”

“If you were me, would you admit it? No. I didn’t commit a crime in the first place, so there’s nothing to admit. It just pisses me off that I stepped into an inescapable trap.”

“If you believe you have been wronged, surrender quietly. I will determine right and wrong.”

“Yeah, fucking right, you right-and-wrong bastard.”

At my scornful reply, Baeksang’s eyes sank into darkness.

“Then it cannot be helped.”

At the same time—

Shing. Tsstststst!

A dazzling radiance surged from the pure-white blade he drew in a flash. Baeksang lowered his treasured sword, infused with Sword Force, and slowly stepped forward.

“The warriors of the Nanman Beast Palace, listen. From this moment onward, we will use our full strength to take the criminal Jin Taekyung into custody. Not a single mistake will be tolerated—”

At that moment, a roar-like shout erupted from somewhere, drowning out the words that were about to leave Baeksang’s mouth.

“Baeksang!”

Only one person in all Nanman could address the great chieftain of the Bai people that way.

“Will everyone stop this at once!”

Whoosh!

A powerful wave of aura pressed down from every direction.

The Beast Miao King halted the slowly tightening encirclement with a single command, then glared at Baeksang with blazing eyes.

“What do you think you’re doing?”

Everyone trembled beneath his fierce aura, but Baeksang did not. He answered in a calm voice.

“You can see exactly what I’m doing, Palace Lord. I intend to take the criminal Jin Taekyung into custody here.”

“Have you forgotten? He is a pavilion master of the Murim Alliance and a member of the Fire Gate Clan, our longtime ally.”

“Are you, of all people, the Palace Lord of the Nanman Beast Palace, shielding the culprit for no reason beyond that?”

“Ridiculous! That boy is not the culprit. Have you already forgotten what happened at Ailao Mountain? He has neither the justification nor the reason to do something like this!”

“But we have a witness who saw him, as well as clear circumstantial evidence.”

“But—”

“Everyone here remembers what happened at Ailao Mountain clearly, myself included. That is why I am taking the trouble to place him under arrest. Of course, if he resists, the order will be to take him dead or alive.”

“Baeksang!”

“We are not finished yet.”

Baeksang’s cold voice continued.

“If Jin Taekyung leaves this place by force, I will spread a net over heaven and earth across all Nanman and pursue him with everything we have. Before that happens, the other Han Chinese under his command will make excellent examples.”

“……!”

The Beast Miao King’s eyes widened at the meaning behind Baeksang’s words—he was prepared to risk war with the Central Plains.

Yayul Mok shouted with a twisted expression.

“Uncle!”

“This is a conversation between tribal chieftains, not between lord and subject. The Young Palace Lord, who has no authority here, should withdraw.”

“But how could you! How could you dare make such a unilateral decision on your own!”

“A unilateral decision…”

Baeksang muttered the words softly, then suddenly raised his head and looked at the sky.

The thick darkness that had settled over the surroundings had begun to disperse, and bright light was slowly spreading from the east.

“Can you see it? It is already the hour of the Rabbit. Dawn is breaking.”

“What does that have to do with this all of a sudden?”

“What would you say if we began the second day of the Tribal Grand Council right here and now? Of course, the new agenda would be…”

Tsst.

The sword in Baeksang’s hand blazed with even more intense light.

“Whether Han Chinese Jin Taekyung lives or dies.”

At that moment, a sound like a bell that only one person in this world could hear pierced my ears.

Ding.

> **System**
>
> An unexpected **Quest**, **Either-Or**, has been generated!

[^1]: Utu-ri is a legendary Korean child hero associated with Jirisan. Jin is comparing that figure to the elderly noodle seller who happens to share the name.
```
