<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1157.txt",
      "sha256": "d6a45ec78f8896f9a63eddf9c5aebfa886d772ecf5548460c523f60a64684fea",
      "bytes": 12784
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "49dc713ea3fa0f74cd2fdd3c4e8274c2eee2689aefe7dfd8311aeb2997ad3350",
      "bytes": 1106
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "7d4396d9a6330a70203162cea821340cc43f73d0c5754dfb3c6a8bfa46a5b17d",
      "bytes": 247107
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "45f91baeca0252c4acae4c01601384c3103ebc2882dbfe414c8d13f24b59f02e",
      "bytes": 777
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f91e89f550ca9cd80d99a223ec428845591fdf2dc25da3de024abb137b860acc",
      "bytes": 760
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "1c810b8427fee6e43535bc11274f217ba7ed19b027ce29300189bebd81fd27b3",
      "bytes": 545
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7f229e511da97bc8c4b6982554373b5e588087c9dfb7d02814237dd3a41b2039",
      "bytes": 1725
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "268d4a6931b9b67d1f1ee6d3f4c25471446b5297b28791567807b34591c4a514",
      "bytes": 623
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "5106de3989d5f9e8f0c025093f1faaebfc8014b7d66a9c27c2a7ea61a2b83e25",
      "bytes": 703
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2cf1fde5dbf865897b3caf0136bb60cad574dbf3ce03be66f6e4ae675193cb8d",
      "bytes": 293256
    }
  ],
  "estimated_tokens": 9665
}
-->

# Durable State Update — Chapter 1157

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
1 and safe_through 1157. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1157. Profile updates may replace only one
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
  "chapter": 1157,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1157,
    "continuity_sources": [1157],
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
    "Morgoth’s three-day deadline is still running; his demand for Cheon Taemin and Jin Taekyung as tribute remains in effect.",
    "Cheon Taemin remains unconscious in a recovery capsule in a hidden Pentagon chamber.",
    "Jin believes Cheon Taemin was the Martial God and The Helper, and suspects Asmodeus was not completely erased; these identities and suspicions are unconfirmed.",
    "Choi Minwoo and most allies are secretly keeping Jin in the chamber until Morgoth’s deadline expires; Chuck Hagel and the Skeleton King were excluded from the plan.",
    "Jin has avoided his family and guildmates, fearing they would die if drawn into the coming battle."
  ],
  "continuity_sources": [
    1155,
    1156
  ],
  "open_questions": [
    "Were Cheon Taemin, the Martial God, and The Helper the same person?",
    "Was Asmodeus completely erased?",
    "Can Jin break out of the chamber without bringing down the Pentagon?",
    "What will happen when Morgoth’s three-day deadline expires?"
  ],
  "safe_through": 1156,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 천태민    | **Cheon Taemin**  |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 도사      | **Daoist**                                                      |
| 대사      | **Master** for a senior Buddhist monk                           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 모스크바 | **Moscow** | Russian city used in Taekyung's modern-world comparison. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 펜타곤 | **Pentagon** | Headquarters of the United States Department of Defense and source of intelligence about terrorist experiments. |
| 아프리카 | **Africa** | Region where terrorist organizations are reportedly conducting Gate and Magic Gem experiments. |
| 스카이 | **Sky** | American epithet for Cheon Taemin. |
| 마법진 | **Magic Formation** | The formation that transports Ma Sanbao and his followers. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 최민우 | 존슨 | allied Hunter to allied Grand Mage | Mr. Johnson | formal-polite | Minwoo calls out to Johnson during the battle. |
| 존슨 | 진태경 | allied friend and comrade-in-arms | Jin | familiar and conversational | Johnson calls Jin 진 while asking what he was thinking. |
| 대마도사 | 진태경 | adversary_to_adversary | you | polite, teasing | She uses polite phrasing while taunting him and warning him not to overexert himself. |
| 진태경 | 대마도사 | adversary_to_adversary | you bitch | insulting-casual | He curses at her while refusing to give up. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 1156
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Ares Guild Master and humanity's greatest Hunter, the Slayer who defeated the Demon King and created the first Mana Cultivation Method during the Great Cataclysm; after more than twenty years in seclusion, he remains unconscious in a secret area within Area A.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1155
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1156
- **Aliases:** None
- **Role:** Magic Johnson is the United States' Grand Mage and a War Mage, one of the two remaining masters of Magic.
- **Personality:** Strategic and ambitious, with a sharp temper when others squander opportunities or act without consulting her.
- **Voice:** He speaks casually and directly, with colloquial phrasing and occasional profanity.
- **Relationships:** He is Jin Taekyung's friend.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1156
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he is driven to protect himself and others and live peacefully with those he cherishes, while carrying guilt over those he failed to save.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the Skeleton King a friend; he trusts Sama Pyo despite suspecting his betrayal, was regarded as a worthy successor by Peng Cheolhu, and received the Martial God’s message through the Bow Saint.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1156
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 1156
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and resolute under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung, whom he regards as a model of taking responsibility in a crisis; he is the maternal grandson of Cheon Taemin.

## Korean source

```text
＃1157화



검푸른 화염을 머금은 창날이 천장을 찌를 듯 높게 솟아오른 그때, 눈을 부릅뜬 것은 비단 최민우 혼자만이 아니었다.

“……!”

그 흔한 욕설 한 마디 내뱉을 시간조차 없었다.

착잡한 눈빛으로 자신이 직접 설계한 비밀 공간에서 벌어지는 상황을 지켜보고 있던 거구의 대마도사는, 조금도 예상치 못했던 진태경의 돌발 행동에 경악했다.

동시에 없는 머리카락마저 쭈뼛 서는 듯한 감각에 사로잡혔다.

‘설마, 아니겠지.’

매직 존슨은 마른침을 꿀꺽 삼켰다.

그가 이토록 긴장하는 이유?

간단했다.

만약 마법이 강제로 파훼된다면, 그 여파는 펜타곤을 뒤흔들기 이전에 시전자인 자신부터 만신창이로 만들어 버릴 테니까.

아니, 어쩌면.

‘죽을지도.’

마법사에게 있어 마나(Mana)란 오감을 넘어선 또 하나의 감각이자 육신과 같은 것.

그렇기에 자신의 마나로 시전한 마법이 강제로 해제되었을 때, 마법사는 그 누구보다 심각한 타격을 입을 수밖에 없다.

이와 같은 사실을 누구보다 잘 알고 있는 매직 존슨이 보안 및 결계 마법을 수백 개나 때려 박는 미친 짓을 한 건, 순전히 믿음 때문이었다.

그가 아는 진태경이라면 결코 자신을 다치게 하지 않을거라는 믿음.

하지만 바로 그 순간.

슈확!

망설임 없이 내리그어진 창날이, 그의 마음에 남은 한 줌의 믿음마저 무참히 베어냈다.

“Fuuuck-!”

매직 존슨은 참았던 욕설과 함께 눈을 질끈 감았다.

그리고 수많은 마법과 이어져 있던 마나의 연결고리가 끊어지는 감각 속, 자신을 죽음까지도 몰아갈 수 있는 무지막지한 여파를 느꼈다.

스아아아.

어디선가 불어온, 따뜻한 열기를 머금은 바람을.

‘……잠깐, 바람?’

들리지도, 느껴지지도 않는다. 하늘과 땅을 떨어 울리는 굉음도, 사방을 뒤흔드는 거대한 힘의 여파도.

단지, 태양을 만난 해무(海霧)처럼 아스라이 흩어지는 기운만이 있을 뿐.

도무지 이해할 수 없는 상황 속, 잠시 눈꺼풀을 움찔거리던 거구의 대마도사는 용기를 발휘하여 감았던 눈을 떴다.

그리고 어느샌가 자신의 앞에 서 있는 한 사람을 멍하니 바라보다, 이내 결심한 듯 입을 열었다.

“진, 솔직히 말해 줘.”

진태경이 창날을 바로 세우며 대답했다.

“말씀하세요.”

“혹시 내가 죽어서 천국에 온 건가?”

“정말 죽었는지는 둘째 치고, 천국이라고 하기에는 너무 삭막하지 않아요? 하늘도 안 보이고.”

“사방이 뿌옇잖아. 꼭 에베레스트 정상이라도 되는 것처럼.”

“수증기에요. 구름이 아니고.”

“제기랄, 그렇군. 그렇다면 천국이 아니라 꿈인가?”

“그건 아니었으면 좋겠네요.”

“왜?”

“꿈속에서까지 나타날 정도라면, 제가 당신 취향일 수도 있다는 이야기니까.”

“오, 이런. 그런 이유일 거라곤 생각 못 했는데.”

쓴웃음을 머금은 채, 매직 존슨이 중얼거렸다.

“좋아, 결국 이렇게 됐네.”

진태경이 담담하게 고개를 끄덕였다.

“그러네요. 결국.”

“진심으로 미안해. 이렇게까지 하고 싶지는 않았는데.”

“이해합니다. 그냥 하는 말이 아니라, 정말로요.”

“그렇게 말해 주니 고맙군. 아마 저 친구도 나와 같은 생각일 거야.”

때맞춰 자욱한 수증기 너머로 모습을 드러낸 최민우가 복잡한 눈빛으로 진태경을 응시했다.

“강해지셨군요. 마지막으로 보았을 때보다도 더.”

기억 속에 존재하는 진태경은 언제나 강했다.

전투원이 아닌 한낱 짐꾼으로 참여했던 첫 레이드 때도, 그 이후에도.

진태경은 늘 최민우의 예상을 아득하게 뛰어넘어 왔고, 그건 오늘도 마찬가지였다.

그리고 그 사실이, 최민우를 괴롭게 만들었다.

“사실…… 잘 모르겠습니다. 진태경 씨가 또 한 번 강해졌다는 사실에 기뻐해야 할지, 아니면 슬퍼해야 할지.”

최민우는 종종 생각해 왔다.

큰 힘에는 큰 책임이 따른다. 이제는 고전이 되어 버린 어느 히어로 영화의 명대사가, 어쩌면 진태경이라는 한 인간을 위해 만들어진 것일지도 모른다고.

그랬기에 최민우가 바라보는 진태경은 그만큼 강하면서도 위태로워 보였다.

스스로가 강해지는 만큼 더욱 거대해진 위협에 홀로 맞서려 들었으니까.

하지만 곧 되돌아온 진태경의 목소리는 최민우의 그것과 달리 가볍고 경쾌했다.

“기왕이면 기쁜 게 낫죠.”

“그런가요.”

“난 그랬으면 좋겠는데. 어차피 슬픈 일이야 언제나 차고 넘치니까.”

“만약 당신이 죽으면, 그때는 어떻게 해야 합니까?”

“그걸 질문이라고.”

피식 웃은 진태경이 말을 이었다.

“그때 가서 슬퍼하세요. 마음껏.”

“……!”

“아직 일어나지도 않은 일에 마음 쓰지는 맙시다. 뭐 이 부분은 나도 서툴러서 팀장님한테 조언할 자격이 없긴 한데…… 직접 겪어 보니까 그게 맞는 것 같더라고.”

최민우는 눈을 깜빡였다.

다르다. 그만의 착각 일수도 있지만, 확연히 달라졌다.

불과 십여 분 전의 진태경은 억지로 꾸며낸 웃음을 짓고 있었지만, 지금의 그는 진심으로 편안한 미소를 짓고 있었다.

마치 커다란 짐 하나를 내려놓은 사람처럼.

그리고 그 이유는, 오직 진태경 자신만이 알고 있었다.

‘내가 죽으면, 이라.’

죽음.

진태경은 마음속으로 그 끈적하고 어두컴컴한 두 글자를 만지작거렸다.

물론 죽음은 언제나 두렵다. 매일, 매 순간 두렵지 않은 적이 없었다.

그러나 오늘에서야 분명히 알게 되었다.

그가 진정으로 두려워하는 것은, 죽음 그 자체가 아닌 자신의 죽음 이후에 벌어질 상황이었다는 것을.

남겨질 사람들이 맞닥트리게 될 위험이었다는 것을.

‘하지만, 이걸로 됐어.’

진태경은 구태여 고개를 돌리지 않았지만, 그의 오감은 어느덧 저 멀리 뒤에 남겨지게 된 한 사람을 향하고 있었다.

천태민.

결코 존재하지 않을 거라 생각했던, 또 한 명의 플레이어(Player)를.

‘설령 내가 정말 죽는다고 해도, 그때는 어쩌면…….’

진태경은 혀끝에 맴도는 뒷말을 삼켰다.

그리고 가까운 친구이자 믿음직한 동료인 두 사람을 또렷이 응시했다.

“세계 헌터 연맹의 맹주(盟主)로서, 현 시간부로 총동원령을 발동합니다. 목적지는 모스크바, 목표는 모르고스와 그 휘하 몬스터들의 섬멸.”

“……!”

“……!”

예상치 못한 말에 두 사람의 눈이 크게 뜨인 그때, 진태경이 단호한 어조로 덧붙였다.

“단, 추가 명령이 있기 전까지 그 어떤 돌발 행동도 있어서는 안 됩니다. 제가 명령을 내릴 수 없는 상황이라면 다르겠지만요.”

“그래. 잘 생각했어. 모두 함께 싸우는…… 잠깐, 명령을 내릴 수 없는 상황이라고?”

뒤늦게 뭔가 이상함을 알아차린 매직 존슨이 제대로 말을 끝마치기도 전에, 진태경이 재차 입을 열었다.

“제 자리가 공석이 되었을 때를 의미합니다.”

그 말에 담긴 뜻을 이해하지 못할 두 사람이 아니다. 최민우는 입술을 깨물었고, 매직 존슨은 침음성을 내뱉었다.

“제기랄, 진.”

“무슨 말을 해도 제 결정은 바뀌지 않아요. 저는 모르고스를 찾아갈 생각입니다. 지금 당장, 저 혼자서요.”

“……정말 그게 최선인가? 승률이 고작 1퍼센트도 안 되는 미친 도박에 목숨을 걸어야겠어?”

“예.”

한 치의 망설임도, 흔들림도 없는 목소리와 눈빛.

그런 진태경의 모습에 매직 존슨은 일순간 할 말을 잃었다.

하지만 동시에, 불현듯 떠올렸다.

지금으로부터 수십 년 전, 모두가 극심한 혼란에 빠져있을 때 유일하게 앞장서서 길을 나아갔던 누군가를.

스스로를 등불 삼아 세상을 밝혔던 영웅을.

‘스카이(Sky).’

그래, 그였다.

그리고 바로 지금, 매직 존슨의 눈앞에는 또 한 명의 천태민이 서 있다.

아니, 진태경이.

“……하.”

악문 잇새 사이로 흘러나온 한숨.

매직 존슨은 마침내 인정할 수밖에 없었다.

진태경이 앞서 말했듯, 어떤 설득으로도 그의 마음을 바꿀 수 없다는 사실과 자신들에게 주어진 역할이 무엇인지.

“좋아, 진. 무슨 계획인지 어디 한번 마음대로 지껄여 봐. 하지만 그전에 이 한마디는 꼭 해야겠군.”

크게 심호흡한 거구의 대마도사는, 새로운 시대의 구원자를 향해 말을 이었다.

“절대로, 무슨 일이 있어도 죽지 마. 내 스태프에 맞아 뒈지기 싫으면.”

진태경이 실소와 함께 대답했다.

“그럴 생각입니다. 두 번이나 죽는 건 사양이라.”

그리고 잠시 후, 진태경의 이야기를 끝까지 들은 두 사람이 침묵에 빠진 그때.

위이이이잉!

조금 전 들었던 이야기만큼이나 강렬한 사이렌 소리가 그들이 머무르고 있던 펜타곤의 지하 깊숙한 곳을 뒤흔들었다.

마법 장비를 타고 울려 퍼진, 다급하기 그지없는 통신원의 목소리도 함께.

- 코드 레드, 코드 레드!

“코드 레드?”

“비상이야. 그것도 최고 등급의. 갑자기 무슨 일이지?”



- 허가받지 않은 마법 사용 감지!

- 경비대는 즉각 출동 바람. 장소는 52구역. 반복한다. 경비대는 즉각 52구역으로 출동할 것!



“52구역이라면…… 이동 마법진이 있는 곳이군.”

“워프(Warp) 마법을 말하는 거예요?”

“그래. 하지만 이미 일주일 전부터 펜타곤 전체의 출입이 금지되어 있을 텐데. 우리가 모르는 내통자가 발각될 것 같으니 도주를 시도한 건가?”

결코 과한 추측은 아니었다. 현재 모르고스에게 항복한 이들 중 대부분은 생존을 위해 그에게 머리를 숙이고 있지만, 적극적으로 협조하는 이들 역시 존재했으니까.

당장 아프리카에서는 지난번 사태로도 완전히 뿌리 뽑지 못한 반군 잔당들이, 남미에서는 마약 카르텔들이 몬스터보다 더욱 흉포하게 날뛰고 있었다.

따라서 매직 존슨의 추론은 제법 합리적이라 할 수 있었다.

적어도, 일반적인 상식선에서는 그랬다.

- 긴급상황! 코드 네임 블루! 코드 네임 블루가 52구역을 통해 빠져나갔다!

이제는 다급함을 넘어 헐떡이기까지 하는 통신원의 외침에 세 사람은 동시에 침묵했으나, 그 이유는 조금 달랐다.

진태경은 저 말에 담긴 뜻을 조금도 알아듣지 못해서.

그리고 다른 두 사람은 그 뜻을 너무나도 잘 알고 있어서.

결국 그들 중 먼저 침묵을 깨트린 것은, 자신을 뚫어져라 바라보는 시선을 참지 못한 진태경이었다.

“좋아요. 제가 멍청한건 알겠으니까 적당히들 하고 말해 줘요. 코드 네임 블루가 뭔지.”

최민우가 눈을 깜빡이며 대답했다.

“어, 음. 진태경 씨는 모르는 게 당연합니다.”

“왜요?”

“그야, 진태경 씨한테는 비밀이거든요.”

지하 복도 한구석에 설치되어 있는 마법 장비와, 영문을 모르는 진태경을 번갈아 바라보던 매직 존슨이 말을 받았다.

“너야, 진.”

“아니, 다짜고짜 그게 뭔…….”

“방금 말한 코드 네임 블루. 그게 너라고.”

“……예?”

진태경이 지금 이 상황을 이해하는 데에는 아주 약간의 시간이 필요했고.

“그러니까, 제가 지금 펜타곤을 무단으로 빠져나갔다는 거예요?”

“글쎄, 정확히 말하자면.”

매직 존슨의 머릿속에는, 이미 이런 짓을 벌일 만한 누군가가 스쳐 지나가고 있었다.

“네 모습을 한 누군가겠지.”

그리고 서둘러 지상으로 향한 그들이 가장 처음 맞닥트린 건.

“빌어먹을, 이런 상황에 다들 나만 놔두고 어디에 있다가 온 거야?”

어느새 혼자가 되어 있던 척 헤이글이었다.
```

## Final English reading copy

```markdown
# Chapter 1157

When the spearhead, wreathed in dark blue flames, rose high enough to pierce the ceiling, Choi Minwoo wasn’t the only one whose eyes went wide.

“……!”

There wasn’t even time to utter a single curse.

The massive Grand Mage, watching the scene unfold in the secret space he’d designed himself, looked on in shock at Jin Taekyung’s completely unexpected move.

At the same time, he was seized by the feeling that even the hair he didn’t have was standing on end.

*No way. Surely not.*

Magic Johnson swallowed hard.

Why was he so tense?

Simple.

If the magic was forcibly broken, the backlash would leave the caster—himself—battered and broken before it ever shook the Pentagon.

No. Maybe…

*I could die.*

To a mage, mana was another sense beyond the five, as much a part of the body as flesh and bone.

That was why when a spell cast with a mage’s own mana was forcibly dispelled, the mage was bound to suffer a more serious blow than anyone else.

Magic Johnson knew this better than anyone. The only reason he’d done something as insane as packing hundreds of security and barrier spells into the space was that he trusted Jin Taekyung.

He trusted that the Jin Taekyung he knew would never hurt him.

But at that very moment—

Whoosh!

The spearhead swept down without hesitation, mercilessly cutting through the last shred of trust left in his heart.

“Fuuuck—!”

Magic Johnson squeezed his eyes shut, finally letting out the curse he’d been holding back.

And as he felt the mana links connecting him to countless spells snap, he sensed the tremendous backlash that could bring him to the brink of death.

A warm breeze, carrying heat, blew from somewhere.

*……Wait. A breeze?*

There was no earthshaking roar to hear, no tremendous force rocking everything around him to feel.

Only energy, scattering faintly like sea fog meeting the sun.

The massive Grand Mage, unable to make sense of what was happening, twitched his eyelids for a moment, then gathered his courage and opened his eyes.

He stared blankly at the person standing in front of him, then spoke as if he’d made up his mind.

“Jin, be honest with me.”

Jin Taekyung straightened his spear and answered.

“Go ahead.”

“Did I die and go to heaven?”

“Whether you’re really dead is another matter, but heaven seems too bleak. We can’t even see the sky.”

“Everything’s all hazy. Like we’re at the top of Mount Everest.”

“It’s water vapor, not clouds.”

“Damn, you’re right. Then if it’s not heaven, is this a dream?”

“I hope not.”

“Why?”

“If I’m showing up even in your dreams, maybe I’m your type.”

“Oh, dear. I never thought that could be the reason.”

Magic Johnson murmured with a bitter smile.

“Okay. So this is how it ends.”

Jin Taekyung nodded calmly.

“Looks like it.”

“I’m truly sorry. I didn’t want things to go this far.”

“I understand. I’m not just saying that. I really do.”

“Thanks for saying that. I think our friend over there feels the same way.”

Right on cue, Choi Minwoo emerged through the thick steam and looked at Jin Taekyung with a complicated expression.

“You’ve gotten stronger. Even stronger than the last time I saw you.”

In Choi Minwoo’s memory, Jin Taekyung had always been strong.

Even on his first raid, when he’d gone along as no more than a porter rather than a combatant. And after that, too.

Jin Taekyung had always far surpassed Choi Minwoo’s expectations. Today was no different.

And that fact made Choi Minwoo ache.

“To be honest… I don’t know whether I should be happy that you’ve gotten stronger yet again, or sad.”

Choi Minwoo had often thought about it.

“With great power comes great responsibility.” Maybe that famous line from a now-classic superhero movie had been written for Jin Taekyung himself.

That was why, to Choi Minwoo, Jin Taekyung seemed every bit as strong as he was precarious.

The stronger he became, the more he tried to face ever greater threats on his own.

But Jin Taekyung’s reply was light and cheerful, nothing like Choi Minwoo’s words.

“Better to be happy, if you ask me.”

“Is that so?”

“That’s what I’d prefer. There’s always plenty to be sad about anyway.”

“If you died, what would I do then?”

“What kind of question is that?”

Jin Taekyung gave a short laugh and went on.

“Be sad when it happens. As much as you want.”

“……!”

“Let’s not worry about something that hasn’t even happened yet. Though I’m not really qualified to give you advice about that, Team Leader. I’m not good at it myself… But I’ve been through it, and I think that’s the right way.”

Choi Minwoo blinked.

He was different. Maybe it was only Choi Minwoo’s imagination, but Jin Taekyung had changed—noticeably.

Just ten minutes ago, Jin Taekyung had been forcing a smile. Now he was smiling with genuine ease.

Like someone who’d set down a heavy burden.

And only Jin Taekyung knew why.

*If I died…*

Death.

Jin Taekyung turned those two sticky, dark words over in his mind.

Of course death was always frightening. There hadn’t been a day, or a moment, when it hadn’t frightened him.

But only today had he realized it clearly.

What he truly feared wasn’t death itself, but what would happen after he died.

The danger the people left behind would face.

*But this is enough.*

Jin Taekyung didn’t bother turning around, but his five senses were already focused on the person he’d left far behind him.

Cheon Taemin.

Another Player—a person he’d once thought could never exist.

*Even if I really do die, maybe then…*

Jin Taekyung swallowed the rest of the words lingering on the tip of his tongue.

Then he looked squarely at the two men who were close friends and reliable comrades.

“As the Alliance Leader of the World Hunter Federation, I’m issuing a full mobilization order, effective immediately. Destination: Moscow. Objective: the annihilation of Morgoth and the monsters under his command.”

“……!”

“……!”

The two men’s eyes widened at the unexpected announcement. Jin Taekyung added in a firm voice:

“However, no one is to do anything rash until I give further orders. Unless I’m in a situation where I can’t issue orders.”

“Right. You’ve thought this through. We’ll all fight together—wait, ‘unless you’re in a situation where you can’t issue orders’?”

Magic Johnson belatedly realized something was wrong, but before he could finish, Jin Taekyung spoke again.

“I mean if my position becomes vacant.”

Neither man could fail to understand what he meant. Choi Minwoo bit his lip, and Magic Johnson let out a low groan.

“Damn it, Jin.”

“No matter what you say, I won’t change my mind. I’m going to Morgoth. Right now, alone.”

“……Are you sure that’s the best option? You’re really going to bet your life on a crazy gamble with less than a one-percent chance of winning?”

“Yes.”

There wasn’t a trace of hesitation or doubt in his voice or eyes.

For a moment, Magic Johnson was at a loss for words.

But then, suddenly, he remembered someone from decades ago. When everyone had been thrown into utter confusion, that person alone had stepped forward and led the way.

A hero who had made himself a beacon and lit up the world.

*Sky.*

Yes. It was him.

And right now, standing before Magic Johnson was another Cheon Taemin.

No—Jin Taekyung.

“……Ha.”

A sigh slipped through Magic Johnson’s clenched teeth.

At last, he had to admit that, just as Jin Taekyung had said, nothing would change his mind. And he had to admit what their role was.

“Fine, Jin. Go on and tell us what your plan is. But first, I have to say this.”

The massive Grand Mage took a deep breath, then spoke to the savior of a new age.

“Whatever happens, don’t you dare die. If you don’t want me to beat you to death with my staff.”

Jin Taekyung let out a quiet laugh.

“I don’t plan to. I’d rather not die a second time.”

A little while later, just as the two men fell silent after hearing Jin Taekyung out—

Wheeeee!

A siren as piercing as the story they’d just heard shook the deep underground of the Pentagon where they were staying.

Along with it came the panicked voice of an operator, booming through the magical equipment.

“Code Red, Code Red!”

“Code Red?”

“It’s an emergency. The highest alert level. What happened all of a sudden?”

“Unauthorized use of magic detected!”

“Security forces, deploy immediately. Location: Area 52. I repeat, security forces are to deploy to Area 52 immediately!”

“Area 52… That’s where the transport Magic Formation is.”

“You mean the Warp magic?”

“Yeah. But access to the entire Pentagon has been forbidden for a week now. Is an inside collaborator we don’t know about trying to escape because they think they’re about to be found out?”

It wasn’t an unreasonable guess. Of those who had surrendered to Morgoth, most had bowed to him to survive, but there were others who were actively cooperating with him.

In Africa, rebel holdouts that hadn’t been completely rooted out in the previous incident were rampaging. In South America, drug cartels were running wild, more ferocious than the monsters.

So Magic Johnson’s guess was fairly reasonable.

At least, by ordinary standards.

“Emergency! Code Name Blue! Code Name Blue has escaped through Area 52!”

The operator’s shout, now so desperate he was almost panting, brought all three men to silence—but for slightly different reasons.

Jin Taekyung didn’t understand what those words meant at all.

The other two understood all too well.

In the end, the first to break the silence was Jin Taekyung, unable to endure their stares.

“Okay. I get that I’m an idiot, so cut it out and tell me what Code Name Blue is.”

Choi Minwoo blinked and replied.

“Uh, well. It’s only natural you wouldn’t know, Mr. Jin Taekyung.”

“Why?”

“Because it’s a secret from you.”

Magic Johnson looked back and forth between Jin Taekyung, who had no idea what was going on, and the magical equipment installed in a corner of the underground corridor.

“It’s you, Jin.”

“What? What does that mean out of nowhere—”

“Code Name Blue, the one they just mentioned. That’s you.”

“……What?”

It took Jin Taekyung a moment to understand what was going on.

“So someone’s saying I slipped out of the Pentagon without permission?”

“Well, if we’re being precise…”

Magic Johnson already had a good idea who would do something like that.

“Someone who looks like you.”

And the first person they ran into when they hurried to the surface was—

“Goddamn it. Where the hell were all of you, leaving me on my own in a situation like this?”

Chuck Hagel, who had somehow ended up all alone.
```
