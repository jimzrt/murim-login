<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1076.txt",
      "sha256": "4eeb744a10481d91569e0d4b144621f9885ec5c8b857ee23a5aa9d00f8b8388a",
      "bytes": 12014
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a140aa7571b567d5866fbd6315c465662e6f8f0ec6c6090d2a7ec44cd8cd88c4",
      "bytes": 1224
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "ddb28ab57c0989c9486f4f046aff6af84289786a1af72e74325cceb626661668",
      "bytes": 242537
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "eea8c6e0ed8ec94dc66be240b9468f62efa0320ba22eb03c71c1b52afa825dfe",
      "bytes": 1115
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "84f73912b82a2bb8d70d10b57b9be046d2a4b81d38174775824ff74d98283285",
      "bytes": 563
    },
    {
      "path": "characters/Hak Woo.md",
      "sha256": "ae3ea4d84d0d328dc980d66c6249d97ecace5a0a482dfb79d5aaf098ab3f10cb",
      "bytes": 613
    },
    {
      "path": "characters/Hyeoncheon.md",
      "sha256": "e7f898f3df59a3febd251417ce2f7689a16d6ebf3b218e59a3948f3718257d4e",
      "bytes": 651
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "bd15c91f9495bc6b33ae71544ebc7e809d5fed26081f990debee5f3ea822fb0f",
      "bytes": 1502
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "54e4c875a7b7a699ca4fe5962f9b82720a9b8f50f13be318a147f97dfbe55520",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fc0e22f2ecc1764fc5c1138b0a3b209e3433397150cd10ac32975d9ae735310a",
      "bytes": 284483
    }
  ],
  "estimated_tokens": 9815
}
-->

# Durable State Update — Chapter 1076

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
1 and safe_through 1076. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1076. Profile updates may replace only one
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
  "chapter": 1076,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1076,
    "continuity_sources": [1076],
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
    "Taekyung’s group reunited with Cheongpung and the Slaughter Saint after several months.",
    "The Slaughter Saint and Cheongpung defeated the ten thousand monsters and stopped Dark Heaven’s pursuit over nearly two days.",
    "Taekyung’s group reached the lakeside with Gung Gibang’s group and brought a bound black-robed captive.",
    "Gung Gibang’s group has prepared a lakeside camp with fires and rations.",
    "The Slaughter Saint and Cheongpung secretly investigated Qinghai for about a month; they identified no spies but remain cautious.",
    "Cheongpung learned to conceal his presence from the Slaughter Saint.",
    "A strange presence surrounds Taiqing Hall; Taekyung suspects it is magical power."
  ],
  "continuity_sources": [
    1074,
    1075
  ],
  "open_questions": [
    "Who is the black-robed captive, and what does he know?",
    "What is the connection between Soonja and the Slaughter Saint?",
    "What does the Bow Saint mean by setting everything right?",
    "What happened to the Great Sir’s boy companion?",
    "What is the strange presence surrounding Taiqing Hall?"
  ],
  "safe_through": 1075,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 삼성     | **Three Saints**    |
| 곤륜파    | **Kunlun Sect**                  |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 청해     | **Qinghai**            |
| 화산     | **Huashan**            |
| 곤륜     | **Kunlun**             |
| 구화산    | **Mount Jiuhua**       |
| 노부      | **this old man / I**                                            |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 학우 | **Hak Woo** | Kunlun Sect top young prodigy known as the Kunlun Cloud Dragon; Taekyung addresses him as Hak. |
| 현천진인 | **Perfected Being Hyeoncheon** | Current Sect Leader of Wudang and Hyeongong's Senior Brother. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 곤륜운룡 | **Kunlun Cloud Dragon** | Epithet of a Kunlun Sect young prodigy. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 허공답보 | **Stepping on Empty Air** | Technique that allows Jongni Chu to move through empty air as if climbing invisible stairs. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 개방도 | **Beggars' Sect disciple** | Member of the Beggars' Sect. |
| 인자 | **ninja** | Japanese assassin skilled in concealment and concealed weapons. |
| 답보 | **stagnation** | Taekyung's current lack of progress in martial arts. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |
| 녕하 | **Ningxia** | Place name; origin of the mounted bandits mentioned by Sima Gong. |
| 청해호 | **Qinghai Lake** | Destination of the retreat; distinct source form from 청해성. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 살성 | 청풍 | senior martial figure to younger companion | you | blunt and familiar | The Slaughter Saint scolds Cheongpung for disappearing without a word. |
| 청풍 | 살성 | younger companion to senior martial figure | old man | polite and familiar | Cheongpung apologizes and explains why he wandered off. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1075
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has also learned concealment from the Slaughter Saint.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival, and the Slaughter Saint has become his mentor in concealment.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 1075
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun, and shares a blunt, teasing friendship with Taekyung.

### Hak Woo.md

# Hak Woo (학우)

- **Safe through:** Chapter 1067
- **Aliases:** Kunlun Cloud Dragon
- **Role:** Hak Woo is the Kunlun Sect's greatest young prodigy and is known as the Kunlun Cloud Dragon.
- **Personality:** He is wary, easily intimidated by threats to his hair, and eager to avoid unnecessary confrontation.
- **Voice:** He speaks politely and defensively, frequently using Daoist invocations.
- **Relationships:** Jin Taekyung is his former rival and can pressure him into leaving, while Ju Hwaran is an acquaintance he addresses formally.

### Hyeoncheon.md

# Perfected Being Hyeoncheon (현천진인)

- **Safe through:** Chapter 1074
- **Aliases:** None
- **Role:** Perfected Being Hyeoncheon is the current Sect Leader of the Kongtong Sect, a veteran Daoist master, and a Supreme Peak martial artist.
- **Personality:** Grave and reflective, he bears the losses of the Great Faction War yet rejects punishing the innocent for their relatives’ crimes.
- **Voice:** Measured, solemn, and calm with the authority of a Sect Leader.
- **Relationships:** Hyeongong is his Junior Brother, and both studied under the same master from childhood.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1075
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1074
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
1076화




그곳의 강물은 푸르렀고, 바다만큼이나 넓었다.

아마도 그래서였을 것이다.

누구도 기억하지 못한 아득한 과거부터 기나긴 시간의 흐름을 따라 크기를 넓혀 가던 이름 없는 담수호가 어느 날부터인가 청해호(靑海湖)라 불리게 된 것은.

그리고 지금 이 순간, 바로 그 청해호의 푸른 강물을 가로지르는 그림자가 있었다.

촤아악.

일사불란하면서도 부드럽게 강물을 밀어내는 십여 자루의 노.

잔잔한 파문을 일으키며 나아가는 그 움직임에 따라, 자욱하게 맺혀 있던 물안개가 흩어지며 그 안에 감추어 두었던 그림자의 실체를 드러냈다.

유선형의 날렵한 곡선.

그리 크지는 않지만, 단단한 나무와 강철로 보강된 몸통.

그리고 바람을 받아 한껏 부푼 돛과, 발을 디딜 엄두조차 나지 않는 그 비좁은 돛대 위에 평온하게 가부좌(跏趺坐)를 틀고 앉은 한 노인까지.

“순풍(順風)이로구나. 더할 나위 없는.”

머리 위에서 들려오는 늙수그레한 목소리에, 뱃머리에 우뚝 선 채로 안개 너머를 주시하고 있던 중년인이 대답했다.

“앞으로의 일 또한 그럴 것입니다.”

“이미 본산(本山)을 빼앗겼는데도?”

“빼앗긴 것이 아니라, 귀한 목숨들을 지키고자 내준 것이지요.”

중년인이 우직한 음성으로 말을 이었다.

“제가 존경하는 어느 분께서 그런 말씀을 하셨습니다. 중요한 것은 집이 아니라 사람이라고. 누구도 살지 않는 집은 버려진 폐가가 되지만, 사람이 있다면 텅 빈 허허벌판에도 궁전을 세울 수 있다고 말입니다.”

“네게 그 말을 한 자가 누구인지는 모르겠으나, 겉만 그럴듯하고 실속 없는 늙은이가 분명하구나.”

“스, 스승님. 어찌 그런 말씀을. 저는 절대 그런 뜻으로…….”

“허허, 안다. 농이니라.”

허둥지둥하는 제자의 모습에, 스스로를 실속 없는 늙은이라 칭한 노인이 빙긋 웃으며 말을 이었다.

“앞으로의 일 또한 순풍처럼 흘러갈 것이라…… 그럴 수만 있다면 바랄 것이 없겠다만, 앞서 불어온 역풍(逆風)이 저리 거세니 어찌할꼬.”

스승의 짓궂은 농담에 고개를 절레절레 내젓던 중년인이 힘 있는 목소리로 대답했다.

“그깟 바람이 제아무리 거세다 한들, 배가 아닌 산을 뒤집을 수는 없는 노릇이지요.”

“네 말이 옳다. 하지만 그 거센 바람에 불씨가 섞여 있다면 어찌하겠느냐?”

“……!”

“우리가 두려워해야 하는 것은 바람이 아니다. 누구도 모르는 깊은 산기슭 어딘가에 숨어, 이내 모든 것을 잿더미로 만들어버릴지도 모르는 작은 불씨 하나다.”

잠시 노인의 말에 담긴 의미를 되새기던 중년인이, 불현듯 얼굴을 굳혔다.

- 스승님. 그 말씀은 혹시…….

어느덧 파르르 떨리는 입술 사이로 흘러나온 한 줄기의 전음(傳音).

그러나 중년인이 그 물음에 대한 답을 듣기도 전, 천천히 몸을 일으킨 노인이 문득 중얼거렸다.

“그럼에도, 맞불을 놓을 기회는 있겠지.”

그 순간.

화아악.

산산이 흩어지는 물안개 너머, 청해호의 강가를 따라 늘어선 수백여 개의 모닥불이 노인의 회백색 눈동자에 담겼다.

바람에 실려 흩날리는 그 불씨들은, 재앙과 맞설 희망의 불씨였다.



* * *



날렵한 형태를 지닌 한 척의 선박이 안개 너머에서 모습을 드러낸 순간, 나는 곧장 저들의 정체를 깨달을 수 있었다.

정확히는, 높게 솟은 돛대 위에서 강가를 굽어보고 있던 어느 노인의 정체를.

쉭.

날개처럼 좌우로 갈라져 펄럭이는 도포 자락.

한 마리의 비조(飛鳥)처럼 높이 솟구친 노인의 신형이 자그마치 수십여 장의 허공을 가로질러 떨어져 내리는 광경에, 곳곳에서 탄성이 터져 나왔다.

“저, 저건.”

“허공답보(虛空踏步)……!”

허공답보란 수 갑자의 공력과 깊은 깨달음이 있어야 펼칠 수 있는 최상승의 경공술.

불과 이틀 전까지 듣도 보도 못한 괴물들과 혈전을 벌인 그들이었지만, 그렇다고 상승 무학에 대한 놀라움이 사라지지는 않았다.

그것과는 별개로, 내 생각은 저들과는 조금 달랐지만.

“허, 대단한 수준의 허공답보로군. 네 녀석이 보기에도 그렇지 않느냐?”

슬쩍 떠보는 듯한 적천강의 물음에, 내가 작게 혀를 찼다.

“아니, 제가 바보로 보이십니까?”

“그 무슨 싸가지 밥 말아 먹은 소리냐.”

“이미 아시잖아요. 무슨 얘긴지.”

“……흠. 영 개눈깔은 아니로구나.”

장단을 맞춰 주지 않는 것에 대해 못마땅한 건지, 아니면 내가 이룬 성취에 기쁜 건지 모를 표정으로 중얼거린 적천강이 허공을 응시했다.

“하여간, 경공술 하나만큼은 제법이란 말이지.”

나는 피식 실소를 흘렸다.

적천강의 평소 화법을 생각한다면 엄청난 극찬이지만, 그조차도 지금 이 순간 천천히 지상을 향해 내려오는 저 노인의 경공술에 비하면 부족함이 있었으니까.

‘능공허도(凌空虛道)보고 제법이라 하면, 경공술 익힌 무림인들은 전부 혀 깨물고 죽어야지.’

하늘 위에는 또 다른 하늘이 있는 법.

무학(武學)의 깊이가 얕거나 무림에 몸담지 않은 이들은 허공답보를 최고로 치지만, 그 위에는 능공허도가 있다.

허공을 밟거나 박차는 것이 아니라, 미끄러지듯 자연스럽게 이동할 수 있는 극상의 경지.

그것이 바로 능공허도였다. 나를 포함한 몇몇 극소수의 초절정 고수들만이 알아볼 수 있는 그 차이가 노인의 발끝에서 보였다.

‘그리고 능공허도의 경지에 오른 사람은, 지난 일백여 년을 통틀어 단 두 사람뿐.’

구화산에 머무르며 수련하던 시절, 적천강의 입을 통해 들은 바가 있었다.

그중 한 명은 끝내 신(神)이라 불리게 되었고, 또 다른 한 명은 자신이 있어야 할 곳으로 돌아갔다고.

머나먼 서쪽 너머의 땅, 그곳의 하늘과 맞닿은 거대한 산자락으로.

스륵.

마침내 소리 없이 땅에 닿은 발끝과 서서히 가라앉는 도포 자락.

그와 동시에, 인자한 인상을 지닌 노인이 모두를 향해 포권을 취했다.

“곤륜(崑崙)의 청허자(淸虛子), 여러 도우들께 인사 올리오.”

“……!”

“……!”

보이지 않는 감정의 파동이 주변을 휩쓸었다.

실로 놀라운 경공술을 보이며 갑작스럽게 나타난 노인의 정체가, 다름 아닌 곤륜파의 장문인(掌門人)이라는 사실에서 것에서 느끼는 충격이었다.

“자, 장문인을 뵙습니다!”

곳곳에서 터져 나오는 다급한 외침과 포권지례.

그러나 늘 그렇듯이 예외는 있었다.

“도우는 개뿔이, 나이 좀 먹었다고 이제 노부와 맞먹으려 드느냐?”

무림판 주임원사이자, 명문대파 담당 일진의 퉁명스러운 인사는 당연한 시작에 불과했다.

“오랜만이네요, 청허. 못 본 사이에 당신도 흰머리가 많이 늘었군요. 마지막으로 보았을 때는 그래도 제법 젊어 보였는데.”

그나마 배운 집안 출신이라고 존댓말이라도 써 주는 활잡이 누님의 어깨너머로, 사람 써는 기술 하나만으로 고금제일이 된 인간 도살자가 불현듯 모습을 드러냈다.

“누군가 했더니, 구면이로군. 결국 장문인까지 됐나?”

“…….”

“…….”

곤륜파 장문인의 등장으로 시끄러웠던 분위기가 삽시간에 고요해졌다.

살성과 궁성, 화왕 적천강까지.

보기만 해도 숨이 턱 막히는 미친 라인업이 아닐 수 없다.

제각각 중년, 장년, 소년의 모습을 하고 있지만 저들이 먹은 무림 짬밥으로만 오병이어의 기적을 일으킬 수 있을 정도니까.

하지만 청허자의 고난은 그것으로 끝이 아니었다.

“음. 빈도의 인사가 늦었구려. 그간 어찌 지냈…….”

짬킹들의 등장에 잠시 머뭇거리던 공동파 장문인, 현천진인이 간신히 말문을 연 그때였다.

“안녕하세요, 청허자 할아버지. 저는 청풍이라고 해요! 같은 청씨니까 앞으로 잘 부탁드려요!”

“본녀는 숙자라 하오. 같은 청씨는 아니지만 끝에 한 글자가 겹치니 그럭저럭 지내 봅시다.”

“태산이, 배고프다. 혹시 오는 길에 고기 잡은 것 없나?”

다른 의미로의 미친 라인업.

그야말로 진짜 광기.

삼성에 버금가는 개노답 삼형제의 등장에 나는 눈앞이 아득해지는 것을 느꼈지만, 청허자는 놀랍게도 허허 웃으며 입을 열었다.

“존경하는 선배님들도, 처음 보는 후배님들도 계시는구려. 다시 한번 모두 반갑소.”

그 순간, 나는 생각했다.

어쩌면 천하제일의 문파는 곤륜파가 아닐까, 하고.

“……와, 이걸 참네.”

반사적으로 입술을 비집고 흘러나온 탄성에, 청허자의 시선이 나를 향해 움직였다.

“이렇게 가까이에서 보는 건 처음이로군. 반갑네, 진 도우.”

지금 청허자가 말했듯이 나는 그를 멀리서나마 마주한 적이 있었다.

굳이 말하자면, 단순히 일면식이 있다 하기엔 조금 깊은 인연일지도 모른다.

성라대연이 한창 진행되던 당시, 한동안 궁기방 등과 함께 어울려 다니던 곤륜운룡(崑崙雲龍) 학우가 바로 청허자의 제자이기도 했으니.

“장문인을 뵙습니다.”

뒤늦게 예의를 갖추어 포권을 취하자, 청허자가 사람 좋은 미소와 함께 고개를 끄덕였다.

“오랜만일세. 도우에 관한 이야기는 그 이후로도 많이 들었네. 학우, 그 아이가 특히나 좋아하더군.”

“그, 혹시…….”

말꼬리를 흐리는 내 마음을 꿰뚫어 본 것처럼, 청허자가 부드러운 어조로 입을 열었다.

“별 탈 없이 잘 지내고 있으니 걱정할 필요 없네.”

“다행입니다.”

학우와 교분을 쌓은 시간이 결코 길다고는 할 수 없지만, 내가 아는 녀석은 충분히 괜찮은 놈이었다.

무림인으로서도, 인간으로서도.

그래서 다음 순간 청허자가 덧붙인 한마디에는 퍽 반가운 마음마저 들었다.

“곧 만나게 될 걸세. 우선은 이곳을 벗어난 후에.”

“그렇군요.”

청해호가 아군의 본거지가 아니라는 사실쯤은 이미 알고 있었다.

궁기방과 개방도들은 단순히 앞서 마중을 나온 것뿐, 아직 암천의 위협은 완전히 사라지지 않았으니까.

다만 청허자의 말을 듣고 떠오른 한 가지 의문이 있다면…….

“그런 것치고는 배가 좀, 음. 많이 작은 것 같은데요.”

나는 떨떠름한 시선으로 강가에 거의 도달한 선박을 바라보았다.

기껏해야 일백여 명은 수용할 수 있을까 싶은 크기의 선박은, 삼천여 명이나 되는 아군을 태우기에 턱없이 부족해 보였다.

“도우의 눈에도 그래 보이나?”

“죄송하지만, 그렇습니다.”

“허허.”

내 솔직한 대답에 소리 내어 웃은 청허자가, 재차 입을 열었다.

“그리 생각할 수도 있겠지. 지금 보이는 바로는.”

“예?”

“아, 이제야 오는군.”

청허자의 시선을 따라 고개를 돌린 나는, 아니 모두는 볼 수 있었다.

촤아악.

이제야 짙은 안개를 해치며 모습을 드러낸, 수십여 척의 선박들을.
```

## Final English reading copy

```markdown
# Chapter 1076

The river there was blue, and as wide as the sea.

Perhaps that was why.

From some distant past no one remembered, an unnamed freshwater lake had grown larger over the long passage of time. And one day, people began calling it Qinghai Lake.

At this very moment, a shadow was crossing the blue waters of Qinghai Lake.

*Shhhhhh.*

A dozen or so oars pushed the water in perfect, graceful unison.

Their movement sent gentle ripples across the surface, scattering the thick mist and revealing the shadow it had concealed.

A sleek, streamlined shape.

Not especially large, but built of sturdy wood and reinforced with steel.

A sail swollen with wind—and, perched cross-legged in perfect calm atop the narrow mast, where no one would even dare set foot, an old man.

“What a tailwind. Couldn’t ask for better.”

At the old man’s voice overhead, the middle-aged man standing tall at the bow, gazing beyond the mist, answered.

“The days ahead will be the same.”

“Even though we’ve already lost our sect’s headquarters?”

“We didn’t lose it. We gave it up to save precious lives.”

The middle-aged man continued in a steadfast voice.

“A person I respect once told me that what matters is not the house, but the people. A house where no one lives becomes an abandoned ruin. But if there are people, they can build a palace even in an empty field.”

“I don’t know who told you that, but he must be an old man who sounds impressive and has nothing to show for it.”

“M-Master. How could you say that? I didn’t mean—”

“Ha ha. I know. I’m teasing.”

The old man, who had just called himself all talk and no substance, smiled at his flustered Disciple and went on.

“So the days ahead will carry us along like a tailwind… I’d wish for nothing more, if only that were possible. But the headwind that came before was so fierce. What are we to do?”

The middle-aged man shook his head at his Master’s mischievous joke, then answered in a strong voice.

“No matter how fierce the wind is, it can’t overturn a mountain instead of a ship.”

“You’re right. But what if that fierce wind carries embers?”

“……!”

“The wind isn’t what we should fear. It’s a single ember, hidden somewhere deep in the mountains where no one knows, that might soon turn everything to ash.”

The middle-aged man considered the meaning of the old man’s words. Then his expression suddenly tightened.

*Master. Do you mean…?*

A single line of Sound Transmission slipped between his trembling lips.

But before he could hear the answer, the old man slowly rose and murmured:

“Even so, there should be a chance to fight fire with fire.”

At that moment—

*Whoosh.*

Beyond the mist as it scattered in all directions, hundreds of campfires lined the banks of Qinghai Lake, reflected in the old man’s gray-white eyes.

Those sparks, carried away by the wind, were sparks of hope that could stand against disaster.



* * *



The moment a sleek ship appeared through the mist, I knew who they were.

Or, more precisely, I knew who the old man was, gazing down at the shore from atop the towering mast.

*Whoosh.*

The hem of his robe flapped, splitting to either side like wings.

The old man soared like a bird, crossed dozens of jang through the air, and descended. Exclamations rose from all around us.

“Th-that’s…”

“Stepping on Empty Air…!”

Stepping on Empty Air was the highest form of lightness skill, one that required several jiazi of internal energy and deep enlightenment.

These people had fought a desperate battle against monsters they’d never seen or heard of until two days ago. But that hadn’t made them any less awed by the highest martial arts.

My thoughts, however, were a little different.

“Now that’s a remarkable display of Stepping on Empty Air. Don’t you think so, too?”

At Jeok Cheongang’s probing question, I clicked my tongue softly.

“Do I look like an idiot to you?”

“What kind of rude thing is that to say?”

“You already know what I mean.”

“……Hm. So you’re not completely blind, after all.”

I couldn’t tell whether he was displeased that I hadn’t played along or pleased by the progress I’d made. Jeok Cheongang murmured and gazed into the air.

“Still, when it comes to lightness skills, he’s pretty good.”

I let out a quiet laugh.

Considering how Jeok Cheongang usually spoke, that was high praise. But even that fell short of the old man’s lightness skill as he slowly descended toward the ground.

*If you call Gliding Across the Void “pretty good,” every martial artist who’s learned a lightness skill should bite their tongue and die.*

There’s always another sky above the sky.

Those with shallow martial arts or no place in Murim considered Stepping on Empty Air the pinnacle. But there was a realm beyond it.

Not stepping on or kicking off the air, but moving through it as naturally as if gliding. That was Gliding Across the Void. Only a handful of Supreme Peak masters, myself included, could recognize the difference. I could see it in the old man’s feet.

*And in the past hundred years, only two people have reached the realm of Gliding Across the Void.*

I’d heard as much from Jeok Cheongang when I was training on Mount Jiuhua.

One of them had eventually come to be called a god. The other had returned to where he belonged.

To a land far to the west, to the vast slopes of a mountain that touched the sky.

*Swish.*

At last, his toes touched the ground without a sound, and his robes settled around him.

At the same time, the kindly-looking old man brought his hands together in greeting to everyone.

“I am Cheongheoja of the Kunlun Sect. My greetings to all my fellow Daoists.”

“……!”

“……!”

An invisible wave of emotion swept through the crowd.

The shock came from the identity of the old man who had appeared so suddenly with such astonishing skill: he was none other than the Sect Leader of the Kunlun Sect.

“W-We greet the Sect Leader!”

Urgent cries and formal bows erupted all around.

But, as always, there were exceptions.

“Fellow Daoist, my ass. You’ve gotten older and now you think you can treat this old man as an equal?”

The curt greeting from Murim’s veteran drill sergeant and the bane of every prestigious sect was only the beginning.

“It’s been a long time, Cheongheo. You’ve got a lot more gray hair now. The last time I saw you, you still looked pretty young.”

Over the shoulder of the bow-wielding lady, who was at least from a respectable family and had bothered to use polite speech, a human butcher appeared—the man who’d become the greatest of all time through his skill at cutting people down.

“Who would’ve thought? We’ve met before. You ended up becoming Sect Leader, then?”

“……”

“……”

The noisy atmosphere from the Kunlun Sect Leader’s arrival fell quiet in an instant.

The Slaughter Saint, the Bow Saint, and the Fire King Jeok Cheongang.

What an insane lineup. Just looking at them was enough to take your breath away.

They might look middle-aged, mature, and boyish, respectively, but with the amount of time they’d spent in Murim, they could perform the miracle of feeding five thousand with five loaves and two fish.

But Cheongheoja’s ordeal wasn’t over.

“Mm. This humble monk’s greeting is overdue. How have you been all this time—”

Perfected Being Hyeoncheon, the Sect Leader of the Kongtong Sect, had hesitated at the arrival of the old hands. He had just managed to get the words out when—

“Hello, Grandpa Cheongheoja. I’m Cheongpung! We both have the surname Cheong, so I hope we get along from now on!”

“I am Soonja. We don’t share a surname, but our names have the same last syllable, so let’s get along well enough.”

“Taishan hungry. Did you catch any meat on your way here?”

A different kind of insane lineup.

Pure, unfiltered madness.

The appearance of the hopeless trio, every bit as disastrous as the Three Saints, made my eyes glaze over. Yet, to my surprise, Cheongheoja chuckled and spoke.

“Some respected Seniors, and some juniors I’m meeting for the first time. It’s a pleasure to meet you all again.”

At that moment, I had a thought.

Maybe the greatest sect under heaven was the Kunlun Sect.

“……Wow. He can actually put up with all that.”

The exclamation slipped from my lips before I could stop it, and Cheongheoja turned his gaze toward me.

“This is the first time we’ve met this close. It’s good to meet you, Fellow Daoist Jin.”

As Cheongheoja had just said, I’d seen him before, if only from a distance.

In fact, you could say my connection to him was a little more than a passing acquaintance.

During the Star-Array Grand Banquet, Hak Woo, the Kunlun Cloud Dragon, had spent some time hanging around with Gung Gibang and the others. He was Cheongheoja’s Disciple.

“I greet the Sect Leader.”

I belatedly brought my hands together in a formal bow. Cheongheoja nodded with a warm smile.

“It’s been a long time. I’ve heard a great deal about you since then. That boy Hak Woo was especially fond of you.”

“Um, by any chance…”

As if he’d seen through the question I couldn’t quite bring myself to finish, Cheongheoja spoke gently.

“He’s doing well. You needn’t worry.”

“That’s a relief.”

I couldn’t say I’d known Hak Woo for long, but the guy I knew was a good one.

As a martial artist, and as a person.

So when Cheongheoja added one more thing, I was glad to hear it.

“You’ll see him soon. Once we’ve left this place, at least.”

“I see.”

I already knew Qinghai Lake wasn’t our home base.

Gung Gibang and the Beggars’ Sect disciples had simply come ahead to meet us. The threat from Dark Heaven hadn’t disappeared completely.

But Cheongheoja’s words did raise one question…

“Even so, the boat seems a little, well… pretty small.”

I looked dubiously at the ship, which had nearly reached the shore.

It looked like it could hold a hundred people at most—nowhere near enough to carry our three thousand allies.

“Does it look that way to you, too?”

“Sorry, but yes.”

“Ha ha.”

Cheongheoja laughed aloud at my honest answer, then spoke again.

“I suppose it might look that way. From what you can see now.”

“Pardon?”

“Ah, they’re finally here.”

Following Cheongheoja’s gaze, I turned. Or rather, we all did.

*Shhhhh.*

Only then did we see dozens of ships emerge through the thick mist.
```
