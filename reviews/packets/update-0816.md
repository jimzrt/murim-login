<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0816.txt",
      "sha256": "b64a4b6cc0773a057ca90dc6e728dbf4ab9ccf5328e4c7bb253a324cecdd3322",
      "bytes": 13184
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ca58ac3947bb77b3a3276dcb3857a4d85bfec661c294951d9dbf633024894ed1",
      "bytes": 1458
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c8fff61ffde9ce550b4d1184cab823120a209474f19e6e8c4529997f78f8d1ba",
      "bytes": 225894
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "59037746896521e00971e6bb79492b961144f8979b7d9687d3d5417f18862a0f",
      "bytes": 776
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5fe8084397b1132d037320e00405ab48360d7f646b56034fd1c8e4de3aa2ad15",
      "bytes": 723
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "dc8ea18ef1e1bf12b7537e95adff4a4b8023a743c50be5c3335ad7043b24eef8",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1e4fd2810f1bc40c6481c5a8d531a7addf849951a24c167a2b0d30ca61501257",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "7995ae2b48828d9af87ff5ca88bcaf6ce2b84426d01fda48bd300e6cad421f80",
      "bytes": 820
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "129974e6f11f14cc393ae3bd0f5641ba588160bd005872ba6c36f3b8580fa33e",
      "bytes": 249016
    }
  ],
  "estimated_tokens": 9712
}
-->

# Durable State Update — Chapter 816

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
1 and safe_through 816. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 816. Profile updates may replace only one
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
  "chapter": 816,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 816,
    "continuity_sources": [816],
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
    "The Prophet is a Level 170 Doppelganger titled “The Final Abyss” and concealed itself for decades, including under the name Muninn.",
    "The Prophet can revive by drawing on victims’ lives and can reproduce their appearances, abilities, and memories.",
    "The Doppelganger has completed its 145th resurrection and continues to regenerate after Jin’s attacks.",
    "The canyon battle between the Hunters and the fanatics is ongoing; roughly eight hundred Hunters are fighting, and the Skeleton King is engaged with a powerful Arab fanatic who targeted Choi Minwoo.",
    "Jin killed Brody Woods, triggering a Level Up that removed Fatigue and Muscle Pain and began restoring internal energy; the Broken Body debuff rejected the healing power.",
    "Magic Johnson says he helped Jin because they are friends; whether Johnson is human remains uncertain."
  ],
  "continuity_sources": [
    814,
    815
  ],
  "open_questions": [
    "Why does The Prophet want Jin to flee, and what does it ultimately want?",
    "Is Magic Johnson human?"
  ],
  "safe_through": 815,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep the Demon Realm language distinct from other languages."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 일격     | **One Strike**                         |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 랭커      | **ranker**            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 프랑스 | **France** | Country containing Paris and Luxembourg Gardens. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 808
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Ares Guild Master and humanity's greatest Hunter, the Slayer who defeated the Demon King and created the first Mana Cultivation Method during the Great Cataclysm; after more than twenty years in seclusion, he remains unconscious in a secret area within Area A.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 815
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 815
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 815
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 813
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

## Korean source

```text
＃816화



도대체 뭐지?

도플갱어는 당황할 수밖에 없었다. 부활하기 무섭게 죽는 거야 그렇다 치자. 딱히 별다른 저항조차 못 한 것도 충분히 예상했다.

사지가 결박되어 있던 데다가, 상대인 진태경은 지금껏 봐 왔던 어떤 인간들보다 강했으니까.

하지만 한 가지만큼은 도저히 이해할 수 없었다.

‘뭐야, 이거.’

안 지친다. 지치질 않는다.

정확히 말하자면, 지쳤다고 생각할 때쯤 다시 멀쩡해진다. 죽음이라면 지긋지긋하게 경험해 왔던 도플갱어조차 슬슬 쌍욕이 튀어나왔다.

“아니, 뭐 이런 씨발놈이…….”

서걱!

욕설이 끝나기도 전에 번뜩이는 섬광. 정확한 힘의 배분과 속력을 지닌 창날이 목젖을 가른다.

그렇게 하나의 생명이 사그라지고, 과거 흡수한 또 다른 생명과 기억이 빈자리를 채웠다.

‘뭐 이런 개 같은 경우가.’

짧은 고통의 순간을 지나 부활한 도플갱어의 눈가가 파르르 떨렸다. 쉴 새도 없이 날아드는 창날이 시야에 들어왔다.

쐐액!

쾌속한 일격.

하지만 이번만큼은 도플갱어도 쉽게 당해 줄 생각이 없었다.

조금 전의 그는 어중간한 B급 헌터에 불과했지만, 새롭게 부활한 지금은 명실상부한 A급 헌터였으니까.

그것도 프랑스에서 스무 손가락 안에 들던 랭커(Ranker).

‘신속의 쟝.’

흡수한 기억 속에서 찾아낸 이명(異名)을 떠올리며, 도플갱어는 유난히 가볍게 느껴지는 발끝으로 지면을 밟았다.

쉭.

가슴을 아슬아슬하게 스치듯 지나가는 바람.

아지랑이처럼 흔들리던 도플갱어의 신형이 수 미터 뒤에서 나타났다.

어렵지 않게 일격을 피해 낸 그의 입가에는 여유로운 미소가 맺혀 있었다.

“지금부터는 호락호락하지 않을…….”

슈확! 푹!

한 줄기의 지풍(指風)이 미간을 관통했다. 호락호락하게 죽음을 맞이한 도플갱어가 부활과 동시에 눈을 깜빡였다.

‘어, 이게 아닌데.’

뭐였는지 제대로 보지도 못했다. 그나마 다행인 점이라면, 이번에는 진태경도 무슨 이유에선지 잠깐 공격을 멈췄다는 점이었다.

“어? 방금 뭐였냐?”

놀란 듯이 묻는 그의 모습에, 도플갱어는 내심 확신했다.

‘그럼 그렇지. 조금 전의 일격은 단순한 운이었나 보군.’

도플갱어의 입장에서는 당연한 의식의 흐름이었다.

무려 한 나라의 상위 랭커였던데다, ‘신속의 쟝’이라 불렸을 만큼 쾌속한 움직임을 지닌 암살 계열의 헌터.

처음부터 피하기로 마음먹었다면 바로 그 미카엘 실베르트조차 제법 신경이 거슬렸을 것이다.

‘진태경이 아무리 특별한 존재라 해도, 미카엘 실베르트와 그만한 격차가 있을 리는 없다.’

하지만 도플갱어는 까맣게 몰랐다. 진태경의 질문이 품고 있었던 진짜 의미를.

‘쟝 피에르? 이 사람은 누군데 경험치를 이렇게 많이 주지?’

처음 듣는 이름이다. 헌터 업계가 아무리 좁다고 해도 세계적인 명성이 있지 않은 이상 외국 헌터 이름까지 줄줄 꿰고 있는 건 무리니까.

‘어쨌든 감사합니다. 편히 쉬세요.’

흡수당한 헌터에게 감사와 애도를 표한 진태경은, 잠시 늘어트렸던 창날을 바로 세웠다.

이 정도면 죽은 이에 대한 예의는 충분히 차렸다. 그가 계속해서 해야 할 일은 이미 정해져 있었다.

더 많은 이들이 희생당하기 전에 경험치를 복사…… 아니, 도플갱어를 완전히 소멸시키는 것.

“시간 아깝다. 한 번이라도 더 죽자.”

푹! 우드득!

“크헉……!”

단말마와 함께 또다시 꺼져 가는 생명의 불씨.

10분도 안 되는 짧은 시간 동안 벌써 200번이 넘는 죽음을 맞이한 도플갱어의 눈동자가 불안하게 흔들리기 시작했다.

‘이대로는 안 된다. 너무 쉽게 생각했어.’

지금껏 수많은 생명을 탐욕스럽게 집어삼켜 온 도플갱어다.

그는 지난 삼십여 년간 세상 곳곳에서 인간들의 영혼과 기억, 힘을 흡수했고 그로 인해 불사(不死)에 가까운 존재로 거듭날 수 있었다.

이는 마계에 존재하는 무수한 종류의 몬스터 중에서도 유일한 능력.

그러나 도플갱어는 자신이 지닌 능력의 명확한 한계점을 알고 있었다.

‘완전한 불사도 아니며, 흡수한 힘을 하나로 합칠 수도 없다.’

장작이 떨어지면 불도 사그라진다. 각기 다른 수천 조각의 파편을 이어 붙여도 하나가 될 수 없다.

물론 그것만으로도 대단한 능력이었지만, 절대자의 운명을 타고난 극소수의 존재들에게는 아니었다.

그래, 자신을 이 땅에 내려보낸 누군가처럼.



‘모든 계획이 완성되기 전까지는, 결코 표적과 마주해서는 안 될 것이다.’



퍼걱!

시야가 까맣게 물들었다. 몇 번째인지 모를 죽음이 도플갱어의 머릿속에 울려 퍼지던 목소리를 끊어 냈다.

“쿨럭.”

고통과 함께 새롭게 태어난 도플갱어의 얼굴 위로 후회가 스쳐 지나갔다.

‘처음부터 가까이 접근하지 말았어야 했어.’

패인(敗因)은 명백했다.

삼십여 년의 세월 동안 도플갱어는 그 어느 때보다 자유로웠고, 천태민마저 사라진 후에는 보이지 않는 곳에서 세상을 주물렀다.

그리고 바로 그 자유와 권력이 도플갱어를 취하게 만들었다.

마계에서의 그는 누군가에게 종속되어 있었으나, 이 세상에서는 뜻한 대로 모든 것을 이룰 수 있는 왕과 다름없었다.

도플갱어가 오만해질수록 명령의 무게는 가벼워졌고, 그가 품은 방심은 무거워졌다.

미카엘 실베르트?

결국 그조차도 도플갱어에게 있어서는 하수인이자 도구였을 뿐이다. 말을 잘 듣는 것은 제법 기특했지만, 언젠가 때가 된다면 쓰임새를 다하고 버려질 패였다.

계획을 준비하기까지는 상당한 시간이 걸렸으나 완성까지는 한 걸음이었다.

그런데…….

‘빌어먹을.’

서걱.

뜨거운 무언가가 가슴을 베어 가른다. 도무지 익숙해지지 않는 고통이 전신을 지배했다.

후우.

도플갱어는 죽음과 동시에 찾아온 생명을 느끼며 끊겼던 숨을 토해 냈다.

그리고 눈을 뜨자마자 시야를 가득 채운 누군가의 주먹을 보았다.

퍽.

눈앞이 아찔하다. 다시 정신을 차린 후에야 머리가 터져 죽었다는 것을 깨달았다.

자신도 모르게 뒷걸음질 친 도플갱어의 발이 조금 전 흘렸던 뇌수를 밟고 미끄러졌다.

“너 같은 새끼한테는 공력도 아깝다.”

진태경의 목소리가 귓가에 닿는다. 너무나도 담담해서 서늘하게 느껴지고, 그 서늘함에 숨이 막힌다.

다음 순간 어마어마한 무게로 가슴을 향해 내리 찍힌 발끝은 그 숨마저 앗아 갔다.

콰직! 우드득! 퍼걱!

시야가 어두워지고 밝아지기를 쉴 새 없이 반복했다.

일 초를 쪼개고 쪼갠 시간 찰나의 순간 속에서, 도플갱어는 몇 번의 죽음과 부활을 겪었다.

속박에서 풀려났음에도 변하는 것은 없었다. 오히려 더욱 다양한 종류의 죽음과 고통이 도플갱어를 기다리고 있었다.

‘왜, 도대체 어째서!’

도플갱어는 분노와 후회의 외침을 마음속으로 토해 냈다.

계획이 완성되기 전까지는 표적과 마주치지 말라는, 주인의 그 명령을 이제야 뼈저리게 이해할 수 있을 것 같았다.

‘이놈은…… 다르다.’

그간 틈틈이 흡수해 왔던 인간들, 혹은 주목을 끌지 않기 위해 멀리서 지켜보며 입맛만 다셨던 그 어떤 인간들과도 달랐다.

아니, 처음부터 인간이 아닌 것 같았다.

마치 천태민처럼.

후웅, 펑!

묵직한 파공성과 함께 활짝 펼쳐진 손바닥이 가슴을 후려친다. 엄청난 힘이 뼈를 부수고 그 안에 담긴 열기가 내장을 태웠다.

쿨럭.

죽은 피를 뿜어낸 도플갱어가 꺼져 가는 눈동자로 진태경을 바라보았다.

서서히 어두워지는 시야를 가득 채우고 있는 그의 얼굴은 흐릿했지만, 전신에서 흘러나오는 강대한 기세는 세상에 존재하는 어느 것보다 선명했다.

“서, 선택받은 자…….”

신음처럼 흘러나온 한 마디와 함께 힘없이 꺾이는 고개.

다시 한번 죽음을 내리기 위해 철퇴처럼 쏘아지던 진태경의 일권(一拳)이, 풀잎처럼 도플갱어의 이마에 닿았다.

툭. 화아악!

내지르던 속도를 이기지 못한 바람이 휘몰아친다. 진태경의 서늘한 시선이 도플갱어의 새로운 얼굴에 닿았다.

“지금, 뭐라고?”

“……!”

도플갱어는 숨을 삼켰다. 자신도 모르게 튀어나온 실언이다.

짧은 순간 끝없이 반복되는 죽음과 부활 사이에서 흐릿해진 의식이 만들어 낸 빈틈이었다.

“난 아무 말도 안 했…….”

“그래?”

덥석, 콰드득!

말을 끝내기도 전에 도플갱어의 눈앞이 까맣게 물들었다.

이제 몇 번째 죽음인지 헤아릴 수도 없을 정도다. 몸 안을 가득 채우고 있던 무수한 생명들은 이제 절반도 남지 않았다.

두개골과 함께 산산조각 난 암반에서 눈을 뜬 도플갱어는, 이제 후회를 넘어 두려움을 느꼈다.

다른 무엇도 아닌, 죽음에 대한 두려움을.

‘이대로면…… 소멸한다.’

도플갱어의 생명은 무한하지 않다. 그는 살아남기 위해 다른 누군가의 생명력을 흡수하고 이를 장작 삼아 불태워 왔다. 과거 다른 동족들이 그러했듯이.

‘그리고 그들 역시 영원한 소멸을 맞이했지.’

한때 도플갱어 종족이 마계를 주름잡았던 때도 있었다.

그러나 긴 세월과 참혹한 숙청이 있었고, 수백의 동족 중 살아남은 것은 그가 유일하다.

도플갱어가 한 존재를 가리키는 이름이자, ‘최후의 심연’이라 불리게 된 이유도 그 때문이었다.

‘나는, 나는 소멸할 수 없어. 반드시 살아남아야 한다!’

도플갱어는 이를 악물며 눈을 떴다. 새로운 생명력과 마나. 그리고 그에게 흡수당한 인간의 능력이 전신에 깃든다.

우우웅. 마나를 머금은 주먹이 희미한 오러를 머금었다. 튕기듯 몸을 일으킨 도플갱어가 진태경의 얼굴을 향해 주먹을 내질렀다.

쐐액!

맹렬한 파공성이 뒤늦게 울려 퍼진 순간. 단단하고 두꺼운 손바닥이 주먹을 가로막았다.

아니, 옥죄었다.

콰드득.

“……!”

정신이 아득해질 정도의 통증.

도플갱어는 자신의 주먹이 두부처럼 으스러졌다는 것을 깨달았다. 이번에도 죽음을 피할 수 없으리라는 사실도 함께.

“야, 뭐 하냐?”

후웅, 쾅!

세상이 뒤집힌다. 고막이 터질 것 같은 굉음과 함께 끊겼던 의식이 돌아왔다.

작은 크레이터의 중심에서 부활한 도플갱어는 즉시 땅을 박찼다.

진태경의 반대편으로.

‘살아남는다. 어떻게든!’

수치심 따위는 사라진 지 오래였다. 상대는, 진태경은 그의 주인이 언급한 바 있던 ‘선택받은 자’였으니까.

도플갱어는 새롭게 부여된 모든 힘을 폭발하듯 끌어올려 신형을 내쏘았다.

팟!

흐릿해진 신형이 공간을 가로질렀다.

아니, 가로지르려 했다.

도플갱어가 두 번째 걸음을 내디딘 그 순간, 한 줄기 섬광이 날아들기 전까지는.

서걱!

목이 떨어져 나간 몸뚱어리가 지면에 처박혔다. 수 미터 밖에서 부활한 도플갱어의 머리 위로 벼락같은 일격이 내리그어졌다.

푸화악!

좌우로 갈라진 몸뚱어리에서 피 분수가 터져 나왔다.

그러나 진태경은 멈추지 않았다. 열기를 머금은 창날이 끝없이 공간을 갈랐다.

쉬쉬쉭!

기울어지는 몸뚱어리를 가로지르는 섬광. 수십 개로 조각난 사지가 땅바닥에 떨어짐과 동시에 무서운 속도로 자라났다.

“으아아아!”

참혹한 죽음 속에서 부활한 도플갱어가 포효했다.

아직까지도 남아 있는 고통의 잔재가 벌레처럼 감각을 갉아 먹었다.

진태경이 조금 전의 일격으로 상당한 공력을 소모했다면, 그는 십여 개의 생명을 바쳐야 했다.

그러나 이제는 도플갱어도 깨달았다. 진태경의 손에서 벗어나기 위해서는, 아껴 두었던 목숨마저 꺼내야 한다는 것을.

스아아아.

그의 두 손을 타고 거대한 마나가 흘러넘쳤다. 어디선가 봤던 얼굴에, 진태경이 신음처럼 중얼거렸다.

“지크프리트 바스만?”
```

## Final English reading copy

```markdown
# Chapter 816

What the hell was going on?

The Doppelganger had no choice but to be bewildered. Dying the moment it came back to life was one thing. It had fully expected to be unable to put up much of a fight, either.

Its limbs had been bound, and Jin Taekyung was stronger than any human it had ever seen.

But there was one thing it simply couldn’t understand.

*What is this?*

He wasn’t getting tired. He wasn’t getting tired at all.

More precisely, just when he thought he was tired, he was back to normal again. Even the Doppelganger, which had experienced death more times than it could count, was starting to let loose a string of curses.

“What the fuck is this bastard……?”

*Slice!*

Before the curse was even out, a flash of light. A spearhead, its power and speed precisely controlled, cut across its throat.

One life faded away, and another life and memory it had absorbed in the past filled the empty space.

*What the hell is this bullshit?*

After passing through a brief moment of pain, the Doppelganger came back to life. Its eyelids trembled. A spearhead flying at it without pause entered its field of vision.

*Whoosh!*

A lightning-fast strike.

But this time, the Doppelganger had no intention of going down so easily.

The person it had been a moment ago was nothing more than a middling B-rank Hunter. But now, after its latest resurrection, it was indisputably an A-rank Hunter.

And not just any A-rank Hunter—a ranker who’d been among the top twenty in France.

*Jean the Swift.*

Recalling the nickname from the memories it had absorbed, the Doppelganger stepped onto the ground with feet that felt unusually light.

*Swish.*

A breeze skimmed past its chest by a hair’s breadth.

Its form, wavering like a heat haze, reappeared several meters behind.

It had dodged the strike without difficulty, and a relaxed smile spread across its lips.

“From here on, things won’t be so ea—”

*Shwhack! Thunk!*

A streak of Finger Qi pierced its forehead. The Doppelganger, which had died without putting up a fight, blinked as soon as it came back to life.

*Huh? That’s not right.*

It hadn’t even seen what happened. The one small consolation was that, for some reason, Jin Taekyung had briefly stopped attacking this time.

“Huh? What was that just now?”

At the sight of him asking in apparent surprise, the Doppelganger felt sure of itself.

*That’s right. That last strike must’ve been pure luck.*

From the Doppelganger’s perspective, that was the natural conclusion.

The man it had just absorbed had been a top-ranked Hunter in his country, with lightning-fast movements that had earned him the name Jean the Swift. An assassin-type Hunter.

If he’d decided from the start to dodge, even Michael Silbert himself would have found him a real nuisance.

*No matter how special Jin Taekyung is, he can’t possibly be that far above Michael Silbert.*

But the Doppelganger had no idea what Jin Taekyung’s question had really meant.

*Jean Pierre? Who’s this guy, and why does he give so much EXP?*

It was a name he’d never heard before. The Hunter world might be small, but unless a Hunter was famous worldwide, there was no way he could know every foreign Hunter’s name by heart.

*Anyway, thank you. Rest in peace.*

After offering his gratitude and condolences to the Hunter who’d been absorbed, Jin Taekyung raised his lowered spearhead.

That was enough respect for the dead. What he needed to do next was already decided.

Before even more people were sacrificed, he had to copy the EXP—no, completely destroy the Doppelganger.

“Don’t want to waste time. Let’s die at least one more time.”

*Thrust! Crack!*

“Gah……!”

With a final cry, another flame of life flickered out.

In less than ten minutes, the Doppelganger had already died over two hundred times. Its eyes began to waver with unease.

*This can’t go on. I underestimated him.*

The Doppelganger had greedily devoured countless lives.

For the past thirty-odd years, it had absorbed human souls, memories, and powers all over the world, becoming something close to immortal.

It was a unique ability, unlike any among the countless kinds of monsters in the Demon Realm.

But the Doppelganger knew the precise limits of its power.

*I’m not completely immortal, and I can’t combine the powers I’ve absorbed into one.*

When the firewood runs out, the fire dies down. Even if you join thousands of different fragments together, they can never become one.

That alone was an incredible ability—but not for the tiny handful of beings born to rule over all others.

Yes, like the one who had sent it down to this land.

*Until every part of the plan is complete, I must never come face-to-face with the target.*

*Whump!*

Its vision went black. Another death—how many now, it couldn’t tell—cut off the voice echoing in the Doppelganger’s mind.

“Cough.”

Regenerated into life along with the pain, the Doppelganger’s face flickered with regret.

*I shouldn’t have gotten close to him in the first place.*

The cause of its failure was obvious.

For more than thirty years, the Doppelganger had been freer than ever. And after Cheon Taemin disappeared, it had manipulated the world from the shadows.

That freedom and power had gone to its head.

In the Demon Realm, it had been subject to someone else. In this world, it was no different from a king, able to do whatever it pleased.

The more arrogant the Doppelganger became, the less weight it gave to its orders—and the heavier its own complacency grew.

Michael Silbert?

In the end, even he had been no more than a minion and a tool to the Doppelganger. It was rather admirable how obedient he was, but when the time came, he’d be a piece that had served its purpose and could be discarded.

Preparing the plan had taken a considerable amount of time, but it had been only one step away from completion.

And yet……

*Damn it.*

*Slice.*

Something hot cut across its chest. Pain it still couldn’t get used to took over its entire body.

*Hoo.*

The Doppelganger felt the new life arrive with its death and exhaled the breath that had been cut off.

The moment it opened its eyes, someone’s fist filled its vision.

*Thwack.*

Its vision swam. Only after it came to again did it realize its head had been smashed apart.

The Doppelganger stumbled backward without meaning to, then slipped as its foot landed in the brain matter it had spilled moments earlier.

“Internal energy’s wasted on a bastard like you.”

Jin Taekyung’s voice reached its ears. He sounded so calm that it was chilling—and that chill left the Doppelganger breathless.

The next moment, a foot came down on its chest with tremendous weight, taking even that breath away.

*Crack! Crunch! Splatter!*

Its vision went dark, then bright, over and over without pause.

Within a single instant, chopped into smaller and smaller fractions of a second, the Doppelganger died and came back to life several times.

Even after it broke free of its restraints, nothing changed. If anything, an even greater variety of deaths and agonies awaited it.

*Why? Why the hell?!*

The Doppelganger gave vent to its anger and regret in a silent scream.

Only now could it truly understand its master’s command never to meet the target before the plan was complete.

*This man…… is different.*

He was unlike any of the humans it had absorbed over the years, or any it had watched from afar, licking its lips while trying not to draw attention.

No—he didn’t seem human at all.

Just like Cheon Taemin.

*Whoom! Boom!*

With a heavy rush of air, an outstretched palm struck its chest. Tremendous force shattered its bones, and the heat within burned its organs.

*Cough.*

The Doppelganger spat dead blood and looked at Jin Taekyung with dimming eyes.

Jin’s face, filling its slowly darkening vision, was blurry. But the powerful aura radiating from his entire body was clearer than anything else in the world.

“The C-Chosen One……”

The words slipped out like a groan. Its head drooped limply.

Jin Taekyung’s fist, shooting forward like a meteor to deliver another death, touched the Doppelganger’s forehead as gently as a blade of grass.

*Tap. Fwoosh!*

The wind swept around them, unable to keep up with the speed of his punch. Jin Taekyung’s cold gaze settled on the Doppelganger’s new face.

“What did you just say?”

“……!”

The Doppelganger swallowed. It had let something slip without meaning to.

A gap created by its fading consciousness, blurred between the endless deaths and resurrections in that brief moment.

“I didn’t say anything……”

“Really?”

*Grab. Crack!*

Before it could finish speaking, the Doppelganger’s vision went black.

It couldn’t even keep track of how many deaths it had suffered now. The countless lives that had filled its body had dwindled to less than half.

The Doppelganger opened its eyes amid bedrock shattered along with its skull. It felt something beyond regret now: fear.

Fear of death itself.

*At this rate…… I’ll be erased.*

The Doppelganger’s life wasn’t infinite. To survive, it had absorbed the life force of others and burned it as firewood, just as its kin had once done.

*And they, too, met Erasure.*

There had once been a time when the Doppelganger species held sway over the Demon Realm.

But long years and a brutal purge had followed. Of the hundreds of its kin, it was the only one left alive.

That was why “Doppelganger” had become a name for a single being—and why it was called “The Final Abyss.”

*I can’t—I can’t be erased. I have to survive!*

The Doppelganger gritted its teeth and opened its eyes. New life force and mana, along with the powers of humans it had absorbed, filled its body.

*Vrrrrm.*

Mana filled its fist, coating it in a faint aura. The Doppelganger sprang to its feet and punched toward Jin Taekyung’s face.

*Whoosh!*

The thunderous rush of air came a moment later. A hard, thick palm blocked its fist.

No—it squeezed it.

*Crack.*

“……!”

The pain nearly made its mind go blank.

The Doppelganger realized its fist had been crushed like tofu. It realized, too, that it wouldn’t be able to avoid death this time either.

“Hey, what are you doing?”

*Whoom! Boom!*

The world turned upside down. Its consciousness returned with a deafening crash that seemed to burst its eardrums.

The Doppelganger came back to life in the center of a small crater and immediately kicked off the ground.

Away from Jin Taekyung.

*I’ll survive. Somehow!*

It had long since forgotten all shame. Its opponent—Jin Taekyung—was the “Chosen One” its master had once mentioned.

The Doppelganger drew out every bit of its newly granted power in an explosive surge and launched itself forward.

*Pop!*

Its blurred form cut through space.

Or tried to.

Until a streak of light came flying at it, just as the Doppelganger took its second step.

*Slice!*

Its headless body slammed into the ground. Several meters away, the Doppelganger came back to life, only for a lightning-fast strike to cleave down over its head.

*Fwoosh!*

A fountain of blood burst from its body, split in two.

But Jin Taekyung didn’t stop. The spearhead, wreathed in heat, kept cutting through the air.

*Shh-shh-shhk!*

A flash of light cut across its tilting body. Its limbs, chopped into dozens of pieces, hit the ground—and immediately began to grow back at a terrifying speed.

“Gyaaaah!”

The Doppelganger roared as it came back to life in the midst of a gruesome death.

The lingering traces of pain were still there, gnawing at its senses like bugs.

If Jin Taekyung had just used up a considerable amount of internal energy with that last strike, the Doppelganger had to sacrifice a dozen or more lives.

But now it understood. To escape Jin Taekyung’s grasp, it would have to use up even the lives it had been saving.

*Fwooooo.*

Vast mana poured over both its hands. Looking at a face he seemed to recognize, Jin Taekyung muttered like a groan:

“Siegfried Bassman?”
```
