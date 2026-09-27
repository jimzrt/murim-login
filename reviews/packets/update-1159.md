<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1159.txt",
      "sha256": "9d0724fd24c9a63b69b507833cfd8b083dcede648e5f3bc057094c9abfa36154",
      "bytes": 11918
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "aa688f82c5c8ab8cc2f344af2f92c32710ea3d44a3f4ed2560ed3064adaff81b",
      "bytes": 1608
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2fd0de0ff721805936794bca4b9ad70fd4d20f40fbc76e97c8e8c5be179dfa5d",
      "bytes": 247561
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7b6144ffe8cb7a499be33af0d9e3ec15f4a0087f5f93541bbf653ba23470eb14",
      "bytes": 760
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "31fc12bdeac17c7a65af0b5cf524b6fbb7282e0004a621ea923bf20ebb8d80e2",
      "bytes": 867
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "07a103039f99d780f84925806452dc7be056a098457a8fd0313faf8561fe9ba9",
      "bytes": 1709
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "cd0fcc067d4680bc822529d1b52989faad643d8c29f3de71c056b4649471d93a",
      "bytes": 623
    },
    {
      "path": "characters/Leviathan.md",
      "sha256": "90e0291335b1fbe19351b2a66cd410e3425577ff114b1abee3f6bb76e40686f4",
      "bytes": 757
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2cf1fde5dbf865897b3caf0136bb60cad574dbf3ce03be66f6e4ae675193cb8d",
      "bytes": 293256
    }
  ],
  "estimated_tokens": 8875
}
-->

# Durable State Update — Chapter 1159

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
1 and safe_through 1159. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1159. Profile updates may replace only one
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
  "chapter": 1159,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1159,
    "continuity_sources": [1159],
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
    "Jin ordered World Hunter Federation forces to mobilize for Moscow against Morgoth and his monsters, but intended to go alone.",
    "The Skeleton King has borrowed Jin Taekyung’s appearance through absorption and is heading toward Morgoth, intending to sacrifice himself in Jin’s form.",
    "The Skeleton King can hear the dead spirits and regards them as his people; he suspects he may once have been human, but has no memories and sometimes experiences déjà vu.",
    "Morgoth was summoned by Asmodeus from beyond distant stars and space, but does not know why; he says he is not devoted to Asmodeus.",
    "Morgoth welcomes a hero who has arrived at his palace; the guest’s identity is not explicitly stated."
  ],
  "continuity_sources": [
    1157,
    1158
  ],
  "open_questions": [
    "Were Cheon Taemin, the Martial God, and The Helper the same person?",
    "Was Asmodeus completely erased?",
    "Who escaped through Area 52 in Jin’s likeness?",
    "What will happen when Morgoth’s three-day deadline expires?",
    "Why did Asmodeus summon Morgoth and prepare the current situation?"
  ],
  "safe_through": 1158,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 생도     | **cadet**                                    |
| 일격     | **One Strike**                         |
| 칭호               | **Title**                      |
| 몬스터     | **monster**           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레비아탄 | **Leviathan** | Ancient S-rank sea monster associated with Asmodeus. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 평화 | **Peace Guild** | Guild name. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 베히모스 | **Behemoth** | Mythical monster emerging from the Pyeongchang Gate. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 언데드 | **undead** | Supernatural beings that are neither dead nor alive. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |
| 드래곤 | **Dragon** | The species to which Morgoth belongs. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 레비아탄 | enemy and hunted monster | Leviathan; you | insulting-casual | Jin orders Leviathan to leave and dismisses its attempt to kill the Skeleton King. |
| 레비아탄 | 진태경 | attacking enemy | you bastard | enraged-insulting | Leviathan directly curses Jin while resisting his attacks. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |
| 도플갱어 | 진태경 | enemy | you | measured and informal | Replies to Jin’s taunt without using a name or title. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1158
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 1158
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger was a Demon Realm being capable of regenerating in new bodies and was erased by Jin Taekyung.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** It speaks with theatrical, grandiose confidence, taunting opponents in polished, self-important phrasing.
- **Relationships:** It claims to have served Demon King Asmodeus as its master and acted on his order, regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1158
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he protects those he cherishes and is learning to face the fear of leaving them in danger without letting it paralyze him.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the Skeleton King a friend; he trusts Sama Pyo despite suspecting his betrayal, was regarded as a worthy successor by Peng Cheolhu, and received the Martial God’s message through the Bow Saint.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1158
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Leviathan.md

# Leviathan (레비아탄)

- **Safe through:** Chapter 829
- **Aliases:** None
- **Role:** Leviathan was an ancient S-rank sea monster and ruler of the sea who was killed by Jin Taekyung after the deep-sea hunt, leaving a final warning that the Cataclysm was approaching.
- **Personality:** Ravenous, domineering, and driven by instinctive hunger for magical power and food.
- **Voice:** Its spoken voice is not established; it communicates in Demon Realm language.
- **Relationships:** Leviathan once served the Demon King Asmodeus and withdrew into the deep sea after his fall; it regards the Skeleton King as a traitor for siding with humanity.

## Korean source

```text
＃1159화



쿵, 구구구궁.

육중한 굉음을 토해 내며 열리는 철문 앞에서, 스켈레톤 킹은 문득 생각했다.

만약 자신이 진짜 인간이었다면, 지금 들려오는 이 소리를 심장 박동 소리로 착각했을지도 모른다고.

하지만 심장이 없어도 선명하게 느낄 수 있었다.

천천히 내딛는 발걸음을 따라 좁혀지는 거리만큼, 그에 맞춰 차례대로 열리는 철문의 숫자만큼 부풀어 오르는 아득한 마력을.

그리고 그 끝에, 이 모든 것의 근원이라 할 수 있는 한 존재가 그를 기다리고 있었다.

“들어오라, 영웅이여.”

나직한 음성과 함께 마지막 문이 열린 그 순간, 스켈레톤 킹은 자신도 모르게 숨을 삼켰다.

‘이건.’

짙은 어둠만 담겨 있던 지금까지와 달리, 어느덧 휘황찬란한 빛으로 물든 두 눈동자.

옛 신화 속 신들의 궁전을 옮겨 놓으면 이런 광경일까.

직경만 무려 수백 미터에 이르는 그곳에는 긴 세월을 간직한 고풍스러운 가구들과 형형색색의 보석들이 가득했고, 아득한 높이의 천장과 사방을 둘러싼 벽면에는 무수한 그림이 음각(陰刻)되어 있었다.

아름답다.

아니, 아름다운 것을 넘어 놀라울 정도다.

그러나 이 눈부신 광경 앞에서도, 스켈레톤 킹의 시선은 오직 한 방향만을 응시하고 있었다.

이 공간의 모든 것들을 몇 번이나 합치고 곱하더라도 비교할 수 없을 만큼 아름답고, 세상 그 무엇보다 끔찍한 힘을 갖춘 존재를.

“이곳이 제법 마음에 든 모양이군. 다행이야.”

마치 보이지 않는 날개라도 펼친 듯, 저 멀리 우뚝 솟은 왕좌(王座)에서 부드럽게 떨어져 내린 궁전의 주인이 빙긋 웃었다.

“내가 누구인지 따로 소개할 필요는 없겠지.”

틀림없이, 그랬다.

그가 누구인지는 스켈레톤 킹뿐만이 아니라 전 세계의 인류 전체가 알고 있었으니.

“……모르고스(Morgoth).”

신음하듯 흘러나온 스켈레톤 킹의 뇌까림에, 모르고스가 미소 띤 얼굴로 고개를 끄덕였다.

“역시 알고 있군. 하지만 이 세상의 관습에 따라 정식으로 통성명을 하는 것도 나쁘진 않겠어.”

그 말에 담긴 뜻을 알아차린 스켈레톤 킹이 대답했다.

이곳에 없는, 있어서도 안 되는 한 사람을 다시금 떠올리면서.

“진태경, 진태경이다.”

“그렇군. 진태경이라…….”

뭔가를 곱씹듯 생각하던 모르고스가 물었다.

“몇 번을 들어도 참 희한한 이름이야. 혹시 이름에 담긴 특별한 의미라도 있나?”

“물론 있지.”

어깨를 으쓱한 스켈레톤 킹이 덧붙였다.

만약 진태경이 이 자리에 있었다면 도플갱어인가 의심했을 만큼, 그에게 가장 잘 어울리는 대답으로.

“좆 까라는 뜻이야.”

잠시 멍한 표정으로 스켈레톤 킹을 바라보던 모르고스가 웃음을 터트렸다.

“이런, 한 방 먹었군. 그래도 꽤 재미있는걸.”

“실컷 웃어 둬. 잠시 뒤에 여러 방 맞고 나면 재미 없어질 테니까.”

스켈레톤 킹은 구태여 적의를 숨기지 않았다.

모르고스를 대면한 순간 깨달았기 때문이다.

방심을 유도한 기습 따위는 절대 통하지 않을 상대라는 것을.

‘어떻게 이럴 수 있지?’

처음이었다. 그저 마주한 것만으로도 압도되는 기분은.

정확히는 지금껏 단 한 번, 그가 스켈레톤 워로드로 불리던 시절에 진태경과의 전투에서 지금과 비슷한 느낌을 받긴 했으나 비교 자체가 무의미했다.

그때의 진태경과 지금의 진태경을 비교할 수 없듯, 스켈레톤 킹 역시 무서운 속도로 성장했으니까.

아니, 단순히 성장 속도로만 따진다면 진태경 이상일지도 몰랐다.

진태경과 함께하게 된 이후부터, 아크 리치를 시작으로 여러 네임드 몬스터를 쓰러트리고 그들의 방대한 마력을 영양분처럼 흡수해 왔던 그다.

이제는 더 이상 왕이라는 칭호가 부족하지 않을 만큼, 실로 강력한 존재로 거듭난 것이다.

하지만…….

‘격이 다르다.’

저주받은 존재, 언데드(Undead).

그와는 반대로 온 세상 만물의 축복 속에서 탄생한 존재, 드래곤(Dragon).

지금 서로를 마주하고 있는 그들은 눈높이만 같을 뿐, 모든 것이 달랐다. 타고난 태생도, 그로부터 비롯된 힘의 크기와 깊이도.

그러나 어째서일까.

스켈레톤 킹은 오히려 더욱 편안해진 마음으로 검 자루를 붙잡았다.

모르고스가 자신의 일거수일투족을 지켜보고 있음에도, 마치 팔짱을 끼는 것처럼 자연스럽게.

“이런, 혹시 지금 나와 싸울 셈인가?”

“왜, 이럴 거라고는 생각 못 했나?”

“아니, 자네가 홀로 나타났을 때부터 예상은 했지. 다만 좋지 않은 선택이라는 걸 말해 주고 싶군.”

“다른 선택지는 처음부터 없었어.”

“선택지가 없다니, 왜 그렇게 생각하는지 이해하기 어려운데.”

고개를 갸웃한 모르고스가 말을 이었다.

“아주 오랜 세월을 살아왔지만, 그럼에도 자네는 매우 흥미로운 존재야. 그리고 나는 뛰어난 인재에 대한 욕심이 많지.”

“그러니까, 투항해라?”

“내 가디언(Guardian)이 되게. 진정한 왕을 가장 가까이에서 수호하는 영광을 누리면서, 더욱 강한 힘과 영생의 삶까지 얻게 될 테니.”

“그것참, 대단한 영광이군.”

“지극히 합리적이면서도 평화로운 방법이기도 하지. 어떤가?”

헛웃음을 흘린 스켈레톤 킹이 입을 열었다.

“진태경.”

“뭐?”

“아까 알려줬잖아. 무슨 뜻인지.”

그 순간.

스르릉.

서릿발 같은 예기를 뿜어내는 은빛 검신이 마침내 세상 밖으로 모습을 드러냈다.

“이게 내 대답이다.”

이는 동시에 진태경의 대답이기도 했다.

스켈레톤 킹이 알고 있는 그라면, 분명 이렇게 행동했을 테니까.

그리고 그런 스켈렡톤 킹의 모습에, 모르고스는 혼잣말처럼 중얼거렸다.

“정말 희한하군. 도무지 이해가 되지 않아.”

“왜, 네놈의 그 거지 같은 제안을 거절한 게 그렇게도 충격이었나?”

“자네의 바보 같은 선택에 실망했다는 건 부정하지 않겠네. 하지만 정말 이해가 되지 않는 점은 따로 있어.”

스륵.

흑요석 같은 눈동자가 천천히 움직이며 상대의 모습을 시야에 담는다.

정확히는, 스켈레톤 킹과 그의 손에 들린 [영웅의 검]을.

그리고 다음 순간 그의 입술 사이로 흘러나온 한마디는, 스켈레톤 킹을 전율케 하기에 충분했다.

“어떻게 자네 같은 언데드 몬스터 따위가, 저런 에고 소드(Ego Sword)를 사용할 수 있는 거지?”

“……!”

“아, 기분 나빴다면 미안하군. 하지만 내가 알고 있는 지식으로도 설명할 수 없는 상황이라서 말이야. 혹시 따로 짚이는 바가 있나?”

스켈레톤 킹은 대답하지 않았다.

아니, 대답할 수 없었다.

찰나의 순간, 한 줄기 벼락처럼 전신을 파고든 충격을 가라앉히는 것만으로도 안간힘을 써야 했으니까.

‘알고 있었어. 내 정체를.’

언제부터였을까.

이름을 밝혔을 때? 혹은 진태경이 늘 사용하던 창이 아닌 검을 꺼내 들었을 때?

그것도 아니면…… 원혼들의 만류를 뒤로한 채 처음으로 모르고스의 권역인 칠흑빛 대지에 발걸음을 디뎠던 그 순간부터?

‘빌어먹을.’

스켈레톤 킹은 이를 악물었다.

그리고 자신의 모든 것을 꿰뚫어 보는 듯한, 흑룡의 두 눈동자를 마주하며 입을 열었다.

“나를 갖고 놀았군. 처음부터 끝까지.”

“이런.”

작게 한숨을 내쉰 모르고스가 말을 이었다.

“괜한 오해로 마음 상해하지 말게. 지금까지 내가 한 말은 모두 진심이었으니까. 자네는 그만큼 특별하면서도 흥미로운 존재야. 수천 년을 살아왔음에도 이런 경우는 몇 번 겪어 보지 못했지.”

“아가리 닥쳐.”

“무례하군. 하지만 용서하겠네. 하등 종족처럼 찰나의 분노에 휩쓸려 귀중한 것을 파괴하기에는 내 지성과 호기심이 허락하지 않거든.”

모르고스는 조금도 동요하지 않았다.

아니, 동요하긴커녕 더욱 흥미로워진 눈빛으로 스켈레톤 킹을 바라보았다.

늙고 교활한 고룡(古龍)의 눈은 마치 곤충 채집을 위해 뒷산으로 향한 어린아이의 그것처럼 반짝이고 있었다.

바로 이 순간, 강력한 기운이 실린 은빛 검신이 자신을 향해 내리그어지고 있음에도.

슈확, 콰드드득!

맹렬한 바람이 공간을 할퀴고, 검에 실린 기운이 반경 십여 미터 안에 존재하는 모든 것을 집어삼킨다.

한때 전 세계를 공포로 몰아넣었던 네임드 몬스터들조차 직격당했다면 죽음을 각오했어야 할 정도의 맹격.

그러나 스켈레톤 킹은 굉음이 터져 나오기도 전에 알 수 있었다.

전력을 쏟아부은 조금 전의 일격이, 적의 털끝 하나조차도 상하게 하지 못했다는 사실을.

구구구궁……!

사방을 뒤흔드는 거대한 울림 너머, 어느덧 저 멀리 우뚝 솟아있는 왕좌(王座)로 이동한 모르고스가 진심을 담아 두 손뼉을 부딪쳤다.

“굉장하군. 굉장해. 이 정도로 강대한 마력이라니. 심지어 느껴지는 마력의 종류도 다양해.”

“……너.”

“아, 그래. 아크 리치, 레비아탄, 베히모스. 그들의 마력을 흡수한 거로군. 하지만 자네의 지금 그 모습은 마법으로 꾸민 것이 아닌 것 같은데…… 혹시 도플갱어라 불리는 존재를 만난 적이 있나?”

일순간, 스켈레톤 킹은 머릿속이 차갑게 식는 듯한 기분에 사로잡혔다.

간파당했다.

그것도 너무도 빨리, 소름이 끼칠 정도로 완벽하게.

그리고 딱딱하게 굳은 스켈레톤 킹의 얼굴을 본 모르고스는 환하게 웃었다.

“역시 그랬군. 대상의 마력은 물론 이능의 일부까지 흡수할 수 있다니. 참으로 놀라운 능력이야. 한낮 언데드, 그것도 스켈레톤에 불과한 자네가 어떻게 그 정도의 힘을 지니게 되었는지 이제야 이해가 되는군.”

“그 한낮 언데드가, 오늘 이 자리에서 드래곤을 죽일 수도 있겠지.”

“도발인가?”

“아니, 진심이다. 어느 정신 나간 인간을 지켜보면서 얻은 교훈이기도 하지.”

씹어뱉듯 중얼거리며 다가오는 스켈레톤 킹의 모습에, 모르고스가 고개를 끄덕였다.

“그래, 물론 그럴 수도 있겠지. 그토록 강대하던 아스모데우스조차 한낱 인간의 손에 저지당했으니. 하지만…….”

모르고스는 스켈레톤 킹을 직시하며 말을 이었다.

“자네가 진태경을 통해 교훈을 얻었듯이, 나 또한 그 소식을 듣고 가장 중요한 것을 깨달았지.”

고오오옹.

공간이 일그러진다.

믿을 수 없이 강력하고 순수한 마력이, 어느덧 보이지 않는 칼날이 되어 사방을 가득 메웠다.

“그의, 아스모데우스의 가장 큰 패착은 바로 오만이라는 걸.”

“……!”

“나는, 너희를 얕보지 않아.”

스켈레톤 킹이 눈을 부릅뜬 그 순간.

파아아앗!

밤하늘보다도 깊고 짙은 칠흑색 섬광이, 그의 전신을 향해 쏘아졌다.
```

## Final English reading copy

```markdown
# Chapter 1159

Boom. Rumble, rumble.

As the iron doors opened with a heavy roar, the Skeleton King had a sudden thought.

If he’d really been human, he might have mistaken the sound for his own heartbeat.

But even without a heart, he could feel it clearly.

With every step he took, the distance narrowed—and with every iron door that opened in turn, the immeasurable magical power swelled.

At the end of it all, one being—the source of everything—waited for him.

“Come in, hero.”

The last door opened with a low voice, and the Skeleton King swallowed involuntarily.

*This is…*

His eyes, which until now had held nothing but deep darkness, were filled with dazzling light.

Would this be what it looked like if someone brought a palace from the myths of old gods into the world?

The place spanned hundreds of meters in diameter. It was filled with antique furniture steeped in the passage of time and jewels of every color. Countless images were carved into the lofty ceiling and the walls surrounding him.

Beautiful.

No—not just beautiful. Astonishing.

Yet even before this blinding sight, the Skeleton King’s gaze fixed on just one thing.

A being more beautiful than anything else in this space could ever be, no matter how many times you added it all together or multiplied it—and possessing a power more terrifying than anything in the world.

“You seem to like the place. Good.”

The palace’s master smiled as he drifted gently down from the throne towering in the distance, as if he had spread invisible wings.

“I don’t need to introduce myself, do I?”

He certainly didn’t.

Not only the Skeleton King, but all of humanity around the world knew who he was.

“…Morgoth.”

The Skeleton King’s mutter came out like a groan. Morgoth smiled and nodded.

“So you do know me. Still, it wouldn’t hurt to formally exchange names, as is the custom in this world.”

The Skeleton King understood what he meant and replied, thinking once more of the one person who wasn’t here—and shouldn’t be.

“Jin Taekyung. Jin Taekyung.”

“I see. Jin Taekyung…”

Morgoth seemed to mull it over, then asked:

“I’ve heard it several times now, but it’s a very strange name. Does it have some special meaning?”

“Of course it does.”

The Skeleton King shrugged and added the answer that suited Jin Taekyung so perfectly, the real one might have mistaken him for a Doppelganger if he’d been here.

“It means ‘fuck you.’”

Morgoth stared at the Skeleton King, momentarily dumbfounded, then burst out laughing.

“Well, you got me. That’s pretty funny.”

“Get all your laughing out now. After you’ve taken a few hits in a minute, you won’t find it so funny.”

The Skeleton King made no effort to hide his hostility.

The moment he faced Morgoth, he’d understood.

A sneak attack meant to catch him off guard would never work against this opponent.

*How is this possible?*

He’d never felt so overwhelmed just by standing before someone.

To be precise, there had been one time: when he was called the Skeleton Warlord, he’d felt something similar while fighting Jin Taekyung. But the comparison was meaningless.

Just as the Jin Taekyung of then couldn’t be compared to the Jin Taekyung of now, the Skeleton King had grown at a terrifying pace, too.

In fact, if they were comparing nothing but growth rates, he might have even surpassed Jin Taekyung.

Since joining Jin Taekyung, he’d defeated one named monster after another, starting with the Arch Lich, and absorbed their vast magical power like nourishment.

He’d become so powerful that the title of king no longer seemed inadequate.

But…

*We’re on different levels.*

A cursed being: undead.

And, in contrast, a being born with the blessing of all creation: a Dragon.

The two facing each other were at eye level, but everything else about them was different. Their innate natures, and the size and depth of the power that came from them.

And yet, why?

The Skeleton King felt more at ease as he gripped his sword hilt.

Even with Morgoth watching his every move, the motion came naturally, as if he were simply folding his arms.

“Now, are you thinking of fighting me?”

“Why? Didn’t you expect this?”

“No, I did, from the moment you appeared alone. I only wanted to tell you it’s a poor choice.”

“There was never another choice.”

“Never another choice? I find it hard to understand why you think that.”

Morgoth tilted his head and continued.

“I’ve lived for a very long time, and yet you’re a fascinating being. I’ve always had a weakness for exceptional talent.”

“So you’re telling me to surrender?”

“Become my Guardian. You’ll have the honor of protecting the true king at his side, and gain even greater power and eternal life.”

“That’s a tremendous honor.”

“It’s also an entirely reasonable and peaceful solution. What do you say?”

The Skeleton King let out a hollow laugh and spoke.

“Jin Taekyung.”

“What?”

“I told you what it means earlier.”

At that moment—

*Shing.*

A silver blade, its edge cold as frost, finally emerged into the open.

“This is my answer.”

It was Jin Taekyung’s answer, too.

The Skeleton King knew him. He would have acted exactly this way.

Morgoth looked at him and muttered, almost to himself:

“How strange. I just can’t understand it.”

“What, are you that shocked I turned down your shitty offer?”

“I won’t deny that your foolish choice disappoints me. But that’s not what I find so hard to understand.”

*Rustle.*

Morgoth’s obsidian eyes moved slowly, taking in his opponent.

More precisely, the Skeleton King and the [Hero’s Sword] in his hand.

The next words that slipped between Morgoth’s lips were enough to send a shiver through the Skeleton King.

“How can an undead monster like you wield an Ego Sword like that?”

“……!”

“Oh, sorry if that offended you. It’s just a situation I can’t explain with what I know. Can you think of any reason?”

The Skeleton King didn’t answer.

No—he couldn’t.

He had to struggle just to steady himself after the shock that had struck through his whole body like a bolt of lightning.

*He knew. He knew who I was.*

Since when?

When he gave his name? Or when he drew a sword instead of the spear Jin Taekyung always used?

Or… from the moment he first set foot on the pitch-black ground in Morgoth’s territory, despite the spirits’ pleas for him not to?

*Damn it.*

The Skeleton King clenched his teeth.

Then, looking into the Black Dragon’s eyes, as if they could see through everything he was, he spoke.

“You were playing with me. From beginning to end.”

“Oh dear.”

Morgoth let out a soft sigh and continued.

“Don’t let a needless misunderstanding upset you. Everything I’ve said so far was sincere. You’re that special and fascinating. Even in the thousands of years I’ve lived, I’ve encountered few cases like this.”

“Shut your mouth.”

“How rude. But I’ll forgive you. My intelligence and curiosity won’t allow me to destroy something precious in a moment of rage like some inferior race.”

Morgoth wasn’t the least bit shaken.

If anything, he looked at the Skeleton King with even greater interest.

The eyes of the old, cunning Ancient Dragon glittered like those of a child heading to the hills to collect insects.

And all the while, a silver blade charged with powerful energy was swinging down at him.

*Fwoosh—CRASH!*

Fierce wind clawed at the space around them, and the power in the sword swallowed everything within a radius of a dozen or so meters.

It was a blow so savage that even the named monsters who’d once struck terror across the world would have faced death if it had hit them directly.

But before the roar even rang out, the Skeleton King knew.

His all-out attack hadn’t even hurt a single hair on his enemy’s head.

Rumble, rumble…

Beyond the enormous tremor shaking the space, Morgoth had already moved to the towering throne in the distance. He brought his hands together in a heartfelt round of applause.

“Impressive. Truly impressive. Such immense magical power—and there are so many different kinds.”

“You…”

“Oh, right. The Arch Lich, Leviathan, and Behemoth. You absorbed their magical power. But your current appearance doesn’t seem to have been created with magic… Have you ever met a being called a Doppelganger?”

For an instant, the Skeleton King felt his mind turn cold.

Found out.

Too quickly, and with such chilling accuracy.

Morgoth broke into a bright smile at the Skeleton King’s stiff expression.

“So that’s it. You can absorb not only a target’s magical power, but some of their abilities, too. What an astonishing ability. Now I understand how you, a mere undead—a Skeleton, at that—came to possess such power.”

“That mere undead might kill a Dragon here today.”

“A taunt?”

“No. I mean it. It’s a lesson I learned by watching a certain lunatic of a human.”

Morgoth nodded at the Skeleton King’s approach, the words spat out through clenched teeth.

“Yes, of course that could happen. Even the mighty Asmodeus was stopped by a mere human. But…”

Morgoth fixed his gaze on the Skeleton King and continued.

“Just as you learned a lesson through Jin Taekyung, I also realized the most important thing when I heard the news.”

*Goooom.*

Space warped.

Incredibly powerful, pure magical power became invisible blades, filling the space around them.

“His—Asmodeus’s—greatest mistake was arrogance.”

“……!”

“I don’t underestimate any of you.”

At the moment the Skeleton King’s eyes widened—

*Fwoooosh!*

A black flash, deeper and darker than the night sky, shot toward his entire body.
```
