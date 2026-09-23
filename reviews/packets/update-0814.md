<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0814.txt",
      "sha256": "1e6c1b4f1d8aed8a76e435d881847818576e3503030d126e5021afd7b101a21c",
      "bytes": 12821
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "cc394e5d9093896a869041e9896dd25eea3f9e86b51270dede67f57d9f63769b",
      "bytes": 1347
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d35561e9eeda408d2d3d95f408c0701d3a519a2572131960be203de4940f932c",
      "bytes": 225775
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "aebdbadbe1ecaebbc3f364493d6a52ad11588ce508be0a463bc694d7ac0f90bf",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "a2b83c3e2986a913c3a68cfdd29362f52d6d62294360c1032ccecda2732682f4",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "46e905c12d13364a74f999edd348166128f32a2ce53d6ede089a8ffb2b961b8e",
      "bytes": 622
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "aa39ffa04fe4d19e5cc53cb8203d994c758cd1b7e7450e881abb393522d7cf7e",
      "bytes": 724
    },
    {
      "path": "characters/Yamamoto.md",
      "sha256": "78e9633fb316cfb5c1c42d22595b09f254579075ac28ece5e54952500b423c6c",
      "bytes": 588
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "00e6d7d0bd6884c780f65f7d2a6a060a0e493a989f7f38fc51b7ef2e9500d415",
      "bytes": 248856
    }
  ],
  "estimated_tokens": 9588
}
-->

# Durable State Update — Chapter 814

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 814. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 814. Profile updates may replace only one
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
  "chapter": 814,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 814,
    "continuity_sources": [814],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "The Prophet is a Level 170 Doppelganger titled “The Final Abyss”; it has devoured countless lives and concealed itself for more than thirty years, including under the name Muninn.",
    "The Doppelganger says it met Michael Silbert during the 2020 Battle of Paris, made a pact with him, and had him kill the remaining humans in exchange for sparing him.",
    "Jin used the single-target Truthful Eye on The Prophet, revealing its identity. The item has been used.",
    "The Prophet is alive and pinned to the cliff after Jin, Magic Johnson, and the Skeleton King attacked it; a distant tremor interrupts them.",
    "Magic Johnson says he helped Jin because they are friends; whether Johnson is human remains uncertain."
  ],
  "continuity_sources": [
    812,
    813
  ],
  "open_questions": [
    "Why did the Doppelganger want to live among humans?",
    "What is causing the tremor in the canyon?",
    "Is Magic Johnson human?"
  ],
  "safe_through": 813,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep the Demon Realm language distinct from other languages."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 살기     | **killing intent**                               |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 야마모토 | **Yamamoto** | Japanese S-rank Hunter named in post-Leviathan media coverage. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 알라 | **Allah** | Deity invoked by the Middle Eastern terrorist groups' rhetoric. |
| 수마 | **sleep demon** | Metaphor for the force keeping Jin unconscious. |
| 재생 | **Regeneration** | The masked man's rapid recovery from shattered bones and severe wounds. |
| 도쿄 | **Tokyo** | City visible behind Huginn's departing ship. |
| 일본 | **Japan** | Country requesting emergency assistance and under Leviathan's attack. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 엄마 | 진태경 | mother_to_son | my son | warm and affectionate | Taekyung's mother praises him during the public welcome. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 진태경 | 야마모토 | Alliance Leader to Japanese S-rank Hunter he sent on the mission | Yamamoto | blunt and familiar | Jin quietly says Yamamoto’s name while treating him. |
| 야마모토 | 진태경 | Japanese Hunter to the Alliance Leader who rescued him | Chōsenjin | insulting | Yamamoto uses the ethnic slur as he regains the ability to speak. |
| 진태경 | 선지자 | enemy commander addressed by Jin | The Prophet | blunt and informal | Jin asks where The Prophet is while confronting the Manticore Lord. |
| 존슨 | 진태경 | allied friend and comrade-in-arms | Jin | familiar and conversational | Johnson calls Jin 진 while asking what he was thinking. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 813
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 813
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 813
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 813
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades as Muninn.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors and is revered by its followers; it made a pact with Michael Silbert during the 2020 Battle of Paris, where Michael killed the surviving humans in exchange for being spared.

### Yamamoto.md

# Yamamoto (야마모토)

- **Safe through:** Chapter 813
- **Aliases:** None
- **Role:** Yamamoto Genji is revealed to be The Prophet, the monster who has posed as Muninn.
- **Personality:** Prideful and easily offended, prone to self-aggrandizement and self-serving assumptions, and cowardly under mortal threat.
- **Voice:** Not established.
- **Relationships:** Jin Taekyung sent Yamamoto on the J1 mission and treated him after the attack, though Jin resents Yamamoto for arriving late during the Leviathan crisis.

## Korean source

```text
＃814화



투둑. 드드득.

지반이 흔들린다. 까마득히 높게 솟은 절벽에서 떨어져 나온 흙과 암석 파편이 하나둘씩 머리 위로 쏟아져 내렸다.

“……빌어먹을.”

매직 존슨이 신음처럼 중얼거린다. 협곡의 출구를 봉쇄한 스켈레톤 킹과 수백의 언데드는 자세를 낮추고 어둠 속을 노려보았다.

정확히는 저 너머에서 다가오고 있는 수많은 적을.

솨아아아.

나는 호흡을 가다듬으며 기감을 끌어올렸다. 한껏 곤두선 감각으로 주위의 모든 정보를 받아들였다.

지면을 통해 전해지는 울림의 크기와 깊이. 서쪽에서 불어오는 바람과 그에 스며 있는 냄새. 그리고 소리.

먼 거리다 보니 적들의 정확한 숫자나 수준을 파악하는 건 무리였으나, 한 가지 사실만큼은 확신할 수 있었다.

‘몬스터가 아니다.’

그렇다면 남은 건 하나뿐이다. 내 시선을 느낀 도플갱어가 피에 젖은 이빨을 드러내며 웃었다.

“인간이란 참 희한한 존재야. 본 적도 없는 존재를 신이라 부르며 목숨을 내던지니까. 근엄한 척 말 몇 마디만 내뱉어도 눈물을 줄줄 흘리더군.”

“광신도들…….”

“나는 처음부터 이 땅이 참 마음에 들었어. 일을 꾸미거나 은폐하기에도 좋고, 무엇보다 종교라면 영혼까지 바치는 인간들이 득실거렸거든. 그런 멍청이들의 믿음을 얻는 건 놀랄 만큼 쉬웠지.”

스슥. 뿌드득.

깨끗하게 잘려 나간 손목의 단면이 꿈틀거린다. 부서진 갑옷 사이로는 단검에 베인 가슴에는 어느새 뽀얀 새 살이 돋아나 있었다.

포션도, 마법도 아니다.

하지만 놈은 지금 이 순간에도 망가진 몸을 회복하고 있었다.

한눈에 봐도 인간의 것이 아닌, 믿을 수 없을 정도의 회복력.

그 누구라도 의심할 수밖에 없는 재생(再生)의 힘.

그러나 이와 같은 광경은 대격변 이전부터 전 세계를 상대로 테러를 벌이던 광신도들에게 다른 모습으로 비쳤을 것이다.

자신들과 같은 붉은 피와 살, 마나를 사용하는 도플갱어에게서 신의 그림자를 엿보았을지도 모른다.

“기적.”

들뜬 목소리가 울려 퍼졌다. 도플갱어는 형형한 안광으로 나를 응시하며 말을 이었다.

“저들이 바라보는 나는 괴물이 아닌 기적 그 자체요, 약속의 땅으로 이끌 선지자다.”

“……!”

“최후의 한 사람이 쓰러지는 순간까지 싸우겠지. 신을 위해. 그리고 나를 위해.”

나는 확신에 찬 도플갱어의 말에 반박하지 않았다.

엄연한 현실이니까.

무슨 수를 쓴다 해도 격돌은 피할 수 없다.

도플갱어는 내가 예상했던 것보다 훨씬 오래전부터 자신의 추종자들을 이 사막에 심었고, 그렇게 시작된 광신도의 물결은 이미 테러라는 형태로 전 세계를 뒤흔들었다.

그러니 내가 저 광신도들에게 도플갱어의 정체를 알려 봤자 아무것도 달라지지 않는다.

‘말 몇 마디 정도로 순순히 넘어갈 놈들이었다면, 광신도라 부르지도 않았겠지.’

이건 결국 괴물과 미친놈들이 만들어 낸 합작품이었고, 지금의 나는 반드시 죽여 없애야 하는 이교도일 뿐이다.

신이 내린 위대한 선지자를 핍박하는 이교도.

“그럼 남은 길은 하나밖에 없네.”

나는 담담하게 뇌까리며 도플갱어를 응시했다. 내가 한 말의 의미를 깨달은 놈이 입꼬리를 말아 올렸다.

“그거 기대되는군.”

“그래?”

푹!

말과 함께 뻗은 단검이 심장을 관통한다.

사지가 결박되어 있었기에 피할 수도 없었던 일격. 그러나 도플갱어는 눈살을 찌푸리며 한숨을 내쉬었다.

“적당히 하지. 더럽게 아프네.”

뿌드득.

끊어졌던 근육이, 박살 났던 뼈가 제자리를 찾는다. 선홍빛 핏물이 차오르고 어린아이처럼 매끄러운 살갗이 그 위를 덮었다.

마치 동영상을 빠르게 재생시킨 것처럼 엄청난 회복 속도.

사지를 꿰뚫고 그대로 절벽 깊숙이 박힌 커다란 뼛조각들마저 재생된 살과 뼈에 밀려 조금씩 들썩이고 있었다.

내가 [진실의 눈]으로 보았던. 그리고 지금도 보고 있는 수많은 레벨 창은 결코 단순한 의미가 아니었다.

‘또 다른 목숨.’

그것은 양분인 동시에 도플갱어가 집어삼킨 희생자들의 생명이다.

마치 동전만 넣으면 되살아나는 오락실 게임 캐릭터처럼, 놈은 끊임없이 부활할 수 있었다.

‘하지만 완전한 불사(不死)는 아니지.’

나는 여전히 손에 쥐고 있던 단검을 비틀었다. 단전에서 솟구친 열기가 혈도를 타고 단검으로 내달렸다.

푹, 퍼엉!

가슴 깊숙이 박아넣은 단검을 따라 흘러나온 열양지기가 도플갱어의 몸 깊숙한 곳에서 폭발한다.

앞서 한 번 관통당했음에도 불구하고 불사신처럼 회복하고 있던 심장이 완전히 으스러지자, 기다렸던 맑은 종소리가 귓가를 울렸다.

띠링.



- [Lv.120 야마모토 겐지]를 처치했습니다!

- 상당량의 경험치를 획득했습니다!



“……!”

한 사람의 생명이 사그라지고, 새로운 생명이 차오른다.

도플갱어는 여전히 웃고 있었다. 녹듯이 흘러내린 살갗 뒤에는 또 다른 누군가의 낯선 얼굴이 준비되어 있었다.

“이런. 바로 그 진태경이 겐지를 죽이다니. 이 사실을 일본에서 알면 한바탕 난리가 나겠는데.”

“아가리 닥쳐.”

낮은 콧대와 입안으로 보이는 덧니.

동양인 중에서도 구분되는 특유의 이목구비를 보아하니, 야마모토 겐지를 제외하고 전멸당했다고 알려진 J1 팀 소속의 헌터가 분명했다.

“그러고 보니 인사를 깜빡했군. 반가워, 난 이노우에 히로시라고 한다. 나가사키에서 어린 시절을 보낸 뒤 도쿄로 상경…….”

덥석, 콰드득.

목을 붙잡고, 그대로 힘주어 비틀었다.

무시무시한 손아귀 힘을 이기지 못하고 단번에 목뼈가 으스러진 도플갱어의 고개가 기이하게 꺾였다.

띠링. 또 한 번의 종소리와 함께 꺾였던 고개가 바로 세워졌다. 새치름하게 웃고 있는 얼굴은 처음 보는 여자의 것이었다.

“오, 혹시 그거 알아? 이 여자, 방금 네가 죽인 그 인간의 연인이었어. 올해 안에 결혼할 생각이었나 봐.”

“……!”

누군가 정지 버튼을 누른 것처럼 우뚝 멈춰선 손. 도플갱어가 흥미진진하다는 듯이 휘파람을 불었다.

“이야, 뜨겁다. 뜨거워. 확실히 이런 면에서는 인간들이 대단하다니까. 우리도 좀 배울 필요가 있어.”

“……너.”

“아, 미안. 불편하게 느껴졌다면 사과하지. 하지만 이게 내 능력인 걸 어떡해?”

나는 이를 악물었다.

도플갱어가 희생자들로부터 흡수한 것은 겉모습뿐만이 아니었다. 그들이 생전에 갖고 있던 능력을 그대로 재현하는 것으로도 모자라, 기억마저 제 것으로 만들었다.

그리고 놈의 주둥이에서 흘러나오는 그들의 기억이, 내 가슴을 송곳처럼 후벼 파고 머뭇거리게 만들었다.

으득.

악문 잇새 사이로 피가 흘렀다.

어느덧 협곡 너머에서는 더욱더 강해진 진동과 함께 흉흉한 살기(殺氣)가 느껴졌고, 눈앞에는 죽여도 죽여도 되살아나는 괴물이 빙긋 웃고 있다.

“진!”

매직 존슨의 다급한 외침이 고막을 때린다. 도플갱어의 입가에 맺힌 미소가 진해졌다.

“마지막 기회야.”

“뭐?”

“바로 지금이, 네가 도망쳐서 살아남을 수 있는 마지막 기회라고.”

“……!”

훅.

서늘한 사막의 바람이 얼굴에 닿았다. 마치 찬물을 뒤집어쓴 기분이다.

석상처럼 굳어 버린 나를 향해 도플갱어가 어깨를 으쓱해 보였다.

“이해해. 자존심 상하고 쪽팔리겠지. 하지만 네가 다른 인간들처럼 여기에서 죽으면? 그건 개죽음이 아니라 영웅의 숭고한 희생인가?”

“……그건.”

“멀리, 넓게 봐야지. 넌 세계 헌터 연맹의 맹주잖아. 과거 어떤 인간이 그랬듯이 이 세상을 구원할 수 있는 유일한 빛이자 희망. 안 그래?”

나긋나긋한 목소리가 귓가를 간질였다. 금기된 사과를 훔쳐 먹으라 권유하는 뱀의 목소리처럼.

낮게 깔린 도플갱어의 속삭임은 부드럽게 내 전신을 휘감았다.

“도망쳐. 그리고 살아남아.”

구구궁.

협곡이 뒤흔들린다. 무수한 광신도들의 발걸음이, 그들이 올라탄 낙타의 발굽이 가파르게 저 어둠 너머에서 다가오고 있었다.

“가족과 친구들을 생각해. 네 죽음으로 인해 그들이 겪을 슬픔과 고통이 얼마나 클지, 상상이나 가?”

“……슬픔과 고통?”

“그래. 너도 이미 겪어 봤잖아.”

나는 소리 없이 입술을 달싹였다.

누군가의 죽음으로 인한 슬픔과 고통. 그래, 겪어 봤다. 마음이 흔들리다 못해 무너질 것 같은 경험이었다.

“누구도 널 비난하지 않아. 심지어는 나조차도 네가 해 온 일들을 존중하지. 그러니 지금이라도…….”

이름 모를 여자의, 아니 도플갱어의 눈동자가 반짝였다.

“도망쳐.”

- 알라 후 아크바르!

수많은 목소리가 모여 하나로 합쳐진 거대한 함성이 어둠이 내리깔린 사막에 울려 퍼진다.

매직 존슨을 중심으로 눈부신 광휘가 어른거렸고, 수백의 언데드들은 흐릿한 안광으로 자신들을 향해 덮쳐 오는 무수한 광신도들의 파도를 바라보고 있었다.

그리고 나는…… 도플갱어의 목을 붙잡고 있던 손을 놓았다.

저벅.

한 걸음 물러나자 웃고 있는 도플갱어의 모습이 보였다. 놈은 마치 어린아이를 대하는 듯한 부드러운 목소리로 말을 건넸다.

“좋아. 잘 생각했어.”

나는 문득 중얼거렸다.

“이게 최선일까?”

“그럴 거야.”

“그렇다면 다행이고.”

고개를 끄덕인 나는 속삭이듯 중얼거렸다.

“오픈. 소환.”

“응?”

서걱!

공허한 되물음과 함께 도플갱어의 목이 솟구쳤다.

마치 책의 페이지를 넘긴 것처럼 새롭게 어깨 위로 솟아난 얼굴이 눈을 깜빡였다.

백염의 창날을 휘감으며 타오르는 열기가 놈의 눈동자를 불그스름하게 달구고 있었다.

“무슨 씨벌 통신 교환 실패한 메타몽 같은 새끼가. 어디서 개수작 부리고 있어?”

그제야 상황을 파악한 도플갱어가 한숨을 내쉬었다.

“이런 미친놈…….”

“좀 더 참신한 거 없냐. 하도 들어서 좀 지겨운데.”

“도대체 이러는 이유가 뭐지?”

“그건 내가 묻고 싶은 말인데.”

“뭐?”

“처음부터 헛소리를 지껄이길래 이게 뭔가 싶었는데, 듣다 보니까 흥미가 생기더라고. 내가 살다 살다 인간한테 도망치라고 하는 몬스터 새끼는 또 처음 봐서 순간 엄마라고 부를 뻔했다, 이 개새끼야.”

“…….”

“너, 도대체 뭐 하는 놈이냐? 들키지 않으려고 안간힘 쓰면서도 티 팍팍 내는 거 보니 멍청한 건 알겠고, 진짜 원하는 게 뭐야?”

짧은 침묵이 흘렀다. 말없이 나를 응시하던 도플갱어가 미간을 찌푸렸다.

“빌어먹을. 일 한번 더럽게 꼬였군. 왜 이렇게 무모하지? 숭고한 희생을 한 영웅. 뭐 그렇게 역사에 남고 싶은 거냐?”

“코끼리 코 빠는 소리 집어치우고 대답이나 해라. 내 장래희망이 장수마을 촌장이야.”

“그럼 도대체 왜……!”

삐이잇!

하늘에서 울려 퍼진 무언가의 울음소리가 도플갱어의 뒷말을 삼켰다.

자연스럽게 머리 위 상공을 올려다본 놈의 눈동자가 문득 크게 뜨였다.

“……저건?”

지금 도플갱어의 눈에 비친 광경을, 나는 이미 알고 있다.

부대를 나누어 떠나기 전, 직접 스켈레톤 킹에게 전음을 날려 지시했던 것이었으니까.

“조금 늦긴 했는데. 그래도 때맞춰 왔네.”

삐이이잇!

수십여 마리의 독수리와 그리핀이 날개를 활짝 편 채 협곡 위를 활강한다.

거대한 날짐승들의 위에는 동쪽으로 떠났어야 했을 헌터들의 얼굴이 보였다.
```

## Final English reading copy

```markdown
# Chapter 814

*Crack. Rumble.*

The ground shook. Clods of dirt and fragments of rock broke away from the impossibly high cliffs and began raining down overhead, one after another.

“……Damn it.”

Magic Johnson muttered with a groan. The Skeleton King and hundreds of undead, blocking the canyon’s exit, crouched low and glared into the darkness.

More precisely, at the countless enemies approaching from beyond it.

*Fwoooosh.*

I steadied my breathing and raised my Qi Sense. With my senses sharpened to their limits, I took in everything around me.

The depth and intensity of the tremors traveling through the ground. The wind blowing from the west, and the scent carried on it. And the sounds.

The distance made it impossible to determine the enemies’ exact number or strength, but I could be certain of one thing.

*They’re not monsters.*

That left only one possibility. The Doppelganger, sensing my gaze, bared its bloodstained teeth in a grin.

“Humans are such strange creatures. They’ll throw their lives away for a being they’ve never even seen, calling it a god. All it takes is a few solemn words, and they’re weeping buckets.”

“Fanatics……”

“I liked this land from the start. It was a good place to make plans and cover them up. Most of all, it was crawling with people willing to give their very souls to religion. It was astonishingly easy to win the faith of fools like that.”

*Squirm. Crack.*

The cleanly severed stump of its wrist twitched. Through the gaps in its shattered armor, I could see fresh, pale flesh already growing over the dagger wound in its chest.

It wasn’t a potion. It wasn’t magic.

And yet, even now, its broken body was healing.

An unbelievable rate of recovery—obviously not human.

A power of Regeneration that anyone would have to question.

But the fanatics who had been launching terrorist attacks around the world since before the Great Cataclysm would have seen it differently.

Perhaps they’d glimpsed the shadow of a god in the Doppelganger, who used mana and had the same red blood and flesh as them.

“A miracle.”

Its voice rang out, brimming with excitement. The Doppelganger stared at me with blazing eyes and continued.

“To them, I am not a monster but a miracle itself—the Prophet who will lead them to the promised land.”

“……!”

“They’ll fight until the very last person falls. For their god. And for me.”

I didn’t argue with the Doppelganger’s confident claim.

It was simply the truth.

No matter what we did, a clash was inevitable.

The Doppelganger had planted its followers in this desert far earlier than I’d expected. And the wave of fanatics that began there had already shaken the world in the form of terrorism.

So even if I told them the truth about the Doppelganger, nothing would change.

*If a few words were enough to make them see reason, they wouldn’t be fanatics.*

This was ultimately the joint work of monsters and madmen. And right now, I was nothing but a heretic who had to be killed.

A heretic persecuting the great Prophet chosen by God.

“Then there’s only one thing left to do.”

I muttered evenly, staring at the Doppelganger. It understood what I meant, and the corners of its mouth curled upward.

“I’m looking forward to it.”

“Yeah?”

*Thud!*

As I spoke, I thrust my dagger forward, piercing its heart.

Its limbs were bound, so there was no way it could dodge. But the Doppelganger frowned and sighed.

“Give it a rest. That hurts like hell.”

*Crack.*

The severed muscles and shattered bones returned to their proper places. Fresh, rosy blood welled up, and smooth, childlike skin covered it.

It healed at a staggering speed, as if a video were playing in fast-forward.

Even the great shards of bone that had pierced its limbs and pinned it deep into the cliff shifted slightly, pushed by the flesh and bone growing around them.

The countless Level windows I’d seen with the **Truthful Eye**—and could still see now—weren’t just numbers.

*Other lives.*

They were fuel, and they were the lives of the victims the Doppelganger had devoured.

Like an arcade game character that came back to life as soon as you fed it a coin, the bastard could revive endlessly.

*But it’s not truly immortal.*

I twisted the dagger still in my hand. Heat surged from my dantian, raced through my acupoints, and flowed into the dagger.

*Thud—boom!*

Scorching Yang Qi poured through the dagger buried deep in its chest and exploded inside the Doppelganger.

Its heart had already been pierced once, yet it had recovered like an immortal. Now it was crushed completely. The clear bell I’d been waiting for rang beside my ear.

*Ding.*

> **System**
>
> Defeated Lv. 120 Yamamoto Genji!
>
> Gained a significant amount of **EXP**!

“……!”

One life faded, and a new one took its place.

The Doppelganger was still grinning. Behind its melting skin, another unfamiliar face was ready to emerge.

“Imagine that. Jin Taekyung killed Genji. Japan’s going to lose its mind when they hear about this.”

“Shut your mouth.”

The low bridge of its nose and the crooked teeth visible in its mouth.

Judging by those distinctive features, clearly East Asian, it had to be a Hunter from J1—one of the team thought to have been wiped out, apart from Yamamoto Genji.

“Come to think of it, I forgot to introduce myself. Nice to meet you. I’m Hiroshi Inoue. I spent my childhood in Nagasaki, then moved to Tokyo…….”

I grabbed it by the throat and twisted hard.

Unable to withstand my tremendous grip, the Doppelganger’s neck snapped at once, its head lolling at a grotesque angle.

*Ding.* Another bell rang, and the twisted head straightened. The face, smiling coyly, belonged to a woman I’d never seen before.

“Oh, did you know? This woman was the lover of the man you just killed. Looks like they were planning to get married this year.”

“……!”

My hand stopped dead, as if someone had hit a pause button. The Doppelganger whistled, clearly enjoying itself.

“Wow. So passionate. Humans really are amazing when it comes to things like this. We could learn a thing or two.”

“……You.”

“Ah, sorry. I apologize if that made you uncomfortable. But what can I do? It’s my ability.”

I clenched my teeth.

The Doppelganger hadn’t just absorbed its victims’ appearances. It could reproduce their abilities exactly as they’d had them in life—and it had their memories, too.

And the memories spilling from its mouth dug into my chest like an awl, making me hesitate.

*Crack.*

Blood seeped between my clenched teeth.

Beyond the canyon, the tremors had grown stronger, and I could feel a fierce killing intent. In front of me, a monster that came back no matter how many times I killed it was smiling faintly.

“Jin!”

Magic Johnson’s urgent shout struck my eardrums. The smile on the Doppelganger’s face deepened.

“This is your last chance.”

“What?”

“Right now is your last chance to run and survive.”

“……!”

*Whoosh.*

The cool desert wind brushed my face. It felt as if I’d been doused in cold water.

The Doppelganger shrugged at me, frozen like a statue.

“I understand. It’d hurt your pride. You’d be embarrassed. But if you die here like the rest of those humans, would that be a pointless death—or a noble sacrifice by a hero?”

“……That’s……”

“You have to look at the bigger picture. You’re the World Hunter Federation’s Alliance Leader. The one and only light and hope who can save this world, like someone from the past. Aren’t you?”

Its gentle voice tickled my ear, like a snake coaxing me to steal and eat the forbidden apple.

The Doppelganger’s low whisper wound softly around my whole body.

“Run. And survive.”

*Rumble.*

The canyon shook. The footsteps of countless fanatics—and the hooves of the camels they rode—were approaching from the darkness beyond.

“Think of your family and friends. Can you even imagine how much sorrow and pain they’ll suffer because of your death?”

“……Sorrow and pain?”

“That’s right. You’ve been through it yourself.”

My lips moved without a sound.

Sorrow and pain over someone’s death. Yeah, I’d been through it. An experience that had shaken me so badly my heart had nearly collapsed.

“No one will blame you. Even I respect everything you’ve done. So even now……”

The eyes of the nameless woman—or rather, the Doppelganger—sparkled.

“Run.”

*Allahu Akbar!*

The mighty roar of countless voices merging into one rang across the darkening desert.

Brilliant radiance shimmered around Magic Johnson, while hundreds of undead stared with dimly glowing eyes at the waves of fanatics surging toward them.

And I……

Let go of the Doppelganger’s neck.

*Step.*

When I took a step back, I saw its smiling face. In a gentle voice, as if speaking to a child, it said:

“Good. You made the right choice.”

I found myself muttering:

“Is this the best option?”

“It has to be.”

“Good. Then I’m glad.”

I nodded, then murmured under my breath.

“Open. Summon.”

“Hm?”

*Shhk!*

Along with its hollow question, the Doppelganger’s head shot into the air.

A new face rose onto its shoulders, as if a page had turned, and blinked.

The heat blazing around **White Flame**’s spearhead was turning its eyes red.

“What the fuck are you, some Ditto from a failed link trade? Quit trying to pull that crap on me.”

Only then did the Doppelganger understand what had happened. It sighed.

“You crazy bastard……”

“Got anything more original? I’ve heard that one so many times I’m sick of it.”

“Why are you doing this?”

“That’s what I want to ask you.”

“What?”

“You started spouting nonsense from the get-go, and I wondered what the hell was going on. But the more I listened, the more curious I got. You’re the first monster I’ve ever seen telling a human to run. For a second, I almost called you Mom, you son of a bitch.”

“……”

“What the hell are you? You’re trying so hard not to get caught, but you keep giving yourself away. So I know you’re stupid—but what do you actually want?”

A brief silence followed. The Doppelganger stared at me without a word, then furrowed its brow.

“Damn it. This has gone to shit. Why are you so reckless? You want to be remembered by history as a hero who made a noble sacrifice?”

“Quit talking out of your ass and answer me. My dream is to be the head of a village where everyone lives to a hundred.”

“Then why the hell……!”

*Scree!*

A cry rang out from the sky, swallowing the Doppelganger’s unfinished words.

It naturally looked up at the sky, and its eyes suddenly widened.

“……What’s that?”

I already knew what the Doppelganger was seeing.

Before the forces split off, I’d used Sound Transmission to give the Skeleton King direct orders.

“They’re a little late, but they made it just in time.”

*Screee!*

Dozens of eagles and griffins glided over the canyon with their wings spread wide.

On the backs of the enormous flying beasts, I could see the Hunters who should have gone east.
```
