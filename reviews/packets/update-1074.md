<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1074.txt",
      "sha256": "b8602551ef8977078a09e683f865f2b3305eb68f0d41b8b93e7ac5e8a97b7b59",
      "bytes": 12059
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f08fffd26277354fc8856119eebfcebcdc6a7927e36b9f7784f1b91fc25a9b82",
      "bytes": 1005
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "efe98ef7fd8c5b9f438a6ab4366afd9557f378570652aa43b8a3112875fe65f2",
      "bytes": 242481
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "2bd303ec3212030a25f252b5e4ce373e26ef31bccfc5ff9ba8db894e0b603bcc",
      "bytes": 1326
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "fb9c03d7878e2735d8fe31bfa75911f948dee0262ec353f87dedb66b2904ac12",
      "bytes": 687
    },
    {
      "path": "characters/Hyeoncheon.md",
      "sha256": "46971f329fed51bd648aa268ba0ab4a0b92f7cd940de014da7113386ffbe6f3b",
      "bytes": 651
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "06976ac22bbe4429503d04dd99bb12981c5a0883397493327cf66fb7cb8ccac4",
      "bytes": 1375
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "8096feaa3fee7a5896a27957ca3354a29e84d9dd1991e2c463da65be7f4efc14",
      "bytes": 1502
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "9cf565f6583041d0bf143e026759172e72fbe67f5d2ee649da43aaa707838b6b",
      "bytes": 700
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "cce33fc8ebdb554d2030d1b9f7718ee2ef7ce922d97143634828edf78cb9ea36",
      "bytes": 700
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "75c6b4ec81631ec4d606552e537243929556d64d4d1662f21b62900eca2830db",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7df8b2357d0faa08e63a571debd66c331206f8c9af0b11d116826f4c7dad2ad4",
      "bytes": 284375
    }
  ],
  "estimated_tokens": 11001
}
-->

# Durable State Update — Chapter 1074

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
1 and safe_through 1074. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1074. Profile updates may replace only one
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
  "chapter": 1074,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1074,
    "continuity_sources": [1074],
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
    "Taekyung’s force was surrounded by ten thousand monsters; the monsters all collapsed after the Great Sir appeared, for an unknown reason.",
    "The Great Sir calls himself Gaettong and says the monsters should obey Chunja’s command; he refers to himself as Chunja after changing his name and gender.",
    "A boy and Cheongpung are nearby; Taekyung recognizes Cheongpung’s voice."
  ],
  "continuity_sources": [
    1072,
    1073
  ],
  "open_questions": [
    "Who are the Great Sir and the boy, and what is their connection to the intruder and his Little Grandpa?",
    "What caused the monsters to collapse, and can they rise again?",
    "Who is directing the monsters, and what became of the sorcerers?",
    "Will Dark Heaven’s pursuit continue after the monsters’ collapse?",
    "Who is Great Sir, and what is his connection to Hyeoncheon and the surviving Kongtong Disciples?"
  ],
  "safe_through": 1073,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 은인     | **Benefactor**                               |
| 화산     | **Huashan**            |
| 소협      | **Young Hero**                                                  |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 현천진인 | **Perfected Being Hyeoncheon** | Current Sect Leader of Wudang and Hyeongong's Senior Brother. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 천호 | **Thousand Captain** | Rank held by Jeong Hogun in the Embroidered Uniform Guard. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |
| 녕하 | **Ningxia** | Place name; origin of the mounted bandits mentioned by Sima Gong. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 아주머니 | childhood_benefactor_to_former_child | Auntie | deferential-polite | Mujin respectfully addresses the local snack-stall vendor who secretly gave him candied hawthorn when he was a child. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 정호군 | 태산 | guard officer questioning a performer | you | blunt and direct | He calls Taishan forward and asks whether he belongs to the circus troupe. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 살성 | 청풍 | senior martial figure to younger companion | you | blunt and familiar | The Slaughter Saint scolds Cheongpung for disappearing without a word. |
| 청풍 | 살성 | younger companion to senior martial figure | old man | polite and familiar | Cheongpung apologizes and explains why he wandered off. |
| 태산 | 대인 | ally addressing an elder | Sir | informal and enthusiastic | Calls out to the Great Sir while praising his shot. |
| 대인 | 태산 | elder addressing a younger ally | young friend | familiar and playful | Offers Taishan a portion of the bird as a reward. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1073
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 1060
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Hyeoncheon.md

# Perfected Being Hyeoncheon (현천진인)

- **Safe through:** Chapter 1071
- **Aliases:** None
- **Role:** Perfected Being Hyeoncheon is the current Sect Leader of the Kongtong Sect, a veteran Daoist master, and a Supreme Peak martial artist.
- **Personality:** Grave and reflective, he bears the losses of the Great Faction War yet rejects punishing the innocent for their relatives’ crimes.
- **Voice:** Measured, solemn, and calm with the authority of a Sect Leader.
- **Relationships:** Hyeongong is his Junior Brother, and both studied under the same master from childhood.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1071
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1073
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 1071
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard and honors Jin Taekyung as a comrade-in-arms after their shared battle.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 1071
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1067
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
1074화




그런 말이 있다.

회자정리(會者定離), 거자필반(去者必返).

모든 만남에는 헤어짐이 있고, 떠남이 있으면 반드시 돌아옴이 있다고.

그리고 지금 이 순간, 나는 그 오래된 격언을 떠올리며 크게 뜨인 눈으로 바라보고 있었다.

사방에 내려앉은 어둠과 널브러진 괴물들 사이를 비집고, 저 멀리서 이곳을 향해 다가오는 두 사람의 모습을.

“여기요! 여기 우리 왔어요!”

“그렇게 소리 지르지 말라고 도대체 몇 번을 말하…… 아니다. 그냥 네놈 멋대로 해라.”

“네! 감사합니다!”

“정말 미쳐 버리겠군.”

발바닥에 스프링이라도 달았는지 폴짝폴짝 뛰는 청년과 그런 모습에 노인네처럼 한숨을 푹 내쉬는 소년의 모습은, 누군가에게 있어 퍽 희한한 광경일지도 모른다.

하지만 나는, 아니 나를 포함한 극소수의 인물들은 이미 저 두 사람의 정체를 알고 있었다.

그중에서도 특히 앞에서 신나게 뛰어오는 청년은. 단 한 번만 보았다 해도 도무지 잊을래야 잊을 수 없는 텐션의 소유자였으니까.

“……청풍?”

나도 모르게 입술을 비집고 흘러나온 그 두 글자에, 앞서 괴물들에게 벌어진 이변으로 멍하니 굳어 있던 사람들이 눈을 깜빡였다.

“청풍이라면 혹시.”

“화, 화산신룡(華山神龍)?”

반응은 즉각적이었다.

내가 곧장 알아볼 정도로 교분이 있는 동시에, 지금 같은 상황에서 나타날 청풍은 온 천하를 거꾸로 뒤집어 탈탈 털어도 한 사람뿐이었으니까.

물론, 타당한 의문을 제기하는 이 또한 있었다.

“전 멀어서 안 보이는데요. 혹시 조장님께서 착각하신 거 아닙니까? 청풍 소협이 왜 갑자기 여기에 나타…….”

혁무진이 어울리지 않게 신중한 어조로 말문을 연 그때, 캄캄한 어둠 너머로 맑은 목소리가 울려 퍼졌다.

“은이이이인!”

“……맞네.”

“……맞네요.”

“……듣자마자 정신이 혼미해지는군. 그놈이 확실하다.”

이 정도면 거의 지문이 아닐까 싶을 정도.

나와 혁무진, 뒤이어 적천강을 끝으로 모든 확인 절차가 마무리된 그때였다.

“은인! 저 왔어요!”

마지막 쐐기를 박는 외침과 함께, 한 줄기의 바람처럼 들이닥친 청풍이 상기된 얼굴로 내게 손을 흔들었다.

“와, 정말 오랜만이에요! 그동안 잘 지내셨어요?”

도대체 이걸 어떻게 반응해야 하는 걸까.

나는 잠시 당혹감과 반가움이 반반 섞인 채로 멍하니 눈앞의 첫 경험 빌런을 바라보다가, 이내 간신히 입을 열었다.

“아니, 전혀.”

“오. 사실 그래 보이긴 해요.”

“그럼 왜 물어봤어?”

“저는 그동안 잘 못 지냈거든요. 하지만 은인은 좀 다르길 바랐어요, 헤헤.”

우울한 말도 해맑게 이어 가는 청풍의 모습에, 나는 지금 이 순간 내가 어떤 반응을 보여야 할지 깨달았다.

정확히는, 나도 모르게 저절로 실소가 터져 나왔다.

“어라, 왜 웃으세요?”

“그딴 걸 질문이라고 하느냐? 네놈 하는 꼬락서니를 보니 어이가 없어서 웃는 거겠지.”

이건 내가 한 대답이 아니다.

슥.

흡사 유령과도 같은 인기척으로 어둠 속에서 모습을 드러낸 소년, 아니 고금제일의 살수가 나를 똑바로 응시하며 덧붙였다.

“물론, 그러는 저 녀석도 만만치 않은 천둥벌거숭이지만.”

언제나 그렇듯 무뚝뚝한 어조.

그러나 그의 입가에 걸린 흐릿한 미소를 본 나는, 대답 대신 소리 내어 웃을 수밖에 없었다.

수개월 만의 조우(遭遇)였다.



* * *



보고 싶었던 이들과의 만남은 언제나 기쁘고 즐겁다.

하지만 우리 중 그 누구도, 현재와 같은 상황에서 모닥불 앞에 앉아 도란도란 이야기꽃을 피울 정도로 멍청하지는 않았다.

“우선 속히 이곳을 빠져나가는 것이 좋겠지. 따라오거라.”

해후(邂逅)의 여운이 완전히 가시기도 전, 언제 그랬냐는 듯 입가의 미소를 지운 살성은 즉각 움직였다.

“조금이라도 짐이 될 만한 것들은 지금 당장 버려라. 특히 거기 있는 얼간이.”

살성에게 지목당한 얼간이, 아니 정호군이 대답했다.

“어느 고인(古人)이신지는 모르나 최소한의 예의를 지키시오. 나는 지엄하신 황제 폐하의 명을 받드는 금의위 천호…….”

쉭.

그야말로 순식간이었다.

살성의 신형이 순간 흐릿해진 것도.

그리고 뒤이어 들려온 바람 소리와 함께, 정호군의 목덜미에 시퍼런 소도(小刀)가 맞닿은 것도.

“계속 지껄여 보거라. 촌각이라도 더 시간을 지체시켰다가는 진짜 고인으로 만들어 줄 테니.”

황제를 향한 정호군과 휘하 금의위들의 충성심은 나를 포함한 모두가 인정할 만큼 대단하다.

그러나 현실은 냉혹한 법.

머나먼 어딘가에 있을 황제와 달리, 너무나도 가까이에 있는 소도를 물끄러미 바라보던 정호군이 무거운 얼굴로 입술을 뗐다.

“앞서 말했듯 본관은 지엄하신 황제 폐하의 명을 받드는 금의위 천호……지만 귀하는 여기 계신 상산후와 짙은 친분이 있어 보이니 참도록 하겠소.”

금의위치고는 심히 추한 변명에, 살성이 건조한 어조로 대답했다.

“그렇게까지 친하지는 않은데.”

“어느 정도 일면식이 있어 보이니 참겠소.”

“당연히 일면식이야 있지만, 친하지 않다니까.”

“…….”

“그냥 참아라. 알겠나?”

“…….”

“대답한 것으로 알지.”

강호의 도리로 마지막 자존심을 지켜 준 살성이 소도를 거두었을 때는, 삼천여 명의 아군 대부분이 경악에 가득 찬 눈빛으로 그를 바라보고 있었다.

아무리 높게 쳐줘도 약관에 못 미치는 소년이 절정의 끝자락에 이른 금의위 천호를 제압했다.

그것도 눈에 보이지 않을 만큼 빠른 속도로, 단숨에.

눈 앞에 펼쳐진 그 믿을 수 없는 광경에 모두가 놀랐지만, 그중에서도 특히 현천진인이 느낀 충격은 생각 이상인 듯했다.

“도우는…… 도대체 누구요?”

서 있는 위치에 따라 보이는 풍경도 변하는 법.

이미 숙련된 초절정 고수인 현천진인은 살성의 진정한 경지를 어렴풋이나마 유추할 수 있는 실력자였고, 의문과 충격에 휩싸여 쉽사리 말을 잇지 못하는 그를 대신해 궁성이 입을 열었다.

“오랜만이네요. 당신을 이렇게 다시 만나게 될 줄이야.”

궁성과 마찬가지로 상대의 정체를 꿰뚫어 본 살성이 쓴웃음을 지으며 대꾸했다.

“이하동문이오. 그날 이후 두 번 다시 만날 일이 없으리라 생각했거늘.”

“강산이 변하고, 세상 역시 변했지요. 모든 것을 되돌리기 위해서는 나서야 했어요.”

주고받는 대화에 더욱더 의문이 깊어지는 주위의 시선 속, 궁성이 나직이 덧붙였다.

“살성(殺星), 당신이 그랬듯이.”

“……!”

“……!”

“……!”

일순간, 주위의 공기가 찌르르 울렸다.

살성.

한때는 온 천하가 손가락질하던 지탄의 대상이었으나, 정마 대전의 발발 이후 숱한 대마두(大魔頭)를 두려움에 떨게 만든 고금제일의 살수.

모든 이들에게 현재의 상황을 온전히 설명하고 납득시키기에는, 그 두 글자만으로도 충분했다.

그리고 그런 궁성을 향해 작게 고개를 끄덕여 보인 살성은, 석상처럼 굳어 버린 사람들을 향해 입술을 뗐다.

“그래서, 이 귀한 시간을 낭비하고 싶은 얼간이가 또 있나?”

물론, 있을 리가 없었다.

정확히는 있더라도 없어야 했다.

적어도 저 질문을 한 이의 별호가 살성이라면.

철컹, 투두둑!

정호군을 비롯한 금의위들이 이제 막 동원 훈련을 끝내고 집에 돌아온 예비군처럼 신속하게 갑옷을 벗어 던지던 그때, 살성의 눈매가 불현듯 가늘어졌다.

“그런데, 저건 도대체 뭐 하는 물건이지?”

살성의 시선을 따라 고개를 돌린 나는, 대번에 그 말에 담긴 뜻을 깨달을 수 있었다.

그가 사지 멀쩡한 인간을 왜 물건이라고 지칭했는지도.

“뭐랄까, 그, 저 양반이 정신이 좀 오락가락합니다.”

“……그건 이미 충분히 느끼고 있다.”

어느샌가 금의위들 사이에 자연스럽게 녹아든 채, 상하의를 신나게 벗어 재끼는 대인을 흐린 눈으로 바라보던 살성이 한숨을 내쉬었다.

“자세한 상황은 들어 봐야 알겠지만, 미친놈이 하나 더 추가된 건 확실해 보이는군.”

물론 기존의 미친놈은, 새롭게 굴러 들어온 미친놈의 육체미 대소동을 바로 옆에서 직관하며 감탄하고 있었다.

“와! 이렇게 과감하게 탈의하는 사람 처음 봐요!”

막 속옷을 벗으려다 정호군에 의해 제지당한 대인이 청풍을 발견하고 눈을 빛냈다.

“칭찬 고맙네. 한데 자네는 누구인가?”

“안녕하세요! 저는 청풍이라고 해요!”

“씩씩하니 보기가 좋구먼. 본녀는 순자라고 하네.”

“잘 부탁드립니다. 아주머니!”

아니.

진짜 미친 새끼들인가.

백 년에 한 번도 있어서는 안 되는 두 천재지변의 만남에 모두가 아연질색한 그때, 고개를 절레절레 내저은 살성이 입을 열었다.

“자, 이제 출발하도록 하지.”

그리고 그런 살성의 손아귀에는, 저 멀리까지 이어진 웬 밧줄 하나가 들려 있었다.

“그건 뭡니까?”

“전리품.”



* * *



결론부터 말하자면, 이후 이어지는 적들의 추격은 없었다.

아니, 있었는데 없었다고 하는 것이 더욱 옳은 표현일지도 모른다.

“먼저 가거라. 금방 뒤따라 갈 테니.”

살성은 그런 말과 함께 몇 번에 걸쳐 자리를 비웠고, 매번 때에 맞춰 되돌아온 그의 몸에서는 늘 역한 피비린내가 풍겼다.

그리고 꼬박 이틀에 가까운 시간이 흘렀을 때, 살성은 이렇게 말했다.

“이제부터는 좀 덜 성가셔지겠군.”

그것이 암천의 끈질긴 추격을 뿌리쳤다는 의미라는 것을 모르는 이는, 나를 포함한 삼천여 명의 아군 중 아무도 없었다.

더불어 살성이 어떤 방식으로 그토록 신속하게 추격자들을 처리했으며, 일만에 달하는 괴물들을 쓰러트린 것 역시 대인이 아니라 그와 청풍의 활약 덕분이라는 사실도.

“읍, 읍.”

밧줄로 전신이 칭칭 묶인 전리품. 아니, 흑의인이 꿈틀거리자 그를 마치 짐짝처럼 옆구리에 끼고 달리던 태산이 솥뚜껑만 한 주먹을 치켜세웠다.

“움직이지 마라. 때린다.”

“읍. 으읍!”

“소리 내지 마라. 먹는다.”

“……!”

협박치고는 좀 이상하긴 했지만, 효과는 아주 확실했다.

흑의인은 곧바로 쥐죽은 듯이 잠잠해졌고, 며칠이나 쉬지 않고 혹독한 강행군을 이어 간 아군은 머지않아 그 지긋지긋하던 광야를 벗어날 수 있었다.

그리고 그런 우리를 기다리고 있던 것은, 난생처음 보는 거대한 호수와 그 주위에 옹기종기 모여 모닥불을 피우고 있는 한 무리의 거지들이었다.

그것도 아주 낯익은 얼굴이 포함되어 있는.

“오오, 왔다. 여기요, 여기!”

멀리서 보아도 지갑에 저절로 손이 갈 만큼 빈티 나는 얼굴.

십만 거지 떼를 이끌 차세대의 왕초 거지, 궁기방이었다.
```

## Final English reading copy

```markdown
# Chapter 1074

There’s an old saying.

*Those who meet must part; those who leave will surely return.*

Every meeting ends in a farewell, and everyone who leaves will one day come back.

At this very moment, that old proverb came to mind as I stared wide-eyed at the two figures approaching from far away, weaving their way between the monsters strewn across the darkness all around us.

“Over here! We’re over here!”

“How many times do I have to tell you not to shout like that…? Never mind. Do whatever the hell you want.”

“Yes! Thank you!”

“This is driving me insane.”

The young man bounced along as if he had springs in his feet, while the boy beside him let out a deep, old-man-like sigh. To some people, it might have been a rather strange sight.

But I—or, rather, a tiny handful of people including me—already knew who those two were.

Especially the young man cheerfully bouncing along in front. Even if you’d seen him only once, he had the kind of energy you could never forget.

“…Cheongpung?”

The name slipped from my lips before I could stop it. The people who’d been frozen in a daze after the monsters’ bizarre collapse blinked.

“If you mean Cheongpung, could it be…”

“T-the Huashan Divine Dragon?”

Their reaction was immediate.

The only Cheongpung who could appear in a situation like this was someone I knew well enough to recognize at a glance. Even if you turned the whole world upside down and shook it out, there was only one.

Of course, there were some with a reasonable question.

“I can’t see from here. Captain, are you sure you’re not mistaken? Why would Young Hero Cheongpung suddenly show up here…”

Just then, Hyuk Mujin opened his mouth, unusually cautious. A clear voice rang out from beyond the pitch-black darkness.

“Benefactooor!”

“…That’s him.”

“…It is.”

“…I knew it. That voice alone is enough to make your mind go foggy. It’s definitely him.”

At this point, the voice was practically a fingerprint.

Hyuk Mujin and I confirmed it, and then Jeok Cheongang put the matter to rest.

“Benefactor! I’m here!”

With that final shout, Cheongpung swept in like a gust of wind, waving at me with a flushed face.

“Wow, it’s been so long! Have you been doing well?”

How was I supposed to respond to that?

I stared at the first-time-experience menace before me, half bewildered and half glad to see him. After a moment, I finally managed to speak.

“No. Not at all.”

“Oh. You do look that way, actually.”

“Then why’d you ask?”

“I haven’t been doing well, you see. But I hoped things might be different for you, hee-hee.”

Watching Cheongpung cheerfully carry on even while saying something gloomy, I realized what I should do right now.

More precisely, a quiet laugh slipped out of me before I knew it.

“Wait, why are you laughing?”

“Is that what you call a question? I’d laugh too if I saw the way you act, you idiot.”

That wasn’t my answer.

Swish.

A boy appeared from the darkness with a presence like a ghost—or rather, the greatest assassin of all time. He stared straight at me, then added:

“Though the one laughing is just as much of a reckless brat.”

His tone was as blunt as ever.

But when I saw the faint smile at the corner of his mouth, I could only laugh aloud instead of answering.

We’d met again after several months.



* * *



Reunions with people you’ve missed are always a joy.

But none of us was stupid enough to sit around a campfire, chatting away, in a situation like this.

“We’d best get out of here quickly. Follow me.”

Before the warmth of our reunion had even faded, the Slaughter Saint wiped the smile from his face and got moving as if nothing had happened.

“Throw away anything that might slow us down. Especially that idiot over there.”

Jeong Hogun, the idiot the Slaughter Saint had pointed out, replied.

“I don’t know which elder you are, but you should at least show some basic courtesy. I am a Thousand Captain of the Embroidered Uniform Guard, serving under His Majesty the Emperor’s solemn command…”

*Whoosh.*

It happened in an instant.

The Slaughter Saint’s figure blurred.

Then came the sound of wind, and a gleaming blue dagger pressed against Jeong Hogun’s neck.

“Keep talking. If you waste even a few more moments, I’ll make you a real dead man.”

Everyone, myself included, recognized the loyalty Jeong Hogun and his Embroidered Uniform Guards had for the Emperor. It was extraordinary.

But reality was cold.

Unlike the Emperor, who was somewhere far away, the dagger was right in front of him. Jeong Hogun stared at it in silence before finally speaking with a grim face.

“As I said, I am a Thousand Captain of the Embroidered Uniform Guard, serving under His Majesty the Emperor’s solemn command…but you appear to have a close relationship with the Marquis of Shangshan, so I’ll let this pass.”

The Slaughter Saint replied in a dry voice to what was an exceedingly poor excuse for an Embroidered Uniform Guard.

“We’re not that close.”

“You seem to know each other at least somewhat, so I’ll let it pass.”

“Of course we know each other, but I said we’re not close.”

“……”

“Just let it go. Understand?”

“……”

“I’ll take that as a yes.”

The Slaughter Saint had spared him the last shred of his dignity in the name of martial-world etiquette. By the time he lowered the dagger, most of our three thousand allies were staring at him in shock.

A boy who wasn’t even twenty, no matter how generously you counted, had subdued a Thousand Captain of the Embroidered Uniform Guard who stood at the very peak of the Peak realm.

And he’d done it in one swift move, so fast he’d been impossible to see.

Everyone was astonished by the unbelievable sight before them, but Perfected Being Hyeoncheon seemed more shaken than anyone.

“Fellow Daoist…who are you?”

The view changes depending on where you stand.

Perfected Being Hyeoncheon was a seasoned Supreme Peak master, skilled enough to vaguely discern the Slaughter Saint’s true realm. He was so caught up in shock and confusion that he couldn’t continue. Bow Saint spoke for him.

“It’s been a long time. I never thought I’d see you again like this.”

The Slaughter Saint had seen through her identity, just as she had his. He answered with a bitter smile.

“I feel the same. I thought we’d never meet again after that day.”

“Mountains and rivers have changed, and the world has changed with them. I had to act to set everything right.”

As the people around them grew more confused with every word they exchanged, Bow Saint quietly added:

“Just as you did, Slaughter Saint.”

“……!”

“……!”

“……!”

The air around us seemed to crackle.

The Slaughter Saint.

Once condemned by the whole martial world, he had become the greatest assassin of all time after the Great War between the Orthodox and Demonic factions began, striking fear into countless great fiends.

Those two words alone were enough to explain the situation and make everyone understand.

The Slaughter Saint gave Bow Saint a small nod, then addressed the people frozen like statues.

“So. Is there another idiot who wants to waste this precious time?”

Of course, there wasn’t.

Or, to be precise, even if there was, there shouldn’t be.

Not if the person asking was called the Slaughter Saint.

*Clank. Clatter!*

Jeong Hogun and the other Embroidered Uniform Guards began throwing off their armor with the speed of reservists who’d just finished a training exercise and were hurrying home. The Slaughter Saint’s eyes suddenly narrowed.

“But what exactly is that thing?”

I followed his gaze and immediately understood what he meant.

I also understood why he’d called a perfectly healthy human being a thing.

“Well, how should I put it… That gentleman’s a little out of his mind.”

“…I’ve already gathered that.”

The Slaughter Saint sighed as he watched the Great Sir, who had somehow blended in among the Embroidered Uniform Guards and was cheerfully stripping off his clothes.

“I’ll have to hear the details, but it seems clear enough that we’ve got one more madman.”

The original madman, of course, was watching the new madman’s striptease in wonder.

“Wow! I’ve never seen anyone take their clothes off so boldly!”

The Great Sir, whom Jeong Hogun had just stopped from removing his underwear, noticed Cheongpung and brightened.

“Thank you for the compliment. And who might you be?”

“Hello! I’m Cheongpung!”

“You’re a spirited young man. I like that. I’m Soonja.”

“Nice to meet you, Auntie!”

No.

Are these guys seriously insane?

Just as everyone stood aghast at the meeting of two natural disasters that shouldn’t occur even once in a hundred years, the Slaughter Saint shook his head and spoke.

“Right. Let’s get going.”

In his hand was a rope that stretched far off into the distance.

“What’s that?”

“War trophy.”



* * *



To get straight to the point, the enemies didn’t pursue us after that.

Or maybe it would be more accurate to say that they did, and they didn’t.

“Go on ahead. I’ll catch up soon.”

The Slaughter Saint said that and left us several times. Each time he returned just when we needed him, his body reeking of blood.

After nearly two full days had passed, he said, “It should be less of a nuisance from here on.”

Not one of our three thousand allies, myself included, doubted what he meant: he’d shaken off Dark Heaven’s relentless pursuit.

And we all knew how he’d dealt with the pursuers so quickly—and that it was he and Cheongpung, not the Great Sir, who had taken down the ten thousand monsters.

“Mm! Mm!”

The trophy—no, the black-robed man bound from head to toe in rope—twitched. Taishan, who was running with him tucked under one arm like a piece of luggage, raised a fist as big as a cauldron lid.

“Don’t move. I’ll hit you.”

“Mm! Mmm!”

“Don’t make noise. I’ll eat you.”

“……!”

It was a strange threat, but it worked perfectly.

The black-robed man immediately fell silent as a mouse. Our allies had been on a brutal forced march for days without rest, but before long we finally escaped that miserable wilderness.

What awaited us was an enormous lake I’d never seen before, and a group of beggars huddled around it, lighting campfires.

One of them had a face we knew very well.

“Oh! They’re here! Over here!”

A face so shabby you’d reach for your wallet just by looking at it from a distance.

Gung Gibang—the next beggar king, destined to lead a hundred thousand beggars.
```
