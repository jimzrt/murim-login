<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1073.txt",
      "sha256": "b76df8abeaeddd4fbe9961b3fa3f426f130aac53fa53efb01cbf68593ae2411f",
      "bytes": 11958
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c29553586f1c5972fd91eb6aa4a7c45fb3d0c53a84522dbb736c32811efb7e96",
      "bytes": 1402
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5be93eb6bd068e9f3140c82d613f582e8e72d687cb3b90fa54d2c393096f3e5c",
      "bytes": 242356
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "19798c7922177b5d9352e92de0ef32d2ece35ee627ac848594cc3fd0547488e9",
      "bytes": 776
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "b40100ce8a90fa80e4bb4611c8c2c2dbf3ea779edb7e32bcc36fa0d50d6caade",
      "bytes": 1326
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "e3390b9a3f03fce747b9f52e3d18b193507a26b09d7f744d67b839920f148568",
      "bytes": 1502
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "6a9c8203eb651d527fec6bd97a5422fc3856dc0247df5ffcf223d55d56f7b33b",
      "bytes": 850
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7df8b2357d0faa08e63a571debd66c331206f8c9af0b11d116826f4c7dad2ad4",
      "bytes": 284375
    }
  ],
  "estimated_tokens": 9210
}
-->

# Durable State Update — Chapter 1073

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
1 and safe_through 1073. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1073. Profile updates may replace only one
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
  "chapter": 1073,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1073,
    "continuity_sources": [1073],
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
    "Jin’s roughly three thousand allies are fighting at least ten thousand surrounding monsters, including mutants.",
    "Jin’s circular formation has Sama Pyo and Jeong Hogun on the wings, Hyeoncheon and the Kongtong Disciples plus Hyuk Sopyung and the Zhongnan Disciples at the rear, and Jeok Cheongang, Bow Saint, and the Fire Dragon Pavilion at the vanguard.",
    "Sorcerers use bells to coordinate monsters; the Blood Lord ordered them to reduce the allied force and capture Jin alive.",
    "A guileless intruder hid among the monsters for two days without detection and calls his teacher “Little Grandpa.”",
    "The intruder says the other sorcerers who came with the black-robed man are dead; the Little Grandpa appeared behind him undetected and incapacitated him."
  ],
  "continuity_sources": [
    1071,
    1072
  ],
  "open_questions": [
    "Who is Great Sir, and what is his connection to Hyeoncheon and the surviving Kongtong Disciples?",
    "Did Jin’s sword strike kill or otherwise affect the watching crow?",
    "Are Dark Heaven’s forces broadly composed of reanimated corpses, and has Ma Sanbao spread the Corpse Art to others?",
    "What is the Lord of Heaven seeking through Jin, and when will he appear?",
    "Who are the intruder and his Little Grandpa?"
  ],
  "safe_through": 1072,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 천태민    | **Cheon Taemin**  |
| 궁성     | **Bow Saint**                 | —              |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 사제     | **Junior Brother**                           |
| 일격     | **One Strike**                         |
| 지능               | **Intelligence**               |
| 몬스터     | **monster**           |
| 노부      | **this old man / I**                                            |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 변이체 | **mutant** | Taekyung's classification for the monster. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 개똥이 | **Gaettong** | One of the names the Lord has used for himself, according to the Seven Masters. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 994
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Ares Guild Master and humanity's greatest Hunter, the Slayer who defeated the Demon King and created the first Mana Cultivation Method during the Great Cataclysm; after more than twenty years in seclusion, he remains unconscious in a secret area within Area A.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1056
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1071
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1071
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Courteous and calculating, he chooses what he believes is right over expedience and accepts responsibility for his choices, even when they expose him to blame.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo is Sima Gong’s son and chosen heir, commands Taishan, and is Jin Taekyung’s friend; he deliberately let Namho suspect his father’s actions to protect their companions, was Ju Hwaran’s former fiancé, and is hostile toward Song Ilseom.

## Korean source

```text
1073화




서걱!

힘차게 내리그은 창날이 첫 희생양을 베어 가른 그 순간부터, 내 가슴은 무겁게 가라앉아 있었다.

적들이 생각 이상으로 강해서?

혹은 마음 한구석으로는 이미 패배라는 단어를 만지작거리고 있어서?

아니다. 틀렸다.

나는 처음부터 아군의 승리를 믿어 의심치 않았다.

다만 언제나 그렇듯이, 스스로의 한계를 실감했을 뿐이었다.

이미 몇 번이나 돌파했음에도 완전히 벗어날 수 없는, 한낱 인간으로서의 한계.

‘이번에는 또 몇 명이 죽을까.’

물론 알고 있다.

나는 모두를 구할 수 있는 전지전능한 신이 아니라는 것을.

나뿐만 아니라 다른 누구라 할지라도 그와 같은 신이 될 수 없다는 사실을.

그것은 아득한 신화 속 영웅들도 마찬가지였고, 인류의 구세주라 불리는 천태민 또한 예외일 수 없었다.

무언가를 얻기 위해서는, 그에 합당한 대가를 치러야 한다.

그 대가가 시간이든, 혹은 목숨이든.

하지만 그 사실을 알고 있다고 한들, 익숙해질 수는 없다.

아니, 결코 익숙해져서는 안 된다.

그렇게 된다면 모든 것이 당연해져 버릴 테니까.

그리고 누군가의 희생과 죽음은, 결코 당연해져서는 안 되는 종류의 것이니까.

콰드드득!

단 한 번.

강기를 실어 휘두른 창날을 따라 섬뜩한 파육음과 함께 자욱한 피 안개가 퍼져 나간다.

만약 상대가 인간이었다면 단숨에 경악과 공포에 사로잡혔을 광경.

그러나 수십여 마리의 괴물들이 잘게 다진 육편(肉片)이 되어 흩어졌음에도 불구하고, 놈들은 아랑곳하지 않고 온 사방에서 물밀듯이 밀려들었다.

그 맹렬하고도 포악한 기세와는 어울리지 않는 촘촘한 전열(前列)을 갖춘 채.

‘놈들의 지능 수준으로는 불가능한 일. 분명 누군가가 있다.’

전투가 본격적으로 시작되기 전, 바람에 실려 사방에서 전해져 왔던 그 음산한 방울 소리들은 결코 환청이 아니었다.

변이체, 혹은 몬스터.

저 끔찍한 괴물들을 정확히 뭐라 지칭해야 할지는 모르겠지만, 어딘가에서 놈들을 꼭두각시처럼 조종하는 사령탑이 존재하는 것만큼은 확실해졌다.

다만 한 가지 문제는…….

‘잘도 숨었군.’

나를 비롯한 초절정 고수들의 존재를 염두에 두었기 때문일까.

다수임이 분명한 그들의 모습은 어디에서도 찾을 수 없었다.

그리고 이는 비단 나뿐만이 아니라, 아군 중 가장 뛰어난 안력(眼力)을 지녔을 한 사람에게도 해당하는 이야기였다.

쉬쉭, 콰아아앙!

동서남북을 향해 연달아 쏘아진 네 줄기의 섬광이 공간을 집어삼키며 폭발한다.

뒤이어 사방을 떨어 울리는 그 거대한 충격파와 굉음 속, 특유의 침착한 음성이 귓가를 파고들었다.

“지금으로서는 보이지도, 느껴지지도 않는다. 최소 백여 장 밖이야.”

이미 내 생각을 꿰뚫어 보는 듯한 궁성의 한마디.

그와 동시에 괴물들의 핏물을 흠뻑 뒤집어쓴 적천강이 나타나 덧붙였다.

“그리고, 더럽게 많기도 하군.”

화륵, 퍼어엉!

말을 끝맺기도 전에 내뻗은 일권(一拳).

공기마저 불사르며 나아간 화염이 끔찍한 열기를 발산하며 괴물들을 집어삼켰다.

- 크르륵!

- 그아아악!

겹겹이 울려 퍼지는 비명.

그러나 강대한 힘이 담긴 일격으로 또 다시 수십에 달하는 적들을 쓰러트렸음에도, 적천강의 표정은 조금도 밝아지지 않았다.

“이대로면 끝도 없다. 여기 있는 놈들을 모조리 전멸시키지 않는 이상, 길은 열리지 않을 터.”

전투의 흐름이 아군에게 유리하게 흘러가고 있다는 것은 명백한 사실이다.

하지만 문제는 사방을 둘러싼 이 수많은 괴물들을 모두 쓰러트리고 난 이후의 일이었다.

삼천여 명의 아군 중 상당수는 분명히 죽거나 다칠 테고, 암천의 추격은 앞으로도 끈질기게 이어질 테니까.

‘빌어먹을.’

나는 치밀어오르는 욕설을 삼키며 주위를 둘러보았다.

일만에 달하는 괴물들에 맞서 전투가 시작된 지 이제 겨우 촌각 남짓.

지금 당장은 나를 포함한 여러 초절정 고수들의 활약으로 별다른 희생자가 나오지 않고 있지만, 그것도 결국은 시간문제나 다름없었다.

‘이미 지쳐 있던 만큼, 금세 허물어지겠지.’

전투란 곧 자기 자신과의 싸움이기도 하다.

제아무리 가려 뽑은 정예라고는 하나, 적들과는 달리 그들은 피륙으로 이루어진 인간.

생사의 기로에 놓였다는 사실을 스스로 인지하는 순간, 인간의 육신은 급속도로 지치고 정신은 흐릿해져만 간다.

그리고 그런 아군을 최대한 보호하기 위해 시작부터 모든 전력을 다하고 있는 초절정 고수들 역시, 평소보다도 더욱 빠른 속도로 힘을 소진하고 있었다.

당장 나만 해도 그들과 마찬가지였으니까.

퍼걱, 쿵!

정확히 종아리의 힘줄을 가른 창날에 높이만 이 장에 달하는 거구가 무릎을 꿇는다.

겉보기에도 도무지 인간 같지 않은 거대한 체구.

괴물들을 둘러싼 피륙은 가죽 갑옷처럼 질겼고, 그보다 단단한 뼈를 가르기 위해서는 더욱더 큰 힘이 필요했다.

퍽.

적잖은 공력이 실어 내뻗은 일장(一掌)으로 놈의 두개골을 으스러트린 나는 이를 악물며 외쳤다.

“대형 유지!”

곳곳에서 복명복창이 울려 퍼졌지만, 그 크기와 기세가 벌써 확연하게 수그러들었음을 단번에 느낄 수 있었다.

‘변화가 필요해.’

공포.

인간에게 주어진 가장 어두운 감정.

지금껏 본 적도, 들은 적도 없는 괴물들에게 포위당한 이상 당연한 일일 수밖에 없다.

그리고 저들을 속박한 공포를 끊어 낼 수 있는 충분한 힘이, 지금의 내게는 있다.

엄청난 힘을 소모하는 대신, 현재의 상황을 타개할 수 있는 최선의 한 수가.

‘한 번. 단 한 번의 기회를 노려 놈들의 전열을 단숨에 찢어발긴다.’

제아무리 단단한 벽이라도 틈새를 벌리는 순간 무너지는 법.

나는 천천히 숨을 삼켰다.

그와 동시에 어느덧 느려진 세상과 멀어져 가는 소음을, 또한 내 안 깊숙한 곳에서 열리는 새로운 감각과 마주했다.

아직까지도 낯설게 느껴지는, 중단전(中丹田)의 감각을.

우우우웅.

불현듯 잘게 떨리는 공간.

나는 주위를 둘러싼 모든 것과 감응(感應)하며 손을 뻗었다.

아니, 뻗으려 했다.

바로 그 순간, 한껏 집중된 내 오감을 깨트릴 만큼 커다란 함성을 내지르며 모습을 드러낸 누군가가 나타나기 전까지는.

“가아아아알!”

각오가 철철 넘쳐흐르는 목소리.

그리고 그에 어울리지 않는 잔망스러운 움직임으로 내 앞을 가로막은 대인이, 어디서 주웠는지 모를 철검을 붕붕 휘둘렀다.

“이 어리석고 불쌍한 괴물들아! 하늘의 뜻을 받들어 이 땅에 강림한 신장(神將), 개똥이가 왔으니 지금 당장 무릎을 꿇어라!”

“……!”

“……!”

일순간 내려앉은 싸늘한 침묵.

나를 비롯한 주위의 아군들은 물론, 사방에서 짓쳐 들던 괴물들까지 흐린 눈으로 대인을 바라보았다.

‘이 새끼 뭐야.’

같은 눈빛. 같은 생각.

하지만 괴물과 인간을 단숨에 대화합의 장으로 이끈 기적을 선보인 장본인은, 아랑곳하지 않고 준엄한 어조로 외침을 이어 갈 뿐이었다.

“어허! 무엇하느냐! 나, 춘자의 명이 들리지 않느냐!”

개명은 물론 성전환까지 단숨에 끝마친 대인의 일갈에, 적천강이 탄식하듯 중얼거렸다.

“저놈부터 잡아 죽였어야 했는데.”

매우 타당한 의견에 나도 모르게 고개를 끄덕일 뻔했지만, 지금은 그게 중요한 게 아니다.

대인이 선봉에 나타났다는 것은 사마표가 이끄는 좌익(左翼)의 전력 공백을 의미했고, 이는 곧 머지않아 아군의 진형 전체가 허물어질지도 모른다는 뜻이었으니까.

‘저 미친놈이……!’

정신이 온전치 않다는 건 익히 알고 있었지만, 하필이면 이 중요한 시점에서 똥을 싸지를 줄이야.

그러나 분노를 표출할 시간조차 없는 것이 현재의 상황.

내가 폐부 깊숙한 곳에서 치밀어오르는 쌍욕을 억누르며 대인을 원래의 자리로 돌려보내려던 그 순간이었다.

쿠웅!

지면을 뒤흔드는 커다란 울림과 함께, 가장 가까운 곳에 있던 괴물이 돌연 한쪽 무릎을 꿇었다.

“……이게 무슨.”

누군가의 입술 사이로 흘러나온 외마디 신음은, 나를 포함한 모두가 동시에 떠올린 의문이기도 했다.

그리고 그 의문에 대한 답을 찾기도 전, 사방을 철벽처럼 포위하고 있던 또 다른 괴물들이 불현듯 몸을 떨었다.

- 크륵. 크르륵.

- 쿠워?

확장되는 동공과 의미를 알 수 없는 신음들.

더불어 그와 동시에 시작된 이변(異變).

쿵. 쿠구구궁!

땅이 울린다. 육중한 몸뚱어리가 연이어 쓰러지며 짙은 먼지구름을 만들어 낸다.

수백에 이어 수백, 또 수백.

그렇게 광활한 갈대숲을 가득 메운 모든 괴물이 쓰러질 때까지.

그것은 마치 거대한 도미노가 허물어지는 듯한 광경이었고, 갑작스럽게 눈 앞에 펼쳐진 그 믿을 수 없는 현상에 나를 포함한 모두는 할 말을 잃어버렸다.

단 한 사람만 빼고.

“음. 그래, 그렇지. 이제야 좀 고분고분해졌구나.”

의기양양하게 뇌까린 대인이 나를 향해 고개를 돌렸다.

“엣헴. 봤나? 내가 이 정도일세.”

물론 봤다.

그것도 바로 앞에서 아주 똑똑히.

그래서 지금 이 순간 내가 쥐어짜 낼 수 있는 말은 한 가지뿐이었다.

“……뭔데, 이거. 꿈인가?”

“꿈이라, 옳은 말일세. 본래 사람의 인생이란 한낮의 꿈과 같은 것이지.”

다 안다는 듯한 미소를 지으며 고개를 끄덕이는 대인의 어깨너머로, 반쯤 넋이 나간 적천강이 나를 바라보았다.

“이게…… 도대체 무슨 상황인 것이냐?”

그렇게 물어봤자 어안이 벙벙한 것은 나 역시 마찬가지.

나는 얼떨떨한 목소리로 대답했다.

“그거야 저도 모르죠.”

“네 녀석도 몰라?”

“예.”

“별 해괴한 경우를 다 보겠군. 노부가 너무 오래 살았나?”

“오래 살긴 하셨죠.”

“아니면 혹시 우리가 같은 꿈을 꾸고 있는 게냐?”

“그럴지도 모릅니다. 혹시 실례가 안 된다면 한 대 때려도 될까요? 제가 맞으면 너무 아플 것 같아서.”

“꿈결치고는 너무나도 네 녀석다운 개소리로구나. 그러고 보니 맞은 지 오래됐지?”

“너무 현실적인 반응이네요. 아무래도 꿈은 확실히 아닌 것 같습니다.”

바로 그때였다.

신속한 태세 전환으로 적천강에게 얻어맞는 불상사를 피한 내 귓가로, 저 멀리에서 누군가의 목소리가 흘러들어온 것은.

“여전하군. 저 둘은 참으로 여전해.”

변성기도 지나지 않은 것 같은 소년의 목소리에 멈칫한 순간.

“와! 저런 사제지간은 처음 봐요!”

뒤이어 바람에 실려 도착한, 잊을 수 없는 경쾌한 음성에 나도 모르게 입술이 벌어졌다.

“……청풍?”
```

## Final English reading copy

```markdown
# Chapter 1073

*Slice!*

From the moment my forcefully swung spear cut through its first victim, my heart had been sinking heavily.

Because the enemies were stronger than I’d expected?

Or because, in a corner of my mind, I’d already been turning the word *defeat* over and over?

No. That was wrong.

I’d believed in our victory from the start, without a doubt.

It was just that, as always, I’d been made to face my own limits.

The limits of a mere human—limits I could never completely escape, no matter how many times I broke through them.

*How many people will die this time?*

Of course, I knew.

I wasn’t an omnipotent god who could save everyone.

And no one else could be such a god, either.

That was true even of the heroes in ancient myths. Cheon Taemin, hailed as humanity’s savior, was no exception.

To gain something, you had to pay a price worthy of it.

Whether that price was time or a life.

But knowing that didn’t make it something I could get used to.

No—it was something I must never get used to.

Because then, I’d start taking everything for granted.

And another person’s sacrifice and death must never become something I take for granted.

*Crraaaack!*

Just once.

The spearhead swept through, wreathed in Force, and a thick mist of blood burst out amid a ghastly squelch of torn flesh.

If the enemies had been human, the sight would have filled them with shock and fear in an instant.

But even as dozens of monsters were minced into chunks and scattered, they didn’t so much as flinch. They surged in from every direction, a relentless tide.

Their ranks were tightly packed—an orderly formation that didn’t match their ferocious, savage momentum.

*Their Intelligence isn’t high enough for this. Someone’s definitely directing them.*

Before the battle had properly begun, the eerie sound of bells had carried on the wind from all around us. It hadn’t been my imagination.

Mutants, or monsters.

I didn’t know exactly what to call those hideous creatures, but one thing was clear: somewhere, a command center was controlling them like puppets.

There was just one problem…

*They’re hiding well.*

Maybe they’d considered the presence of Supreme Peak masters like me.

Whatever the reason, I couldn’t find them anywhere. There had to be quite a few, too.

And I wasn’t the only one who couldn’t see them. The same was true even of the person among our allies with the sharpest eyes.

*Whoosh—BOOM!*

Four streaks of light shot one after another toward the east, west, north, and south, devouring space before exploding.

Amid the massive shock waves and thunderclaps that shook the air in every direction, a familiar, calm voice reached my ears.

“I can’t see or sense them from here. They’re at least a hundred *jang* away.”

The Bow Saint spoke as if she’d already read my mind.

At the same time, Jeok Cheongang appeared, drenched in the monsters’ blood, and added, “And there are a hell of a lot of them.”

*Fwoosh—BOOM!*

Before he’d even finished speaking, he thrust out a fist.

Flames raced forward, burning even the air, and swallowed up the monsters in a blast of scorching heat.

“Grrr…”

“Aaagh!”

Screams rang out over one another.

Yet even after a mighty strike brought down dozens more enemies, Jeok Cheongang’s expression didn’t brighten in the slightest.

“At this rate, it’ll never end. Unless we wipe out every last one of them, we won’t open a path.”

It was obvious the battle was going our way.

The problem was what would happen after we’d taken down all the countless monsters surrounding us.

A substantial number of our three thousand allies would surely be killed or injured, and Dark Heaven’s pursuit would continue relentlessly.

*Damn it.*

I swallowed the curses rising in my throat and looked around.

The battle against ten thousand monsters had begun only moments ago.

For now, thanks to the efforts of several Supreme Peak masters, myself included, we hadn’t suffered any notable casualties. But that was only a matter of time.

*They were already exhausted. They’ll crumble before long.*

Battle was also a fight against yourself.

No matter how carefully selected and elite they were, they were still human, made of flesh and blood—not like their enemies.

The moment people realized they were standing at the threshold between life and death, their bodies grew exhausted at an alarming rate, and their minds began to blur.

The Supreme Peak masters, who’d been giving everything from the start to protect our allies as much as possible, were also burning through their strength faster than usual.

I was no different.

*Thwack! Thud!*

My spearhead cut cleanly through the tendon in a monster’s calf. The hulking beast, a full two *jang* tall, dropped to one knee.

Its enormous frame didn’t look human in the slightest.

The flesh covering the monsters was tough as leather armor. Cutting through their bones, which were even harder, required even more strength.

*Crack.*

I poured a good deal of internal energy into a palm strike and crushed its skull. Gritting my teeth, I shouted, “Hold the formation!”

Shouts of acknowledgment rang out from every direction, but I could feel at once how much quieter and weaker they’d already become.

*Something has to change.*

Fear.

The darkest emotion given to humankind.

Of course they were afraid. They were surrounded by monsters they’d never seen or heard of before.

And right now, I had enough power to break the chains of fear holding them down.

There was one move—our best chance to turn the situation around, even if it took a tremendous amount of strength.

*One chance. Just one. I’ll find an opening and rip through their formation in a single strike.*

Even the strongest wall would collapse once a crack was forced into it.

I slowly drew in a breath.

At the same time, the world began to slow, the noise around me faded away, and a new sense opened deep within me.

The sensation of the Middle Dantian—a feeling that still seemed unfamiliar.

*Rumble…*

The space around me suddenly trembled.

I reached out, sensing everything that surrounded me.

Or tried to.

Right then, someone appeared, letting out a roar loud enough to shatter my intensely focused senses.

“Gaaaaal!”

His voice was overflowing with resolve.

And with a sprightly, utterly incongruous flourish, the Great Sir who’d cut in front of me swung a steel sword around in wide circles. I had no idea where he’d found it.

“You foolish, pitiful monsters! Gaettong, a divine general descended upon this land in answer to Heaven’s will, has arrived! Get on your knees this instant!”

“……!”

“……!”

A cold silence fell.

My allies stared blankly at the Great Sir. So did the monsters surging in from every direction.

*What the hell is this guy?*

Same look. Same thought.

But the man responsible for the miracle of bringing humans and monsters together in a moment of mutual incomprehension carried on shouting in a stern voice, undeterred.

“Hey! What are you waiting for? Can’t you hear Chunja’s command?”

At the Great Sir’s pronouncement, having changed not only his name but his gender, Jeok Cheongang muttered like a man sighing, “We should’ve grabbed that guy and killed him first.”

It was a perfectly reasonable suggestion. I almost nodded along, but that wasn’t what mattered right now.

The Great Sir showing up at the vanguard meant there was a gap in the left wing, led by Sama Pyo. And that meant our entire formation might soon collapse.

*That lunatic…!*

I knew he wasn’t in his right mind, but I hadn’t expected him to pull this shit at the most critical moment.

But we didn’t have time to vent our anger.

I was trying to suppress the curses rising from deep in my lungs and send the Great Sir back to his original position when—

*BOOM!*

The ground shook with a tremendous rumble. The nearest monster suddenly dropped to one knee.

“What… What is this?”

The single gasp that slipped from someone’s lips was the same question that had occurred to all of us, me included.

Before we could find an answer, the other monsters forming an iron wall around us began to tremble.

“Grrk. Grrrk.”

“Kuwo?”

Their pupils dilated. Strange, meaningless groans escaped them.

And then the change began.

*Thud. Rumble!*

The ground shook. Heavy bodies fell one after another, raising thick clouds of dust.

Hundreds, then hundreds more, and then hundreds again.

It went on until every monster filling the vast reed bed had fallen.

It was like watching an enormous domino chain collapse. Faced with the unbelievable sight unfolding right before our eyes, everyone—including me—was struck speechless.

Everyone except one person.

“Mm. Yes, that’s right. You’re finally being a little more obedient.”

The Great Sir turned to me, muttering smugly.

“Ahem. Did you see that? I can do this much.”

Of course I’d seen it.

I’d seen it all very clearly, right in front of me.

So at that moment, I could manage just one question.

“…What is this? Am I dreaming?”

“A dream, you say? That’s a fair way of putting it. A person’s life is, after all, like a dream in the light of day.”

The Great Sir nodded with a knowing smile.

Over his shoulder, Jeok Cheongang looked at me, half out of his mind.

“What… What in the world is going on?”

As if I knew. I was just as dumbfounded.

I answered in a dazed voice, “I have no idea either.”

“You don’t know?”

“No.”

“I’ve seen all sorts of bizarre things, but this takes the cake. Have I lived too long?”

“You certainly have.”

“Or are we perhaps sharing the same dream?”

“Could be. If you don’t mind, could you hit me once? If you hit me, it’d hurt too much.”

“For a dream, that’s a very you-like load of bullshit. Come to think of it, it’s been a while since I hit you, hasn’t it?”

“That’s a very realistic reaction. I guess it’s definitely not a dream.”

That was when it happened.

I swiftly changed course to avoid the disaster of getting hit by Jeok Cheongang, and a voice reached my ears from far away.

“Those two really haven’t changed.”

I paused at the voice of a boy who sounded too young to have gone through puberty.

“Wow! I’ve never seen a Master and Disciple like that before!”

The next moment, a cheerful voice I could never forget arrived on the wind. My lips parted before I knew it.

“…Cheongpung?”
```
