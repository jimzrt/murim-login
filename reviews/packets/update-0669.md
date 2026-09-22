<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0669.txt",
      "sha256": "1679acc353377f8e08dbe1a26a3a777e1835effba83661dd47489cfd5d6f7e60",
      "bytes": 12877
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4be40e562e13ab5279ce6dab584fab808f8769565401897ccf731218b4eeb768",
      "bytes": 2219
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "90fbc5af66a53c979eb81e4f99d3a7bf49ae990d077ae46d7867ad560fdaf362",
      "bytes": 202324
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "94874afd9b9cc46e39b485ca70827b5dc49e7278ff09755286fbcef565cfc916",
      "bytes": 1177
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6ed1025fd31507ffb28087efce9632958e0bffb2df276198188a8b577681c0c1",
      "bytes": 553
    },
    {
      "path": "characters/Namho.md",
      "sha256": "85f0308bd91043c928b6900ac6888c733b599db762822ebd793aff2349dda3bc",
      "bytes": 843
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "87ff57bc95a85a3838607906b7c62cba0a80842784f929264cfad4bf53c8c81a",
      "bytes": 936
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "945c3a59b3518685fcd0f67b71b0f57db813c3ab112022198eee55a3b69bc078",
      "bytes": 795
    },
    {
      "path": "characters/Wonhu.md",
      "sha256": "e293fd95d995d67c34db160ee7109202d965e0ed90861cd31a5832398eea4281",
      "bytes": 415
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "63918a3c460fddb2d311344897d7d195301a0ca3685e503a1812ee99d102f615",
      "bytes": 806
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "504ac11f9e0cfe388d6a073cdae10ea6fe1d880c5427a63e85dae7f8e6bb8c61",
      "bytes": 207739
    }
  ],
  "estimated_tokens": 10951
}
-->

# Durable State Update — Chapter 669

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 669. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 669. Profile updates may replace only one
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
  "chapter": 669,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 669,
    "continuity_sources": [669],
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
    "Jin Taekyung has escaped the underground prison and broken free of the restraints designed to contain him.",
    "Jin can wield an invisible Middle Dantian force and overwhelming physical power while his internal energy is believed to remain sealed.",
    "Jin has defeated the Bai captain and several Peak-level squad captains with his bare force and chains.",
    "Yayul Mok and the Seven Miao Tigers are fighting alongside Jin inside the underground prison, with Yayul still carrying the antidote.",
    "Taishan is arriving from the prison stairs in a starving and highly aggressive state.",
    "The rescue attempt remains an active confrontation between Jin's group and the Bai warriors.",
    "Jin's public execution remains scheduled for noon in two days.",
    "The Beast Miao King and Yayul Mok continue risking their positions and lives to rescue Jin and avert war between Nanman and the Central Plains.",
    "Baeksang remains conflicted about stopping the rescue despite the chieftains' support for Jin's execution."
  ],
  "continuity_sources": [
    668,
    667
  ],
  "open_questions": [
    "What is the exact source and limit of Jin's Middle Dantian force while his internal-energy seal remains in place?",
    "Can Jin, Yayul Mok, and the Seven Miao Tigers escape the underground prison before the scheduled execution?",
    "How will Taishan's arrival affect the battle with the Bai warriors?",
    "Will the failed infiltration expose the Beast Miao King and Yayul Mok and trigger war with the Central Plains?",
    "Will Baeksang allow the rescue to proceed despite the chieftains' demand for Jin's execution?"
  ],
  "safe_through": 668,
  "temporary_decisions": [
    "Use Great Chieftain for 대족장 and Escape from Namshank for 남생크.",
    "Use Deputy Stronghold Lord for 부채주 and Stronghold Lord for 채주.",
    "Retain underground prison for 뇌옥 and use Dizziness Acupoint for 훈혈.",
    "Capitalize Will when referring to the System-linked martial concept 의지.",
    "Use Middle Dantian for 중단전 and Seizing an Object Through Empty Space for 허공섭물; Jin's ability is similar but explicitly distinct."
  ],
  "version": 1
}
```

## Exact glossary matches

| 남만야수궁  | **Nanman Beast Palace**          |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 중원     | **Central Plains**                               |                                                       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 원후 | **Wonhu** | Named member of the Beast Miao King's personal guard, the Seven Miao Tigers. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 산니백육 | **Garlic Pork** | Boiled pork sliced thin and served with garlic sauce. |
| 어향육사 | **Fish-Fragrant Shredded Pork** | Shredded pork dish. |
| 경장육사 | **Beijing Sauce Shredded Pork** | Shredded pork dish. |
| 규화계 | **Beggar's Chicken** | Named inn dish. |
| 매채구육 | **Maechae Guyuk** | Pork belly with preserved mustard greens; the abbreviation is explained in a footnote. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 점혈 | **Pressure-Point Strike** | System-named technique used by Jeok Cheongang on Taekyung. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 심력 | **mental strength** | Inner mental capacity injured by Jongni Chu's feint. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 일다경 | **the time it takes to drink a cup of tea** | Duration in the progression of Jeok's lost time. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 철구 | **iron balls** | Training weights attached to Taekyung. |
| 단환 | **pill** | A martial elixir in pill form; Mungyeong gives Taekyung a custom-made one. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 칠묘호 | **Seven Miao Tigers** | The Beast Miao King's personal guard, composed of elite Miao warriors. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |
| 남생크 | **Namshank** | Quest-title pun on Shawshank in Escape from Namshank. |
| 소궁주 | **Young Palace Lord** | Title used for Yayul Mok as heir of the Nanman Beast Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야율목 | 남호 | Nanman Young Palace Lord to elderly guest and Hidden Shadow Pavilion agent | old man | respectful and familiar | Yayul Mok uses the honorific 노인장 while praising Namho's knowledge of White Tigers. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 야율목 | 원후 | Young_Palace_Lord_to_elder_personal_guard | Wonhu | formal-commanding | Calls on Wonhu to open a path through the surrounding guards. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 666
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes, and one of only two Supreme Peak masters in Nanman; he has imprisoned Jin Taekyung and joined forces with twenty tribal chieftains to arrange Jin's execution at noon in two days.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with enduring grief over Hwi's death and a guarded but still powerful bond with his sworn elder brother that now leaves him visibly conflicted.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of his deceased only child Baekhwi, whom the Great Snow Fiend killed during the Great Faction War; he opposes the Nanman Beast Palace joining the Murim Alliance, distrusts the Central Plains because of the alleged wartime betrayal, and is alleged by Heugung to have colluded with Dark Heaven.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 668
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 665
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 664
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 668
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate, a member of the Fire Dragon Pavilion, and a prisoner in the cell above Jin Taekyung after breaking both wrists of a Nanman attendant who underfed him.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Wonhu.md

# Wonhu (원후)

- **Safe through:** Chapter 668
- **Aliases:** None
- **Role:** Wonhu is the eldest member of the Seven Miao Tigers, the Beast Miao King's personal guard.
- **Personality:** No personality traits are established.
- **Voice:** No distinctive voice is established.
- **Relationships:** Wonhu serves Yayul Cheok as a personal guard.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 668
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and his father, Baeksang is his father's sworn younger brother, and he is risking his position and life alongside his father to rescue Jin Taekyung.

## Korean source

```text
＃669화



일다경(一茶頃). 아니, 어쩌면 촌각(寸刻).

뇌옥의 모든 상황이 정리되기까지는 차 한잔 마실 시간도 걸리지 않았다.

허기짐으로 반쯤 광폭화가 진행된 태산이 계단을 막고, 나를 선두로 야율목과 칠묘호가 나아가자 백족 전사들은 전의를 상실했다.

나로서는 매우 다행스러운 일이었다.

최대한 신속하게 뇌옥을 빠져나가야 하는 사정도 있었지만, 아직 중단전(中丹田)의 효용을 완전히 깨닫지 못한 나로서도 슬슬 한계를 느끼고 있었기 때문이다.

이미 구속구를 끊는 데에 엄청난 심력(心力)을 소모한 와중에 한 차례의 짧은 전투까지, 속이 울렁거리고 가슴이 아파 오던 차에 등장한 태산은 천군만마나 다름없었다.

“우워어어어!”

음. 사실 저 정도면 헐크에 가깝나.

그리고 적들의 빠른 투항에는 초절정 고수인 내 존재뿐만 아니라, 음산하기 짝이 없는 태산의 중얼거림이 크게 한몫했다.

“%#$%&^&%^&%^#$!”

“허억!”

굶주림으로 번들거리는 눈동자.

백족 전사들로서는 알아들을 수 없는 언어를 속사포처럼 내뱉으며 다가오는 태산의 모습이 공포, 그 자체였겠지만 나는 저 주문의 실체를 잘 알고 있었다.

“오리구이 매채구육 어향육사 경장육사 산니백육 회과육 고노육 장우육 동파육 마파두부!”

“…….”

“궁보계정 향고유채 왕만두 규화계 탕초리적! 으아아아아!”

음.

놈들이 한어(漢語)를 알아듣지 못해서 참 다행이다. 어쩌면 신들린 듯이 음식 이름을 외치면서 천천히 다가오는 게 더 무서울 수도 있겠지만.

“배애고오파아아아아아!”

“히이이익! 사술이다! 저 괴물이 사술을 쓰려 한다!”

“항복! 항복하겠소!”

저 새끼 최소 남만 한정 사이어인.

반응만 보면 배고파가 아니라 에네르기파인 줄 알겠다.

물론 그런 내 생각과는 별개로 배고파의 효과는 확실했고, 이에 굴하지 않고 앞으로 나선 몇몇 용기 있는 놈들마저 태산에게 박살 나면서 상황은 끝났다.

“두려워 말라! 돌겨역!”

“할 수 있다! 놈을 쳐라!”

앞으로 나선 놈들은 중원에서도 그럭저럭 초일류 취급받을 만큼 괜찮은 실력자들이었다.

그들이 가진 유일한 문제는 상대가 영 좋지 않았다는 것뿐이다.

퍽! 콰지직!

우두둑!

통나무처럼 굵은 팔다리가 휘둘려지자 사방으로 튕겨 나가는 신형들.

그 모습을 확인한 백족 전사들은 침을 꿀꺽 삼키며 병장기를 내려놓았고, 야율목과 칠묘호는 아연한 눈빛으로 나를 바라봤다.

“왜. 뭐.”

“아니, 그. 공력 금제 당한 거 아니었나?”

“아. 금제 당했지. 지금도 못 써.”

“……그런데 어떻게.”

“나는 말하자면 길고, 저놈은 그냥 타고났고.”

인간의 신체는 기본적으로 한계가 있는 법인데, 시스템으로 그 한계를 아득히 뛰어넘은 나와 달리 태산은 자연적으로 발생한 괴물이다.

공력이 없는 상태에서도 일류 고수 정도는 쥐잡듯 때려잡을 수 있을 정도로.

‘어릴 때 감마선에 노출되기라도 했나.’

나름 합리적인 의심이었지만, 지금 상황에서는 그게 중요한 게 아니다.

나는 이미 전의를 상실한 채 스스로 무장을 해제한 백족 전사들을 바라보며 작게 중얼거렸다.

“자. 우선 여기부터 정리하자고.”



* * *



결론부터 말하자면, 투항한 백족 전사들은 살아남았다. 정확히는 야율목이 그들을 살렸다.

투둑. 털썩.

점혈(點穴) 당한 몸뚱어리가 의식을 잃고 쓰러진다.

며칠 전 애뇌산으로 향하는 길에 면식을 익힌 칠묘호가 그들을 한곳에 모아 뇌옥에 처박았고, 우리는 지체하지 않고 지상으로 이어진 계단으로 향했다.

철벅.

“아까도 말했지만…… 후회할 거야.”

걸음과 함께 불쑥 던진 한마디. 그 말에 담긴 의미를 알아들은 야율목이 고개를 저었다.

“그럴 일 없다.”

“이미 얼굴도 훤히 드러난 마당에, 놈들이 정신을 차리게 되면 누구 이름부터 댈까.”

야율목은 남만야수궁의 소궁주니 더 말할 것도 없고, 칠묘호 역시 묘족을 대표하는 전사들인 만큼 얼굴이 제법 알려진 자들.

부족이 다르다고는 하지만 저들 중 일부는 이미 이들의 정체를 알아차렸을 것이다.

“이 사실이 밝혀지는 건 시간문제야. 입을 막았어야 했어.”

“상관없다.”

“상관이 없긴, 염병하고 있네. 이 길로 도주할 것도 아니라면서 상관이 왜 없어? 만약 여기 남아 있으면…….”

“정체가 밝혀지겠지. 당장 목숨이 위태롭지는 않겠지만 대회의의 결정을 거스른 대가를 톡톡히 치를 테고.”

“이런 말 해서 미안하긴 한데, 혹시 좆 되는 취미 있냐? 뇌옥에 갇히는 게 버킷 리스트야?”

“버귀…… 발음하기도 힘들군. 나로서는 그게 뭔지 잘 모르겠지만, 이미 감수하고 벌인 짓이다.”

야율목이 나직한 목소리로 말을 이었다.

“비록 부족은 다르지만 오랜 세월 같은 땅에서 함께한 남만인이다. 만약 동족을 죽인다면, 우리도 괴물이 되어 버리는 거야.”

야율목의 말을 듣고 있자니 문득 한 사람이 떠올랐다. 오직 복수를 위한 괴물이 되어 버린 그가.

‘백상.’

그래, 어쩌면 이것이 인간과 괴물의 차이일지도 모르겠다.

자신의 목적을 이루기 위해 덧없는 목숨을 희생시키지 않는 것. 그러나 나는 무거운 마음으로 입을 열었다.

“모두 죽였어야 했어.”

“살인을 좋아하는군. 한족들은 다 너처럼 그 모양인가?”

“미친놈. 내가 마두(魔頭)라도 되는 줄 아냐? 이건 그냥…….”

“그만하면 됐다. 말 안 해도 이미 알고 있으니까.”

“뭐?”

고개를 돌려보니, 야율목이 소리 없이 웃고 있었다.

“우리가 걱정돼서 그런 거겠지. 널 구하려다가 곤경에 처했다는 죄책감 때문에.”

“…….”

“비록 중원과 언어는 다르지만, 벗이라는 단어는 남만에도 있다. 어쩌면 너와 내가 어느덧 그런 사이가 되었을지도 모르겠군. 아니면 나 혼자만의 착각이든지.”

“……!”

빌어먹을. 도무지 무슨 말을 해야 할지 모르겠다.

내가 할 말을 잃은 그때, 끝없이 위로 이어져 있던 계단이 끝나고 마침내 뇌옥의 입구가 모습을 드러냈다.

“원후.”

야율목의 부름에 고개를 끄덕인 중년인이 앞으로 나선다.

원숭이를 닮은 그가 커다란 열쇠 꾸러미를 차례대로 꽂자, 묵직한 소음과 함께 거대한 철문이 열리기 시작했다.

구구구궁.

서서히 열리는 철문 너머로 은은한 달빛이 새어 들어온 그때, 야율목이 품에서 자그마한 목갑 두 개를 꺼냈다.

“공력의 금제를 풀 수 있는 해약(解藥)이다. 백족의 비전으로 만들어진 물건이라 두 개밖에 구하지 못했지만, 공력을 회복한 너라면 능히 다른 이들을 이끌고 남만을 빠져나갈 수 있을 것이다.”

“다른 이들이라면 혹시?”

“노인과 부상자라 그래서인지는 몰라도 경계가 매우 취약하더군. 적어도 그 부분에 있어서만큼은 철두철미한 백 숙부답지 못했어.”

야율목의 대답과 동시에 나는 볼 수 있었다. 완전히 열린 철문 너머로 의식을 잃은 채 백호의 등에 실려 있는 두 사람을.

“주군! 남호!”

반가운 얼굴들을 발견한 태산은 헐레벌떡 뇌옥을 빠져나갔고, 나는 복잡한 표정으로 야율목을 응시했다.

“너…….”

“가라. 우리가 가급적 최대한 시간을 끌어 줄 테니. 물론 길어야 반 시진 안에 발각되겠지만 약간의 도움은 될 거다.”

모르겠다. 이 상황에서 무슨 말을 해야 할지.

만약 이들의 도움이 없었다면 어떻게 되었을까.

나와 태산, 단둘이서 자력으로 뇌옥을 탈출할 수는 있었어도 결코 지금처럼 신속하게 남만야수궁을 빠져나올 수는 없었을 것이다.

내게 있어 내궁 어딘가에 억류되어 있던 남호와 사마표의 존재는, 만근의 철구 이상으로 강력한 구속이었으니까.

‘어쩌면 그 과정에서 다시 사로잡혔을지도 모르지.’

하지만 이들은 혼신의 힘을 다해 나를 도왔다. 자신들이 위험에 처할 것을 감수하면서까지.

그 덕분에 나는 악수(惡手)를 무를 수 있는 두 번째 기회를 얻을 수 있게 되었다.

“……고맙다.”

지금까지 미처 하지 못했던 감사 인사에, 야율목과 칠묘호. 그리고 뇌옥 밖에서 백족 전사들로 위장하고 있던 이들까지 희미한 미소를 지으며 고개를 저었다.

“고마워할 필요 없소.”

“그럼. 그저 남만이 당신에게 진 빚을 갚은 것뿐이지.”

“애뇌산에 제 형이 있었습니다. 은공 덕분에 다시 만날 수 있게 되었지요.”

얼굴도, 이름도 모르는 이들이 나를 도왔고 누군가는 은공이라 부른다.

나는 그 모두의 얼굴을 한 사람, 한 사람 눈에 담았다.

그리고 야율목의 손에 들린 목갑을 받아들고 흐릿한 달빛 아래로 걸음을 내디뎠다.

사박.

축축하게 젖어 있는 땅을 밟은 그 순간.

띠링.



- 처형 집행 전까지 뇌옥 탈출(완료)

- 퀘스트 성공 조건을 달성하셨습니다!

- 퀘스트, [남생크 탈출]을 성공적으로 완료했습니다!

- 퀘스트 완료 보상을 지급합니다!

- 막대한 경험치를 획득했습니다!

- 레벨 업!

- 일부 부상과 상태 이상이 해제됩니다!



귓가를 파고드는 퀘스트 알림과 함께, 오직 나만이 느낄 수 있는 시원한 바람이 전신을 휩쓸었다.

솨아아아!

꼬박 하루가 넘는 시간 동안 뻣뻣하게 굳어 있던 근육. 아직 턱없이 부족한 중단전의 힘을 억지로 끌어올리느라 피로가 누적된 전신이 회복되고, 마지막으로 하단전(下丹田)을 옭아매고 있던 힘이 힘없이 녹아내린다.

후우.

크게 내뱉은 날숨에 열양지기로부터 흘러나온 열기가 뒤섞였다.

그런 내 모습에 무언가를 느낀 듯, 야율목과 칠묘호가 눈을 크게 떴다.

‘놀랍기도 하겠지. 아직 해약은 복용하지도 않았으니까.’

하지만 미주알고주알 설명해 줄 생각도, 시간도 없는 상황이다.

태산에게 간식이라며 목갑 안의 단환을 던져 준 나는, 정신을 잃은 사마표에게도 나머지 하나를 먹였다.

화륵, 스르륵.

열양지기에 의해 물처럼 녹아내리는 단환. 액체로 화한 단환이 그대로 목을 넘어가자, 약간 창백했던 사마표의 얼굴에 혈색이 돈다.

‘생각보다 상태가 괜찮긴 하지만…… 당분간은 무리하면 안 돼.’

남호야 그렇다 치고 믿음직한 전투원인 사마표가 제힘을 발휘할 수 없다는 건 큰 단점이지만, 그렇다고 해서 이곳을 빠져나갈 가망이 없어지는 것은 아니다.

아니, 오히려 내가 투항하기 전보다 낫다.

‘척후대를 제외한 다른 대원들의 신병을 확보했고, 약간의 깨달음도 얻었으니.’

거기에 더해, 야율목은 생각지 못했던 호의를 다시 한번 더 베풀기까지 했다.

“이 녀석과 함께 가라.”

그르릉.

익숙한 울음소리.

슬픈 눈으로 평생을 함께한 친구이자 주인을 바라본 백호가 나를 향해 등을 내밀고 있었다.

“무야호는 남만에 존재하는 백호 중에서도 영물로 불리는 녀석이다. 나와는 형제와도 같은 아이니, 부디 잘 챙겨 줄 거라 믿는다.”

낮게 가라앉은 야율목의 목소리를 알아들었다는 듯, 백호가 내 손을 핥고는 코를 대고 킁킁거린다.

그런 녀석을 바라보며 희미하게 웃은 야율목이 한 방향을 가리켰다.

“이만 가라. 우리가 처음 만났던 장소에서 곧장 동북쪽을 향해 달리면 척후대와 조우할 수 있을 것이다.”

그리고 바로 그 순간이었다.

퍽.

타격음과 함께 덜컥 흔들리는 신형. 허물어지는 야율목의 몸을 받아 든 원후가 나를 향해 씩 웃었다.

“말 안 해도 아실 거라 믿소.”

“당신들…….”

“소궁주를 부탁합니다.”
```

## Final English reading copy

```markdown
# Chapter 669

The time it takes to drink a cup of tea.

No, perhaps mere moments.

It had taken less than the time needed to drink a cup of tea for everything in the underground prison to be settled.

With Taishan—half-maddened by hunger—blocking the stairs, and Yayul Mok and the Seven Miao Tigers advancing with me at the front, the Bai warriors lost their will to fight.

It was a very fortunate development for me.

We needed to escape the underground prison as quickly as possible, but I was also beginning to feel my limits. I still had not completely grasped the full utility of the Middle Dantian.

I had already expended a tremendous amount of mental strength breaking my restraints, and then there had been one short battle on top of that. My stomach was churning, and pain had begun to spread through my chest.

Taishan’s appearance at that precise moment was like having an entire army at my side.

“Gwoooooooh!”

Hmm. Actually, at this point, he was closer to the Hulk.

And the eerie muttering Taishan kept spouting had played a major role in the enemies’ quick surrender, along with my presence as a Supreme Peak master.

“%#$%&^&%^&%^#$!”

“Gasp!”

Eyes gleaming with hunger.

To the Bai warriors, Taishan approaching while rattling off incomprehensible words at machine-gun speed must have been the very embodiment of terror.

But I knew the true nature of his incantation all too well.

“Roast duck! Maechae Guyuk[^1]! Fish-Fragrant Shredded Pork! Beijing Sauce Shredded Pork! Garlic Pork! Twice-Cooked Pork! Sweet and Sour Pork! Soy-Braised Beef! Dongpo Pork! Mapo Tofu!”

“……”

“Kung Pao Chicken! Stir-Fried Mushrooms and Vegetables! King-Size Dumplings! Beggar’s Chicken! Sweet-and-Sour Carp! Aaaaaaah!”

Hmm.

It was a good thing they could not understand Han Chinese. Although perhaps approaching slowly while chanting the names of food like a man possessed was even more frightening.

“Hungryyyyyyyyy!”

“Eek! It’s dark arts! That monster is about to use dark arts!”

“Surrender! I surrender!”

That bastard was a Saiyan, at least by Nanman standards.

Judging by their reactions, you would have thought he was shouting “Kamehameha!” instead of “I’m hungry!”

Regardless of what I thought, “hungry” clearly worked. Even the few brave men who stepped forward undaunted got wrecked by Taishan, bringing the situation to an end.

“Do not fear! Charge!”

“We can do this! Strike him!”

The men who stepped forward were skilled enough to be regarded as fairly capable First Rate masters even in the Central Plains.

Their only problem was that their opponent was a particularly bad match for them.

Thud! Craaack!

Crack-crack!

As Taishan swung his log-thick limbs, bodies went flying in every direction.

The sight made the Bai warriors swallow hard and lower their weapons. Yayul Mok and the Seven Miao Tigers stared at me in stunned disbelief.

“What? Why are you looking at me?”

“No, it’s just… weren’t you hit by a restriction on your internal energy?”

“Ah. I was. I still can’t use it.”

“……Then how?”

“Explaining mine would take a while. That guy was simply born that way.”

The human body naturally had limits. Unlike me, who had surpassed those limits by a tremendous margin through the System, Taishan was a naturally occurring monster.

Even without internal energy, he could beat a First Rate master as easily as swatting a rat.

*Was he exposed to gamma radiation as a child or something?*

It was a fairly reasonable suspicion, but that was not important right now.

I looked at the Bai warriors who had lost their will to fight and disarmed themselves, then muttered quietly.

“All right. Let’s clean things up here first.”

* * *

To give you the conclusion first, the Bai warriors who surrendered survived.

More precisely, Yayul Mok spared them.

Thud. Collapse.

A body struck by a Pressure-Point Strike lost consciousness and collapsed.

The Seven Miao Tigers, whom I had gotten acquainted with a few days earlier on the way to Ailao Mountain, gathered them in one place and locked them inside the underground prison. We did not waste any time before heading toward the staircase leading to the surface.

Squelch.

“I told you before… you’ll regret this.”

The words came abruptly as we walked. Understanding what I meant, Yayul Mok shook his head.

“That will not happen.”

“Our faces were fully exposed. Once they regain consciousness, whose name do you think they’ll give first?”

Yayul Mok was the Young Palace Lord of the Nanman Beast Palace, so there was no need to say more. The Seven Miao Tigers were also well-known warriors who represented the Miao people.

Though their tribes were different, some of the prisoners had probably already realized who they were.

“It’s only a matter of time before this comes to light. We should have silenced them.”

“It does not matter.”

“Like hell it doesn’t. You said we weren’t going to flee along this path, so why wouldn’t it matter? If we remain here…”

“Our identities will be revealed. Our lives will not be in immediate danger, but we will pay dearly for defying the Tribal Grand Council’s decision.”

“I hate to ask this, but do you have some kind of hobby where you enjoy getting fucked? Is getting locked in an underground prison on your bucket list?”

“Bucki… It is difficult even to pronounce. I do not know what it means, but I already took that risk when I did this.”

Yayul Mok continued in a low voice.

“Our tribes may be different, but we are all Nanman people who have lived together on the same land for countless years. If we kill our own kind, we will become monsters as well.”

Listening to Yayul Mok, I suddenly thought of someone.

A man who had become a monster for the sake of revenge alone.

*Baeksang.*

Yes. Perhaps this was the difference between humans and monsters.

Not sacrificing fleeting lives to accomplish one’s own purpose.

But I opened my mouth with a heavy heart.

“We should have killed them all.”

“You like killing. Are all Han Chinese like you?”

“You crazy bastard. Do you think I’m some kind of fiend? It’s just…”

“That is enough. I already know, even without you saying it.”

“What?”

When I turned my head, Yayul Mok was smiling soundlessly.

“You are worried about us. You feel guilty because we got ourselves into trouble trying to save you.”

“……”

“Though our languages are different from those of the Central Plains, the word ‘friend’ exists in Nanman as well. Perhaps you and I have become friends without realizing it. Or perhaps that is merely my own delusion.”

“……!”

Damn it. I had no idea what I was supposed to say to that.

Just as I lost my words, the staircase that had stretched endlessly upward finally came to an end, and the entrance to the underground prison appeared before us.

“Wonhu.”

At Yayul Mok’s call, a middle-aged man nodded and stepped forward.

Looking like a monkey, he inserted a large ring of keys one after another. With a deep, heavy rumble, the enormous iron door began to open.

Grooooan.

Faint moonlight seeped through the slowly opening door. At that moment, Yayul Mok took two small wooden cases from inside his robes.

“This is an antidote that can release the restriction on your internal energy. It was made using a secret Bai technique, so I was only able to obtain two. Once your internal energy is restored, you should be able to lead the others out of Nanman.”

“The others, you mean…?”

“I do not know whether it is because they are old and injured, but the security there was extremely lax. At least in that respect, Uncle Baeksang was not as thorough as usual.”

At the same time as Yayul Mok answered, I saw them.

Beyond the fully opened iron door, two unconscious people were being carried on the back of a White Tiger.

“Lord! Namho!”

Seeing the familiar faces, Taishan hurriedly ran out of the underground prison. I stared at Yayul Mok with complicated emotions.

“You…”

“Go. We will hold them off for as long as we can. Of course, we will be discovered within half a shichen at most, but even that should help.”

I did not know.

I had no idea what I was supposed to say in this situation.

What would have happened if I had not had their help?

Taishan and I might have been able to escape the underground prison on our own, but without their help, we never would have been able to flee the Nanman Beast Palace as swiftly as we could now.

Namho and Sama Pyo, who had been detained somewhere inside the Inner Palace, had been restraints more powerful than ten thousand geun of iron balls.

*Perhaps I would have been captured again in the process.*

But they had helped me with everything they had, even while accepting that they might be placed in danger themselves.

Because of that, I had been given a second chance to take back a bad move.

“……Thank you.”

At the thanks I had not managed to offer until now, Yayul Mok and the Seven Miao Tigers—as well as the men disguised as Bai warriors outside the underground prison—smiled faintly and shook their heads.

“You do not need to thank us.”

“Indeed. We merely repaid the debt Nanman owed you.”

“My hyung was on Ailao Mountain. Thanks to you, I can meet him again.”

People whose faces and names I did not know had helped me, and one of them called me his benefactor.

I committed each of their faces to memory, one by one.

Then I accepted the wooden cases from Yayul Mok and stepped beneath the dim moonlight.

Squelch.

The moment my foot landed on the damp earth—

Ding!

> **System**
>
> - Escape from the underground prison before the execution (**Complete**)
>
> - You have fulfilled the Quest success conditions!
>
> - You have successfully completed the Quest, **Escape from Namshank**!
>
> - Issuing the Quest completion Reward!
>
> - You obtained a massive amount of EXP!
>
> - Level Up!
>
> - Some injuries and Status Effects have been removed!

Along with the Quest notifications piercing my ears, a refreshing breeze that only I could feel swept through my entire body.

Whoooosh!

My muscles had been stiff for more than a full day. The fatigue that had accumulated throughout my body from forcibly drawing up the still woefully insufficient power of the Middle Dantian began to fade.

Finally, the force constricting my Lower Dantian melted away helplessly.

Hoo.

Heat from the Scorching Yang Qi mingled with the breath I exhaled deeply.

Yayul Mok and the Seven Miao Tigers widened their eyes, as if they had sensed something from my appearance.

*Of course they’re surprised. I haven’t even taken the antidote yet.*

But I had neither the time nor the intention to explain every little detail.

I tossed Taishan one of the pills from the wooden case, telling him it was a snack, then fed the other one to the unconscious Sama Pyo.

Fwoosh. Sssslip.

The pill melted like water under the influence of the Scorching Yang Qi. Once it transformed into liquid and passed down Sama Pyo’s throat, color returned to his slightly pale face.

*He’s in better shape than I expected, but he can’t afford to overexert himself for the time being.*

Leaving Namho aside, the fact that Sama Pyo—our reliable fighter—could not fight at full strength was a major disadvantage.

But that did not mean our chances of escaping had vanished.

No. We were in a better position than before I surrendered.

*We’ve secured the others apart from the reconnaissance squad, and I’ve gained a little insight as well.*

On top of that, Yayul Mok had shown me another unexpected kindness.

“Go with this one.”

Grrrr.

A familiar growl.

The White Tiger, looking at its lifelong friend and master with sad eyes, held out its back toward me.

“Muyaho is a spiritual creature even among the White Tigers of Nanman. He is like a sibling to me, so I trust you will take good care of him.”

As if it understood Yayul Mok’s low voice, the White Tiger licked my hand, then pressed its nose against me and sniffed.

Yayul Mok smiled faintly as he watched it, then pointed in one direction.

“Go now. If you run straight northeast from the place where we first met, you will encounter the reconnaissance squad.”

And it was precisely then.

Thud.

A body jolted with the sound of an impact. Wonhu caught Yayul Mok as he collapsed, then grinned at me.

“I trust you understand without us saying it.”

“You people…”

“Please look after the Young Palace Lord.”

[^1]: Maechae Guyuk is pork belly served with preserved mustard greens; the Korean name is a shortened rendering of the Chinese dish name.
```
