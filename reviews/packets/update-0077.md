<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0077.txt",
      "sha256": "42c417377bc2bfb9119a7e1e9f1163da8d34cab6c1fbfe90aa2f551e7f7536df",
      "bytes": 13984
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d0299e27eb9f8f1ed134f332be7de970ec507f3ae43846938de92cd717ef2fc9",
      "bytes": 6321
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d7a61f4eb769b5160c3d9d19475d46ead7e4f4aa0f3a194efd0b8710d3f5336d",
      "bytes": 5049
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "093a625b24a13671b47d29e7694db49685eb6b597afb9a4f5073fbb8c08c6160",
      "bytes": 1579
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "bf1af568801b9077614d082195bf72f1ede636bf26f42b3d6c7dd55e35bba5b8",
      "bytes": 23807
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7ebd92de1177847c0c0a5ffe100ca55d09aedfedaca4023c18485fc964c052a9",
      "bytes": 4611
    }
  ],
  "estimated_tokens": 12238
}
-->

# Durable State Update — Chapter 77

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 77. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 77. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 77,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 77,
    "continuity_sources": [77],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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

## Prior durable context

```json
{
  "active_continuity": [
    "Taekyung successfully logged out after roughly twenty days in Murim; his watch showed 2:05:35 in the modern world, and he states that ten modern-world days now correspond to one hour in Murim.",
    "Taekyung currently has fifteen years of internal energy. Circulating his qi slightly increases his internal energy, and Sleep Mode normally keeps his sleep below three hours except when he is seriously injured.",
    "Seong Jinho is thirty, has lived with Taekyung as a friend and brother for years, and now plans to move out of the goshiwon soon, though the date is not fixed.",
    "Team Leader Choi owns the café where he meets Taekyung and gives him a contract; Taekyung signs it, after which a System alert appears.",
    "After ten days of Mukyung's training, Taekyung mastered the Jin Family's Spear Technique and Jin Family's Manoeuvre Technique; the Training? Trial! Quest succeeded and granted a Level Up, an Inventory reward, and notice of an additional reward.",
    "Hyuk Mujin remains badly injured and under treatment after the attack; the unidentified assassin may be the Head Elder's hidden disciple.",
    "Jin Mukyung reunited with Jin Wikyung after three years but remains detached and prioritizes sword training. Jin Wikyung plans to summon every Shanxi sect on New Year's Day and may seek to become Alliance Leader.",
    "Wipeng leads thirty elites south under the pretext of pursuing the nonexistent assassin, visited Song Sword Sect, and delivered Wikyung's summons as both summons and warning; Wikyung found no information on Dark Heaven in the family records.",
    "Gong Yacheong is recovering and will take charge of the rebuilt Sakju Branch; Socheon and Soyul will accompany him in six months. Soyul is five and does not know her parents are dead.",
    "The Returnee title grants Taekyung All Stats +10 and activates Login and Logout. Taekyung accepted that he was half-finished, asked Mukyung for help, and received a System time limit of 9 days 20 hours 23 minutes.",
    "Childeuk is an injured former meal-delivery servant who became a Level 12 martial artist directly under Jin Wikyung; Wikyung publicly embraced and praised him after acknowledging a minor misunderstanding.",
    "Lee Seowol is the new female Sect Leader of the Mount Heng Sword Sect. Taekyung received the forced Yesterday's Enemy, Today's Ally Quest to deliver an invitation for New Year's Day; its completion and Reward remain unknown.",
    "Taekyung, Mukyung, and Hyuk Mujin departed for Eung-hyeon in a four-horse carriage because Lee Seowol requested their visit and Mukyung may learn Peak martial arts.",
    "Taekyung is now a member of the Peace Guild and completed the Guild Membership achievement, receiving 10 points.",
    "Taekyung's Peace Guild contract provides a 500 million won signing bonus, a fixed monthly salary of 50 million won, a seventy-percent settlement share, and Guild-provided housing, a car, and other benefits.",
    "The Peace Guild's Guild house is Sooni's Super, a dilapidated corner store in Bucheon's Gate-dense district, on property purchased from the former owner's surviving family for slightly more than 2 billion won per pyeong.",
    "Im Kkeokjeong joined the Peace Guild after Team Leader Choi recruited him while he was hospitalized.",
    "The Peace Guild has five members: Taekyung, Team Leader Choi, Butler Kim, Im Kkeokjeong, and Miss Song. Miss Song is a founding member and was shopping for Taekyung's welcome party.",
    "Essence of the Himalayas increases Taekyung's Intelligence by 1 for one hour."
  ],
  "continuity_sources": [
    76
  ],
  "open_questions": [
    "The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed.",
    "It remains unresolved whether Hyuk Mujin will actually become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung's summons and whether he will become Alliance Leader.",
    "It remains unresolved whether Song Sword Sect has any connection to the attack.",
    "The reason the System displayed the same 2-hour-22-minute Time Limit twice remains unexplained.",
    "The nature of the minor misunderstanding that injured Childeuk remains undisclosed.",
    "Taekyung's prior relationship with Lee Seowol and the missing details of his memories about her remain unclear.",
    "Miss Song's full identity, background, and capabilities remain unrevealed."
  ],
  "safe_through": 76,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun; use junzi for 군자 and Junzi Sword for 군자검 with a cultural footnote.",
    "Retain Hyung-nim for 형 and 형님 in Taekyung's deferential speech; use Three Questions Gorge for 삼문협, Great Hero for 대협, and Ghost Sword for 귀검.",
    "Use Alliance Leader for 맹주 and summon for 소집; use New Year's Day for 원단 and close the sect's gates for 봉문.",
    "Use Sleep Mode for 수면 모드, Medicine King Hall Master for 약왕당주, four-horse carriage for 사두마차, and goshiwon for 고시원 with a footnote.",
    "Use Return for 귀환, Returnee for 귀환자, Ren and Du meridians for 임독양맥, Heart Demon for 심마, Paralysis Acupoint for 마혈, and Mute Acupoint for 아혈.",
    "Use fist-and-kicking technique for 권각술 and recognition for 인정; render 낙류검 as Falling Flow Sword, 질풍십이권 as Twelve Gale Fists, 화염신장 as Flame Divine Palm, and 분근착골 as Tendon-Splitting and Bone-Twisting.",
    "Render 비급 제작 as Martial Arts Manual Creation, 맷집 as Toughness, 천무지체 as Heavenly Martial Physique, 장칠득 as Jang Childeuk, Martial Artist Jang for 장 무인, 인의예지 as benevolence, righteousness, propriety, and wisdom, 호환 as killed by a tiger, and 일각 as fifteen minutes.",
    "Use Squad Leader for 조장님, Third Young Master for 삼공자님, Mujin for 무진아, seventh-tier student for 내신 칠 등급, Team Leader Choi for 최 팀장, Designer-Brand Junkie for 명품충, Qi Sense for 기감, Peace Guild for 평화, Essence of the Himalayas for 히말라야의 정수, Sooni's Super for 순이네 수퍼, and pyeong for 평당."
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 송송이    | **Song Song**     |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 상태               | **Status**                     |
| 아이템              | **Item**                       |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 임꺽정 | **Im Kkeokjeong** |

## Listed compact profiles

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 76
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** E-rank Hunter; veteran member of the Peace Guild’s Gate party and current member of the Peace Guild
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother and recommends him to Team Leader Choi

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 74
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

## Korean source

```text
＃77화



남자 둘이 술잔을 기울이다 보면 온갖 얘기가 다 튀어나오기 마련이다. 돈, 사람, 미래…….

그중에서도 진호 형이 선호하는 대화 주제는 여자였다.

그는 술만 들어갔다 하면 세상에서 가장 슬픈 남자가 되어 첫사랑을 회상하곤 했다.



‘고2 때 처음 만났지.’

‘이 인간 또 취했네.’

‘때는 바야흐로 꽃이 만개한 3월의 새 학기. 교실 문 열고 걔가 딱 들어오는데…….’

‘눈앞이 아찔했겠지. 귀에서는 막, 천국의 종소리가 댕댕 울려 퍼지고?’

‘어? 어떻게 알았냐?’

‘백 번도 넘게 들었으니까. 천국의 종소리는 개뿔. 아주 소설을 써라.’

‘네가 사랑을 몰라서 그래, 인마. 하긴 모태 솔로가 뭘 알겠냐마는.’

‘못 사귄 게 아니라 안 사귄 거거든.’

‘모쏠 새끼들이 꼭 저 소리 하더라. 무슨 모쏠 가이드북이라도 있냐? 너 누구 좋아해 본 적도 없지?’

‘……이, 있을걸?’

‘어휴, 됐다. 백 번, 천 번 말해 봤자 뭐 하냐. 직접 겪어 봐야 알지. 술이나 한잔 더 따라 봐.’



몇 달 전의 술자리가 지금 갑자기 생각난 이유는 간단했다.

‘형 말이 맞았어.’

댕- 대앵-

들린다. 종소리가.



* * *



송 양.

늘씬한 체구에 조막만 한 얼굴. 식재료가 가득 담긴 봉투를 양손에 주렁주렁 매단 천사가 나를 발견하고 멈칫했다.

“누구?”

고혹적이면서도 청량한 목소리에 정신이 아득해지고, 오밀조밀 인형 같은 이목구비에 가슴이 쿵쾅거렸다.

‘세상에.’

나는 마른침을 삼켰다. 지난 27년간 모태 솔로로 지내 왔던 게 바로 오늘을 위해서였다는 생각이 든다.

머릿속에서는 이미 시뮬레이션이 돌아가는 중이다.

‘집은 마당이 있는 전원주택. 아이는 둘에 고양이 한 마리. 완벽해.’

운기조식 때도 꿈쩍 않던 연애 세포가 살아 숨 쉰다.

나는 최대한 낮은 목소리로 말하려 입을 열었다. 자칭 연애 고수라는 진호 형은 마음에 드는 여성에게는 중저음을 사용하라고 누누이 강조해 왔다.

“저는…….”

“이쪽은 진태경. 송 양도 알지? 그 왜, 지난번에 한 번 얘기했었잖아. 내가 아끼는 동생이 C급 헌터로 재각성 했다고.”

“아, 그분이세요? 생각보다 젊으시네.”

“…….”

나는 난데없이 끼어든 임꺽정의 발을 지그시 밟으며 재차 입을 열었다.

“네. 제가 바로 그…….”

“뭘 이렇게 많이 사 오셨습니까? 따로 예약해 둔 식당이 있는데요.”

“비싸고 양도 적은데 거길 왜 가요? 그냥 안에서 고기나 좀 구워 먹으면 되지.”

“…….”

최 팀장. 당신 내 손으로 죽인다. 반드시 죽일 거야.

훼방꾼들을 차례차례 노려봤다. 내 살벌한 시선에 뭔가 말하려던 김 집사가 조용히 입을 다물었다.

‘기회는 지금뿐이야.’

아무도 끼어들지 않는 완벽한 타이밍. 마침 송 양도 나를 보고 있다. 나는 매력적인 중저음으로 말했다.

“안녕하세요. 이번에 C급 헌터가 된 스물일곱 살 진태경이라고 합니다. 생일은 4월 22일. 별자리는 황소자리고, 혈액형은 RH+A형입니다. 취미는 독서와 영화 평론. 앞으로 잘 부탁드려요.”

“…….”

“…….”

“…….”

아무도 입을 열지 않는 고요한 침묵, 마침내 그녀의 붉은 입술이 열렸다.

“아, 네.”

송 양이 사슴 같은 눈망울로 빤히 나를 바라봤다. 내 동굴 목소리에 제대로 뻑이 간 표정이다. 거기에 취미가 독서와 영화 평론이라는 지적인 면모까지 부각시켰으니 100퍼센트다.

‘고마워 진호 형. 잘되면 술 살게.’

마음속으로 환호성을 내지르던 그때, 최 팀장이 더듬거리는 목소리로 끼어들었다.

“시, 식사라도 하면서 천천히 얘기해 볼까요? 송이 씨도 장 보느라 고생하셨을 텐데.”

또다시 대화를 방해받았다는 분노는 그녀의 이름을 듣는 순간 흔적도 없이 사라졌다.

“송이 씨요?”

“송송이. 송송이예요. 제 이름.”

차분한 목소리로 대답한 송 양, 아니 송이 씨가 가게 안으로 쏙 들어갔다. 나는 멍하니 서서 그녀의 이름을 되새겼다.

“송송이…….”

세상에, 이름도 예뻐. 매력적이야. 눈부셔.

머리부터 발끝까지 내 스타일이다. 운명의 상대를 만났다는 생각에 반쯤 넋이 나간 나를 깨운 건 최 팀장의 목소리였다.

“태경 씨.”

“예, 예?”

“저기…… 아닙니다. 천천히 들어오세요.”

한숨을 푹 내쉰 최 팀장이 등을 돌렸다. 뭐야, 왜 저래?

“제가 뭐 잘못했어요?”

내 물음에 최 팀장의 뒤를 따르던 김 집사가 멈칫했다.

“그…… 힘내십시오.”

두 사람이 떠나자 남은 건 임꺽정과 나, 단둘뿐이었다.

“형님. 제가 뭐 실수한 거예요?”

“실수? 아니, 넌 죄를 저지른 거야.”

“죄요?”

“그래. 결코 용서받지 못할 죄를 지었지.”

“헉.”

내가 무슨 실수라도 했나? 가슴이 덜컥 내려앉은 그때, 임꺽정이 굳은 얼굴로 말을 이었다.

“한 여자의 마음을 훔친 죄.”

“……!”

“짜식. 남자인 나도 반할 뻔했다. 송 양 표정 봤어? 완전 뻑 갔더라. 게임 끝이야, 끝!”

“저, 정말요?”

“축하한다, 태경아! 국수 먹자!”

“형니임-!”

와락!

나는 감격을 이기지 못하고 임꺽정의 품에 안겼다. 그가 호탕하게 웃으며 내 등을 두드렸다.

“애는 몇 명 낳을 거야? 뭐? 두 명? 그러지 말고 세 명 해! 으하하하!”



* * *



가게 내부.

문 앞에 바짝 붙어 있던 최 팀장과 김 집사가 서로를 마주 보았다.

“김 집사님, 어떻게 생각하세요?”

“마법 아이템으로 소리를 차단한 도련님의 현명한 판단에 감탄할 뿐입니다.”

“그렇죠?”

“그렇습니다.”

두 사람은 약속이라도 한 듯이 뒤를 힐끔거렸다. 송송이는 부산하게 식사를 준비 중이었다.

“만약 방금 대화를 송이 씨가 들었으면…….”

“송이 씨께서 당장 길드를 탈퇴하더라도 저희가 위약금 물어 줘야 됩니다.”

“저런 멘트는 어디서 배운 걸까요? 혹시 김 집사님께서 젊었을 때…….”

김 집사가 정색하고 대답했다.

“도련님, 방금 말씀은 상당히 듣기 거북하군요. 저런 멘트는 대격변 이전에도 없었습니다.”

“태경 씨, 모태 솔로겠죠?”

“모태 솔로가 아니면 제가 오늘부터 김 집사가 아니라 박 집삽니다.”

“임 헌터님도 문제가 있던데요.”

“이런 말씀 드리기 좀 그렇지만, 입마개를 씌우고 싶었습니다.”

“임 헌터님, 미혼 맞죠?”

“안타깝게도 기혼입니다. 애도 둘 딸린.”

“도대체 어떻게……?”

“저도 그게 의문입니다.”

길드의 미래가 어둡다.

두 사람이 어두운 얼굴로 고개를 젓던 그 순간이었다.

“저기요.”

등 뒤에서 들려오는 목소리.

앞치마를 걸친 송송이가 허리춤에 손을 얹고 두 사람을 바라보고 있었다.

“두 분이서 뭘 그렇게 속닥거리세요? 준비하는데 손 하나 까딱 안 하고.”

“아, 송이 씨. 그게.”

“식사 후에는 저희가 치우겠습니다.”

“됐고요. 식사 준비 끝났으니까 와서 들어요. 그리고 임씨 아저씨랑…….”

송송이가 한숨처럼 말을 이었다.

“그, 황소자리도 부르시고.”



* * *



적당히 달궈진 불판 앞.

내가 비장한 얼굴로 입을 열었다.

“송이 씨.”

집게와 가위를 막 집어 든 송이 씨가 멈칫했다.

“네?”

“주십시오. 제가 굽겠습니다.”

“괜찮아요. 이따 뒷정리할 때나 도와주시면 되는데.”

“제 취미가 고기 굽기, 특기는 고기 자르기입니다.”

“……독서와 영화 평론 아니었어요?”

“그건 빙산의 일각에 지나지 않습니다.”

테이블 밑으로 임꺽정의 발을 건드리자 곧장 지원 사격이 들어왔다.

“송 양이 몰라서 하는 말인데 이 친구가 고기 하나는 끝내주게 잘 구워. 언제 한번은 불판 다섯 개를 동시에 막, 어? 고기를 씹으면 육즙이 아주 그냥 입 안에서 주르륵. 머릿속에서는 폭죽이 펑펑!”

나는 점잖게 한마디를 보탰다.

“별자리는 황소자리.”

“그렇지! 황소자리 남자가 말이야, 고기도 잘 굽고 성격도 순수하고 참 우직…….”

우지직.

최 팀장이 부러진 나무젓가락을 내려놓으며 중얼거렸다.

“죄송합니다. 힘 조절이 안 돼서.”

“여기요.”

기다렸다는 듯이 새 젓가락을 건네주는 송이 씨의 모습에 억장이 무너진다. 인정하긴 싫지만 미인과 미남. 선남선녀의 투 샷은 매우 잘 어울렸다.

‘설마. 아니겠지?’

애써 부정해 보지만 마음이 착잡하다.

나는 울적한 얼굴로 고기를 불판에 올렸다.

치이이익.

송이 씨는 최 팀장이랑 무슨 사이일까.

치이이익.

예전부터 친분이 있었던 건 확실하다. 괜히 길드 창립 멤버가 아닐 테니까.

치이이익.

생각해 보니까 최 팀장 저 자식 수상해. 아까부터 대화를 끼어들지 않나, 멀쩡한 젓가락은 왜 부러트려서 맥을 끊어?

치이이익.

B급 헌터라는 놈이 힘 조절을 못 해서 그랬다는 게 말이야, 방구야. 송이 씨 앞이라고 힘 센 거 자랑하나? 나는 쇠젓가락으로 매듭도 지을 수 있는데…….

“저기요.”

퍼뜩 고개를 들었다. 호수처럼 맑은 눈동자가 나를 빤히 응시하고 있었다.

“타요.”

“예, 예?”

“탄다구요. 고기.”

“헉!”

치지지직.

황급히 고기를 뒤집었지만 이미 늦었다.

“그냥 제가 할게요.”

“아뇨. 제가.”

“생각해 보니 그래도 오늘 처음 오셨는데 고기는 제가 구워서 대접하는 게 맞죠.”

세상에, 외모만 천사 같은 게 아니다.

‘아, 송이 씨. 당신은 도덕책.’

그녀의 비단결 같은 마음씨에 다시 한번 반했다.

서걱. 서걱.

치이익.

집게를 건네받은 그녀가 솜씨 좋게 고기를 굽고 자른다.

나는 멍하니 그 모습을 지켜봤다.

‘고기 굽는 모습도 예쁘네.’

대충 틀어 올려 쪽진머리, 분주히 움직이는 희고 가느다란 손. 동작 하나하나에서 빛이 난다.

“으음.”

얼마나 지났을까, 신중한 얼굴로 고기를 지켜보던 그녀가 말했다.

“다 익었다. 거기 접시 좀 주실래요?”

“옙.”

일회용 용기에 다 익은 고기를 척척 담아낸다. 아까부터 느낀 건데, 한두 번 해 본 솜씨가 아니다.

“이런 거 많이 해 보셨나 봐요.”

“네.”

“혹시 고기 집 알바 하셨어요?”

“네.”

“우와. 얼마나요?”

“2년이요.”

“히야, 언제요?”

“고등학교 때요.”

“허어, 그때 알바 하는 애들 별로 없었는데.”

“아, 네.”

어쩜 좋아. 생활력 강한 것도 딱 내 스타일이야.

이상하게 대답이 짧은 것 같지만 기분 탓일 거다. 호응을 위한 추임새도 마음껏 퍼부어 주었다.

‘대화 자체는 순조로워.’

진호 형이 말하길, 공통점부터 파고들어야 호감을 얻을 수 있다고 했다. 나는 열정적으로 말을 내뱉었다.

“저랑 비슷하네요. 하루 두 탕, 세 탕도 뛰고 그랬는데. 어느 하루는 일 끝나고 집에 왔더니…….”

“아, 네. 그런데 저기.”

“네?”

“너무 가까운 것 같아서요. 불판 아직 뜨거운데…….”

나도 모르게 몸이 송이 씨를 향해 잔뜩 기울어진 상태였다.

“괜찮습니다. 그까짓 거 조금 데이고 말죠. 하하하!”

“그래도 조심하는 게.”

“정말 괜찮아요. 걱정 안 하셔도 돼요.”

“…….”

어쩐지 송이 씨의 낯빛이 어둡다. 이거 설마.

‘내가 다칠까 봐 걱정하는 건가!’

충격이다. 오늘 처음 만난 나를 이렇게까지 생각해 주다니.

그리고 확실히 알았다. 그녀도 내게 관심이 있다는 사실을.

환청처럼 진호 형의 목소리가 어디선가 들려왔다.



‘커플이 되는 가장 중요한 덕목이 뭔지 알아? 바로 용기야.’

‘태경아, 명심해라. 용기 있는 자가 미인을 얻는다.’



형, 나 이제야 알 것 같아. 그리고 고마워.

‘그래. 용기를 내자.’

나는 떨리는 마음으로 그녀를 응시했다. 지금부터 하려는 말은 27년 인생을 통틀어 난생처음으로 뱉는 거다.

“송이 씨. 우리 오늘부터 1일…….”

그 순간, 벌떡 일어난 최 팀장이 외쳤다.

“1일! 오늘은 진태경 헌터님이 우리 길드 가족이 된 첫날입니다! 김 집사님?”

“예, 도련님! 술 준비됐습니다!”

언제나 느긋하던 김 집사가 소주잔을 번개 같은 속도로 채워 넣었다.

콸콸콸!

꼴꼴꼴이 아니라 콸콸콸이다.

반은 버리고 반은 때려 붓는 모습에 어이가 없었지만 나는 반드시 해야 할 말이 있었다.

“송이 씨. 다시 한번 말할게요. 우리…….”

최 팀장이 술잔을 번쩍 치켜들었다.

“우리 길드를 위하여!”

“송이 씨. 저쪽은 신경 쓰지 말고 내 말 들어요.”

송이 씨가 대답했다.

“위하여!”

“…….”

내 말 못 들은 거겠지? 그래, 못 들었을 거야.
```

## Final English reading copy

```markdown
# Chapter 77

When two men sit around tilting their glasses of liquor, all kinds of topics are bound to come spilling out. Money, people, the future…

Of all those topics, the one Jinho hyung preferred was women.

Whenever he got drunk, he became the saddest man in the world and reminisced about his first love.

*I first met her when I was a high school sophomore.*

*This guy's drunk again.*

*It was March, the start of a new school year, with flowers in full bloom. She opened the classroom door and walked in, and then…*

*You must have been dazzled. The bells of heaven must have started ringing in your ears—ding, ding, ding?*

*Huh? How did you know?*

*Because I've heard this story more than a hundred times. The bells of heaven, my ass. Go write a novel.*

*That's because you don't understand love, you punk. Then again, what would a lifelong single know?*

*It's not that I couldn't date. I chose not to.*

*You lifelong-single bastards always say that. Is there some kind of guidebook? You've never even liked anyone, have you?*

*……I think I have.*

*Oh, forget it. What good is it to tell you a hundred or a thousand times? You have to experience it yourself to understand. Pour me another drink.*

The reason I suddenly remembered that drinking session from a few months ago was simple.

*Hyung was right.*

Ding—ding—

I could hear them. The bells.



* * *



Miss Song.

She had a slender figure and a tiny face. An angel with grocery bags hanging from both hands spotted me and stopped short.

“Who are you?”

Her captivating yet refreshing voice made my mind go blank, while her delicate, doll-like features made my heart pound.

*My God.*

I swallowed dryly. It felt as though I had spent the past twenty-seven years as a lifelong single just for this day.

A simulation was already running in my head.

*Our home will be a country house with a yard. Two children and one cat. Perfect.*

The dating cells that had never budged, even while I circulated my qi, were springing to life.

I opened my mouth to speak in the lowest voice I could manage. Jinho hyung, a self-proclaimed master of romance, had always stressed that I should use a deep, resonant voice with a woman I liked.

“I’m…”

“This is Jin Taekyung. You’ve heard about him too, right, Miss Song? You know, the one I told you about last time. I said my beloved little brother had reawakened as a C-rank Hunter.”

“Oh, you’re that person? You’re younger than I expected.”

“……”

I gently stepped on Im Kkeokjeong’s foot, who had interrupted me out of nowhere, and opened my mouth again.

“Yes. I’m the very…”

“Why did you buy so much? We have a restaurant reserved.”

“It’s expensive and the portions are tiny. Why go there? We can just grill some meat inside.”

“……”

*Team Leader Choi. I’m going to kill you with my own hands. I really am.*

I glared at the meddlers one after another. Butler Kim had been about to say something, but he quietly closed his mouth under my murderous stare.

*This is my only chance.*

It was the perfect moment. No one was interrupting, and Miss Song was looking right at me. I spoke in an attractive, deep voice.

“Hello. My name is Jin Taekyung. I’m twenty-seven years old and recently became a C-rank Hunter. My birthday is April 22. I’m a Taurus, and my blood type is RH-positive, type A. My hobbies are reading and film criticism. I hope we get along.”

“……”

“……”

“……”

In the still silence, no one said a word. At last, her red lips parted.

“Oh, yes.”

Miss Song stared straight at me with her deerlike eyes. Her expression suggested that she had been utterly enchanted by my cavernous voice. And I had even highlighted my intellectual side by mentioning reading and film criticism. This was a hundred-percent success.

*Thank you, Jinho hyung. If this works out, drinks are on me.*

Just as I was cheering inside, Team Leader Choi interrupted in a stammering voice.

“W, why don’t we talk over a meal? Miss Song must be tired from grocery shopping.”

My anger at being interrupted again vanished without a trace the moment I heard her name.

“Song is your first name?”

“Song Song. Song Song is my name.”

Miss Song—or rather, Song Song—answered in a calm voice before slipping inside the store. I stood there blankly, repeating her name to myself.

“Song Song…”

My God, even her name was beautiful. So charming. So dazzling.

She was my type from head to toe. I was half out of my mind at the thought that I had met my fated partner when Team Leader Choi's voice snapped me out of it.

“Mr. Jin.”

“Yes, yes?”

“Um… Never mind. Take your time coming in.”

Team Leader Choi let out a deep sigh and turned away. *What was wrong with him?*

“Did I do something wrong?”

At my question, Butler Kim, who was following Team Leader Choi, stopped short.

“Um… Stay strong.”

Once the two of them left, only Im Kkeokjeong and I remained.

“Hyung-nim. Did I make some kind of mistake?”

“A mistake? No. You committed a crime.”

“A crime?”

“Yes. A crime you could never be forgiven for.”

“Gasp.”

Had I really done something wrong? Just as my heart sank, Im Kkeokjeong continued with a solemn expression.

“The crime of stealing a woman's heart.”

“……!”

“You little punk. Even I almost fell for you. Did you see Miss Song's expression? She was completely smitten. It's over. You won!”

“R-Really?”

“Congratulations, Taekyung! Let's eat noodles!”[^1]

“Hyung-nim!”

I could not contain my emotion and threw myself into Im Kkeokjeong's arms. He laughed heartily and patted me on the back.

“How many kids are you going to have? What? Two? Don't stop there—make it three! Hahahaha!”

[^1]: In Korean, “eating noodles” is a traditional expression associated with celebrating someone's wedding.

* * *



Inside the store.

Team Leader Choi and Butler Kim, who had been pressed right up against the door, turned to face each other.

“What do you think, Butler Kim?”

“I can only admire the Young Master's wise decision to block out the sound with a magic item.”

“Right?”

“Precisely.”

As if they had planned it, the two men glanced over their shoulders. Song Song was busily preparing the meal.

“If Miss Song heard that conversation just now…”

“Even if Miss Song quit the Guild on the spot, we would have to pay the penalty.”

“Where did he learn lines like that? Could it be that you used to say things like that when you were young, Butler Kim?”

Butler Kim answered with a stern expression.

“Young Master, that remark was highly unpleasant to hear. Lines like that did not exist even before the Great Cataclysm.”

“Mr. Jin is a lifelong single, right?”

“If he is not, then starting today I am no longer Butler Kim. I am Butler Park.”

“Hunter Im seems to have problems too.”

“I hate to say this, but I wanted to put a muzzle on him.”

“Hunter Im is unmarried, right?”

“Unfortunately, yes. He even has two children.”

“How on earth…?”

“I wonder the same thing.”

The Guild's future was bleak.

It was at that moment, while the two men shook their heads with gloomy expressions, that a voice came from behind them.

“Excuse me.”

Song Song stood there wearing an apron, one hand on her hip as she looked at the two men.

“What are you two whispering about? You haven't lifted a finger to help while I was preparing everything.”

“Oh, Miss Song. It's just…”

“We'll clean up after the meal.”

“Never mind that. The food is ready, so come and eat. And call Mr. Im and…”

Song Song continued with a sigh.

“That… Taurus, too.”



* * *



In front of the grill, which had been heated to just the right temperature, I opened my mouth with a solemn expression.

“Miss Song.”

Song Song stopped just as she picked up the tongs and scissors.

“Yes?”

“Give them to me. I'll grill the meat.”

“It's okay. You can help clean up afterward.”

“My hobby is grilling meat, and my specialty is cutting it.”

“……I thought your hobbies were reading and film criticism?”

“That was only the tip of the iceberg.”

When I nudged Im Kkeokjeong's foot under the table, immediate backup arrived.

“You wouldn't know this, Miss Song, but this guy can grill meat like nobody's business. One time, he was working five grills at once, just—huh? And when you bite into it, the juices flood your mouth. Fireworks start going off in your head!”

I added one more point in a dignified tone.

“I'm a Taurus.”

“That's right! A Taurus man can grill meat, and he's pure-hearted and honest and so steadfast…”

Crack.

Team Leader Choi set down the broken wooden chopsticks and muttered, “I'm sorry. I couldn't control my strength.”

“Here.”

Song Song handed him a new pair of chopsticks as if she had been waiting for it. My heart sank.

I hated to admit it, but the beautiful woman and handsome man made a wonderful pair.

*No way. It can't be.*

I tried to deny it, but my heart felt heavy.

With a gloomy expression, I placed the meat on the grill.

Sizzle.

What kind of relationship did Song Song have with Team Leader Choi?

Sizzle.

It was obvious they had known each other for a long time. She wouldn't be a founding member of the Guild for no reason.

Sizzle.

Come to think of it, that bastard Team Leader Choi was suspicious. He had been interrupting our conversation from the start. And why had he broken perfectly good chopsticks and ruined the mood?

Sizzle.

A B-rank Hunter claiming he could not control his strength? What kind of excuse was that? Was he showing off how strong he was in front of Song Song? I could tie a knot in metal chopsticks, too…

“Excuse me.”

I looked up with a start. Eyes as clear as a lake were staring straight at me.

“It's burning.”

“Yes, yes?”

“The meat. It's burning.”

“Gasp!”

Sizzle-sizzle-sizzle.

I hurriedly flipped the meat, but it was already too late.

“I'll do it.”

“No. I will.”

“Come to think of it, since you're here for the first time today, it's only right that I grill the meat and serve you.”

My God. She wasn't just an angel on the outside.

*Oh, Miss Song. You’re an ethics textbook.*[^2]

[^2]: In Korean, “ethics textbook” is a pun on a phrase meaning “what on earth are you?”

I fell for her gentle nature all over again.

Slice. Slice.

Sizzle.

After taking the tongs from me, she grilled and cut the meat with practiced skill.

I watched her in a daze.

*She even looks beautiful while grilling meat.*

Her hair was loosely twisted into a bun, and her slender, pale hands moved busily. Every one of her movements seemed to shine.

“Hmm.”

How much time had passed? She had been watching the meat carefully when she spoke.

“It’s done. Could you hand me a plate?”

“Yes, ma'am.”

She neatly placed the fully cooked meat into a disposable container. I had noticed it earlier, but this was clearly not something she had done only once or twice.

“You must have done this a lot.”

“Yes.”

“Did you work part-time at a barbecue restaurant?”

“Yes.”

“Wow. For how long?”

“Two years.”

“Wow, when?”

“When I was in high school.”

“Huh. Not many people worked part-time jobs back then.”

“Oh, yes.”

*What am I going to do? Even her resourcefulness is exactly my type.*

Her answers seemed strangely short, but that had to be my imagination. I showered her with plenty of little responses to keep the conversation going.

*The conversation itself is going smoothly.*

Jinho hyung had said that you had to start by finding common ground if you wanted someone to like you. I spoke passionately.

“We're pretty similar. I used to work two or even three shifts in a day. One day, after I finished work and came home…”

“Oh, yes. But, um.”

“Yes?”

“You seem a little close. The grill is still hot…”

Without realizing it, I had leaned my entire body toward Song Song.

“It's fine. I'll just get a little burned. Hahaha!”

“You should still be careful.”

“I'm really fine. You don't have to worry.”

“……”

Song Song's expression seemed strangely dark. *Could it be…?*

*Is she worried that I might get hurt?*

It was shocking. She was thinking about me this much even though we had only met today.

And then I knew for certain. She was interested in me, too.

Jinho hyung's voice reached me from somewhere, like a hallucination.

*Do you know what the most important virtue is when it comes to becoming a couple? Courage.*

*Taekyung, remember this. A man with courage wins the beauty.*

*Hyung, I think I finally understand. And thank you.*

*That's right. Let's be brave.*

I looked at her with a trembling heart. What I was about to say was something I had never once said in my entire twenty-seven years of life.

“Miss Song. Starting today, you and I are on day one…”

At that moment, Team Leader Choi jumped to his feet and shouted.

“Day one! Today is the first day Hunter Jin Taekyung has become part of our Guild family! Butler Kim?”

“Yes, Young Master! The soju is ready!”

The usually unhurried Butler Kim filled the shot glasses at lightning speed.

Glug-glug-glug!

Not a gentle trickle—it was pouring full blast.

Half of it spilled, while the other half was poured in with such force that I was left speechless. But there was something I absolutely had to say.

“Miss Song. Let me say it again. You and I…”

Team Leader Choi raised his glass high.

“To our Guild!”

“Miss Song. Ignore them and listen to me.”

Song Song answered.

“To our Guild!”

“……”

She didn't hear me, right? Yes. She couldn't have heard me.
```
