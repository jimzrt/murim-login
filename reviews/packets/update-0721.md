<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0721.txt",
      "sha256": "4a16e4b0d913964e16a73ba31fe2bcab07cdb4a61de9fb16a968ae374b61dd55",
      "bytes": 14353
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1bd1c8c499d407d358ef5b85e1152ce84de89bcd8e0597352ee41f341bcdf7c0",
      "bytes": 1418
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5471124723f1e27b4de9cf0fe8060b7f8a51fa29c674a8e84c34c4ec4fdae675",
      "bytes": 208682
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "3ce8e3fa5aad7a503b28ff1585f38fe829381a2c1b6abe91e3195f4e4f0978ed",
      "bytes": 846
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "2ec79135167b3465a0ecc2cf37f7e47f4711da796fadf31d1610f5cb57bb11c6",
      "bytes": 553
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "905b33e27d4f4a6fa486ded0d2fa2681e88e0051765355bc401152b3ce19b4bd",
      "bytes": 1355
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "3c1ef006ee9d0a1fdfead4cf520b3b5fef1ca4529b56be8ad5cc96f280d31c18",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "46035c93c3b9b06739b26f1c6fad1a9c6562afd9a2c5fd2611532491a22ce60d",
      "bytes": 1787
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "ee16864fb0b4ed8fbfd95ff1510a354123ad2a13866347e4399921f9f7a68b43",
      "bytes": 622
    },
    {
      "path": "characters/White Tiger.md",
      "sha256": "c422ed70b389437660e133a5761b5dc1b23e499b52fef6e475143ebd54efdf94",
      "bytes": 641
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8c9370e66f36ae1c5da9e5fb2bed205edcf0688392c7bf8f70a9318539923074",
      "bytes": 219239
    }
  ],
  "estimated_tokens": 12227
}
-->

# Durable State Update — Chapter 721

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 721. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 721. Profile updates may replace only one
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
  "chapter": 721,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 721,
    "continuity_sources": [721],
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
    "The Sacred Land is distinct from the Poisonblood Grounds and is Nanman's life-filled heart.",
    "The Sacred Land's Pond of Life heals living bodies and purifies evil or impure energy.",
    "Jin Taekyung completed Quest [Corrupted Divine Artifact] by immersing the corrupted sacred stone in the Pond of Life.",
    "The artifact's demonic qi was completely purified, and the artifact became a new sacred stone.",
    "The Pond of Life released its remaining life energy as rain across Nanman and then dried up.",
    "The rain will soak Nanman for three days, enriching the soil, sustaining evergreen plants, and healing the wounded.",
    "The new sacred stone will remain in Nanman with a new guardian spirit.",
    "Muyaho is the new guardian spirit and is affectionate toward Jin Taekyung.",
    "Jeok Cheongang wanted to take the new guardian spirit, but the Beast Miao King refused."
  ],
  "continuity_sources": [
    720
  ],
  "open_questions": [
    "How will Muyaho's new role as guardian spirit develop?",
    "When will the Pond of Life recover its lost energy?"
  ],
  "safe_through": 720,
  "temporary_decisions": [
    "Render 생명의 연못 as Pond of Life.",
    "Render 타락한 신석 as Corrupted Sacred Stone, distinct from 타락한 신물, Corrupted Divine Artifact.",
    "Treat Muyaho as the new guardian spirit of the Sacred Land."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 일신     | **One God**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무림맹    | **Murim Alliance**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 무인     | **martial artist**                               | Default term                                          |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 태원     | **Taiyuan**            |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 대한민국 | **Korea** | Country reference. |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 대태원진가 | **great Jin Family of Taiyuan** | Formal exalted reference to the Jin Family of Taiyuan. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 사자후 | **lion's roar** | Taekyung's term for Song Il's crowd-shattering roar. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 백호 | 진태경 | guardian_spirit_to_human_ally | you | terse and irritated | The White Tiger responds telepathically after Jin calls it Whitey and jokes about its former name. |
| 야수묘왕 | 적천강 | junior allied master to legendary senior martial master | Old Master Jeok | formal-deferential | The Beast Miao King respectfully addresses Jeok while asking him to sit and consulting him about the demonic stone. |
| 적천강 | 야수묘왕 | senior allied martial master to Nanman Beast Palace Lord | you | blunt, commanding, and mocking | Jeok orders the Beast Miao King to stand aside and mocks his inability to destroy the corrupted artifact. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 720
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people who has resumed leadership of Nanman after the rift disaster.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang was his sworn younger brother and childhood companion, and the Beast Miao King killed him at his request; Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple and ally.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 718
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 717
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 720
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 719
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 719
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### White Tiger.md

# White Tiger (백호)

- **Safe through:** Chapter 720
- **Aliases:** Whitey
- **Role:** The White Tiger was the guardian spirit and protector of the land; after absorbing the sacred stone, it entered the rift to seal it, became corrupted, and was killed.
- **Personality:** Irritable and contemptuous of Jin Taekyung's jokes.
- **Voice:** Telepathic, terse, and easily exasperated.
- **Relationships:** The White Tiger shared a roughly three-hundred-year friendship with Yayul Cheon and entrusted Jin Taekyung and Jeok Cheongang with killing it if corruption overcame it.

## Korean source

```text
＃721화



‘그날’로부터 열흘 가까운 시간이 흐른 지금도, 남만야수궁에서는 수복 작업이 계속되고 있었다.

심장부라 할 수 있는 내궁(內宮)은 완전히 초토화되었고, 전투의 여파로 인해 외궁(外弓) 역시 상당한 피해를 입은 상황.

다행히 전사와 맹수들까지 총동원하여 짧은 시간 만에 대부분의 잔해를 수습할 수 있었지만, 당장 터전을 잃은 부족민들을 위해 지어야 하는 가옥과 전각을 생각하면 앞길이 구만리였다.

“자, 셋 하면 동시에 들자고. 하나, 둘.”

“흐읍!”

드드득!

힘을 합쳐 커다란 바위를 들어 올리고, 멍든 어깨에 두꺼운 목재를 짊어진다.

그러나 쉼 없이 계속되는 중노동에도 누구 하나 볼멘소리 없이 작업을 이어 나갔다.

이건 모두를 위한 일이었으니까.

남만야수궁은 이 땅을 살아가는 모든 이들의 상징이었고, 선조들에게 물려받은 마음의 고향이다.

함께 일하고 있는 이들이 어느 부족인지, 무엇을 입고 먹는지, 어떤 토속신을 믿는지 따위는 더 이상 중요하지 않다.

이 자리에 있는 모두는 오직 남만야수궁의 재건(再建)이라는 목표 하나로 이곳에 왔고, 그건 어느 중년인이 삼백 리나 되는 거리를 걸어 찾아온 이유이기도 했다.

팍!

힘차게 내려친 도끼날이 두꺼운 목재에 가로막혀 튕겨 나온다. 그와 동시에 손바닥을 타고 전해지는 쓰라린 통증.

본능적으로 신음을 흘린 중년인을 향해 한 청년이 다가왔다.

“그거 그렇게 휘두르는 거 아닌데. 잠깐 손 좀 줘 보세요.”

중년인이 엉겁결에 손을 내밀었다. 가업을 이어 일평생 상인으로 살아온 그의 손바닥은 어느새 물집과 피로 범벅이 되어 있었다.

“어이고, 아프시겠다. 이런 일 거의 안 해 보셨죠?”

“그, 그렇네만.”

“이게 힘만 준다고 되는 게 아니에요. 도끼날에 체중을 싣는 느낌으로 나무의 결을 따라서 한 번에 빡, 그렇게 하셔야지. 제가 시범 한번 보여 드릴까요?”

중년인은 변죽 좋게 말을 건네는 청년을 물끄러미 바라보았다.

친숙한 그의 태도에도 불구하고 미묘하게 낯설었다.

단지 처음 보는 얼굴이라서가 아니라 청년의 생김새가. 그리고 어린아이처럼 어눌한 어투까지.

그제야 문득 드는 떠오르는 생각이 있었다.

“혹시?”

“한족이냐고요? 맞습니다.”

“아, 그럼 소문으로만 듣던 그…….”

“예. 제가 바로 그 사람입니다.”

“오오. 오오오!”

탄성을 내지르는 중년인을 향해, 청년이 그윽한 미소를 지으며 입을 열었다.

“혁무진이라고 합니다.”

“열화신룡 진태…… 뭔 무진?”

“혁무진이요. 그 유명한 열화신룡 진태경의 오른팔! 대태원진가의 기둥! 자랑스러운 무림맹 화룡각의 부각주!”

뭐지, 이놈은.

‘혁, 뭐?’

한족 중에 그런 이름도 있었나.

열변을 토하는 혁무진을 떨떠름한 눈빛으로 바라보던 중년인이 다시 도끼를 잡으려던 그때였다.

툭. 투두둑.

갑자기 떨어져 내리기 시작한 빗방울.

동시에 일하던 이들 사이로 한숨이 흘러나왔다. 해야 할 일이 산더미인데, 비까지 오면 작업 속도가 느려지는 건 당연지사다.

“젠장. 이젠 하다 하다 마른하늘에 비까지 오는군.”

“뭐 어쩌겠나. 잠시 지나가는 소나기려니, 하고 생각해야지.”

“자자. 조금만 더 힘을 내자고!”

중년인은 힐끗 하늘을 바라보았다.

분명 먹구름 한 점 없는 맑은 날씨인데 비라니. 변화무쌍한 기후를 지닌 남만이라 해도 흔한 일은 아니었다.

‘그래도 소나기 정도라면 괜찮지.’

이미 전신이 땀으로 흠뻑 젖어 있었기 때문일까. 갑작스럽게 찾아온 비가 썩 나쁘게만 느껴지지는 않는다.

아니, 오히려 손바닥에 부딪히는 빗방울이 상처를 씻어 내리는 것 같아 기분이 좋았다.

‘시원하다.’

중년인이 자신도 모르게 지그시 눈을 감은 그 순간이었다.

덥석.

손목을 옥죄는 강한 힘. 그리고 깜짝 놀라 눈을 뜬 중년인은 볼 수 있었다.

“……뭐야, 이거.”

잔뜩 굳어 있는 혁무진의 얼굴과, 그의 시선이 머무른 자신의 손바닥에서 벌어지고 있는 변화를.

스르륵.

사라진다. 아니, 아물고 있다.

양 손바닥 가득 잡혀 있던 물집도, 도끼질로 인해 짓이겨지고 찢어진 살갗도.

흥건한 핏물이 빗방울에 씻겨 내려간 빈자리에는, 전보다 더 뽀얗고 단단해진 근육과 살이 그를 기다리고 있었다.

“……!”

“……!”

약속이라도 한 것처럼 동시에 눈을 부릅뜬 두 사람이 하늘을 올려다본 그 순간.

둥. 둥. 두웅!

햇빛을 머금은 빗줄기 사이로, 누군가의 귀환을 알리는 북소리가 들려오기 시작했다.



* * *



기적(奇蹟).

그 두 글자로 모든 것을 설명할 수 있었다. 아니, 그렇게 표현할 수밖에 없는 현상이었다.

투둑. 솨아아아.

어느 순간부터 떨어져 내리기 시작한 빗줄기.

따스한 온기를 머금은 그것은 무수한 건물과 대지를 적시며 꽃과 새싹을 피워 올렸고, 살아 있는 모든 것들의 머리 위로 떨어져 내렸다.

그들이 입은 상처와 피로를 씻어 내리며.

“상처가, 상처가 나았다!”

“몸이 가뿐해졌어!”

“이, 이게 도대체…….”

- 크릉?

그리고 이 믿기 힘든 현실 앞에 넋이 나간 그들을 일깨운 것은, 어디선가 울려 퍼진 사자후(獅子吼)였다.

- 남만야수궁주의 이름으로 명하니, 모두 밖으로 나와라!

강대한 공력이 실린 외침은 외궁 곳곳으로 뻗어 나갔고, 홀린 듯이 명령을 좇아 걸음을 옮긴 이들은 한 마리의 거대한 백호와 모두의 앞에 우뚝 선 세 사람을 볼 수 있었다.

적천강. 야수묘왕. 그리고 진태경.

“일단 네놈 말대로 죄다 불러 모으긴 했는데, 이제 어쩔 셈이냐?”

“그냥 나와서 비 맞으라고 하면 되는 거 아닌가? 어차피 직접 겪어 보면 알게 될 텐데.”

적천강과 야수묘왕의 속삭임에, 진태경은 망설임 없이 고개를 저었다.

뼛속까지 무인(武人)이라 할 수 있는 저들과 달리, 현대에서 나고 자란 그는 마케팅의 효과가 얼마나 큰지 알고 있었다.

“비 한번 맞으면 끝입니까? 그 전에 예쁘게 가공해서 포장을 해야죠.”

“가공? 포장?”

“대관절 그것이 무엇이냐?”

“그, 말하자면 복잡한데. 이번 경우에는 일종의 정치질이라고 보면 됩니다.”

대저 무인이란 족속들은 늙어 죽을 때가 되어도 정치와 거리가 멀다. 그러나 21세기 대한민국에서 태어났다면 이야기가 다르다.

단지 게임을 못한다는 이유만으로도 죽일 놈이 되는 냉혹한 세상.

재미 삼아 접속한 게임에서 수십 번이나 고아가 되었던 진태경은 정치의 중요성을 누구보다 잘 알고 있었다.

‘잘한 놈을 못한 것처럼, 못한 놈을 잘한 것처럼. 그리고…….’

잘한 놈을 더욱 잘한 놈으로 만들어 주는 게 바로 정치요, 현대판 마케팅인 것이다.

진태경은 이 절호의 기회를 놓칠 생각이 추호도 없었다.

‘그냥 이대로 우와 기적이다! 하고 끝나면 섭섭하지.’

내심 중얼거린 진태경은 심호흡했다. 그리고 사람들을 향해 공력을 실은 외침을 토해냈다.

“모두 들어라, 이건 대지모신(大地母神)께서 내리신 성스러운 비다!”

대지모신?

처음 듣는 이름에 사람들은 눈을 깜빡였고, 야수묘왕은 떨떠름한 표정으로 속삭였다.

“그게 뭐냐.”

“신이요.”

“우리 땅에는 그런 신 없는데.”

“지금 생겼는데요.”

“……?”

이 새끼 뭐지?

큰 혼란에 빠진 야수묘왕이 할 말을 잃은 그때, 진태경이 외침을 이었다.

“대지모신은 이 땅의 어머니이며, 유일한 신이시다!”

“……!”

“……!”

유일신(唯一神).

멍하니 진태경의 외침을 듣고 있던 사람들이 그 세 글자에 입을 벌렸다.

남만이 어떤 곳인가.

서른두 개의 부족이 공존하고, 부족의 숫자보다도 많은 백여 개가 넘는 토속신이 존재하는 곳이다.

그런데 유일신이라니.

아무리 재앙을 겪고 남만야수궁이 개판이 되었어도, 평생 믿어 온 신앙심은 여전한 법. 곳곳에서 분노 가득한 목소리가 터져 나왔다.

“어찌 그런 헛소리를!”

“대지모신이라니, 들어본 적도 없다!”

“그대가 남만을 위해 애쓴 것은 알지만, 감히 그런 망발을 입에 담다니! 내가 모시는 목신(木神)만이 유일한 신이시다!”

“어딜 목신을 들이대! 화신(火神)이야말로 진정한 신이시다!”

“아니, 이 새끼가!”

그야말로 아수라장이 되어 버린 장내. 그러나 멱살잡이까지 하며 싸우는 신도들을 바라보는 진태경의 표정은 흐뭇했다.

‘병신들.’

오호십육국만큼이나 혼란스러운 남만의 종교 판. 그 덕분에 일이 쉬워지게 생겼다.

저들과는 달리 자신의 주장에는 명분과 근거가 충분했으니까.

“멍청한 놈들 같으니! 이 성스러운 비를 맞으면서도 대지모신의 은총을 느끼지 못했단 말이냐!”

쩌렁쩌렁하게 울려 퍼지는 준엄한 일갈에 소음이 씻은 듯이 사라졌다.

타 신도를 향해 회심의 어퍼컷을 날리려던 부족민 하나가 혼란스러운 표정으로 하늘을 바라보았다.

솨아아아아.

맑은 하늘에서 쏟아져 내리는 빗줄기. 병든 이들을 고치고, 새싹을 틔우는 저 비를 보고 있자니 절로 마음이 복잡해진다.

“하, 하지만 목신께서는…….”

“그래서, 열흘 전에는 목신이 뭐 했는데? 내가 산에 불 지르고 다닐 때도 별거 없더만.”

“그, 그건.”

머뭇거리는 신도를 입닥치게 만든 진태경이 외쳤다.

“이 자리에 모인 모두가 보았을 것이다! 그날의 눈부신 광휘를! 따스한 온기를!”

“……!”

“그날의 기적도, 오늘의 기적도 모두 너희를 불쌍히 여기신 대지모신께서 내리신 축복이다!”

사람들의 눈빛이 흔들렸다.

진태경의 말마따나 그들은 모든 것을 보고, 겪은 산 증인이다. 심지어 머리 위로 떨어져 내리는 빗줄기 역시 믿을 수 없는 기적이 아닌가.

“대지모신…….”

심지어 이름까지 따스하고 정겹다. 그 네 글자를 읊조리는 것만으로도 어머니의 품이 생각난다.

게다가 유일신이란다. 하나밖에 없는 유일신.

“그, 그럼 지금까지 저희가 모셔 왔던 다른 신들은 무엇입니까?”

누군가의 질문에, 진태경이 한 치의 망설임도 없이 대답했다.

“감히 위대하신 대지모신과 잡신(雜神)을 비교할 수는 없지.”

“자, 잡신……!”

“대지모신께서 기적을 내리시며 말씀하셨다. 알쓸잡신. 알아봤자 쓸모없는 잡신들로부터 그대들을 지키라고.”

“오오. 오오오!”

“허어어. 이럴수가! 기적에 이어 신탁까지!”

어느덧 한 마음 한뜻이 된 탄성과 함께 뜨겁게 달아오르는 분위기.

진태경은 이 순간을 놓치지 않고 번쩍 두 손을 들어 올렸다.

“다 같이 외쳐라! 대지모신!”

“대지모신! 대지모신!”

“더 크게!”

“대지모신! 대지모신!”

“따라 해라. 모신천국! 불신지옥!”

“모신천국! 불신지옥!”

“대지모신을 믿는 남만인은 죽어서도 구원받을 것이요, 믿지 않는 자는 죽어서 불구덩이에 떨어지리라!”

“우와아아아! 모신이시여!”

“저희를, 이 땅을 구원하소서어억!”

어느새 대지모신의 아들딸이 되어 버린 부족민들의 모습에, 야수묘왕은 넋 나간 눈빛으로 진태경을 바라보았다.

‘뭐 하는 짓이야, 이 미친놈아.’

말리고 싶다. 말려야 한다.

정치질이니 포장이니 하는 건 모르겠고, 일단 다들 눈빛부터 맛탱이가 가 버렸다.

피를 토하듯이 대지모신을 부르짖는 소리에 하늘과 땅이 울렸다.

“모신천국! 불신지옥!”

“아까 목신 믿는다는 놈 어디 갔어!”

“저기 있다! 저놈이다! 불구덩이에 처박아라!”

“헉! 아니오! 나, 난 이미 개종했소!”

“증거를 대라!”

“모, 모신천국! 불신지옥!”

“아군이다! 포박 중지! 이제 화신 믿던 놈 찾아라!”

사방에서 넘쳐흐르는 개종의 물결.

무려 수천, 수만에 달하는 이들이 발산하는 압박감에 내심 화신을 한 번 믿어 볼까, 고민하던 적천강조차 입을 다물었고 야수묘왕은 어떻게든 이 미친 광기를 멈추게 하고 싶었다.

“이, 이제 그만…….”

그리고 야수묘왕이 간신히 목소리를 끄집어낸 그 순간. 진태경의 외침이 울려 퍼졌다.

“모두 조용! 남만야수궁의 궁주이자, 대지모신께 선택받으신 제사장께서 말씀하시지 않느냐!”

“그만…… 뭐?”

“말씀하십시오. 제사장님.”

뭔 사장?

‘제사장? 내가?’

야수묘왕이 미처 그 단어의 의미를 깨닫기도 전에, 무수한 시선이 날아와 그를 향했다.

온 사방에 내려앉은 숨 막히는 적막.

나름 인망 있는 궁주였던 그조차 본적 없던, 그 어느 때보다 사랑과 신뢰가 듬뿍 담긴 시선들.

“……!”

다음 순간, 석상처럼 굳어 있던 야수묘왕의 입술이 열렸다.

“모신천국. 불신지옥.”

“와아아아아!”

그것은 위대하신 대지모신의 보살핌 아래, 진정한 남만 대통합이 이루어진 역사적인 순간이었다.
```

## Final English reading copy

```markdown
# Chapter 721

Even now, nearly ten days after *that day*, restoration work was still underway at the Nanman Beast Palace.

The Inner Palace, which could be called its heart, had been completely devastated, and the Outer Palace had also suffered considerable damage in the aftermath of the battle.

Fortunately, by mobilizing all the warriors and beasts, they had managed to clear away most of the rubble in a short time. But considering all the houses and pavilions that still had to be built for the tribespeople who had suddenly lost their homes, the road ahead seemed endless.

“Now, let’s lift it together on three. One, two.”

“Hngh!”

Crack!

They combined their strength to lift a huge boulder, then hoisted thick timber onto bruised shoulders.

Yet despite the unending hard labor, not a single person complained as they continued working.

Because this was work for everyone's sake.

The Nanman Beast Palace was a symbol of everyone who lived on this land, a spiritual homeland passed down from their ancestors.

It no longer mattered which tribe the people working together belonged to, what they wore or ate, or which local deity they believed in.

Everyone present had come here for one goal alone: the reconstruction of the Nanman Beast Palace.

It was also the reason one middle-aged man had walked three hundred li to reach this place.

Whack!

The ax blade he swung with all his strength bounced off the thick timber. At the same time, a sharp pain traveled up through his palm.

A young man approached the middle-aged man, who had instinctively groaned.

“You’re not supposed to swing it like that. Let me see your hand for a moment.”

The middle-aged man instinctively held out his hand. He had inherited the family business and spent his entire life as a merchant, but his palms were now covered in blisters and blood.

“Ouch, that must hurt. You’ve hardly ever done this kind of work, have you?”

“I-I suppose not.”

“This isn’t something you can do just by using your strength. You have to put your weight behind the ax blade and follow the grain of the wood. One solid whack, like this. Want me to demonstrate?”

The middle-aged man stared blankly at the young man speaking to him so affably.

Despite his easygoing manner, there was something subtly unfamiliar about him.

It wasn’t merely because he was a stranger. It was the young man’s appearance—and his awkward way of speaking, almost like a child.

Only then did a thought suddenly occur to him.

“Could you be…?”

“You mean, am I Han Chinese? That’s right.”

“Ah, then you’re the one I’ve only heard about through rumors…”

“Yes. I’m that very person.”

“Oh! Ohhh!”

As the middle-aged man exclaimed, the young man opened his mouth with a gracious smile.

“My name is Hyuk Mujin.”

“The Blazing Flame Divine Dragon Jin Tae…what Mujin?”

“Hyuk Mujin. The famous Blazing Flame Divine Dragon Jin Taekyung’s right-hand man! The pillar of the great Jin Family of Taiyuan! The proud Vice Pavilion Master of the Murim Alliance’s Fire Dragon Pavilion!”

What the hell was wrong with this guy?

*Hyuk…what?*

Had the Han Chinese started giving people names like that?

The middle-aged man stared at Hyuk Mujin with an uncertain expression, but just as he was about to pick up his ax again—

Tap. Tap-tap.

Raindrops suddenly began to fall.

At the same time, sighs escaped from the people working nearby. There was a mountain of work left to do, and rain would naturally slow them down.

“Damn it. Now it’s raining from a clear sky, too.”

“What can we do? We’ll just have to think of it as a passing shower.”

“Come on, everyone. Let’s keep going a little longer!”

The middle-aged man glanced up at the sky.

Rain from a clear day without a single cloud? Even in Nanman, with its unpredictable climate, this was unusual.

*Still, if it’s only a shower, it should be fine.*

Perhaps because his entire body was already soaked in sweat, the sudden rain didn’t feel entirely unpleasant.

No. In fact, the raindrops striking his palms felt as though they were washing away his wounds, and he found himself enjoying it.

*Refreshing.*

The middle-aged man unconsciously closed his eyes for a moment.

Then—

Grab!

A powerful hand clamped around his wrist. Startled, the middle-aged man opened his eyes and saw it.

“What…is this?”

Hyuk Mujin’s face had gone rigid.

His gaze was fixed on the middle-aged man’s palm, where something strange was happening.

Slowly.

It was disappearing. No—it was healing.

The blisters that had filled both palms, the skin crushed and torn by swinging the ax…

The rain washed away the abundant blood, revealing new muscle and flesh beneath—paler and firmer than before.

“……!”

“……!”

As though they had planned it together, the two men looked up at the sky with wide eyes.

Boom. Boom. Booooom!

Between the sunlit streams of rain, the sound of drums began to ring out, announcing someone’s return.

* * *

A miracle.

Everything could be explained with those two words. No, it was the only way to describe the phenomenon.

Tap. Ssshhh.

At some point, rain had begun falling.

Warmth filled the rain as it soaked countless buildings and the earth, causing flowers and sprouts to bloom. It fell upon the heads of every living thing.

Washing away their wounds and fatigue.

“My wound! My wound healed!”

“My body feels so light!”

“W-what in the world is this…?”

—Growl?

What roused the people, who had been dazed before this unbelievable reality, was a lion’s roar that rang out from somewhere.

—By order of the Palace Lord of the Nanman Beast Palace, I command you all to come outside!

The shout, filled with powerful internal energy, spread throughout the Outer Palace. Those who began walking as if bewitched by the command saw a massive White Tiger and three people standing tall before everyone.

Jeok Cheongang. The Beast Miao King. And Jin Taekyung.

“I called everyone here like you told me to. What are you planning to do now?”

“Wouldn’t it be enough to tell them to come outside and get rained on? They’ll understand once they experience it themselves.”

At the Beast Miao King and Jeok Cheongang’s whispers, Jin Taekyung shook his head without hesitation.

Unlike those two, who were martial artists to the bone, he had been born and raised in the modern world. He knew exactly how effective marketing could be.

“Is it over after they get rained on once? First, you have to process it properly and package it.”

“Process it? Package it?”

“What in the world does that mean?”

“It’s complicated, but in this case, you can think of it as a kind of political maneuvering.”

Martial artists were generally far removed from politics, even when they were old and nearing death.

But being born in twenty-first-century Korea was a different story.

It was a ruthless world where you could become someone who deserved to die just because you were bad at a game.

Jin Taekyung, who had been called an orphan dozens of times in games he had logged into just for fun, knew the importance of politics better than anyone.

*Make the guy who did well look like he failed, and the guy who failed look like he did well. And…*

Politics—modern marketing—was what made the guy who had done well look even better.

Jin Taekyung had no intention of letting this perfect opportunity slip away.

*It’d be a shame to just end things with everyone going, “Wow, a miracle!”*

He muttered inwardly, then took a deep breath. He shouted toward the people, filling his voice with internal energy.

“Listen, everyone! This is a holy rain bestowed by the Earth Mother Goddess!”

The Earth Mother Goddess?

The people blinked at the unfamiliar name, while the Beast Miao King whispered with a displeased expression.

“What is that?”

“A god.”

“There’s no god like that in our land.”

“There is now.”

“……?”

*What the hell is wrong with this bastard?*

As the Beast Miao King fell into deep confusion and lost all words, Jin Taekyung continued shouting.

“The Earth Mother Goddess is the mother of this land, and she is the One God!”

“……!”

“……!”

The One God.

The people who had been listening blankly to Jin Taekyung opened their mouths at those three words.

What kind of place was Nanman?

Thirty-two tribes coexisted here, and there were more than a hundred local gods—more gods than there were tribes.

And now he was claiming there was only one God?

Nanman might have suffered a disaster and the Nanman Beast Palace might have gone to shit, but the faith they had held all their lives remained.

Angry voices erupted from every direction.

“How dare you say such nonsense!”

“The Earth Mother Goddess? I’ve never heard of her!”

“I know you have worked hard for Nanman, but how dare you utter such blasphemy! The Wood God I worship is the One God!”

“What do you mean, the Wood God? The Fire God is the true god!”

“Why, you little bastard!”

The entire courtyard became a chaotic mess.

Yet Jin Taekyung looked pleased as he watched the believers grabbing one another by the collars and fighting.

*Idiots.*

Nanman’s religious scene was as chaotic as the Sixteen Kingdoms.[^1] Thanks to that, things were about to become much easier.

Unlike theirs, his claim had both justification and evidence.

“You fools! Even while being drenched in this holy rain, you still can’t feel the Earth Mother Goddess’s grace?”

His stern reprimand rang across the courtyard, and the noise vanished as if it had been washed away.

One tribesman who had been about to throw a decisive uppercut at another believer looked up at the sky in confusion.

Ssshhhhhh.

Rain poured from the clear sky.

As he watched the rain heal the sick and coax sprouts from the earth, he couldn't help feeling conflicted.

“B-but the Wood God…”

“So what did your Wood God do ten days ago? Even when I was setting fire to the mountain, it didn’t do much.”

“Th-that…”

Jin Taekyung silenced the hesitating believer with a shout.

“Everyone gathered here must have seen it! The dazzling radiance of that day! The warmth!”

“……!”

“The miracle that day and the miracle today are both blessings bestowed by the Earth Mother Goddess, who took pity on you!”

The people’s eyes wavered.

Just as Jin Taekyung said, they had all seen and experienced everything themselves. Even the rain falling on their heads was an unbelievable miracle.

“The Earth Mother Goddess…”

Even her name was warm and familiar. Simply murmuring those four words made them think of a mother’s embrace.

And she was the One God, too. The one and only One God.

“Th-then what are the other gods we’ve worshiped until now?”

At someone’s question, Jin Taekyung answered without the slightest hesitation.

“How dare you compare the great Earth Mother Goddess with miscellaneous gods?”

“M-miscellaneous gods…!”

“The Earth Mother Goddess bestowed this miracle and gave me a divine message: ‘Useless gods. The kind that aren’t worth knowing.’ She told me to protect you from them.”

“Oh! Ohhh!”

“How could this be? A miracle, and now a divine revelation, too!”

Before long, the atmosphere grew feverish, filled with shouts from people united in heart and mind.

Jin Taekyung seized the moment and raised both hands high.

“Shout together! Earth Mother Goddess!”

“Earth Mother Goddess! Earth Mother Goddess!”

“Louder!”

“Earth Mother Goddess! Earth Mother Goddess!”

“Repeat after me. Mother Goddess Heaven! Unbeliever Hell!”

“Mother Goddess Heaven! Unbeliever Hell!”

“Those in Nanman who believe in the Earth Mother Goddess will be saved even after death, while those who do not believe will fall into a pit of fire when they die!”

“Woooooah! O Mother Goddess!”

“Save us! Save this land!”

The tribespeople had already become sons and daughters of the Earth Mother Goddess.

The Beast Miao King stared at Jin Taekyung with an empty expression.

*What the hell are you doing, you lunatic?*

He wanted to stop him. He had to stop him.

He didn’t know anything about politics or packaging, but everyone’s eyes had already gone completely off the rails.

The heavens and earth shook beneath the people’s cries, shouted as though they were vomiting blood.

“Mother Goddess Heaven! Unbeliever Hell!”

“Where’s that guy who said he believed in the Wood God?”

“He’s over there! That one! Throw him into the fiery pit!”

“Gasp! No! I-I’ve already converted!”

“Prove it!”

“M-Mother Goddess Heaven! Unbeliever Hell!”

“He’s one of us! Stop tying him up! Now find the guy who believed in the Fire God!”

A wave of conversions overflowed in every direction.

The oppressive force radiating from thousands—tens of thousands—of people was so great that even Jeok Cheongang, who had privately wondered whether he should try believing in the Fire God, fell silent.

The Beast Miao King, meanwhile, desperately wanted to stop this insane fervor.

“E-enough now…”

And at the moment the Beast Miao King finally managed to drag a voice from his throat, Jin Taekyung’s shout rang out.

“Everyone, quiet! The Palace Lord of the Nanman Beast Palace—the priest chosen by the Earth Mother Goddess—is about to speak!”

“Enough…what?”

“Please speak, Priest.”

“What kind of boss?”

*Priest? Me?*

Before the Beast Miao King could even understand the meaning of the word, countless gazes flew toward him.

A suffocating silence settled over the entire area.

Even he, a Palace Lord with considerable popularity, had never seen gazes so filled with love and trust.

“……!”

The next moment, the lips of the Beast Miao King, who had gone rigid like a statue, parted.

“Mother Goddess Heaven. Unbeliever Hell.”

“Waaaaaaaaah!”

Under the care of the great Earth Mother Goddess, it was a historic moment—the true unification of Nanman.

[^1]: The Sixteen Kingdoms was a period of political fragmentation and competing states in Chinese history.
```
