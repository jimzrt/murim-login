<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1059.txt",
      "sha256": "d05d70a81e6269426a2299c23ea5db573fa903971f6efb7d4413a268e13baa4d",
      "bytes": 13349
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "78153ead4ddebee20c18bc4e248872fd5073adbd26e7942b80364990df814285",
      "bytes": 1548
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "00393f64552a324b59de22435e669f9c3775156bdb7d88fb36f641805263e183",
      "bytes": 241117
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "305ea2b637921a8bb2af3bc26672abc4b648e467468b8679cf71e149b245413e",
      "bytes": 760
    },
    {
      "path": "characters/Hyeoncheon.md",
      "sha256": "27164be7a01734a836e1c9eca0dc1d573fb62a5dcf50a26278a5e32fa7a97514",
      "bytes": 599
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "0f07218b13545c873b5f1b6510a4fa6b00a24965babd4a65817a3d46de45e2ef",
      "bytes": 1502
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "d179896461f3c25e7942fce509571797dea6309f44e65db5a872e9a51f21c5aa",
      "bytes": 850
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "ae6cf9d9bb69877e204eaebe096b5ecc8f5fd4f0c1e5f46e2f9fb23188a29928",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "63565749fa11fa0c3684c530a89be1e03f64c3a4257e94ed92dd6f86b55e3cfe",
      "bytes": 282603
    }
  ],
  "estimated_tokens": 10797
}
-->

# Durable State Update — Chapter 1059

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
1 and safe_through 1059. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1059. Profile updates may replace only one
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
  "chapter": 1059,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1059,
    "continuity_sources": [1059],
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
    "Sama Pyo has approached Hyeoncheon and offered to accept punishment for his deceased father Sima Gong’s crimes; Hyeoncheon has drawn his sword.",
    "Hyeoncheon and roughly a hundred surviving Kongtong Disciples believe Sima Gong and other Gansu leaders betrayed them at Dunhuang.",
    "Sima Gong, Song Il, and Hwangbo Eom are dead; the Kongtong survivors reached the battlefield before learning of their deaths.",
    "Sama Pyo deliberately left Namho clues about his father’s covert actions to protect their companions without openly accusing his father.",
    "Sama Pyo intends to leave the Fire Dragon Pavilion and face what lies ahead alone; Jin Taekyung calls him a friend and orders him not to die.",
    "The Lord of Heaven’s identity and connection to Asmodeus remain unknown.",
    "Some Kongtong Sect survivors vanished to an unknown location.",
    "The Grand Mage departed for Qinghai on a new mission; the identity of the other servant remains unknown.",
    "A mysterious green light remains in the dispersing darkness."
  ],
  "continuity_sources": [
    1057,
    1058
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven, and is he connected to Asmodeus?",
    "Where did the missing Kongtong Sect survivors go?",
    "What is the new mission in Qinghai, and who is the other servant there?",
    "What is the mysterious green light?",
    "Will Hyeoncheon strike Sama Pyo down?"
  ],
  "safe_through": 1058,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 궁성     | **Bow Saint**                 | —              |
| 무림맹    | **Murim Alliance**               |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 마적     | **mounted bandits**                              |                                                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 게이트     | **Gate**              |
| 하남     | **Henan**              |
| 청해     | **Qinghai**            |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 현천진인 | **Perfected Being Hyeoncheon** | Current Sect Leader of Wudang and Hyeongong's Senior Brother. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 숭산 | **Mount Song** | Mountain where Shaolin Temple is located. |
| 점혈 | **Pressure-Point Strike** | System-named technique used by Jeok Cheongang on Taekyung. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 절체절명 | **Life-or-Death Crisis** | Sudden System Quest forcibly accepted during the confrontation at Mount Song. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 인자 | **ninja** | Japanese assassin skilled in concealment and concealed weapons. |
| 대초자곤 | **two-section staff** | Weapon carried by Sama Pyo's giant subordinate. |
| 검기상인 | **the level of injuring others with Sword Energy** | Realm description used for Moon Beauty Saber. |
| 숭산결의 | **Mount Song Resolution** | The event marking the formal gathering of the Murim Alliance at Mount Song. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 호거아 | **Tiger Giant Child** | Epithet for Taishan. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 한스 | **Hans** | Hunter killed by a dagger during the battle. |
| 돈황 | **Dunhuang** | City identified as the foremost defensive line in Gansu. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 현천진인 | 사마표 | Kongtong Sect Leader confronting the son of a man he believes betrayed the survivors | Sama family boy | formal, then cold and severe | Initially addresses him as 도우, then shifts to 사마가의 아해야 before demanding that he bring his father. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1058
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyeoncheon.md

# Perfected Being Hyeoncheon (현천진인)

- **Safe through:** Chapter 1058
- **Aliases:** None
- **Role:** Perfected Being Hyeoncheon is the current Sect Leader of the Kongtong Sect, a veteran Daoist master, and a Supreme Peak martial artist.
- **Personality:** Grave, dignified, reflective, and burdened by memories of the Great Faction War.
- **Voice:** Measured, solemn, and calm with the authority of a Sect Leader.
- **Relationships:** Hyeongong is his Junior Brother, and both studied under the same master from childhood.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1053
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1058
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Courteous and calculating, he chooses what he believes is right over expedience and accepts responsibility for his choices, even when they expose him to blame.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo is Sima Gong’s son and chosen heir, commands Taishan, and is Jin Taekyung’s friend; he deliberately let Namho suspect his father’s actions to protect their companions, was Ju Hwaran’s former fiancé, and is hostile toward Song Ilseom.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1058
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
1059화




그것은 나와 다른 이들에게 있어, 아주 짧은 찰나의 순간이었을 뿐이다.

비록 누군가에게는 터무니없이 느리고 숨 막히게 느껴지는, 주마등(走馬燈)의 일부였겠지만.

스릉.

예리한 강철이 자신을 가둔 검갑을 스치듯 빠져나가는 소리는 소름이 돋을 정도로 희미했고, 이는 곧 완벽에 가까운 발검술(拔劍術)을 의미했다.

한 치의 오차도 없는, 가장 적절한 힘과 속도.

그리고…….

주인의 의지를 따라 목표를 비스듬히 가로지르는, 명확한 궤적.

서걱!

회피하기에는 너무나도 가까웠던 거리. 너무나도 큰 무위의 격차.

거기에 더해 마치 스스로의 운명을 받아들이듯, 피할 의지조차 보이지 않은 채 조용히 눈을 감은 사마표까지.

당연하게도 그 어떤 이변조차 일어나지 않았고, 순간을 쪼개며 번뜩인 검광(劍光)은 허공에 붉은 꽃을 흩뿌렸다.

촤아악!

멈췄던 시간이 흐른다.

비틀거리는 사마표의 뒷모습 너머로, 높게 솟구치는 피분수가 모두의 망막을 선명하게 물들인다.

가까이에 있던 공동파의 제자들은 물론이고 나와 화룡각 대원들.

거기에 더하여, 당장이라도 달려가고 싶은 마음을 온 힘을 다해 억누르고 있던 누군가 역시도.

“안 돼!”

사마표를 중심으로 이어지던 모든 상황을 초조하게 지켜보던 태산의 인내심은 딱 거기까지였다.

사방을 떨쳐 울리는 천둥 같은 고함과 함께, 목말을 타고 있던 불쌍한 노인을 던지듯 내려놓은 구척장신의 거구(巨軀)가 지금껏 본 적 없는 맹렬한 속도로 쏘아졌다.

화아악!

바람 소리는 거칠었으나 나아가는 방향은 더할 나위 없이 올곧다.

누가 말릴 틈새도 없이 포탄처럼 튀어 나간 태산의 신형은 오직 한 사람, 비틀거리며 뒷걸음질 치고 있는 사마표의 등 뒤를 향해 뻗어 나가는 중이었다.

마치, 포위하듯 사마표의 주위를 에워싸고 있던 공동파의 제자들 따위는 안중에도 없다는 듯이.

“놈!”

“멈추지 못할까!”

파파팟!

곳곳에서 동시다발적으로 터져 나온 대갈일성(大喝一聲)과 함께 흐릿해지는 신형들.

표홀한 움직임으로 경로를 가로막은 수십여 명의 공동파 제자들이 저마다의 병장기를 들어 태산을 겨누었다.

잔혹하고도 처절했던 돈황의 전투에서 어찌 살아남을 수 있었는지를 증명하듯, 핏물로 끈적이는 그들의 날붙이에는 하나같이 검기상인(劒氣傷人)의 경지에 올랐음을 증명하는 빛줄기가 맺혀 있었다.

그러나 그것은 수십의 절정 고수가 앞길을 가로막았음에도, 오히려 더 맹렬한 속도로 쏘아지고 있는 태산의 손에 들린 대초자곤(大相子根) 역시 마찬가지였다.

“크아아아아!”

호거아(虎巨兒).

별호에 담긴 의미 그대로 평소에는 순수한 어린아이 같으나, 그 타고난 용력과 무위는 그야말로 맹수와 다름없는 태산이다.

분노한 호랑이처럼 포효한 태산이 온 힘을 다해 휘두른 대초자곤을 따라 엄청난 광풍이 휘몰아쳤다.

후우우웅!

닳고 닳은 무림인이라 해도 등골이 서늘해질 수밖에 없는 무시무시한 파공성.

하지만 공동파의 제자들은 한 걸음도 물러서지 않았다.

아니, 오히려 흉흉한 기색으로 짓쳐 드는 태산을 향해 휘황한 검광을 흩뿌렸다.

쐐애액!

순식간에 강렬한 살의(殺意)가 공간을 뒤덮는다.

바람을 짓뭉개며 나아가는 대초자곤과, 바람을 가르며 쏘아지는 칼날들.

그리고 그 절체절명의 순간을 비집으며, 나는 힘주어 발걸음을 내디뎠다.

쉭.

한 걸음.

단 한 걸음이면 족했다.

그것으로 수 장의 공간이 단숨에 지워지고 주위의 풍경이 뒤바뀐다.

어느덧 태산과 공동파 제자들 사이를 파고든 나는, 망설임 없이 쌍장(雙掌)을 뻗었다.

파앙!

압축된 공기가 폭발한다. 양 손바닥을 타고 한껏 억제된 화염신장의 열풍(熱風)이 터져 나와 모든 것을 밀어냈다.

서로를 향해 흉흉하게 휘둘려지던 병장기들은 물론, 그것을 쥐고 있던 주인들의 몸뚱어리까지도.

촤르륵!

목적을 이루지 못한 채 허공으로 솟구친 무기들과 바람 앞의 갈대처럼 휘청이며 물러나는 신형들.

“……!”

“……!”

피로 뒤덮인 와중에도 지면에서 뿌옇게 일어난 먼지 너머, 불가항력(不可抗力)에 의해 뒷걸음질 친 황망한 얼굴들을 향해 나는 피로에 젖은 목소리로 툭 내뱉었다.

“다들 힘이 썩어나나. 적당히들 하지.”

그리고 누군가 뭐라 대답하기도 전, 눈앞에서 벌어진 이 갑작스러운 상황을 말없이 지켜보고만 있던 현천진인을 향해 재차 입을 열었다.

“뒤늦게나마 인사드립니다. 일전에 하남(河南)에서 한번 뵈었었죠.”

신 무림맹이 처음으로 탄생했던 숭산결의(嵩山決意) 당시, 짧게나마 안면을 튼 적이 있던 현천진인이 작게 고개를 끄덕였다.

“오랜만이군, 진 도우(道友).”

나는 문득 마음 한구석이 아려왔다.

비록 일각 남짓도 되지 않은 짧은 과거의 인연이었음에도 그랬다.

과거, 친할아버지와 같은 인자한 음성과 웃음으로 내 무공을 칭찬했던 노도사는 이제 어디에도 없다.

귓가에 닿은 현천진인의 목소리는 사막의 모래 알갱이처럼 파삭거렸고, 그의 입가에는 슬픔과 분노의 잔재가 남아 있었다.

주름진 손아귀에 잡힌 채 파르르 떨리고 있는 검신처럼.

아마도 노도사와 평생을 함께했을 애병의 끝에서 천천히 떨어지는 핏물은, 지금 이 순간에도 완전히 털어내지 못한 감정 때문이리라.

“각주! 이게 무슨 짓인가! 당장 비켜라!”

그래, 저 녀석이 있었지.

그제서야 정신을 차린 태산의 고함에, 나는 잠시 깊이 빠져있던 감정의 늪에서 빠져나올 수 있었다.

그리고 동시에, 어느새 대초자곤을 고쳐잡으며 앞으로 나서는 녀석을 불러세웠다.

아주 조금은, 나만의 거친 방식으로.

퍽!

정확히 복부를 파고든 일권에, 새우처럼 굽혀진 구척장신의 거구가 딱딱하게 굳는다.

자신도 모르게 흡, 하고 헛숨을 삼킨 태산이 부릅뜬 눈으로 나를 바라보며 목소리를 쥐어 짜냈다.

“가, 각주…….”

“머리 좀 식혀.”

나직한 한 마디와 함께, 나는 망설임 없이 녀석의 뒷목을 손날로 후려쳤다.

쿵.

어지간해서는 점혈도 안 먹힐 것 같은 두꺼운 피부와 뼈를 지닌 강골도 압도적인 힘 앞에서는 무소용인 법.

흡사 곰이 쓰러지는 소리와 함께 침묵이 찾아왔다.

한발 늦게 도착한 화룡각 대원들도, 태산을 향해 재차 달려들려던 공동파의 제자들도 당황한 얼굴로 나를 바라보았다.

단 한 사람, 침잠한 눈빛으로 상황을 주시하던 현천진인을 제외하고.

“풍문에 의하면 어린 흑룡 옆에 거대한 대호가 있다더니…… 듣던 대로 힘이 넘치는군. 충성심도 대단하고.”

현천진인이 미동조차 없이 쓰러져 있는 사마표를 바라보며 뇌까렸다.

“보기보다 좋은 수하를 두었어. 그렇지 않나?”

“덩치만큼이나 멍청해서 그렇지, 착한 녀석은 맞습니다. 그리고…….”

나는 씁쓸한 표정으로 덧붙였다.

“장문인께서 자비를 베풀어 주신 저 친구도, 생각하시는 것보다 훨씬 괜찮은 녀석이고요.”

“……!”

“……!”

순간, 주위의 공기가 찌르르 울렸다.

내 말에 담긴 의미를 깨달은 이들은 약속이라도 한 것처럼 동시에 눈을 부릅떴고, 현천진인은 말없이 눈을 감았다.

마치, 아직 마음속에 남아 있는 살심(殺心)을 애써 지워 내려는 듯.

“후회……하십니까?”

침묵을 깨트린 나는 현천진인을 응시했다.

앞서 그가 허리춤에서 검이 뽑아 휘두른 순간부터, 나는 본능적으로 알고 있었다.

저 완벽한 발검술에는, 갈등이 서려 있을지언정 조금의 살기도 담겨 있지 않다는 것을.

결국 노도사의 검은 누군가의 목숨을 끊어 내지 못하리라는 것을.

그랬기에 나서지 않았다.

흔들린 검 끝이 사마표의 피륙을 얕게 베었으나, 이는 마지막 남은 한 줌의 갈등 때문이라는 것을 충분히 느끼고 있었으니까.

“후회라, 물론일세.”

“한데 어째서.”

“눈을. 그 눈을 보았으니까.”

현천진인은 불현듯 눈을 떴다. 그리고 자신의 머리 위에서 펄럭이는, 공동파의 깃발을 응시하며 말을 이었다.

“돈황에서 마지막으로 보았던 제자들의 눈을 닮아 있었네. 깊고, 올바르며, 죽음 앞에서도 굽히지 않는. 그런 눈이었지.”

혹자는 말한다.

사람의 눈은, 마음의 창이자 거울이라고.

아마도 그래서였을 것이다.

복수심을 간직한 채 이곳에 온 노도사가, 스스로 죽음을 찾아온 원수의 혈육을 끝끝내 죽이지 못한 것은.

“빈도(貧道)는 한낱 말코 도사일세. 도가의 경전보다는 검에 심취하여 일평생을 살았고, 피를 흘리며 죽어 가는 제자들을 구할 수도 없었지. 하지만…….”

파르르 떨리는 입술 사이로 뜨거운 숨결이 흘러나왔다.

“근래에 만난 누군가가 이런 말을 하더군. 단지 원수의 피를 이었다는 이유 하나만으로 목숨을 거둔다면, 그것이야말로 마도(魔道)가 아니고 무엇이겠냐고.”

나는 알 수 있었다.

비록 현천진인의 목소리는 나를 향하고 있을지라도, 그 안에 담긴 뜻은 공동파의 제자 모두를 아우르기 위한 것이라는 것을.

철퍽.

누군가의 손아귀에서 미끄러진 검이 피 웅덩이에 처박힌다.

불과 촌각 전만 하더라도 숨 막히는 살기를 뿜어내던 그들은, 어느 순간부터 넋 나간 눈빛으로 서로를 바라보고 있었다.

마치 머리부터 발끝까지 피를 뒤집어쓴 자신들의 사형제를 통해, 살아남은 적들을 찾아내어 가축처럼 도살하던 스스로의 모습을 떠올리듯이.

그리고 눈물을 삼켰다.

소리 없이. 눈앞을 스치는 그리운 얼굴들과 감정을 애써 억누르며.

“복수는 반드시 이룰 것이나, 복수를 행함에 있어 연좌(緣坐)는 없다. 오늘부터 새롭게 쌓아 올릴 공동파는 그래야만 한다.”

현천진인은 살아남은 모든 제자들을 향해 선언했다.

비록 공든 탑은 무너졌으나, 반석(盤石)을 통해 다시 쌓아 올리겠노라고.

더욱더 견고한 탑을 쌓아 올릴 그 반석에, 무고한 피는 묻히지 않겠노라고.

동시에 젖은 눈으로 자신의 제자들을 바라보며 이렇게 말했다.

“마음껏 울어라. 어쩌면 그 눈물도 오늘이 마지막이 될 테니.”

그리고 다음 순간, 나는 조용히 눈을 감고 귀를 닫았다.

화룡각 대원 모두도. 뒤늦게 소란을 알아차리고 다가온 다른 이들 역시도 마찬가지였다.

듣지 않으려 해도 들을 수밖에 없는, 처절하면서도 구슬픈 통곡과 울음소리가 사방에 흘러넘쳤지만 상관없었다.

무수한 시체와 핏물로 뒤덮인 이 전장의 누구도 그들의 울음소리를 듣지도, 기억하지도 못할 테니까.

혹은…….

이미 모두가 함께 눈물을 흘리고 있으니까.

툭.

어깨를 두드리는 누군가의 익숙한 손길에, 나는 어느새 희뿌연 습막이 맺힌 눈가를 소매로 훔쳤다.

“노야.”

“늦었을까 걱정했는데, 괜한 걱정이었던 모양이구나.”

고개를 돌리자, 승리의 함성이 울려 퍼질 무렵부터 어디론가 사라졌던 적천강과 궁성이 그곳에 있었다.

아니, 엄밀히 말해서 그곳에 있는 것은 비단 그 두 사람뿐만이 아니었다.

“크흑, 크흐흐흑!”

세상 서러운 듯이 눈물을 줄줄 쏟아내는 한 사내.

가만히 서 있기만 해도 헛구역질이 나오는 게이트에서 수년을 개처럼 구른 나조차도 난생처음 맡아 보는, 끔찍한 냄새를 풍기는 어느 괴인(怪人)이 나를 향해 불쑥 손을 내밀었다.

‘뭐지, 이거.’

나오려던 눈물도 쏙 들어간 채 눈을 깜빡이던 그때, 내 손을 그대로 끌어당겨 덥석 안은 괴인이 한스럽게 통곡하기 시작했다.

“으허허허헝! 어이오고오오!”

아니, 진짜 무슨 상황인데.

잠깐의 뇌 정지 후, 나오려던 눈물마저 쏙 들어간 내가 물었다.

“……그, 도대체 누굽니까?”

적천강이 망설임 없이 대답했다.

“미친놈.”

“예?”

“어느 흉악하게 생겨먹은 마적 나부랭이들은, 대인(大人)이라고도 부르더군.”

“……!”
```

## Final English reading copy

```markdown
# Chapter 1059

For me and everyone else, it was only the briefest instant.

Though for someone, it might have felt unbearably slow and suffocating—a moment from a life flashing before their eyes.

*Shing.*

The sound of sharp steel slipping from the scabbard that held it was so faint it raised goose bumps. It meant the sword had been drawn almost perfectly.

Not a hair’s breadth off. The right amount of force, at the right speed.

And…

A clear trajectory, following its master’s will as it cut diagonally across its target.

*Shhk!*

The distance was too short to dodge. The gap in their martial prowess was too great.

And Sama Pyo had quietly closed his eyes without even trying to evade, as if accepting his fate.

Of course, nothing out of the ordinary happened. The sword light that flashed in a split second scattered red flowers through the air.

*Shwaaa!*

Time started moving again.

Beyond Sama Pyo’s staggering back, a fountain of blood shot high into the air, staining everyone’s vision.

The Kongtong Disciples nearby. The Fire Dragon Pavilion members and me.

And someone else, too, who had been doing everything in their power to hold back the urge to rush over.

“No!”

Taishan’s patience, stretched taut as he anxiously watched everything unfolding around Sama Pyo, had finally snapped.

With a thunderous shout that rang in every direction, the giant—over nine feet tall—set down the poor old man riding on his shoulders as if he were tossing him aside and shot forward at a speed I’d never seen from him before.

*Whoosh!*

The wind roared around him, but his path was as straight as could be.

Before anyone had a chance to stop him, Taishan shot forward like a cannonball, heading straight for Sama Pyo as he staggered backward.

He didn’t seem to care one bit about the Kongtong Disciples who had surrounded Sama Pyo, as if to box him in.

“You bastard!”

“Stop right there!”

*Papat!*

Shouts erupted all around them, and blurry figures appeared in every direction.

Dozens of Kongtong Disciples moved with elusive speed to block Taishan’s path. Each raised their weapon and aimed it at him.

Their blades were slick with blood. And, as if to prove how they had survived the brutal, desperate battle at Dunhuang, every one of them bore the gleam of Sword Energy—the level at which it could injure others.

But Taishan’s two-section staff, clutched in his hands as he shot forward even faster despite dozens of Peak masters blocking his way, shone with the same light.

“Raaaargh!”

Tiger Giant Child.

True to the meaning of his epithet, Taishan was usually as innocent as a child, but his inborn strength and martial prowess were those of a beast.

Roaring like a furious tiger, Taishan swung his two-section staff with all his might. A tremendous gale swept along with it.

*Whoooosh!*

Even a hardened veteran of the Murim would have felt a chill run down their spine at that terrifying whistle through the air.

But the Kongtong Disciples didn’t take a single step back.

No—they unleashed dazzling sword light at Taishan as he charged them with a menacing look.

*Shwiiing!*

In an instant, the space was filled with murderous intent.

The two-section staff barreling through the wind, and blades shooting through the air.

And, slipping into that life-or-death moment, I took a forceful step forward.

*Shhk.*

One step.

Just one was enough.

Several yards of space vanished in an instant, and the scene around me changed.

I had already slipped between Taishan and the Kongtong Disciples. Without hesitation, I thrust out both palms.

*Bang!*

Compressed air exploded. The heat of the Flame Divine Palm, held back as much as I could, burst from my palms and shoved everything away.

Not only the weapons being swung fiercely at one another, but the bodies of the people holding them, too.

*Clatter!*

Weapons shot up into the air without reaching their targets. The figures that wielded them stumbled backward, swaying like reeds in the wind.

“……!”

“……!”

Through the dust that rose hazily from the ground amid all the blood, I looked at their bewildered faces as they were forced back. My voice came out tired and flat.

“Do you all have energy to burn? Take it down a notch.”

Before anyone could answer, I spoke again, this time to Perfected Being Hyeoncheon, who had silently watched the sudden scene unfold before him.

“Apologies for the late greeting. We met once before in Henan.”

Perfected Being Hyeoncheon had briefly met me at the Mount Song Resolution, where the new Murim Alliance was first formed. He gave a slight nod.

“It’s been a while, my friend Jin.”

A corner of my heart ached.

Even though our connection had lasted no more than fifteen minutes, it still did.

The old Daoist who had once praised my martial arts with a kind voice and laugh, like my own grandfather, was nowhere to be found now.

Perfected Being Hyeoncheon’s voice, reaching my ears, was as dry and brittle as grains of desert sand. The traces of grief and anger remained at the corners of his mouth.

Just like the sword trembling in his wrinkled hand.

The blood slowly dripping from the tip of the treasured sword he had likely carried with him his entire life must have come from the emotions he still hadn’t managed to shake off.

“Pavilion Master! What are you doing? Move aside, now!”

Right. That guy was here, too.

Taishan’s shout brought me back to my senses. I pulled myself out of the emotional swamp I’d been sinking into.

At the same time, I called out to the guy as he adjusted his grip on the two-section staff and stepped forward.

In my own rough way.

*Thump!*

My fist drove straight into his abdomen. The giant, nearly nine feet tall, bent over like a shrimp and went rigid.

Taishan drew in a startled breath. He stared at me wide-eyed, then squeezed out a few words.

“P-Pavilion Master…”

“Cool your head.”

With that quiet word, I brought the edge of my hand down on the back of his neck without hesitation.

*Thud.*

Even a tough guy with skin and bones so thick that a Pressure-Point Strike probably wouldn’t work was no match for overwhelming strength.

The sound of him falling was like a bear hitting the ground. Silence followed.

The Fire Dragon Pavilion members, who arrived a moment later, and the Kongtong Disciples, who had been about to charge at Taishan again, stared at me in bewilderment.

Everyone except Perfected Being Hyeoncheon, who watched in silence with a sunken gaze.

“I heard there was a giant tiger beside the young Black Dragon… You’re every bit as strong as they say. And fiercely loyal, too.”

Perfected Being Hyeoncheon muttered as he looked at Sama Pyo, still lying motionless.

“He’s a better subordinate than he looks. Don’t you think?”

“He’s as dumb as he is big, but he’s a good guy. And…”

I added with a bitter expression, “That friend you showed mercy to is a much better person than you think, Sect Leader.”

“……!”

“……!”

The air around us gave a sharp, electric shiver.

Those who understood what I meant opened their eyes wide at the same time, as if on cue. Perfected Being Hyeoncheon closed his eyes without a word.

As if trying to wipe away the killing intent still lingering in his heart.

“Do you… regret it?”

I broke the silence and looked at Perfected Being Hyeoncheon.

From the moment he had drawn his sword at his waist and swung it, I’d known instinctively.

That perfect draw held conflict, but not the slightest trace of killing intent.

That the old Daoist’s sword would never take someone’s life.

That was why I hadn’t stepped in.

I could feel that though his unsteady sword tip had cut shallowly into Sama Pyo’s skin, it was because of the last bit of conflict he had left.

“Regret it? Of course I do.”

“Then why?”

“His eyes. I saw those eyes.”

Perfected Being Hyeoncheon suddenly opened his eyes. He looked up at the Kongtong Sect flag fluttering above his head and continued.

“They were like the eyes of my Disciples, the last time I saw them in Dunhuang. Deep, upright, and unbowed even in the face of death. Those were their eyes.”

Some say a person’s eyes are the windows and mirrors of the heart.

Perhaps that was why the old Daoist, who had come here carrying his desire for revenge, couldn’t bring himself to kill the son of his enemy—the man who had come here seeking death himself.

“I’m just a wretched old Daoist. I devoted my life to the sword instead of the Daoist scriptures, and I couldn’t save my Disciples as they bled and died. But…”

A hot breath slipped between his trembling lips.

“Someone I met recently said this to me. If you take someone’s life simply because they share the blood of your enemy, what else could that be but the Demonic Path?”

I understood.

Even though Perfected Being Hyeoncheon’s voice was directed at me, what he meant to say was for every Kongtong Disciple to hear.

*Splat.*

A sword slipped from someone’s grasp and plunged into a pool of blood.

Only moments earlier, they had been giving off suffocating killing intent. Now, they stared at one another with vacant eyes.

As if they were remembering themselves through the sight of their fellow Disciples, drenched in blood from head to toe—remembering how they had searched for their surviving enemies and slaughtered them like livestock.

And they swallowed their tears.

In silence. Struggling to hold back the emotions and beloved faces that passed before their eyes.

“Revenge will be carried out, but it will not extend to the relatives of the guilty. The Kongtong Sect we build anew from this day forward must be that way.”

Perfected Being Hyeoncheon declared this to all his surviving Disciples.

Though the tower they had painstakingly built had fallen, he would build it again upon bedrock.

And no innocent blood would stain the bedrock on which they built an even stronger tower.

Then, looking at his Disciples with tear-filled eyes, he said, “Cry to your hearts’ content. These tears may be your last today.”

The next moment, I quietly closed my eyes and shut out the sound.

So did every member of the Fire Dragon Pavilion. So did the others who had come over after belatedly realizing what was happening.

The desperate, sorrowful wails and sobs filled the air. They couldn’t help hearing them, even if they didn’t want to.

But it didn’t matter.

No one on this battlefield, covered in countless corpses and pools of blood, would hear or remember their crying.

Or…

Maybe everyone was already crying together.

*Tap.*

At the familiar touch of someone patting my shoulder, I wiped the hazy moisture from my eyes with my sleeve.

“Old Master.”

“I was worried I might be late, but it seems that worry was misplaced.”

I turned around. Jeok Cheongang and the Bow Saint were there. They had disappeared somewhere around the time the shouts of victory began to ring out.

No—strictly speaking, they weren’t the only ones there.

“Ugh, sob… sob!”

A man wept openly as if his heart were breaking.

Even after spending years being worked like a dog in Gates so disgusting that just standing in one made me gag, I’d never smelled anything like this. A certain foul-smelling oddball thrust his hand toward me.

*What the hell is this?*

I blinked, my tears already gone, when the oddball grabbed my hand, yanked me close, and wrapped me in a tight embrace. Then he began to sob miserably.

“Waaah! Uuughhh!”

No, seriously, what was going on?

After my brain stalled for a moment, and whatever tears had been about to come out disappeared completely, I asked, “……Um, who exactly are you?”

Jeok Cheongang answered without hesitation.

“A madman.”

“What?”

“Some vicious-looking mounted bandits call him ‘Great Sir,’ too.”

“……!”
```
