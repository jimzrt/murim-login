<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1160.txt",
      "sha256": "60e2c92aa44ba87c94a44b0d4a7eda05d52e4646a6edceb1aafdaac29cfb3fb5",
      "bytes": 13115
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "903288ed83015c1bc60b4d02cdc441f940326cee67ab8bf7cc697b7d83af41cb",
      "bytes": 1858
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2fd0de0ff721805936794bca4b9ad70fd4d20f40fbc76e97c8e8c5be179dfa5d",
      "bytes": 247561
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "6cb5ca42c27275ce911801e2565733c24f1e27e3c35a9dfb6fdc08df0098f1bb",
      "bytes": 777
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8681d3b5224c43efb0d42f9d89ef2e6db0c99ffb8c0c3e7032d8238b18a057ec",
      "bytes": 760
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ea97ac74fa96d9a248346977d059f1509b3fa5cbcd83c200871de32f4e72339e",
      "bytes": 1709
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "80f6655e0bf97935c3b5d48a2b9d739501472fa8f5d1539bfbcd156a4f61be76",
      "bytes": 623
    },
    {
      "path": "characters/Morgoth.md",
      "sha256": "d3d1155c96fb7fb978ac8080aa974657c2f027b798a9b735d97b4798d3f53f7d",
      "bytes": 777
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f649e1c8b8c90bc946df11556e5576674e12644e5461312fe1d42e0257ee2185",
      "bytes": 293564
    }
  ],
  "estimated_tokens": 9548
}
-->

# Durable State Update — Chapter 1160

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
1 and safe_through 1160. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1160. Profile updates may replace only one
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
  "chapter": 1160,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1160,
    "continuity_sources": [1160],
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
    "Morgoth’s three-day deadline and demand for Cheon Taemin and Jin Taekyung as tribute remain in effect.",
    "Cheon Taemin remains unconscious in a recovery capsule in a hidden Pentagon chamber.",
    "Jin believes Cheon Taemin was the Martial God and The Helper, and suspects Asmodeus was not completely erased; these identities and suspicions are unconfirmed.",
    "The World Hunter Federation was ordered to mobilize for Moscow against Morgoth and his monsters; Jin intended to go alone.",
    "The Skeleton King has reached Morgoth’s palace disguised as Jin Taekyung and is fighting Morgoth after refusing to become his Guardian.",
    "The Skeleton King absorbed power and some abilities from the Arch Lich, Leviathan, and Behemoth; Morgoth inferred he had encountered a Doppelganger.",
    "The Skeleton King wields the Hero’s Sword, an Ego Sword; Morgoth cannot explain how an undead can use it.",
    "Morgoth’s magical attack is now directed at the Skeleton King; the outcome is unresolved.",
    "The Skeleton King can hear the dead spirits and regards them as his people; he suspects he may once have been human, but has no memories and sometimes experiences déjà vu.",
    "Morgoth was summoned by Asmodeus from beyond distant stars and space, but does not know why; he says he is not devoted to Asmodeus."
  ],
  "continuity_sources": [
    1158,
    1159
  ],
  "open_questions": [
    "Were Cheon Taemin, the Martial God, and The Helper the same person?",
    "Was Asmodeus completely erased?",
    "Who escaped through Area 52 in Jin’s likeness?",
    "What will happen when Morgoth’s three-day deadline expires?",
    "Can the Skeleton King survive Morgoth’s magical attack, and how can he wield the Hero’s Sword?"
  ],
  "safe_through": 1159,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 몬스터     | **monster**           |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 용족 | **dragonkin** | Monster classification including wyverns and drakes. |
| 오크 | **Orc** | Monster species. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 대적자 | **the Adversary** | Ancient human enemy remembered by the Arch Lich. |
| 블링크 | **Blink** | Arch Lich movement spell |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 소평 | **So Pyeong** | Alliance office worker assigned to prepare a report. |
| 모스크바 | **Moscow** | Russian city used in Taekyung's modern-world comparison. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |
| 무영 | **No Shadow** | The concealed Supreme Peak assassin serving the Emperor. |
| 언데드 | **undead** | Supernatural beings that are neither dead nor alive. |
| 적도 | **Red Blade** | Named blade that shatters in Taekyung’s flames. |
| 흑룡공 | **Black Dragon Duke** | Title in Morgoth's System announcement. |
| 드래곤 | **Dragon** | The species to which Morgoth belongs. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 1157
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Ares Guild Master and humanity's greatest Hunter, the Slayer who defeated the Demon King and created the first Mana Cultivation Method during the Great Cataclysm; after more than twenty years in seclusion, he remains unconscious in a secret area within Area A.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1159
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1159
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he protects those he cherishes and is learning to face the fear of leaving them in danger without letting it paralyze him.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the Skeleton King a friend; he trusts Sama Pyo despite suspecting his betrayal, was regarded as a worthy successor by Peng Cheolhu, and received the Martial God’s message through the Bow Saint.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1159
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Morgoth.md

# Morgoth (모르고스)

- **Safe through:** Chapter 1159
- **Aliases:** None
- **Role:** Morgoth is a Dragon and the sovereign of a vast palace who seeks to recruit the Skeleton King as his Guardian.
- **Personality:** He is composed, curious about unusual powers, and confident in his own strength; he says he does not underestimate humanity after Asmodeus was stopped by a human.
- **Voice:** He speaks in polished, courteous, formal phrasing, often asking measured questions while expressing condescension or fascination.
- **Relationships:** Asmodeus summoned Morgoth, though Morgoth says he is not devoted to him; Morgoth offers the Skeleton King the role of Guardian, which the Skeleton King refuses.

## Korean source

```text
＃1060화



언데드(Undead).

죽음을 맞이했으나 죽지 않았고, 움직일 수 있으나 살아있다고 말할 수 없는 존재들.

하지만 그런 언데드라 한들 불사(不死)는 아니다.

단지, 소멸이라는 또 다른 형태의 죽음을 맞이할 뿐.

‘소멸이라.’

느려진 시간 속, 사방을 뒤덮은 무수한 칠흑색 섬광을 보며 스켈레톤 킹은 마음속으로 읊조렸다.

아직 자신이 가지 못한 길.

그럼에도 끝내 가야 하는 그 길을 떠올리며, 조용히 두 눈을 감았다.

물론 그도 알고 있었다.

지금이라도 움직인다면 소멸만큼은 피할 수 있다는 것을.

마지막 영혼 한 조각까지 잿가루가 될 만큼 온 힘을 다해 몸부림친다면, 저 끔찍하리만치 강대한 고룡의 몸뚱어리에 자그마한 검상(劍傷) 하나쯤은 남겨 줄 수도 있다는 것을.

그러나 결국 부질없는 짓이었다.

그 이상을 바라기에는 힘의 크기가, 격의 차이가 너무나도 아득했다.

‘반전은 없어. 이 몸은, 아니 진태경은 오늘 이 자리에서 쓰러진다. 세상을 파멸로 몰고 갈 괴물에 의해서.’

그리고 이 소식은 금세 전해질 것이다.

모든 것이 빠른 세상이니까.

그렇기에 진태경의 모습으로 이곳까지 오며 최대한 사람들의 이목을 끌었다. 지금쯤이면 전 세계의 모든 인류가 모스크바를 향해 촉각을 곤두세우고 있을 터였다.

‘그렇게만 된다면, 나는 후회하지 않는다.’

하지만 그런 스켈레톤 킹과는 달리, 사람들은 후회하는 동시에 분노할 것이다.

보이지 않는 손에 떠밀려 기꺼이 최후를 맞이한 영웅의 모습에, 그제야 자신들이 저지른 실수를 깨닫고 결집하여 싸울 것이다.

설령 이 모든 일의 전말이 밝혀지더라도, 한번 굳혀진 마음은 쉽게 흔들리지 않으리라.

‘그래, 그걸로 된 거야.’

그런데 왜일까.

그토록 수없이 다짐하고 되새겼음에도, 자신의 마음은 납덩이처럼 무거운 것일까.

공간을 짓뭉개는 파공음에 귀가 먹먹하고, 두 눈은 눈꺼풀에 굳게 가려져 있음에도 보이고 들리는 저 얼굴들과 목소리는 무엇일까.

또한 어째서.

콰과과과광-!

육신은 물론 그 안에 담긴 영혼까지 흔적도 없이 집어삼킬 것만 같던 강대한 마력이, 저 무시무시한 칠흑빛 섬광들이 단 한 줄기도 자신에게 닿지 않는 것일까.

‘이건.’

불현듯 엄습해 온 기시감과 함께 스켈레톤 킹은 눈을 떴다.

그리고 보았다.

저 멀리, 왕좌에 비스듬히 등을 기댄 채 기이하리만치 번뜩이는 눈빛으로 자신을 응시하고 있는 흑룡의 모습을.

“역시, 처음부터 그럴 생각이었나.”

“……!”

“아무래도 앞서 했던 말을 정정해야 할 것 같군. 나는 너희를…… 아니 자네를 과소평가하고 있던 모양이야.”

흑요석을 박아 넣은 것 같은 두 눈동자에 스켈레톤 킹의 모습이 담긴다.

수천 년의 세월에 걸쳐 서서히 닳고 마모되어 버린, 고룡의 심장은 지금 이 순간 힘차게 요동치고 있었다.

“왜 피하지 않았지?”

이미 자신의 겉모습뿐만 아니라 모든 상황을 꿰뚫고 있는 물음에, 스켈레톤 킹이 이를 악물었다.

“그래야만 하니까.”

“……!”

까드득.

황금으로 이루어진 왕좌의 손잡이가 가루가 되어 부서진다.

그러나 그것은 결코 자신을 기만하려 했던 스켈레톤 킹에 대한 분노의 표출이 아니었다.

모르고스는 떨고 있었다.

솟구치는 흥분과 환희로.

‘그래야만 한다고?’

그래, 바로 이것이다.

만약 조금 전 스켈레톤 킹이 어떤 방식으로든 맞서 싸우려 했다면, 모르고스는 조금의 망설임도 없이 전력을 다해 그를 소멸시켰을 것이다.

찰나의 호기심에 흔들려, 천태민과 진태경이라는 대어를 놓칠 생각은 추호도 없었으니까.

‘한낱 인간의 몸으로 마왕을 쓰러트린 대적자. 그리고 그 뒤를 이어 세상을 이끌어 가는 자.’

오직 그 두 사람만이 모르고스가 이 세상에서 얻고자 한 가장 큰 목적이자 이유였다.

적어도 조금 전까지는.

하지만 방금, 스켈레톤 킹이 보여 준 모습은 그의 마음을 송두리째 뒤흔들기에 충분했다.

‘저주받은 언데드 몬스터가 이 정도의 영혼을 간직하고 있다니.’

살고자 하는 욕망은 누구에게나 있다. 인간에게도, 몬스터에게도.

그러나 희생은 다르다.

모르고스는 유희라는 이름으로 아득한 시간에 걸쳐 여러 종족과 함께해 왔지만, 그중 가장 고결하다는 숲의 요정들에게서조차 이 정도의 충격을 받진 못했다.

아니, 비교 자체가 무의미했다.

모르고스가 세상의 지배자로서 탄생했듯이, 그들 역시 순수한 마음을 타고난 종족이었으니까.

하지만 스켈레톤 킹은 명백한 언데드 몬스터였다.

씻을 수 없는 저주로 인해 타락한 존재.

그런 그가, 오직 분노와 공포로 이루어져 있었어야 할 언데드 몬스터가 스스로를 희생하려 했다.

소멸에 대한 두려움을 느꼈음에도, 잠시나마 최후를 미룰 힘이 있음에도 끝끝내 물러서지 않았다.

‘어떻게 이럴 수 있지?’

마치 새로운 종족을 발견한 듯한 놀라움.

오직 호기심을 쫓아 자신이 쌓아 올린 모든 것마저 내버린 채 악룡(惡龍)이 되기를 선택한 모르고스는, 일생을 통틀어 가장 강렬한 충동을 느끼고 있었다.

정확히는, 그의 드높은 지성으로도 도저히 억누를 수 없는 탐욕을.

‘갖고 싶다.’

아니, 반드시 가져야만 했다.

가장 타락한 육신에 깃든 고귀한 영혼.

태어나 처음 보는 저 기이한 존재를 완전히 자신의 것으로 만들어 소유한다면, 그 놀라운 본질은 물론 그가 지난 수천 년간 염원한 미지의 영역에 닿을 수 있을 것 같았다.

지금의 모르고스를 만들어 낸 가장 큰 의문이자 원동력에.

“안 되겠군. 참을 수 없어.”

혼잣말처럼 중얼거린 모르고스가 왕좌에서 일어난 그 순간.

팟.

그야말로 찰나였다.

족히 수십 미터 이상 떨어져 있던 모르고스의 신형이 흔적도 없이 사라진 것도.

전신의 신경을 곤두세우고 있던 스켈레톤 킹이, 불현듯 엄습 해오는 오싹한 한기를 느낀 것도.

‘블링크(Blink)!’

그제야 떠오른 생각이 뇌리를 스쳤지만, 이미 늦은 후였다.

그의 상대는 드래곤. 그 어떤 종족도 범접할 수 없는 마나의 축복 속에서 태어난 존재였으니.

그리고 숨 쉬듯 자연스럽게 발현된 무영창 주문과 함께, 블링크 마법의 한계를 초월하여 나타난 모르고스의 일격이 스켈레톤 킹의 등줄기를 후려쳤다.

콰드드드득!

막을 수도, 피할 수도 없었다.

끔찍한 파열음과 함께 포탄처럼 튕겨 나가는 신형.

스켈레톤 킹이 허공에서 균형을 바로잡기도 전에, 다시금 공간을 뛰어넘은 모르고스가 손을 뻗었다.

스아악, 서걱!

귓가를 파고든, 소름이 끼치도록 낮은 파공성.

그와 동시에 온 힘을 다해 거리를 벌린 스켈레톤 킹은, 지금 막 자신의 왼쪽 팔이 몸뚱어리에서 떨어져 나갔다는 것을 알아차렸다.

마지막 순간 본능적으로 몸을 비틀지 않았다면, 팔이 아닌 다른 부위를 잃었으리라는 사실도.

‘처음부터 두 다리를 노렸다. 날 소멸시키기 위한 공격이 아니었어.’

그리고 이어 들려온 모르고스의 목소리에, 스켈레톤 킹은 자신의 짐작이 옳았음을 깨달았다.

“괜한 저항은 그만두게. 어차피 시간 낭비일 뿐이니까.”

사실이었다.

구태여 어떤 이유를 더할 것도, 뺄 것도 없는.

두 존재에게는 그들 사이에 놓인 거리보다도 수십 배는 넓고 깊은 격차가 존재했으니까.

“생각이 바뀌었네. 자네를 가져야겠어.”

흥미라는 감정을 넘어 탐욕으로 일렁이는 눈빛.

스켈레톤 킹은 이와 같은 모르고스의 변화를 명확히 이해할 수 없었지만, 한 가지 사실만큼은 확신할 수 있었다.

아무것도 보이지 않던 캄캄한 어둠 속에서, 비로소 야트막한 빛줄기가 스며들기 시작했음을.

“이해한다. 이 몸이 워낙 잘생기긴 했지. 사실 지금처럼 못생긴 얼굴을 하고 있는 게 억울하게 느껴질 정도야.”

담담한 대꾸와 함께, 스켈레톤 킹은 하나밖에 남지 않은 손으로 [영웅의 검]을 비스듬히 들어 올렸다.

‘기회는 단 한 번.’

분명 처음이자 마지막이 될, 지금의 그에게 남은 유일한 길.

우우웅.

거대하지만 혼탁한 마력이 샘솟는다.

그 본질과는 전혀 어울리지 않는 은빛 검신을, 스켈레톤 킹의 전신을 휘감으며.

그러나 살아있는 안개처럼 일렁이며 공간을 잠식해 나가는 그 막강한 기운조차, 모르고스가 지닌 힘에 비견할 수는 없었다.

“스켈레톤 킹. 가장 어둡고 차가운 무덤에서 깨어나 왕관을 손에 넣은 자, 저주받은 언데드의 왕이여.”

흑룡공(黑龍公) 모르고스.

한때 세 개의 달과 태양, 열두 개의 대륙과 아홉 바다를 아우르던 드래곤 로드가 환하게 웃으며 두 팔을 벌린다.

마계의 대공이라는 위명에 걸맞은, 믿을 수 없을 만큼 순수하면서도 강대한 마력으로 모든 것을 짓누르며.

“나에게로, 너의 진정한 주인에게로 오라.”

바로 그 순간.

솨아아악!

두 존재 사이에 놓여 있던 공간이 사라졌다.

아니, 스켈레톤 킹의 눈에는 마치 뒤틀리는 동시에 지워지는 것처럼 보였다.

하지만 마력으로 이루어진 날개를 활짝 편 채, 소리조차 앞질러 쇄도하는 모르고스와 달리 그의 두 다리는 여전히 굳건히 제자리를 지키고 서 있었다.

다만, 하나밖에 남지 않은 손으로 펼치는 최후의 일격만이 있을 뿐.

슈확!

검극(劍極)은 허공을 관통하며 나아갔다.

한 치의 떨림도 없이.

당당하면서도 담담하게.

지금껏 감당해 본 적 없는 거대한 힘을 실은 채, 주인의 의지에 따라 오직 한 방향을 향해 쏘아졌다.

다름 아닌, 스켈레톤 킹의 목을 향해.

“……!”

소리 없는 비명이 있다면 이런 것일까.

찰나를 쪼개고 쪼갠 순간 속, 이 믿을 수 없는 광경을 목격한 모르고스는 두 눈을 부릅뜨며 손을 뻗었다.

그리고.

화악-!

그 어떤 어둠보다도 깊고도 거대한 섬광이, 온 사방을 집어삼키며 솟아올랐다.



* * *



만약 모스크바에 거주하던 누군가가 살아남아 이 광경을 보았다면, 분명 두 글자를 떠올렸을 것이다.

종말(終末).

세상의 단말마.

살아 있는 모든 것들의 최후.

하지만 이미 죽음의 땅이자 마계의 일부나 다름없게 된 그곳에서, 가장 먼저 위기를 느낀 것은 인간이 아닌 존재들이었다.

쿵.

대지 깊은 곳으로부터 솟아오르는 듯한 울림.

본능을 넘어 영혼을 자극하는 그 거대한 파동에, 일대를 뒤덮은 수많은 몬스터가 일제히 고개를 들었다.

순간의 허기에 사로잡혀 가까이에 있던 오크를 산 채로 씹어 삼키던 대형 몬스터들도.

이를 징벌하기 위해 다가가던 데스 나이트와 병력 보강을 위해 언데드 몬스터를 일으켜 세우던 리치들도.

군데군데 높게 솟은 첨탑과 검은 구름 밑을 맴돌던 용족들도.

단 한 마리의 예외도 없이 모두가 움직임을 멈췄고, 고개를 돌려 이 불길한 울림의 근원지를 바라보았다.

이제 자신들의 새로운 왕이나 다름없는 흑룡공 모르고스의 거처.

드래곤 레어(Dragon Lair)를.

화아아아악.

어느 순간, 불현듯 솟구쳐 오른 빛줄기. 

아니, 어둠.

하지만 어째서인지 조금의 친숙함도 느껴지지 않는 그것은, 레어의 중심부에서 터져 나와 하나의 거대한 기둥이 되어 하늘을 향해 솟아올랐다.

끝없이. 

모든 것을 지워 내며.

첨탑을, 용족을, 그 끝에서 빛을 가로막고 있던 구름을 가르고 마침내 하늘을 관통했다.

그리고.

쿠웅.

넋 나간 시선으로 그 기이한 광경을 지켜보고 있던 몬스터들은 동시에 깨달았다.

조금 전 자신들에게 주어진 그 잠깐의 시간이 얼마나 귀중한 것이었는지를.

구구구구궁-!

찢어진 먹구름의 사이로 쏟아져 내린 빛줄기가, 파도치듯 뒤집히는 대지를 비추고 있었다.
```

## Final English reading copy

```markdown
# Chapter 1160

Undead.

Beings who had met death but had not died; who could move, yet could not be called alive.

But even the undead were not immortal.

They simply met another kind of death: Erasure.

*Erasure, huh.*

As time slowed, the Skeleton King gazed at the countless black flashes covering every direction and murmured to himself.

A path he had not yet taken.

And yet, one he would have to walk in the end.

He quietly closed his eyes.

Of course, he knew.

If he moved now, he could still avoid Erasure.

If he struggled with every ounce of his strength, until the last fragment of his soul crumbled into ash, he might even leave a tiny sword wound on that terrifyingly powerful Ancient Dragon’s body.

But in the end, it would be pointless.

The gap in their power—the difference in their very being—was too vast for him to hope for anything more.

*There’s no turning this around. This body—or rather, Jin Taekyung—will fall here today. At the hands of a monster bent on destroying the world.*

And word would spread soon.

Everything moved fast in this world.

That was why he had drawn as much attention as possible on his way here in Jin Taekyung’s form. By now, everyone around the world would be watching Moscow closely.

*If that happens, I won’t regret it.*

But unlike the Skeleton King, the people would regret what they had done—and be furious.

At the sight of a hero, driven by an unseen hand to willingly meet his end, they would finally realize their mistake. Then they would unite and fight.

Even if the whole truth came to light, hearts once set would not be easily swayed.

*Yeah. That’s enough.*

But why?

Even after making that resolve and repeating it to himself countless times, why did his heart feel as heavy as lead?

The sound of space being crushed left his ears ringing. His eyes were firmly shut behind their lids, yet he could still see those faces and hear those voices. What were they?

And why—

*KA-BOOOOM!*

—hadn’t a single one of those terrible black flashes touched him, though the tremendous magical power seemed capable of devouring not only his body, but the soul within it, without a trace?

*This is…*

A sudden sense of déjà vu swept over him. The Skeleton King opened his eyes.

And saw him.

Far away, a Black Dragon sat leaning at an angle against his throne, staring at him with eyes that gleamed strangely.

“Just as I thought. Was that your plan from the start?”

“……!”

“I suppose I should take back what I said earlier. It seems I underestimated all of you… No, I underestimated you.”

The Skeleton King’s reflection gleamed in eyes like pieces of obsidian.

After slowly wearing away over thousands of years, the Ancient Dragon’s heart was now pounding fiercely.

“Why didn’t you dodge?”

The Skeleton King gritted his teeth at the question. Morgoth had already seen through not only his appearance, but the whole situation.

“Because I had to.”

“……!”

*Crack.*

The armrest of the golden throne crumbled to dust.

But it was not an outburst of anger at the Skeleton King for trying to deceive him.

Morgoth was trembling.

With rising excitement and joy.

*Because you had to?*

Yes. This was it.

If the Skeleton King had tried to fight back in any way, Morgoth would have erased him with all his power, without the slightest hesitation.

He had no intention of letting a moment’s curiosity cost him the two prized catches he sought: Cheon Taemin and Jin Taekyung.

*The Adversary who defeated the Demon King in a mere human body. And the one who would lead the world after him.*

Those two alone had been Morgoth’s greatest purpose and reason for coming to this world.

At least, until a moment ago.

But the sight the Skeleton King had just shown him was enough to shake him to the core.

*A cursed undead monster, and it has a soul like this.*

Everyone wanted to live. Humans and monsters alike.

But sacrifice was different.

Morgoth had spent vast stretches of time among many races in the name of amusement. Yet even among the Elves of the forest, supposedly the most noble of them all, he had never felt so astonished.

No. There was no point in comparing them.

Just as Morgoth had been born to rule the world, they had been born with pure hearts.

But the Skeleton King was unmistakably an undead monster.

A being corrupted by an inescapable curse.

And yet he had tried to sacrifice himself—the very undead monster who should have been made of nothing but rage and fear.

Though he felt afraid of Erasure, and had the power to delay his end, even for a little while, he still refused to retreat.

*How is this possible?*

It was like discovering an entirely new species.

Morgoth, who had chosen to become an evil dragon, abandoning everything he had built over the ages in pursuit of curiosity alone, felt the strongest urge of his life.

To be precise, he felt a greed his lofty intellect could not possibly suppress.

*I want him.*

No. He had to have him.

A noble soul dwelling in the most corrupted of bodies.

If he could make this strange being, whom he had never seen before, completely his own, then perhaps he could reach not only that extraordinary essence, but the realm of the unknown he had longed for over thousands of years.

The greatest question—and driving force—that had made Morgoth who he was.

“This won’t do. I can’t hold back.”

The moment Morgoth murmured to himself and rose from his throne—

*Flash.*

It happened in an instant.

Morgoth’s figure vanished without a trace, though he had been dozens of meters away.

The Skeleton King, every nerve on edge, felt a sudden chill rush over him.

*Blink!*

The thought flashed through his mind, but it was already too late.

His opponent was a Dragon, born blessed by mana in a way no other race could approach.

Morgoth cast a wordless spell as naturally as breathing, pushed Blink magic past its limits, and appeared to strike the Skeleton King in the back.

*CRRACK!*

He couldn’t block it or dodge it.

His body flew like a cannonball with a dreadful cracking sound.

Before the Skeleton King could regain his balance in midair, Morgoth leapt across space again and reached for him.

*Fwoosh—slice!*

A chillingly low whistle cut through the air by his ear.

At the same time, the Skeleton King put everything he had into widening the distance—and realized his left arm had just been severed from his body.

He also knew that if he hadn’t twisted instinctively at the last moment, he would have lost something other than his arm.

*He was aiming for both my legs from the start. He wasn’t trying to erase me.*

Morgoth’s voice followed. The Skeleton King knew his guess had been right.

“Stop resisting. It’s only a waste of time.”

It was true.

There was nothing to add or take away from that.

The gap between them was dozens of times greater than the distance separating them.

“I’ve changed my mind. I want you.”

Morgoth’s eyes flickered with greed now, not mere curiosity.

The Skeleton King couldn’t fully understand this change in him, but he was certain of one thing.

In the pitch-black darkness where he could see nothing, a faint glimmer of light had finally begun to seep in.

“I understand. I am pretty damn handsome, after all. In fact, it feels like a crime to be stuck with a face this ugly.”

With a calm retort, the Skeleton King raised the [Hero’s Sword] at an angle in his one remaining hand.

*One chance.*

The only path left to him now. It would surely be the first and last.

*Vwooom.*

His enormous but murky magical power welled up.

It wrapped around the Skeleton King’s body, swirling around the silver blade—so utterly at odds with its nature.

Yet even that mighty force, rippling like living mist as it swallowed up the space around them, could not compare to Morgoth’s power.

“Skeleton King. You awoke in the darkest, coldest grave and took the crown in your hand—the king of the cursed undead.”

The Black Dragon Duke Morgoth, once a Dragon Lord who had ruled over three moons and a sun, twelve continents and nine seas, smiled brightly and spread his arms.

His pure yet impossibly powerful magical power, worthy of his title as a Demon Realm archduke, pressed down on everything.

“Come to me—to your true master.”

At that very moment—

*Fwoooosh!*

The space between them disappeared.

No—the Skeleton King saw it twist and vanish at the same time.

But unlike Morgoth, who came hurtling toward him faster than sound, his wings of magical power spread wide, the Skeleton King’s two legs remained firmly planted where they were.

All that remained was the final strike he would unleash with his one remaining hand.

*Shwoosh!*

The tip of the sword shot through the air.

Without the slightest tremor.

With confidence, yet calm.

Carrying a force greater than anything it had ever borne, it flew in the single direction its wielder intended.

Not at Morgoth, but at the Skeleton King’s own neck.

“……!”

If a scream could make no sound, would it look like this?

In the instant, divided into countless fractions of a second, Morgoth witnessed the unbelievable sight. His eyes flew wide and he reached out.

And then—

*FWOOSH!*

A flash, deeper and more vast than any darkness, erupted and swallowed everything around them.

* * *

If someone living in Moscow had survived to see it, they would surely have thought of one word:

Apocalypse.

The world’s death cry.

The end of all living things.

But in that place, already a land of death and little different from part of the Demon Realm, the first to sense danger were not humans.

*Thud.*

A rumble seemed to rise from deep beneath the earth.

The vast wave struck something beyond instinct, stirring the soul. Across the area, countless monsters raised their heads in unison.

Even the large monsters who, seized by a moment’s hunger, had been chewing a nearby Orc alive.

Even the Death Knights approaching to punish them, and the Liches raising undead monsters to reinforce their ranks.

Even the dragonkin circling the tall spires and the black clouds overhead.

Every last one of them stopped moving and turned toward the source of the ominous rumble.

The dwelling of the Black Dragon Duke Morgoth, now as good as their new king.

The Dragon Lair.

*Whoooosh!*

Suddenly, a beam of light shot upward.

No—darkness.

For some reason, it felt not the least bit familiar. It burst from the heart of the lair and rose skyward in a single enormous pillar.

Without end.

Erasing everything in its path.

It split the spires, the dragonkin, and the clouds blocking the light above them, then finally pierced the sky.

And then—

*Thud.*

The monsters, watching the strange sight with vacant stares, realized at the same time how precious the brief moment they had just been given was.

*Rrrrrumble!*

A beam of light poured down through the rift in the torn black clouds, illuminating the earth as it heaved and rolled in waves.
```
