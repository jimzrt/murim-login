<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0703.txt",
      "sha256": "1490e676a6cf6a20d14df69b4242932d053d631c6404b37ec483020f0fe63124",
      "bytes": 13124
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6dd3042710e456fab7d80300f9f6ca2df409ceb58b35e16eec36c10963e64ef2",
      "bytes": 2193
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "377408edd6bffa87540301dadb4da6acf3c4b03a8a29b32bdd22758532ccb70f",
      "bytes": 206401
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "47b96f17ee0978d5b562719841adbfa0c4fa85b0e8afadd6eac3474a13c069cd",
      "bytes": 830
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d2d310dc556c37420cbd5dc9a1d05d676d6cdc0b7bfda70296f4133335b8db1d",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ea226f657807f982b631354cdcb073e4c13fcd4b2f4d3e348e5a7fc1f49b1ba4",
      "bytes": 1914
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a673d0abe5c9214aeb0599429375f671e4e630c4c2047310071c27def0df589f",
      "bytes": 622
    },
    {
      "path": "characters/Masked Man.md",
      "sha256": "135378c16a40ba8233b2cdd07fd2cd3b106ca2ad5fa83ab8200ed3e0d1e26283",
      "bytes": 643
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "1bd908589d26ef8c8d8908e0ca773e28b3058c5adc1b3f34c7ea1be9d4f12d56",
      "bytes": 907
    },
    {
      "path": "characters/White Tiger.md",
      "sha256": "0a61d01c4b97981202cee8d861bf63fbfbd25f4dda567ebb258c41cb362205bb",
      "bytes": 637
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "39588518517f0306c0f8c6983a12c725399d58da9336fd2022f2fd66d620875e",
      "bytes": 216408
    }
  ],
  "estimated_tokens": 11447
}
-->

# Durable State Update — Chapter 703

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 703. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 703. Profile updates may replace only one
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
  "chapter": 703,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 703,
    "continuity_sources": [703],
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
    "The rift's demonic qi is causing the humans and beasts remaining in the Inner Palace to mutate, and the Southern Heaven Demon Empress grows stronger as the demonic qi thickens.",
    "The Southern Heaven Demon Empress is Honglan, the creator of the rift behind the Inner Palace, and she is fighting Jin Taekyung while pursuing the Lord of Heaven's plan.",
    "The Southern Heaven Demon Empress's masked hunting dog regenerates from shattered bones and severe wounds through a power that defies heaven and appears unable to feel pain.",
    "Jin Taekyung is injured but continues fighting the Southern Heaven Demon Empress and the masked man alongside the exhausted guardian spirit.",
    "Jin and the guardian spirit must end the battle before the Inner Palace's humans and beasts complete their mutation.",
    "The Lord of Heaven is interested in Jin, and the Southern Heaven Demon Empress initially sought to capture him for that reason rather than kill him.",
    "Jin has severed one of the Southern Heaven Demon Empress's wrists and wounded her side through a calculated sequence of life-threatening feints.",
    "One Annihilation has begun against the Southern Heaven Demon Empress, but an urgent cry of \"Human!\" coincides with the eruption of a massive unknown vortex."
  ],
  "continuity_sources": [
    702
  ],
  "open_questions": [
    "What is the masked man's identity, and what is his relationship with the Great Snow Fiend?",
    "Why is the Lord of Heaven interested in Jin Taekyung?",
    "Can Jin and the guardian spirit stop the mutation in the Inner Palace before it finishes?",
    "What is the source and meaning of the urgent thought that cried \"Human!\", and what caused the massive vortex?",
    "Will One Annihilation defeat the Southern Heaven Demon Empress, and can Jin survive the exchange?"
  ],
  "safe_through": 702,
  "temporary_decisions": [
    "Use demonic qi for 마기.",
    "Use Force for 강기 and Scorching Yang Qi for 열양지기.",
    "Use Empty-Hand Seizes the Blade for 공수납백인.",
    "Use backflow for 역류 and qi-blood for 기혈.",
    "Use One Annihilation for 일섬."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 남만야수궁  | **Nanman Beast Palace**          |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 복면인 | **Masked Man** | The Southern Heaven Demon Empress's trained hunting dog; identity remains unknown. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 탈진 | **Exhaustion** | System status effect caused by exhausting all internal energy while severely injured. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 변이체 | **mutant** | Taekyung's classification for the monster. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 성지 | **Sacred Land** | Former name of the Poisonblood Grounds when beasts ruled Ailao Mountain. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |
| 신석 | **sacred stone** | Stone said to have existed alongside the Black Tiger's birth. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 신물 | **divine artifact** | General term for a sacred or divine object, distinct from 신석. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 백호 | 진태경 | guardian_spirit_to_human_ally | you | terse and irritated | The White Tiger responds telepathically after Jin calls it Whitey and jokes about its former name. |
| 진태경 | 수호령 | human ally to guardian spirit | guardian spirit | quiet and commanding | Jin whispers that they should go as they advance toward Baeksang. |
| 수호령 | 남천마후 | guardian_spirit_to_hostile_supernatural_opponent | you | terse, accusatory, and contemptuous | The guardian spirit tells the Southern Heaven Demon Empress that it knows her true essence and condemns her as a Fiend. |
| 남천마후 | 수호령 | hostile_supernatural_opponent_to_guardian_spirit | hideous beast | playful, taunting, and dismissive | She insults the guardian spirit while addressing it as a beast. |
| 수호령 | 진태경 | guardian spirit to human ally | Human | terse and alarmed | The guardian spirit cries out to Jin as the Southern Heaven Demon Empress sends him crashing into the ground. |
| 진태경 | 복면인 | hostile combatant to unknown hostile combatant | you | blunt, hostile, and incredulous | Jin directly questions the masked man about his identity and his relationship with the Great Snow Fiend. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 701
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who seeks Jin Taekyung, Cheongpung, and Jeok Cheongang after escaping the confrontation at Mount Song.
- **Personality:** Calm, confident, theatrically frivolous, casually cruel, and ruthlessly destructive; treats allies as disposable tools and enjoys provoking stronger opponents.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven alongside the Western Heaven Demon Lord, has received the Lord of Heaven's power for the coming Great War, and still seeks to kill Cheongpung, Jeok Cheongang, and Jin Taekyung.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 702
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 702
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an injured leader who has wounded the Southern Heaven Demon Empress and initiated One Annihilation in their unresolved battle.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 702
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Masked Man.md

# Masked Man (복면인)

- **Safe through:** Chapter 701
- **Aliases:** None
- **Role:** The Masked Man is the Southern Heaven Demon Empress's carefully trained hunting dog, a dark-force fighter who regenerates from grievous injuries and appears unable to feel pain.
- **Personality:** The Masked Man is emotionless, silent, and indifferent to extreme bodily damage.
- **Voice:** No spoken voice has been established.
- **Relationships:** He serves the Southern Heaven Demon Empress as her hunting dog; his identity and relationship with the Great Snow Fiend remain unknown.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 702
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is Honglan, the former Lower District Sect singing courtesan, the creator of the massive rift behind Nanman's Inner Palace, and the enemy who grows stronger as its demonic qi thickens while pursuing the Lord of Heaven's plan after Jin Taekyung severed one of her wrists and wounded her side.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### White Tiger.md

# White Tiger (백호)

- **Safe through:** Chapter 699
- **Aliases:** Whitey
- **Role:** The White Tiger is the guardian spirit of the sacred stone, restored to its former silver-white tiger form, and now leads the beast army in rescuing those overwhelmed by the demonic qi and carrying them toward the Outer Palace.
- **Personality:** Irritable and contemptuous of Jin Taekyung's jokes.
- **Voice:** Telepathic, terse, and easily exasperated.
- **Relationships:** The White Tiger carries Jin Taekyung and Yohi, guards the sacred stone, and advances with Jin's forces.

## Korean source

```text
＃703화



콰아아아……!

숨이 막혔다.

아직도 가시지 않은, 지금도 끝없는 울림과 함께 계속되는 굉음이 아득하게만 들려온다.

하지만 그럼에도 불구하고, 시스템 알림만큼은 또렷하게 귓가에서 울려 퍼지는 중이었다.

삑! 삐비빅!



- 상태 이상, [심각한 내상]이 부여됩니다!

- 상태 이상, [심각한 탈진]이 부여됩니다!

- 상태 이상, [심각한 근육 파열]이 부여됩니다!

- 상태 이상…….

.

.

끊임없이 들려오는 시스템 알림. 아니, 경고음은 내 몸 상태가 얼마나 심각한지 조목조목 짚어 준다.

아마 시스템이 의사였다면 세상 심각한 표정으로 나를 바라보며 이렇게 말했을 것이다.

‘환자분. 이런 말씀 드리기 뭐 하지만…… 이번엔 진짜 좆 된 것 같습니다. 그러니까 왜 자꾸 일섬을 쓰고 지랄이세요. 혹시 단명하는 게 버킷리스트입니까?’

거 참, 친절하기도 하지.

상상만으로 기분이 거지 같아질 것 같지만, 희한할 정도로 지금의 나는 별다른 심경의 변화가 없었다.

그리고 그럴 수 있는 이유는 생각보다 간단하다. 상상보다 더 거지 같은 현실이 나를 기다리고 있기 때문이었다.

“쿨럭.”

주륵. 투두둑.

기침과 함께 터져 나온 핏물이 지면에 흩뿌려진다.

잠깐 건더기도 씹힌 걸 보니 내장 조각이 틀림없는데, 이런 걸 보면 확실히 일섬이 혜자……는 씨발. 무슨 편의점 도시락도 아니고.

‘빌어먹을.’

시야가 아득하다. 조금 전까지만 하더라도 신병이기 부럽지 않게 날카롭던 감각은 버려진 오두막의 도끼처럼 무뎌졌고, 언제나 팔랑개비처럼 휘둘렀던 백염은 세상에서 가장 무거운 것이 되어 버렸다.

하지만 이 와중에도 그나마 멀쩡한 것이 한 가지 있다면, 지금 이 순간에도 팔뚝에서 느껴지는 통증이었다.

으적. 으적.

나는 흐릿한 시선으로 ‘그것’을 바라보았다.

짐승처럼 삐죽 솟은 이빨로 끊임없이 살점을 씹어 대고, 핏물을 삼키는 그것의 눈에는 탐욕과 광기만이 가득했다.

나와 같은 인간이라고는 믿을 수 없을 만큼.

“맛있냐?”

으적.

“그래, 맛있나 보네.”

나도 모르겠다.

더 이상 알아듣지 못할 걸 뻔히 알면서도 왜 이런 말을 건네는지. 내 팔목으로 실시간 먹방 스트리밍을 찍고 있는 이 괘씸한 놈을 왜 가만히 내버려 두는지.

그건 어쩌면…… 다른 누군가의 손을 빌리고자 하는 이기심과 한때 인간이었을 존재에 대한 마지막 동정심이었는지도 모르겠다.

슈화악! 서걱!

으적…….

어디선가 들려온 파공성과 함께, 맹렬하게 살점을 씹어 대던 이빨이 축 늘어진다.

내가 붉은 눈동자를 부릅뜬 채 굳어 버린 청년을 바라보고 있던 그때, 피와 먼지로 범벅이 된 은빛 갈기가 눈앞을 스쳤다.

- 인간. 안 괜찮아 보이는군.

수호령. 녀석의 존재를 인식하기 무섭게 다리에 힘이 풀린다. 나는 갈기를 붙잡으며 힘없이 대꾸했다.

“보통은 처음에 괜찮냐고 묻지 않나?”

- 난 인간과 다르다. 안 괜찮아 보이기에 굳이 묻지 않았다.

“거 마음에 드네. 그 새카만 놈은?”

- 죽였다. 이번이 네 번째였지.

“뭐?”

- 계속해서 일어나더군. 시간이 흐를수록 회복하는 속도가 빨라지고, 놈 역시 강해졌다. 이번 역시 마찬가지일지도 모르지.

균열. 정확히는 균열로부터 흘러나온 마기의 영향이다.

그리고 마기에 의해 복면인이 강해지는 만큼, 수호령은 서서히 약해졌을 것이다.

처음처럼 커다란 빛을 뿜어내지 못하는 입 안의 신석처럼.

‘수호령은 신석(神石)과 힘을 공유하니까.’

이제야 수호령의 몸 곳곳에 깊숙한 상처가 보인다. 지친 듯 들썩이는 어깨와 가파른 숨결도.

그런 내 시선을 눈치챘는지, 녀석이 거대한 동체를 상처가 보이지 않게 돌렸다.

“미안하다.”

흐릿한 목소리로 건넨 한 마디. 청백색의 눈동자로 나를 물끄러미 바라보던 수호령이 고개를 저었다.

- 넌 할 만큼 했다.

“마지막에…….”

- 안다, 저것들이 끼어들지 않았다면 성공했겠지.

나는 힘없는 시선으로 주위를 둘러보았다. 갈가리 찢겨 나간 시신들이 시야에 들어온다.

일섬을 쏘아 보내려던 마지막 순간, 수호령의 경고와 함께 가장 먼저 변화를 끝마치고 내게 달려든 변이체(變異體)들의 흔적이었다.

‘미처 예상하지 못했어.’

아니, 신경 쓸 여유조차 없었다고 해야 옳다.

그리고 지금과는 달리 주위를 둘러보지 못할 만큼 급박한 상황에 처해 있던 내게, 변이체들은 맹렬하게 달려들었다.

‘그리고 죽었지.’

어림잡아 일백에 달하는 그들을 기다리고 있던 것은 일섬이 불러온 강대한 와류였다.

하지만 찰나를 쪼개고 쪼갠 그 짧은 시간 속, 변이체들은 본능적으로 나를 저지하여 자신들의 임무를 다했다.

팔뚝을 물어뜯어 방향을 틀고, 눈앞의 시야를 가로막고, 막을 수 없는 거대한 기운 앞에 몸을 내던졌다.

그리고 그렇게…… 한 사람은 살아남을 수 있었다.

“남천마후.”

침음성과도 같은 내 목소리에, 흐릿한 먼지구름 사이로 우뚝 서 있던 인영이 걸음을 내디딘다.

사박.

일섬의 여파에 휘말려 모든 것이 소멸해 버린 일각(一角). 그 모든 것의 중심에서 유일하게 살아남은 괴물이, 붉은 눈동자를 빛내며 모습을 드러냈다.



* * *



붉다. 모든 것이 붉었다.

하늘도. 땅도. 그 사이에 있는 모든 것들이. 그와 동시에 보여서는 안 될 것들이 보였다.

‘아.’

남천마후는 멍하니 자신의 손을 내려다보았다.

수 갑자에 달하는 공력과 숱한 정혈(精血)을 취하며 얻어 낸, 새하얗고 매끄러운 손은 더 이상 찾아볼 수 없다.

자글자글한 주름과 검버섯으로 가득한, 죽어 가는 고목의 가지처럼 비쩍 마른 손이 그곳에 있었다.

“아. 아아…….”

터져 나간 실핏줄로 붉게 물든 눈동자에 물기가 어렸다.

이럴 수는, 이럴 수는 없다. 세상 누구보다 아름다웠던 자신이었다. 아름다워야 했던 그녀였다.

하지만 백 년에 가까운 세월 동안 익혀 온 대공(大功)은 깨졌고, 남천마후는 늙고 추한 본래의 모습을 저주처럼 되찾았다.

그리고 아득한 충격과 분노에 몸을 떨던 그녀는, 자신에게 찾아온 저주가 억눌렀던 노화(老化)뿐만이 아님을 깨달았다.

‘아파.’

문득 엄습하는 격통에 몸을 살핀 후에야 비로소 알 수 있었다.

보이지 않는 짐승에게 베어 먹힌 것처럼 뜯겨 나간 옆구리의 살점과 송두리째 날아가 버린 한쪽 팔.

그리고 엄청난 열기에 의해 녹아 버린 얼굴 반쪽을.

“……!”

남천마후는 눈을 부릅떴다. 그것은 있을 수도 없고, 있어서도 안 되는 일이었다.

옆구리의 상처는 회복할 수 있다. 한쪽 팔도 솜씨 좋은 술사(術士)라면 흉터 없이 붙여줄 수 있을 것이다.

하지만 얼굴은 아니다. 그녀가 그토록 멸시하는 혈주(血主)와 같은 길을 걷지 않는 한, 끔찍한 화상을 입은 얼굴에는 흔적이 남고 말 것이다.

“안 돼. 이건, 이건 말도 안…….”

넋 나간 사람처럼 중얼거리던 남천마후의 움직임이 우뚝 멈췄다. 어느새 눈물에 젖은 핏빛 눈동자에 비친 한 사람 때문이었다.

진태경.

보인다. 그리고 느껴진다.

모든 것을 지워 버린 눈부신 섬광 뒤, 힘을 잃고 껍데기만 남아 버린 녀석의 모습이. 자신의 젊음과 아름다움을 빼앗아 버린 하찮은 존재가.

동시에 찾아온 일념(一念)이 남천마후의 전신을 사로잡았다.

‘죽인다.’

그 순간. 수많은 감정으로 혼란하던 머릿속이 차갑게 식었다.

아득한 세월을 살아온 괴물은 망설임 없이 어둠을 두른 채 걸음을 옮겼다.

사박. 사박.

콰드득.

한 걸음, 한 걸음마다 남천마후의 전신에서 흘러나온 기운이 주위를 짓눌렀다.

비록 젊음을 잃었지만, 아직 놈을 죽일 만한 힘은 남아 있다.

옆구리와 팔에서 흐르던 피는 어느덧 멎어 있었고 진탕되었던 내부는 느리지만 조금씩 안정되어 가고 있었다.

갑작스럽게 돌아온 노화가 저주라면, 지금 이 순간에도 짙어지고 있는 균열의 마기(魔氣)는 남천마후에게 있어 축복이었다.

제 몸을 가누는 것조차 힘든 진태경과, 그 앞을 가로막은 어느 노린내 나는 짐승을 갈기갈기 찢어 버릴 수 있게 해 주는 축복.

- 멈춰라.

스아아아.

울려 퍼지는 의념과 함께 수호령의 중심으로 번져 나가는 빛무리.

어느새 그 주위를 빼곡하게 둘러싼 일천의 변이체들이 바짝 몸을 움츠렸지만, 남천마후의 발걸음은 멈추지 않았다.

파앙!

한 치의 망설임도 없이 쏘아진 장력, 핏빛 강기와 뒤섞인 어둠이 신석의 빛을 짓누르며 진태경을 덮쳤다.

쾅!

굉음과 함께 지면이 터져 나간다. 찰나의 순간, 진태경의 목덜미를 입에 물고 번개처럼 몸을 날린 수호령이 낮은 울음소리를 흘렸다.

- 신석이…….

뒷말은 삼켰지만, 수호령이 깨달은 현실은 잔인할 정도로 명확했다.

우우우웅.

입안에서 잘게 떨리는 움직임이 느껴진다. 마치 한창때의 젊은이를 상대하는 노인처럼, 신석이 지닌 힘은 지금 이 순간에도 줄어들고 있었다.

더불어 오랜 세월 신석을 지켜 온 어느 백호의 힘도 함께.

‘이무기가 남긴 영기(靈氣)로도 부족했나.’

그 정도로 본래의 힘을 모두 온전히 회복하리라고는 생각하지 않았다.

더군다나 수신룡은 한 차례 변이되었던 영향으로 그리 많은 기운을 남기지 못했으니까.

‘마기가 너무 강하다. 신석의 힘조차 억누를 정도로.’

균열로부터 흘러나오는 마기는 이미 내궁을 넘어 외궁으로 잠식해 나가는 상황.

수호령이 이끌고 온 성지의 맹수들이 있었지만, 신석마저 약해진 마당에 맹수들마저 마기의 영향에 놓인다면 사태는 걷잡을 수 없이 악화된다.

아니, 이미 최악이다.

완전히 마기의 영향에 놓인 일천에 달하는 변이체가 사방을 빈틈없이 에워싸고, 남천마후라는 강자마저 끝끝내 살아남아 그들을 노리고 있으니까.

‘이대로라면…….’

피할 수 없는 생각에 수호령의 낯빛이 어두워진 그때. 진태경이 힘없는 목소리로 입을 열었다.

“가라.”

- 뭐?

“고생했어. 그동안 욕봤다.”

- ……!

자신을 향해 크게 뜨인 청백색 눈동자를 바라보며, 진태경은 백염을 지팡이 삼아 힘겹게 몸을 일으켰다.

“이만하면 됐어. 넌 빠져나가서 사람들을 구해. 이 좆 같은 땅에서 최대한 빨리, 멀리 벗어나라고.”

- 그걸 지금 말이라고…….

“장담하는데, 네가 아무리 빨라도 나 데리고 가면 얼마 못 버텨. 아마 반 시진도 안 돼서 내가 먼저 내려 달라고 징징댈걸. 운기조식 안 하면 뒈질 테니까.”

장난스럽지만 냉정한 한 마디에 수호령이 입을 다문 그때, 진태경이 씩 웃으며 말을 이었다.

“그러니까, 가. 더 늦기 전에.”

말을 끝마친 진태경이 고개를 돌려 남천마후를 응시한다.

금방이라도 꺼질 것 같은 청년의 눈빛과 분노로 타오르는 혈광이 허공에서 맞닥트렸다.

“자, 순순히 따라갈 테니까 이제 그만하자. 천주인지 개잡주인지, 어디 한 번 보러 가자고.”

남천마후가 대답 대신 손을 들었다.

쉭, 피핏!

빛살처럼 날아든 지풍(指風)이 목덜미를 찢었다. 진태경이 아무렇지 않게 어깨를 으쓱해 보였다.

“화났으면 말로 하지 그러냐. 가뜩이나 피 많이 흘렸는데. 가다가 죽으면 어쩌시려고?”

남천마후가 서늘한 목소리로 대답했다.

“그럼 곤란한데.”

“이제 좀 말이 통하…….”

“이 정도로 죽으면 안 돼. 내 손으로 천천히 찢어 죽일 테니까.”

“……지는 않네. 뒷감당은 어찌하시려고?”

“괜찮아. 신물을 가져가면 천주께서도 기뻐하실 테니. 백호의 가죽은 덤이고.”

그리고 환하게 웃은 남천마후가 손을 펼친 그 순간.

구웅-!

거대한 울림이, 남만야수궁을 휩쓸었다.
```

## Final English reading copy

```markdown
# Chapter 703

Kwoooooong…!

I couldn’t breathe.

The roar still hadn’t faded. It continued alongside endless reverberations, sounding impossibly distant.

And yet the System notifications continued ringing clearly in my ears.

> **System**
>
> *Beep! Beep-beep!*
>
> - **Status Effect:** Severe Internal Injury has been applied!
>
> - **Status Effect:** Severe Exhaustion has been applied!
>
> - **Status Effect:** Severe Muscle Rupture has been applied!
>
> - **Status Effect:** …

The System notifications—or rather, the warning sounds—continued without pause, methodically pointing out just how serious my condition was.

If the System had been a doctor, it would probably have looked at me with the gravest expression in the world and said:

*“Patient, I hate to tell you this, but… it looks like you’re really screwed this time. So why the hell do you keep using One Annihilation? Is dying young on your bucket list?”*

How considerate.

Just imagining it was enough to make me feel like shit, but strangely, I wasn’t experiencing much of a change in mood right now.

The reason was simpler than I expected.

A reality even shittier than anything I could imagine was waiting for me.

“Cough.”

Splatter. Drip, drip.

Blood burst from my mouth with the cough and scattered across the ground.

I’d even felt some chunks in it, so they were definitely pieces of my organs. Seeing that, I had to admit that One Annihilation was incredibly generous—

*Fuck. It wasn’t a convenience-store lunchbox.*

*Damn it.*

My vision was hazy. My senses, which had been sharp enough to rival a divine weapon only moments ago, had grown dull as an ax abandoned in a ruined cabin. White Flame, which I had always swung around like a pinwheel, had become the heaviest thing in the world.

But if there was one thing that was still relatively fine amid all this, it was the pain I could still feel in my forearm.

Crunch. Crunch.

I stared at *it* through my blurred vision.

It kept chewing on my flesh with teeth that jutted out like an animal’s, swallowing mouthfuls of blood. Its eyes were filled with nothing but greed and madness.

It was impossible to believe that it had once been human like me.

“Good?”

Crunch.

“Yeah. I guess it is.”

I didn’t know.

Why was I speaking to it when I knew perfectly well that it could no longer understand me? Why was I leaving this bastard alone while he livestreamed an eating show using my wrist?

Perhaps it was selfishness—the desire to borrow someone else’s hand.

Or perhaps it was the last shred of pity I had for something that had once been human.

Shwaaak! Slash!

Crunch…

Along with the sound of something slicing through the air, the teeth that had been chewing so ferociously went slack.

Just as I stared at the frozen young man with his red eyes wide open, a silver mane covered in blood and dust swept across my vision.

—Human. You do not appear to be all right.

The guardian spirit.

The moment I recognized its presence, the strength left my legs. I clutched its mane and answered weakly.

“Don’t people usually ask if someone’s all right first?”

—I am different from humans. Since you did not appear to be all right, I saw no reason to ask.

“I like that about you. What about that pitch-black bastard?”

—I killed him. That was the fourth time.

“What?”

—He kept getting back up. The longer time passed, the faster he recovered, and he grew stronger as well. This time may be no different.

The rift.

More precisely, it was the effect of the demonic qi flowing from the rift.

And as the Masked Man grew stronger from the demonic qi, the guardian spirit must have been growing weaker by degrees.

Just like the sacred stone in its mouth, which could no longer release the massive radiance it had possessed at the beginning.

*The guardian spirit shares its power with the sacred stone.*

Only now could I see the deep wounds scattered across the guardian spirit’s body. Its shoulders heaved with exhaustion, and its breathing was ragged.

Perhaps it noticed me looking, because it turned its massive body to hide the wounds from view.

“I’m sorry.”

At my weak words, the guardian spirit stared at me with its blue-white eyes before shaking its head.

—You did all you could.

“At the end…”

—I know. If those things had not interfered, you would have succeeded.

I looked around with exhausted eyes.

Torn corpses came into view.

They were the remains of the mutants who had completed their transformation first and rushed at me alongside the guardian spirit’s warning, just as I was about to fire One Annihilation.

*I didn’t anticipate it.*

No.

It would be more accurate to say that I hadn’t had the time to worry about it.

Unlike now, I had been in such a desperate situation that I couldn’t even look around. The mutants had charged at me with incredible ferocity.

*And then they died.*

What awaited roughly one hundred of them was the immense vortex created by One Annihilation.

But in that brief instant, split into smaller and smaller fractions of time, the mutants had instinctively stopped me and fulfilled their mission.

They had bitten into my forearm and changed the direction of my attack. They had blocked my view. They had thrown themselves in front of an enormous force that could not be stopped.

And that was how one person survived.

“Southern Heaven Demon Empress.”

At my voice, which sounded more like a groan, a figure standing tall amid the hazy cloud of dust took a step forward.

Scuff.

A section of the ground had been caught in the aftermath of One Annihilation, and everything there had been erased.

From the very center of it all, the only monster to survive emerged, her red eyes glowing.

* * *

Everything was red.

The sky. The ground. Everything in between.

At the same time, things that should never have been visible came into view.

*Ah.*

The Southern Heaven Demon Empress stared blankly down at her hand.

The smooth, snow-white hand she had gained by taking several jiazi’s worth of internal energy and vast amounts of vital essence was nowhere to be seen.

In its place was a withered hand covered in fine wrinkles and age spots, as dry and thin as the branch of a dying tree.

“Ah. Aah…”

Moisture gathered in her bloodshot eyes, stained red by ruptured capillaries.

This couldn’t be happening.

It couldn’t.

She had been more beautiful than anyone in the world. She was supposed to be beautiful.

But the grand art she had cultivated for nearly a century had been shattered, and the Southern Heaven Demon Empress had been forced to reclaim her original, old, and ugly appearance as though it were a curse.

Then, as her body trembled with distant shock and rage, she realized that the curse that had descended upon her was not merely the aging she had suppressed.

*It hurts.*

Only after examining herself in response to the sudden agony did she finally understand.

The flesh along her side had been torn away as though gnawed off by an invisible beast, and one of her arms had been blown away completely.

Half of her face had melted beneath the tremendous heat.

“……!”

The Southern Heaven Demon Empress’s eyes flew open.

It was impossible.

It was something that should never have happened.

The wound in her side could heal. Even her arm could be reattached without leaving a scar if she found a skilled enough practitioner.

But her face was different.

Unless she walked the same path as the Blood Lord, whom she despised so deeply, the face that had suffered such terrible burns would be scarred forever.

“No. This… this makes no…”

The Southern Heaven Demon Empress mumbled like a woman who had lost her mind, then suddenly stopped.

It was because of the person reflected in her blood-red eyes, now wet with tears.

Jin Taekyung.

She could see him.

She could feel him.

After the dazzling flash that had erased everything, he remained—a powerless shell of a man.

The pitiful creature that had stolen her youth and beauty.

At the same time, a single thought seized the Southern Heaven Demon Empress’s entire body.

*Kill him.*

At that moment, the mind that had been confused by countless emotions turned cold.

The monster who had lived for an age wrapped herself in darkness and moved forward without hesitation.

Scuff. Scuff.

Crack.

With every step, the energy flowing from the Southern Heaven Demon Empress’s body crushed the surrounding area.

She might have lost her youth, but she still possessed enough strength to kill him.

The blood flowing from her side and arm had already stopped, and her battered insides were slowly, but steadily, stabilizing.

If the sudden return of aging was a curse, then the demonic qi of the rift, which continued growing denser even now, was a blessing to the Southern Heaven Demon Empress.

A blessing that would allow her to tear apart Jin Taekyung, who could barely stand on his own, and the musty old beast standing in front of him.

—Stop.

Ssssss.

Along with the guardian spirit’s resonating thought, a halo of light spread from its center.

The thousand mutants packed tightly around it hunched down, but the Southern Heaven Demon Empress did not stop walking.

Bang!

A palm strike shot forward without the slightest hesitation. Darkness mixed with blood-red Force pressed down on the sacred stone’s light and engulfed Jin Taekyung.

Boom!

The ground exploded with a deafening roar.

In that instant, the guardian spirit bit Jin Taekyung by the nape and darted away like lightning, releasing a low growl.

—The sacred stone…

It swallowed the rest of its words, but the reality it had realized was cruelly clear.

Rumble…

It felt tiny tremors coming from inside its mouth.

Like an old man facing a young man in his prime, the power held by the sacred stone was diminishing even now.

And so was the strength of the White Tiger that had protected the sacred stone for ages.

*Even the spiritual energy left behind by the imugi wasn’t enough?*

The guardian spirit had never expected to fully recover all of its original strength from that alone.

Moreover, the Water God Dragon had been unable to leave behind much energy because of the effects of its previous mutation.

*The demonic qi is too strong.*

*Strong enough to suppress even the sacred stone’s power.*

The demonic qi flowing from the rift had already spread beyond the Inner Palace and begun encroaching on the Outer Palace.

The guardian spirit had brought the beasts of the Sacred Land with it, but if the beasts also fell under the demonic qi’s influence while even the sacred stone was weakening, the situation would deteriorate beyond control.

No.

It was already the worst possible situation.

Nearly a thousand mutants completely under the demonic qi’s influence surrounded them without leaving a single opening, while even the powerful Southern Heaven Demon Empress had survived to the bitter end and was now hunting them.

*If this continues…*

Just as the guardian spirit’s expression darkened at the unavoidable thought, Jin Taekyung spoke in a weak voice.

“Go.”

—What?

“You’ve worked hard. You’ve been through enough.”

—……!

As he looked into the guardian spirit’s wide blue-white eyes, Jin Taekyung used White Flame as a cane and struggled to stand.

“This is enough. Get out and save the people. Get out of this goddamn place as quickly and as far away as possible.”

—You’re saying that now…

“I guarantee it. No matter how fast you are, I won’t last long if you take me with you. I’ll probably start whining for you to put me down in less than half a shichen. I’ll die if I don’t circulate my qi.”

The guardian spirit fell silent at the playful but cold words.

Jin Taekyung continued with a crooked smile.

“So go. Before it’s too late.”

When he finished speaking, Jin Taekyung turned his head and stared at the Southern Heaven Demon Empress.

The young man’s eyes, which seemed as though they could go out at any moment, met the blood-red light burning with fury in midair.

“All right. I’ll come along quietly, so let’s stop this. Lord of Heaven or Lord of Fucking Dogs, whatever he is, let’s go see him.”

The Southern Heaven Demon Empress raised her hand instead of answering.

Swish, spit!

Finger Qi flew like a beam of light and tore into the back of his neck.

Jin Taekyung casually shrugged his shoulders.

“If you’re angry, why not say so? I’ve already lost a lot of blood. What if I die on the way?”

The Southern Heaven Demon Empress answered in a chilling voice.

“That would be troublesome.”

“Now we’re finally talking—”

“You mustn’t die this easily. I’ll tear you apart slowly with my own hands.”

“……I guess we’re not exactly communicating. What are you planning to do about the fallout?”

“It will be fine. The Lord of Heaven will be pleased if I bring him a divine artifact. The White Tiger’s pelt will be a bonus.”

The Southern Heaven Demon Empress spread her hand as she smiled brightly.

Kwoooong—!

A tremendous rumble swept across the Nanman Beast Palace.
```
